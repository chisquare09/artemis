export interface MaterialChunk {
  chunk_index: number;
  content: string;
  token_count: number;
}

export interface MaterialSummary {
  material_id: string;
  title: string;
  description: string | null;
  source_type: string;
  source_url: string | null;
  language: string;
  tags: string[];
  chunk_count: number;
}

export interface MaterialDetail extends MaterialSummary {
  unit_code: string;
  chunks: MaterialChunk[];
}

export interface UnitMaterialsResponse {
  unit_code: string;
  materials: MaterialSummary[];
}

export interface CreateMaterialParams {
  title: string;
  description?: string;
  source_type: string;
  source_url?: string;
  language?: string;
  raw_text?: string;
  level_code?: string;
  unit_code: string;
  tags?: string[];
}

export interface LinkMaterialParams {
  unit_code: string;
  purpose?: string;
}
