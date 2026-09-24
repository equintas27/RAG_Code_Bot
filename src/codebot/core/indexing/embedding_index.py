import numpy
from .cos_similarity import calculate_similarity

class EmbeddingIndex:
    def __init__(self):
        self._embeddings = []
        self._chunk_ids = []

    def add(self, embedding: numpy.ndarray, chunk_id: int):
        self._embeddings.append(embedding)
        self._chunk_ids.append(chunk_id)

    def search(self, query_embedding: numpy.ndarray) -> list[dict]:
        result = []
        for emb, id in zip(self._embeddings, self._chunk_ids):
            s_score = calculate_similarity(emb, query_embedding)
            result.append({"chunk_id": id, "score": s_score})
        return (result)



