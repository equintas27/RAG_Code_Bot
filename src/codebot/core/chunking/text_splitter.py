def text_splitter(text, chunk_size, overlap) -> list[str]:
    
    chunks = []
    start = 0

    if chunk_size <= 0 or overlap <= 0:
        raise ValueError("chunk_size and overlap must be biggest than 0")
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")
   
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)
        start = start + chunk_size - overlap
    return chunks 

if __name__ == "__main__":
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chunk_size = 10
    overlap = 3

    s = text_splitter(text, chunk_size, 3)
    print (s)