import { apiGet, apiPost } from "./api-client";
import type { ProgressOverview, UnitProgress, ExerciseResultProgressResponse } from "@/types/progress";

export async function getProgressOverview(): Promise<ProgressOverview> {
  return apiGet("/api/progress/overview");
}

export async function getUnitProgress(unitCode: string): Promise<UnitProgress> {
  return apiGet(`/api/progress/units/${unitCode}`);
}

export async function submitExerciseProgress(
  unitCode: string,
  exerciseId: string,
  score: number,
  weakPoints: string[],
  skillFocus = "reading"
): Promise<ExerciseResultProgressResponse> {
  return apiPost("/api/progress/exercise-result", {
    unit_code: unitCode,
    exercise_id: exerciseId,
    score,
    weak_points: weakPoints,
    skill_focus: skillFocus,
  });
}
