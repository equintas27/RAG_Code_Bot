import pymupdf

pdf_path = "data/documents/sonangol/Relatorio-2025.pdf"

document = pymupdf.open(pdf_path)

print(f"Número de páginas: {len(document)}")
full_text = ""

for page in document:
    text = page.get_text()
    full_text += text

print ("\n --- Páginas --- \n")
print(full_text)