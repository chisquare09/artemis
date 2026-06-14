from app.core.exceptions import NotFoundException
from app.modules.curriculum.unit_catalog import ensure_unit_exists
from app.modules.rag.retriever import retrieve_chunks


def retrieve(unit_code: str, query: str, limit: int = 5) -> dict:
    ensure_unit_exists(unit_code)
    chunks = retrieve_chunks(unit_code, query, limit)
    return {
        "unit_code": unit_code,
        "query": query,
        "chunks": chunks,
        "retrieval_strategy": "keyword",
    }
