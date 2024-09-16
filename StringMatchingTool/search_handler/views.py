import asyncio
from concurrent.futures import ThreadPoolExecutor
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from .utils import process_text_file, use_bm25, get_lines  # Import the async processing function
import uuid  # For generating unique result IDs
from .boyermoore import search

# Initialize the thread pool executor
executor = ThreadPoolExecutor()

def save_session_sync(session, key, value):
    """Synchronous function to save session data."""
    session[key] = value
    session.save()

async def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        query = request.POST.get('query')

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
        
        # Save results to the session using threading
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(executor, save_session_sync, request.session, results_id, results)

        # Return the results ID to the client
        return JsonResponse({'results_id': results_id, 'query': query})

    return render(request, 'my-react-app/index.html')


def get_results(request, results_id, query):
    # Fetch results from session
    results = request.session.get(results_id, [])    
    docs = use_bm25(results, query)
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
                'lines': lines
            })
        else:
            response.append({
                'id':  doc['id'],
                'offsets': None,
                'content': doc['content'],
                'query': query
            })
    #clear session after the code execution finishes
    print("Session cleared")
    request.session.pop(results_id, None)
    
    #return render(request, "file_handler/results.html", {"results": results})
    return JsonResponse(response, safe=False)

