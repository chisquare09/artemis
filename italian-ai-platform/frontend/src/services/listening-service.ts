import { apiGet, apiPost } from "./api-client";
import type { ListeningTask, ListeningAnswer, ListeningSubmitResponse } from "@/types/listening";

export async function getListeningTask(unitCode: string): Promise<ListeningTask> {
  return apiGet(`/api/listening/units/${unitCode}`);
}

export async function submitListeningAnswers(unitCode: string, answers: ListeningAnswer[]): Promise<ListeningSubmitResponse> {
  return apiPost("/api/listening/submit", { unit_code: unitCode, answers });
}
