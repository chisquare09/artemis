"use client";
import { Card } from "@/components/ui/Card";
import type { ExerciseItemFeedback } from "@/types/exercise";

interface Props {
  score: number;
  feedback: ExerciseItemFeedback[];
  weakPoints: string[];
}

export function ExerciseFeedback({ score, feedback, weakPoints }: Props) {
  return (
    <div className="space-y-4">
      <Card>
        <h4 className="font-semibold mb-2">Score: {score}%</h4>
        {weakPoints.length > 0 && (
          <p className="text-sm text-gray-600">Areas to review: {weakPoints.join(", ")}</p>
        )}
      </Card>
      {feedback.map((f) => (
        <Card key={f.item_id}>
          <div className={`text-sm font-medium ${f.is_correct ? "text-green-600" : "text-red-600"}`}>
            {f.is_correct ? "✓ Correct" : "✗ Incorrect"}
          </div>
          {!f.is_correct && <p className="text-sm mt-1">Correct answer: {f.correct_answer}</p>}
          <p className="text-sm text-gray-600 mt-1">{f.explanation}</p>
        </Card>
      ))}
    </div>
  );
}
