export type StudyModeId = "daily-communication" | "academic-purpose";
export type BackendStudyModeId = "daily_communication" | "academic_purpose";
export type CEFRLevel = "A1" | "A2" | "B1" | "B2";

export interface StudyModeSummary {
  code: BackendStudyModeId;
  name: string;
  description?: string;
}

export interface LevelSummary {
  code: CEFRLevel | string;
  name: string;
  order_index: number;
}

export interface CurriculumOverview {
  title: string;
  description?: string;
  language: string;
  version: string;
  levels: LevelSummary[];
  study_modes: StudyModeSummary[];
}

export interface LevelDetail extends LevelSummary {
  goal?: string;
  exit_outcomes: string[];
}

export interface UnitSummary {
  code: string;
  title: string;
  summary?: string;
  order_index: number;
  available?: boolean;
}

export interface ActivitySummary {
  activity_type: string;
  title: string;
  description?: string;
  skill_focus?: string;
  order_index: number;
}

export interface UnitDetail extends UnitSummary {
  level_code: string;
  objectives: Record<string, string[]>;
  activities: ActivitySummary[];
}

export interface ObjectiveGroup {
  category: string;
  items: string[];
}
