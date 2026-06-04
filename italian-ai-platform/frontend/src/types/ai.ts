export interface ExplainLessonRequest {
  unit_code: string;
  study_mode?: string;
}

export interface ExplainLessonResponse {
  unit_code: string;
  provider: string;
  explanation: string;
  used_context?: Record<string, unknown>;
}

export interface AnswerLessonQuestionRequest {
  unit_code: string;
  question: string;
  study_mode?: string;
}

export interface AnswerLessonQuestionResponse {
  unit_code: string;
  provider: string;
  answer: string;
  used_context?: Record<string, unknown>;
}

export interface AIResponseDisplay {
  type: "explanation" | "answer";
  content: string;
  provider: string;
}
