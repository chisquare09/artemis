export type StudyModeId = "daily-communication" | "academic-purpose";
export type CEFRLevel = "A1" | "A2" | "B1" | "B2";

export interface UnitSummary {
  code: string;
  title: string;
  available: boolean;
}

export interface ObjectiveGroup {
  category: string;
  items: string[];
}
