MAX_CHUNK_SIZE = 800


def chunk_text(text: str, max_size: int = MAX_CHUNK_SIZE) -> list[dict]:
    if not text:
        return []
    chunks = []
    start = 0
    idx = 0
    while start < len(text):
        end = min(start + max_size, len(text))
        if end < len(text):
            for sep in [". ", "! ", "? ", "\n"]:
                last = text.rfind(sep, start, end)
                if last > start:
                    end = last + len(sep)
                    break
        content = text[start:end].strip()
        if content:
            chunks.append({"chunk_index": idx, "content": content, "token_count": len(content.split())})
            idx += 1
        start = end
    return chunks
