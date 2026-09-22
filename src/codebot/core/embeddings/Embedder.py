from Embedding_Model import EmbeddingModel

def generate_chunk_embedding(chunk: str, embedding_model: EmbeddingModel) -> list[float]:

    vetor = embedding_model.model.encode_document(chunk)
    print(type(vetor))