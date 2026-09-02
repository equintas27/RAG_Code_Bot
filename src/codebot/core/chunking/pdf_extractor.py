import pymupdf
from codebot.core.chunking.text_splitter import text_splitter, reconstruct_chunks

def find_overlap(chunk1, chunk2):
    max_overlap = min(len(chunk1), len(chunk2))

    for size in range(max_overlap, 0, -1):
        if chunk1[-size:] == chunk2[:size]:
            return size

    return 0

def extract_pdf_with_metadata(pdf_path: str, chunk_size: int = 1000, overlap: int = 200) ->list[dict]:    
    
    document = pymupdf.open(pdf_path)
    all_chunks = []
    chunk_id = 0

    for page_num, page in enumerate(document, start=1):
        text = page.get_text()
        if text.strip():
            page_chunks = text_splitter(text, chunk_size, overlap)
        for chunk in page_chunks:
            all_chunks.append({
                "content" : chunk,
                "metadata" : {
                    "id" : chunk_id,
                    "source": pdf_path,
                    "page" : page_num,
                }
            })
            chunk_id += 1
    return (all_chunks)