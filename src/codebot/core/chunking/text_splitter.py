def text_splitter(text, chunk_size, overlap) -> list[str]:
    
    chunks = []
    lines = text.split("\n")
    current_chunks = ""

    if chunk_size <= 0 or overlap <= 0:
        raise ValueError("chunk_size and overlap must be biggest than 0")
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")   
    for line in lines:
        if len(current_chunks) + len(line) + 1 > chunk_size:
            if current_chunks:
                cut_position = current_chunks.rfind(" ")
                chunk = current_chunks[:cut_position]
                chunks.append(current_chunks)
                current_chunks = current_chunks[-overlap:]
            #current_chunks = ""
        current_chunks += line + "\n"
        
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
    for chunk in chunks:
        print("--CHUNCK--")
        print(chunk)
   # s = text_splitter(text, chunk_size, 3)
    #print (s)