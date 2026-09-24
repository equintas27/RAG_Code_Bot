from tests.aux_functions_tests import find_overlap, reconstruct_chunks
from codebot.core.chunking.text_splitter import text_splitter
from codebot.core.chunking.pdf_extractor import extract_pdf_with_metadata
from codebot.core.embeddings.embedder import generate_chunk_embedding, adding_embedding
from codebot.core.embeddings.embeddingmodel import EmbeddingModel
from codebot.core.indexing.embedding_index import EmbeddingIndex

if __name__ == "__main__":
    path = "data/documents/sonangol/Relatorio-2025.pdf"
    chunks = extract_pdf_with_metadata(path)

    new_chunks = adding_embedding(chunks)
    index = EmbeddingIndex()
    for chunk in new_chunks:
        index.add(chunk["embedding"], chunk["metadata"]["id"])

    print(f"Tamanho da quantidade de embeddings: {len(index._embeddings)}")
    print(f"Tamanho da quantidade de ids: {len(index._chunk_ids)}")

    for emb, _id in zip(index._embeddings, index._chunk_ids):
        print (f"Vector: {emb}")
        print (f"Id: {_id}")