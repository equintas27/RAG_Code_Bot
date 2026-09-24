from tests.aux_functions_tests import find_overlap, reconstruct_chunks
from codebot.core.chunking.text_splitter import text_splitter
from codebot.core.chunking.pdf_extractor import extract_pdf_with_metadata
from codebot.core.embeddings.embedder import generate_chunk_embedding, adding_embedding
from codebot.core.embeddings.query_embeddings import generate_query_embedding
from codebot.core.embeddings.embeddingmodel import EmbeddingModel
from codebot.core.indexing.embedding_index import EmbeddingIndex


if __name__ == "__main__":
    path = "data/documents/sonangol/Relatorio-2025.pdf"
    chunks = extract_pdf_with_metadata(path)

    embedding_model = EmbeddingModel ()

    new_chunks = adding_embedding(chunks, embedding_model)
    index = EmbeddingIndex()
    for chunk in new_chunks:
        index.add(chunk["embedding"], chunk["metadata"]["id"])

    print(f"Tamanho da quantidade de embeddings: {len(index._embeddings)}")
    print(f"Tamanho da quantidade de ids: {len(index._chunk_ids)}")

    emb = generate_query_embedding("O que é a Sonangol", embedding_model)
    result = index.search(emb)
    for item in result:
        print(f"ID: {item['chunk_id']} | Score: {item ['score']}")