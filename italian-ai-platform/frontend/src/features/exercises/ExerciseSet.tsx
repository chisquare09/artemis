"use client";
import { useState } from "react";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { generateExercise, submitExercise } from "@/services/exercise-service";
import { submitExerciseProgress } from "@/services/progress-service";
import { ExerciseQuestion } from "./ExerciseQuestion";
import { ExerciseFeedback } from "./ExerciseFeedback";
import type { GenerateExerciseResponse, SubmitExerciseResponse } from "@/types/exercise";

interface Props {
  unitCode: string;
  studyMode?: string;
}

export function ExerciseSet({ unitCode, studyMode = "daily_communication" }: Props) {
  const [exercise, setExercise] = useState<GenerateExerciseResponse | null>(null);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [result, setResult] = useState<SubmitExerciseResponse | null>(null);
  const [nextAction, setNextAction] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async () => {
    setLoading(true);
    setError(null);
    setResult(null);
    setNextAction(null);
    try {
      const data = await generateExercise(unitCode, "quiz", 5, studyMode);
      setExercise(data);
      setAnswers({});
    } catch {
      setError("Could not load exercises. Please make sure the backend API is running.");
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    if (!exercise) return;
    setLoading(true);
    setError(null);
    try {
      const answerList = exercise.items.map((item) => ({ item_id: item.item_id, answer: answers[item.item_id] || "" }));
      const data = await submitExercise(exercise.exercise_id, answerList);
      setResult(data);
      // Update progress
      try {
        const progressResult = await submitExerciseProgress(unitCode, exercise.exercise_id, data.score, data.weak_points, "reading");
        setNextAction(progressResult.next_suggested_action);
      } catch {
        // Progress update failed, but exercise feedback still shows
      }
    } catch {
      setError("Could not submit answers. Please make sure the backend API is running.");
    } finally {
      setLoading(false);
    }
  };

  const modeLabel = studyMode === "academic_purpose" ? "Academic" : "Daily";

  return (
    <Card>
      <h3 className="font-semibold mb-2">Practice Quiz <span className="text-xs text-gray-400">({modeLabel})</span></h3>
      <p className="text-sm text-gray-500 mb-4">Generate and complete a short grammar and vocabulary quiz.</p>
      {error && <p className="text-sm text-red-500 mb-4">{error}</p>}
      {!exercise && (
        <Button onClick={handleGenerate} disabled={loading}>
          {loading ? "Loading..." : "Generate quiz"}
        </Button>
      )}
      {exercise && !result && (
        <div className="space-y-4">
          <p className="text-sm text-gray-600">{exercise.instructions}</p>
          {exercise.items.map((item) => (
            <ExerciseQuestion
              key={item.item_id}
              item={item}
              value={answers[item.item_id] || ""}
              onChange={(v) => setAnswers((prev) => ({ ...prev, [item.item_id]: v }))}
            />
          ))}
          <Button onClick={handleSubmit} disabled={loading}>
            {loading ? "Submitting..." : "Submit answers"}
          </Button>
        </div>
      )}
      {result && (
        <>
          <ExerciseFeedback score={result.score} feedback={result.feedback} weakPoints={result.weak_points} />
          {nextAction && <p className="text-sm text-blue-600 mt-4">{nextAction}</p>}
        </>
      )}
    </Card>
  );
}
