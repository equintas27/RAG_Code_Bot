from tests.aux_functions_tests import find_overlap, reconstruct_chunks
from codebot.core.chunking.text_splitter import text_splitter
from codebot.core.chunking.pdf_extractor import extract_pdf_with_metadata
from codebot.core.embeddings.generate_chunk_embedding import generate_chunk_embedding
from Embedding_Model import EmbeddingModel

if __name__ == "__main__":
    path = "data/documents/sonangol/Relatorio-2025.pdf"
    chunks = extract_pdf_with_metadata(path)

    Embedding_Model embedding_model
    emb = generate_chunk_embedding (chunks[0], embedding_model)
    

    
    