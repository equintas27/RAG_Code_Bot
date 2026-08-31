import pymupdf
from codebot.core.chunking.text_splitter import text_splitter

def extract_pdf(pdf_path) ->str:    
    document = pymupdf.open(pdf_path)

    full_text = ""

    for page in document:
        text = page.get_text()
        full_text += text
    return (full_text)


if __name__ == "__main__":
    #path = "data/documents/sonangol/Relatorio-2025.pdf"
    #text_1 = extract_pdf(path)
    #paragraphs = text_1.split("\n")
    #chunks = text_splitter(text_1, 1000, 50)

    #for chunk in chunks:
        #print("--CHUNCK--")
        #print(chunk)
    #print ("\n --- Páginas --- \n")
    #print(paragraphs[:15])
    #print(text_1.count("\n"))
    #print(text_1.count("\n\n"))
    text = "Sonangol aumentou a produção nacional"

    position = text.rfind(" ")

    print(position)
    print(text[:position])
    print(text[position:])