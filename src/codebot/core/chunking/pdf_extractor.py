import pymupdf
from codebot.core.chunking.text_splitter import text_splitter

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