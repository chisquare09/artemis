from app.core.exceptions import NotFoundException
from app.modules.rag.retriever import retrieve_chunks

VALID_UNITS = {"A1.5"}


def retrieve(unit_code: str, query: str, limit: int = 5) -> dict:
    if unit_code not in VALID_UNITS:
        raise NotFoundException(f"Unit {unit_code} not found")
    chunks = retrieve_chunks(unit_code, query, limit)
    return {
        "unit_code": unit_code,
        "query": query,
        "chunks": chunks,
        "retrieval_strategy": "keyword",
    }
