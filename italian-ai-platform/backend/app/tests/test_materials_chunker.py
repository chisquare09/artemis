from app.modules.materials.chunker import chunk_text


def test_short_text_creates_one_chunk():
    chunks = chunk_text("Caffè espresso.")
    assert len(chunks) == 1


def test_long_text_creates_multiple_chunks():
    long_text = "Ciao. " * 200
    chunks = chunk_text(long_text)
    assert len(chunks) > 1


def test_chunk_index_is_correct():
    long_text = "Buongiorno. " * 150
    chunks = chunk_text(long_text)
    for i, chunk in enumerate(chunks):
        assert chunk["chunk_index"] == i


def test_token_count_greater_than_zero():
    chunks = chunk_text("Vorrei un caffè, per favore.")
    assert chunks[0]["token_count"] > 0


def test_empty_text_returns_empty():
    assert chunk_text("") == []
