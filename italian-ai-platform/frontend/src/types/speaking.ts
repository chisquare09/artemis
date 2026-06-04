export interface RoleplayTurn {
  speaker: string;
  text: string;
}

export interface StartRoleplayResponse {
  session_id: string;
  unit_code: string;
  scenario_id: string;
  title: string;
  system_role: string;
  learner_role: string;
  current_turn: RoleplayTurn;
  turns: RoleplayTurn[];
}

export interface RoleplayFeedback {
  is_appropriate: boolean;
  message: string;
  weak_points: string[];
}

export interface RespondRoleplayResponse {
  session_id: string;
  accepted: boolean;
  feedback: RoleplayFeedback;
  next_turn?: RoleplayTurn;
  is_complete: boolean;
}

export interface FinishRoleplayResponse {
  session_id: string;
  unit_code: string;
  score: number;
  status: string;
  summary: string;
  feedback: RoleplayFeedback[];
  weak_points: string[];
  next_suggested_action: string;
}
