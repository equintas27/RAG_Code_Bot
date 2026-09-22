from .embeddingmodel import EmbeddingModel

def generate_chunk_embedding(chunk: str, embedding_model: EmbeddingModel) :

    vetor = embedding_model.model.encode_document(chunk)
    print(type(vetor))
    print(len(vetor))
    print(vetor)