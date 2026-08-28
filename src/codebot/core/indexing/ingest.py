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
    path = "data/documents/sonangol/Relatorio-2025.pdf"
    text_1 = extract_pdf(path)
    txt = text_splitter(text_1, 1000, 200)
    print ("\n --- Páginas --- \n")
    print(txt[0])