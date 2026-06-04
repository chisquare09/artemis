import { apiPost } from "./api-client";
import type { GenerateExerciseResponse, SubmitExerciseAnswer, SubmitExerciseResponse } from "@/types/exercise";

export async function generateExercise(unitCode: string, activityType = "quiz", count = 5, studyMode = "daily_communication"): Promise<GenerateExerciseResponse> {
  return apiPost("/api/exercises/generate", { unit_code: unitCode, activity_type: activityType, count, study_mode: studyMode });
}

export async function submitExercise(exerciseId: string, answers: SubmitExerciseAnswer[]): Promise<SubmitExerciseResponse> {
  return apiPost("/api/exercises/submit", { exercise_id: exerciseId, answers });
}
