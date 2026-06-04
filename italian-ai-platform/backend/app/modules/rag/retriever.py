from app.modules.rag.query_utils import normalize, expand_query
from app.modules.materials import service as materials_service


def score_chunk(query_terms: list[str], chunk_content: str) -> float:
    content_terms = set(normalize(chunk_content))
    if not content_terms:
        return 0.0
    matches = sum(1 for t in query_terms if t in content_terms)
    return matches / len(query_terms) if query_terms else 0.0


def retrieve_chunks(unit_code: str, query: str, limit: int = 5) -> list[dict]:
    query_terms = normalize(query)
    expanded_terms = expand_query(query_terms)

    try:
        unit_materials = materials_service.get_unit_materials(unit_code)
    except Exception:
        return []

    all_chunks = []
    for mat in unit_materials.get("materials", []):
        try:
            detail = materials_service.get_material(mat["material_id"])
        except Exception:
            continue
        for chunk in detail.get("chunks", []):
            score = score_chunk(expanded_terms, chunk["content"])
            all_chunks.append({
                "material_id": mat["material_id"],
                "material_title": mat["title"],
                "chunk_id": f"{mat['material_id']}_{chunk['chunk_index']}",
                "chunk_index": chunk["chunk_index"],
                "content": chunk["content"],
                "score": round(score, 3),
                "metadata": {},
            })

    with_scores = [c for c in all_chunks if c["score"] > 0]
    if not with_scores:
        return []
    with_scores.sort(key=lambda c: c["score"], reverse=True)
    return with_scores[:limit]
