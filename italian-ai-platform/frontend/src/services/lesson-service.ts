import { apiGet } from "./api-client";
import type { LessonPageData } from "@/types/lesson";

export async function getLesson(unitCode: string, studyMode?: string): Promise<LessonPageData> {
  const params = studyMode ? `?study_mode=${studyMode}` : "";
  return apiGet<LessonPageData>(`/api/lessons/${unitCode}${params}`);
}
