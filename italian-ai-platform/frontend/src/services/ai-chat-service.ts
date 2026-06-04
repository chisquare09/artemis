import { apiPost } from "./api-client";
import type { ExplainLessonResponse, AnswerLessonQuestionResponse } from "@/types/ai";

export async function explainLesson(unitCode: string, studyMode?: string): Promise<ExplainLessonResponse> {
  return apiPost("/api/ai/explain-lesson", { unit_code: unitCode, study_mode: studyMode });
}

export async function answerLessonQuestion(unitCode: string, question: string, studyMode?: string): Promise<AnswerLessonQuestionResponse> {
  return apiPost("/api/ai/answer-question", { unit_code: unitCode, question, study_mode: studyMode });
}
