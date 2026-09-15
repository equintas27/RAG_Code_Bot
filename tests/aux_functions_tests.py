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
