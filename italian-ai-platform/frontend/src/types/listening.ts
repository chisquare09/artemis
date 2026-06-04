export interface ListeningQuestion {
  question_id: string;
  question_type: string;
  prompt: string;
  options?: string[];
}

export interface ListeningTask {
  unit_code: string;
  title: string;
  instructions: string;
  transcript: string;
  show_transcript_by_default: boolean;
  questions: ListeningQuestion[];
}

export interface ListeningAnswer {
  question_id: string;
  answer: string;
}

export interface ListeningFeedbackItem {
  question_id: string;
  is_correct: boolean;
  message?: string;
  correct_answer: string;
  explanation: string;
  weak_point?: string;
}

export interface ListeningSubmitResponse {
  unit_code: string;
  score: number;
  status: string;
  feedback: ListeningFeedbackItem[];
  weak_points: string[];
  next_suggested_action: string;
}
