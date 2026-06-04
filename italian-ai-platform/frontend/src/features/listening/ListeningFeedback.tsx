"use client";
import { Card } from "@/components/ui/Card";
import type { ListeningFeedbackItem } from "@/types/listening";

interface Props {
  score: number;
  feedback: ListeningFeedbackItem[];
  weakPoints: string[];
}

export function ListeningFeedback({ score, feedback, weakPoints }: Props) {
  return (
    <div className="space-y-4">
      <Card>
        <h4 className="font-semibold mb-2">Score: {score}%</h4>
        {weakPoints.length > 0 && (
          <p className="text-sm text-gray-600">Areas to review: {weakPoints.join(", ")}</p>
        )}
      </Card>
      {feedback.map((f) => (
        <Card key={f.question_id}>
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
