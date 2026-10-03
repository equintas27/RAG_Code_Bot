from .embeddingmodel import EmbeddingModel
import numpy

def generate_chunk_embedding(chunk: str, embedding_model: EmbeddingModel) ->  list[numpy.ndarray]:
    vetor = embedding_model.model.encode_document(chunk)
    return (vetor)

def adding_embedding(chunks: list[dict], embedding_model: EmbeddingModel) -> list[dict]:
    
    for chunk in chunks:
        emb = generate_chunk_embedding(chunk["content"], embedding_model)
        chunk["embedding"] = emb
        return (chunks)