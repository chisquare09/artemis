import { apiGet, apiPost } from "./api-client";
import type { MaterialDetail, UnitMaterialsResponse, CreateMaterialParams, LinkMaterialParams } from "@/types/material";

export async function createMaterial(params: CreateMaterialParams): Promise<MaterialDetail> {
  return apiPost("/api/materials", params);
}

export async function getUnitMaterials(unitCode: string): Promise<UnitMaterialsResponse> {
  return apiGet(`/api/materials/units/${unitCode}`);
}

export async function getMaterial(materialId: string): Promise<MaterialDetail> {
  return apiGet(`/api/materials/${materialId}`);
}

export async function linkMaterialToUnit(materialId: string, params: LinkMaterialParams): Promise<{ material_id: string; unit_code: string; linked: boolean }> {
  return apiPost(`/api/materials/${materialId}/link-unit`, params);
}
