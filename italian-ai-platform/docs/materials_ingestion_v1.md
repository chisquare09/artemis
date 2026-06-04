# Materials Ingestion v1

Learning materials storage and chunking for curriculum units.

## Overview

Materials are linked to curriculum units (e.g., A1.5) and chunked for future RAG retrieval.

## Supported Source Types

| Type | Status |
|------|--------|
| manual_text | Fully supported |
| pdf | Metadata only (extraction later) |
| webpage | Metadata only (crawling later) |
| youtube_transcript | Metadata only (fetching later) |

## API Endpoints

### POST /api/materials
Create a new material.

```json
{
  "title": "Café menu",
  "description": "Practice material",
  "source_type": "manual_text",
  "raw_text": "Caffè espresso 1,20 euro.",
  "unit_code": "A1.5",
  "tags": ["cafe", "menu"]
}
```

### GET /api/materials/units/{unit_code}
List materials for a unit.

### GET /api/materials/{material_id}
Get material detail with chunks.

### POST /api/materials/{material_id}/link-unit
Link material to additional unit.

## Chunking

- Max chunk size: 800 characters
- Preserves sentence boundaries (., !, ?, newline)
- Token count: word count approximation

## Storage

- In-memory store for development
- Database models available when DATABASE_URL configured
- Tests pass without database

## Frontend

- MaterialList: displays materials for unit
- MaterialCard: summary display
- MaterialDetail: shows chunks
- AddManualMaterialForm: create manual_text materials

## Future Steps

- Step 16: RAG retrieval
- Later: embeddings, vector search
- Later: PDF extraction, webpage crawling, YouTube transcript fetching
