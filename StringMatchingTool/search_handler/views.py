import asyncio
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.files.storage import default_storage
from asgiref.sync import sync_to_async
from .models import FileProcessingResult
from .utils import process_text_file, use_bm25, get_lines
import uuid
from .boyermoore import search

async def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        query = request.POST.get('query')
        print(len(files))
        
        # Save files to media directory
        file_paths = []
        for file in files:
            file_path = default_storage.save(file.name, file)
            file_path = default_storage.path(file_path)  # Get the absolute file path
            file_paths.append(file_path)

        # Asynchronously process files using the utility function
        tasks = [process_text_file(file_path) for file_path in file_paths]
        results = await asyncio.gather(*tasks)

        # Generate a unique results ID
        results_id = str(uuid.uuid4())
        
        # Save results to the database using sync_to_async
        await sync_to_async(FileProcessingResult.objects.create)(
            result_id=results_id, query=query, results=results
        )
        print("Results saved to database")

        # Return the results ID to the client
        return JsonResponse({'results_id': results_id, 'query': query})

    return render(request, 'upload.html')

def get_results(request, results_id, query):
    # Fetch results from the database
    result_record = get_object_or_404(FileProcessingResult, result_id=results_id)
    results = result_record.results

    docs = use_bm25(results, query)
    print(docs)
    response = []
    for doc in docs['result']:
        if(search(doc['content'], query)!=None):
            content = doc['content']
            offset_list = search(doc['content'], query)
            lines = get_lines(content, offset_list)
            response.append({
                'id': doc['id'],
                'content': content,
                'query': query,
                'offset_list': offset_list,
                'lines': lines['results'],
                'line_offsets': lines['offsets']
            })
        else:
            response.append({
                'id':  doc['id'],
                'offsets': None,
                'content': doc['content'],
                'query': query
            })
    return JsonResponse(response, safe=False)
