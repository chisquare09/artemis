export interface LessonActivity {
  activity_type: string;
  title: string;
  description?: string;
  skill_focus?: string;
  order_index: number;
}

export interface LessonProgress {
  completion_percentage: number;
  mastery_score: number | null;
  status: string;
}

export interface LessonAIHelperContext {
  unit_code: string;
  level: string;
  title: string;
  summary?: string;
  objective_types: string[];
  note: string;
}

export interface LessonPageData {
  level: string;
  unit_code: string;
  title: string;
  summary?: string;
  objectives: Record<string, string[]>;
  activities: LessonActivity[];
  progress: LessonProgress;
  ai_helper_context: LessonAIHelperContext;
  study_mode: string;
  mode_label: string;
  mode_focus?: string;
  mode_specific_guidance?: string;
}
