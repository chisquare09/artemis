"use client";
import { useState } from "react";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { explainLesson, answerLessonQuestion } from "@/services/ai-chat-service";
import { AIResponseCard } from "./AIResponseCard";
import { LessonQuestionInput } from "./LessonQuestionInput";
import type { AIResponseDisplay } from "@/types/ai";

interface Props {
  unitCode: string;
  studyMode?: string;
}

export function AITutorPanel({ unitCode, studyMode = "daily_communication" }: Props) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [responses, setResponses] = useState<AIResponseDisplay[]>([]);

  const handleExplain = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await explainLesson(unitCode, studyMode);
      setResponses((prev) => [...prev, { type: "explanation", content: res.explanation, provider: res.provider }]);
    } catch {
      setError("Could not reach the AI tutor. Please make sure the backend API is running.");
    } finally {
      setLoading(false);
    }
  };

  const handleQuestion = async (question: string) => {
    setLoading(true);
    setError(null);
    try {
      const res = await answerLessonQuestion(unitCode, question, studyMode);
      setResponses((prev) => [...prev, { type: "answer", content: res.answer, provider: res.provider }]);
    } catch {
      setError("Could not reach the AI tutor. Please make sure the backend API is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card>
      <h3 className="font-semibold mb-2">AI Tutor</h3>
      <p className="text-sm text-gray-500 mb-4">Ask questions about this lesson or request an explanation.</p>
      <div className="space-y-3">
        <Button onClick={handleExplain} disabled={loading}>
          {loading ? "Loading..." : "Explain this lesson"}
        </Button>
        <LessonQuestionInput onSubmit={handleQuestion} disabled={loading} />
        {error && <p className="text-sm text-red-500">{error}</p>}
        {responses.map((r, i) => (
          <AIResponseCard key={i} type={r.type} content={r.content} provider={r.provider} />
        ))}
      </div>
    </Card>
  );
}
