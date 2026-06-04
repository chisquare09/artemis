from app.modules.rag.query_utils import normalize, expand_query
from app.modules.rag.retriever import score_chunk


def test_normalize_removes_punctuation():
    assert normalize("How are you?") == ["how", "are", "you"]


def test_normalize_lowercases():
    assert normalize("HELLO World") == ["hello", "world"]


def test_expand_query_maps_bill_to_conto():
    terms = ["bill"]
    expanded = expand_query(terms)
    assert "conto" in expanded


def test_expand_query_maps_coffee_to_caffe():
    terms = ["coffee"]
    expanded = expand_query(terms)
    assert "caffè" in expanded


def test_score_chunk_keyword_overlap():
    score = score_chunk(["caffè", "prezzo"], "Caffè espresso costa 1 euro")
    assert score > 0


def test_score_chunk_no_overlap():
    score = score_chunk(["pizza"], "Caffè espresso costa 1 euro")
    assert score == 0


def test_score_chunk_empty_terms():
    score = score_chunk([], "Caffè espresso")
    assert score == 0
