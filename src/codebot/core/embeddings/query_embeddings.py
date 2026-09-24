from .embeddingmodel import EmbeddingModel
import numpy as np

def generate_query_embedding(query: str, query_model: EmbeddingModel) -> np.ndarray:
    vetor = query_model.model.encode_query(query)
    return (vetor)