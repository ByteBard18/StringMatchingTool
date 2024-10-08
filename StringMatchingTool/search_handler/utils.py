# file_handler/utils.py

import aiofiles
import os
import re
from django.conf import settings
from rank_bm25 import BM25Okapi
# from django.http import JsonResponse

async def process_text_file(file_path):
    """
    Asynchronous function to process a text file and prepare it for BM25 indexing.
    """
    if not os.path.exists(file_path):
        return {'status': 'failed', 'message': 'File does not exist.'}
    
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            content = await file.read()
            # Example preprocessing (e.g., text normalization, tokenization)
            processed_content = preprocess_text(content)
            
            # Create the JSON object
            file_id = os.path.basename(file_path)
            json_object = {
                'id': file_id,
                'content': processed_content
            }
            
            # Return JSON object
            return json_object

    except Exception as e:
        return {'status': 'failed', 'message': str(e)}

def preprocess_text(text):
    """
    Function to preprocess text (e.g., normalize, tokenize).
    """
    normalized_text = text.lower()  # Example: simple normalization to lowercase
    normalized_text = re.sub(r'\s+', ' ', normalized_text)
    normalized_text = re.sub(r'[^\x00-\x7F]', '', normalized_text)
    # normalized_text = re.sub(r'[^\w\s]', '', normalized_text)
    return normalized_text

def use_bm25(corpus, query):
    tokenized_corpus = [doc['content'].split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    
    tokenized_query = query.split(" ")
    
    doc_scores = bm25.get_scores(tokenized_query)
    scores = doc_scores.tolist()
    count_relevant = sum(1 for score in scores if score!=0)
    res = bm25.get_top_n(tokenized_query, corpus, n=count_relevant)
    return {'result': res}
    # return {'result': corpus}

def get_lines(content, offsets):
    offset_flag = False
    line_start = 0
    results = []
    line_offset  = []
    # Ensure offsets are in a set for faster lookup
    offsets_set = set(offsets)
    
    for i in range(len(content)):
        if content[i] == '.' or i == len(content) - 1:
            # Check if there is an offset in the current line
            if offset_flag:
                line = content[line_start:i + 1].strip()
                results.append(line)
            line_start = i + 1
            offset_flag = False
        
        if i in offsets_set:
            offset_flag = True
            line_offset.append(i-line_start)
    
    return {'results':results, 'offsets':line_offset}
