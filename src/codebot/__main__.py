from tests.aux_functions_tests import find_overlap, reconstruct_chunks
from codebot.core.chunking.text_splitter import text_splitter
from codebot.core.chunking.pdf_extractor import extract_pdf_with_metadata

if __name__ == "__main__":
    path = "data/documents/sonangol/Relatorio-2025.pdf"
    chunks = extract_pdf_with_metadata(path)

    for i in range(2, len(chunks) - 1):
        current = chunks[i]
        next_chunk = chunks[i + 1]

        if current["metadata"]["page"] == next_chunk["metadata"]["page"]:
            overlap_found = find_overlap(
                current["content"],
                next_chunk["content"]
            )

            print(
                f"Chunk {current['metadata']['id']} → "
                f"Chunk {next_chunk['metadata']['id']} | "
                f"Overlap encontrado: {overlap_found}"
            )
    