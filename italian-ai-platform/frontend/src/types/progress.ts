export interface SkillProgress {
  listening: number;
  reading: number;
  writing: number;
  speaking: number;
}

export interface ReviewQueueItem {
  unit_code: string;
  skill: string;
  target: string;
  priority: string;
  status: string;
}

export interface ProgressOverview {
  user_id: string;
  active_level: string;
  active_mode: string;
  overall_completion_percentage: number;
  skill_progress: SkillProgress;
  weak_points: string[];
  review_queue: ReviewQueueItem[];
  recent_activity: string[];
}

export interface UnitProgress {
  user_id: string;
  unit_code: string;
  status: string;
  completion_percentage: number;
  mastery_score: number | null;
  completed_activities: number;
  total_activities: number;
  weak_points: string[];
  last_studied_at: string | null;
}

export interface ExerciseResultProgressRequest {
  unit_code: string;
  exercise_id: string;
  score: number;
  weak_points: string[];
  skill_focus: string;
}

export interface ExerciseResultProgressResponse {
  unit_progress: UnitProgress;
  skill_progress: SkillProgress;
  review_items_created: number;
  next_suggested_action: string;
}
