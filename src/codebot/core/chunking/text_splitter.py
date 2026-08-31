def reconstruct_chunks(chunks):
    if not chunks:
        return ""

    reconstructed = chunks[0]

    for chunk in chunks[1:]:
        overlap_found = 0

        for i in range(min(len(reconstructed), len(chunk)), 0, -1):
            if reconstructed.endswith(chunk[:i]):
                overlap_found = i
                break

        reconstructed += chunk[overlap_found:]

    return reconstructed

def text_splitter(text, chunk_size, overlap) -> list[str]:
    
    chunks = []
    lines = text.splitlines(keepends=True)
    current_chunks = ""

    if chunk_size <= 0 or overlap <= 0:
        raise ValueError("chunk_size and overlap must be biggest than 0")
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")   
    for line in lines:
        if len(current_chunks) + len(line) + 1 > chunk_size:
            if current_chunks:
                chunks.append(current_chunks)
                overlap_start = len(current_chunks) - overlap
                overlap_start = current_chunks.find(" ", overlap_start)
                if overlap_start != -1:
                    current_chunks = current_chunks[overlap_start + 1:]
        current_chunks += line
        
    if current_chunks:
                chunks.append(current_chunks)
    return chunks  

if __name__ == "__main__":
    text = """Primeira linha.
Segunda linha.
Terceira linha.
Quarta linha."""
    #chunk_size = 10
    #overlap = 3
    chunks = text_splitter(text, 10, 3)
    for i, chunk in enumerate(chunks):
        print(f"\n--CHUNCK{i}--")
        print(chunk)
   # s = text_splitter(text, chunk_size, 3)
    #print (s)