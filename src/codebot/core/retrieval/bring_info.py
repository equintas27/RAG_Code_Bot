def bring_chunk_content(chunks: list[dict], chunk_id: int) -> str | None:
    for chunk in chunks:
        if chunk["metadata"]["id"] == chunk_id:
            return (chunk["content"])
    return (None)

def bring_all_content(chunks: list[dict], chunk_ids: list[int]) -> list[str] | None:
    all_content = []

    for id in chunk_ids:
        content = bring_chunk_content(chunks, id)
        if content:
            all_content.append(content)
    return (all_content)