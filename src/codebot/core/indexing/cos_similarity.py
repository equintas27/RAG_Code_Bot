import numpy as np

def calculate_similarity(emb1: np.ndarray, emb2: np.ndarray) -> float:
    norm_emb1 = np.linalg.norm(emb1)
    norm_emb2 = np.linalg.norm(emb2)
    
    if norm_emb1 == 0.0 or norm_emb2 == 0.0:
        return (0.0)
    scalar_product = np.dot(emb1, emb2)
    similarity = scalar_product / (norm_emb1 * norm_emb2)
    return (similarity)

