from .embeddingmodel import EmbeddingModel
import numpy

def generate_chunk_embedding(chunk: str, embedding_model: EmbeddingModel) ->  list[numpy.ndarray]:
    vetor = embedding_model.model.encode_document(chunk)
    return (vetor)

def adding_embedding(chunks: list[dict]) -> list[dict]:
    
    embedding_model = EmbeddingModel ()
    
    for chunk in chunks:
        print(f"ID da chunk: {chunk["metadata"]["id"]}")
        emb = generate_chunk_embedding(chunk["content"], embedding_model)
        chunk["embedding"] = emb
        print(f"Tamanho do embedding {len(chunk["embedding"])}")
    return (chunks)