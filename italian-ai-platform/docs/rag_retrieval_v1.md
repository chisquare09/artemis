# RAG Retrieval v1

Keyword-based retrieval over material chunks for AI context augmentation.

## Overview

RAG (Retrieval-Augmented Generation) retrieves relevant learning material chunks to provide context for AI Q&A responses.

## Retrieval Strategy

**Keyword matching** (v1):
- Normalize query: lowercase, remove punctuation, split into terms
- Expand query using bilingual term map
- Score chunks by keyword overlap
- Return top N chunks sorted by score

## Query Expansion Map

English to Italian café terms:
| English | Italian |
|---------|---------|
| bill | conto |
| price | prezzo |
| cost | costa |
| coffee | caffè |
| cappuccino | cappuccino |
| croissant | cornetto |
| please | per favore |
| menu | menu |
| water | acqua |

## API Endpoint

### POST /api/rag/retrieve

```json
{
  "unit_code": "A1.5",
  "query": "How do I ask for the bill?",
  "limit": 5
}
```

Response:
```json
{
  "unit_code": "A1.5",
  "query": "How do I ask for the bill?",
  "chunks": [
    {
      "material_id": "...",
      "material_title": "...",
      "chunk_id": "...",
      "chunk_index": 0,
      "content": "Il conto, per favore.",
      "score": 0.5,
      "metadata": {}
    }
  ],
  "retrieval_strategy": "keyword"
}
```

## Material Chunk Source

Uses material chunks from Step 15 materials ingestion:
- In-memory store when no DATABASE_URL
- Database when configured

## AI Q&A Integration

`answer_lesson_question` automatically:
1. Retrieves top 3 relevant chunks
2. Includes chunk content in prompt context
3. Returns `retrieved_chunks` in `used_context`

## Future Upgrades

- Embeddings (sentence transformers)
- Vector search (pgvector)
- Semantic retrieval
- Hybrid keyword + semantic scoring
