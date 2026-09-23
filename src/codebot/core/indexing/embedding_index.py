import numpy

class EmbeddingIndex:
    def __init__(self):
        self._embeddings = []
        self._chunk_ids = []

    def add(self, embedding: numpy.ndarray, chunk_id: int):
        self._embeddings.append(embedding)
        self._chunk_ids.append(chunk_id)

    def search(self, embedding: numpy.ndarray):

