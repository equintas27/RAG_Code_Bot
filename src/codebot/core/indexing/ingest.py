
from codebot.core.chunking.text_splitter import text_splitter, reconstruct_chunks
from codebot.core.chunking.pdf_extractor import extract_pdf_with_metadata

if __name__ == "__main__":
    path = "data/documents/sonangol/Relatorio-2025.pdf"
    chunks = extract_pdf_with_metadata(path)

    for i, chunk in enumerate (chunks):
        print(f"--CHUNCK{i}--")
        print(chunk)
    #paragraphs = text_1.split("\n")
    #chunks = text_splitter(text_1, 1000, 200)
    #sizes = [len(chunk) for chunk in chunks]

   # print("Total de chunks:", len(chunks))
    #print("Menor chunk:", min(sizes))
    #print("Maior chunk:", max(sizes))
    #print("Média:", sum(sizes) / len(sizes))
    #
    #small_overlaps = 0
    #for i in range(len(chunks) - 1):
        #overlap = find_overlap(chunks[i], chunks[i + 1])

        #if overlap < 150:
            #print(f"\nChunk {i} -> {i + 1}: overlap = {overlap}")
            #print("FINAL DO CHUNK ANTERIOR:")
            #print(repr(chunks[i][-250:]))
            #print("INÍCIO DO PRÓXIMO CHUNK:")
           # print(repr(chunks[i + 1][:250]))
            #small_overlaps += 1

    #print("Overlaps menores que 150:", small_overlaps)

    #overlaps = []

    #for i in range(len(chunks) - 1):
      #  overlap = find_overlap(chunks[i], chunks[i + 1])
     #   overlaps.append(overlap)

    #print("Menor overlap:", min(overlaps))
    #print("Maior overlap:", max(overlaps))
    #print("Média:", sum(overlaps) / len(overlaps))      

    #for i, chunk in enumerate(chunks):
      #  if len(chunk) < 100:
     #       print(f"Chunk {i} muito pequeno: {len(chunk)} caracteres")
    
    #for i, chunk in enumerate(chunks):
      #  if len(chunk) > 1000:
     #       print(f"ERRO: Chunk {i} tem {len(chunk)} caracteres")

    #for i in range(len(chunks) - 1):
        #overlap = find_overlap(chunks[i], chunks[i + 1])

    #if overlap != 200:
     #   print(
      #      f"Chunk {i} -> {i + 1}: "
       #     f"overlap = {overlap}"
        #)
    #print(repr(chunks[766][-200:]))
    #print(repr(chunks[767][:200]))
    #for i, chunk in enumerate(chunks):
    #    print(f"\n--CHUNCK {i}--")
    #   print(chunk)   
    #print ("\n --- Páginas --- \n")
    #print(paragraphs[:15])
    #print(text_1.count("\n"))
    #print(text_1.count("\n\n"))
    #text = "Sonangol aumentou a produção nacional"

    #position = text.rfind(" ")

    #print(position)
    #print(text[:position])
    #print(text[position:])
    #text = """Primeira linha.
    #Segunda linha.
    #Terceira linha."""

    #chunks = text_splitter(text, 30, 10)

    #for i, chunk in enumerate(chunks):
    #    print(f"Chunk {i}: {len(chunk)} caracteres")
    #    print(repr(chunk))
    #reconstructed = reconstruct_chunks(chunks)

    #print("\n--- ORIGINAL ---")
    #print(repr(text_1))

    #print("\n--- RECONSTRUÍDO ---")
    #print(repr(reconstructed))

    #print("\n--- RESULTADO ---")
    #print(text_1 == reconstructed)
    #print (f"Total de chunks {len(chunks)}")
    #for i, chunk in enumerate(chunks):
     #   print(f"Chunk {i}: {len(chunk)} caracteres")
       #     print(f"find_overlap_:{find_overlap(chunk[i], chunk[i + 1])} ")
        