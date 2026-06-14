import { apiGet } from "./api-client";
import type { CurriculumOverview, LevelDetail, UnitDetail, UnitSummary } from "@/types/curriculum";

export async function getCurriculumOverview(): Promise<CurriculumOverview> {
  return apiGet<CurriculumOverview>("/api/curriculum");
}

export async function getLevels(): Promise<LevelDetail[]> {
  return apiGet<LevelDetail[]>("/api/levels");
}

export async function getLevel(levelCode: string): Promise<LevelDetail> {
  return apiGet<LevelDetail>(`/api/levels/${levelCode}`);
}

export async function getLevelUnits(levelCode: string): Promise<UnitSummary[]> {
  return apiGet<UnitSummary[]>(`/api/levels/${levelCode}/units`);
}

export async function getUnit(unitCode: string): Promise<UnitDetail> {
  return apiGet<UnitDetail>(`/api/units/${unitCode}`);
}
