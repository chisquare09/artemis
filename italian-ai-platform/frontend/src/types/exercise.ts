export type ExerciseItemType = "multiple_choice" | "fill_blank" | "short_answer" | "short_writing";

export interface ExerciseItem {
  item_id: string;
  item_type: ExerciseItemType;
  prompt: string;
  options?: string[];
  order_index: number;
}

export interface GenerateExerciseResponse {
  exercise_id: string;
  unit_code: string;
  activity_type: string;
  title: string;
  instructions: string;
  items: ExerciseItem[];
  study_mode?: string;
}

export interface SubmitExerciseAnswer {
  item_id: string;
  answer: string;
}

export interface ExerciseItemFeedback {
  item_id: string;
  is_correct: boolean;
  message?: string;
  correct_answer: string;
  explanation: string;
  weak_point?: string;
}

export interface SubmitExerciseResponse {
  exercise_id: string;
  score: number;
  status: string;
  feedback: ExerciseItemFeedback[];
  weak_points: string[];
  explanations: string[];
}
