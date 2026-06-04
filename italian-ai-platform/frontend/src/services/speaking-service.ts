import { apiPost } from "./api-client";
import type { StartRoleplayResponse, RespondRoleplayResponse, FinishRoleplayResponse } from "@/types/speaking";

export async function startRoleplay(unitCode: string, scenarioId = "cafe_ordering"): Promise<StartRoleplayResponse> {
  return apiPost("/api/speaking/roleplay/start", { unit_code: unitCode, scenario_id: scenarioId });
}

export async function respondRoleplay(sessionId: string, message: string): Promise<RespondRoleplayResponse> {
  return apiPost("/api/speaking/roleplay/respond", { session_id: sessionId, message });
}

export async function finishRoleplay(sessionId: string): Promise<FinishRoleplayResponse> {
  return apiPost("/api/speaking/roleplay/finish", { session_id: sessionId });
}
