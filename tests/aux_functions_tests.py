def find_overlap(chunk1, chunk2):
    max_overlap = min(len(chunk1), len(chunk2))

    for size in range(max_overlap, 0, -1):
        if chunk1[-size:] == chunk2[:size]:
            return size

    return (0)

def reconstruct_chunks(chunks):
    if not chunks:
        return ""

    reconstructed = chunks[0]

    for chunk in chunks[1:]:
        overlap_found = 0

        for i in range(min(len(reconstructed), len(chunk)), 0, -1):
            if reconstructed.endswith(chunk[:i]):
                overlap_found = i
                break

        reconstructed += chunk[overlap_found:]

    return (reconstructed)

def aux(ls):
    for i in range(2, len(chunks) - 1):
        current = chunks[i]
        next_chunk = chunks[i + 1]

        if current["metadata"]["page"] == next_chunk["metadata"]["page"]:
            overlap_found = find_overlap(
                current["content"],
                next_chunk["content"]
            )

            print(
                f"Chunk {current['metadata']['id']} → "
                f"Chunk {next_chunk['metadata']['id']} | "
                f"Overlap encontrado: {overlap_found}"
            )
