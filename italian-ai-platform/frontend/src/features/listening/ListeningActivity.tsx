"use client";
import { useState, useEffect } from "react";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { getListeningTask, submitListeningAnswers } from "@/services/listening-service";
import { ListeningQuestion } from "./ListeningQuestion";
import { ListeningFeedback } from "./ListeningFeedback";
import type { ListeningTask, ListeningSubmitResponse } from "@/types/listening";

interface Props {
  unitCode: string;
}

export function ListeningActivity({ unitCode }: Props) {
  const [task, setTask] = useState<ListeningTask | null>(null);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [result, setResult] = useState<ListeningSubmitResponse | null>(null);
  const [showTranscript, setShowTranscript] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getListeningTask(unitCode)
      .then((data) => { setTask(data); setLoading(false); })
      .catch(() => { setError("Could not load listening activity."); setLoading(false); });
  }, [unitCode]);

  const handleSubmit = async () => {
    if (!task) return;
    setLoading(true);
    try {
      const answerList = task.questions.map((q) => ({ question_id: q.question_id, answer: answers[q.question_id] || "" }));
      const data = await submitListeningAnswers(unitCode, answerList);
      setResult(data);
    } catch {
      setError("Could not submit listening answers.");
    } finally {
      setLoading(false);
    }
  };

  if (loading && !task) return <Card><p className="text-sm text-gray-500">Loading...</p></Card>;
  if (error) return <Card><p className="text-sm text-red-500">{error}</p></Card>;
  if (!task) return null;

  return (
    <Card>
      <h3 className="font-semibold mb-2">{task.title}</h3>
      <p className="text-sm text-gray-500 mb-2">{task.instructions}</p>
      <p className="text-xs text-gray-400 mb-4">Audio playback will be added later. For now, use the transcript-based listening practice.</p>
      <Button onClick={() => setShowTranscript(!showTranscript)} variant="secondary">
        {showTranscript ? "Hide transcript" : "Show transcript"}
      </Button>
      {showTranscript && (
        <pre className="mt-4 p-3 bg-gray-50 rounded text-sm whitespace-pre-wrap">{task.transcript}</pre>
      )}
      {!result && (
        <div className="mt-4 space-y-4">
          {task.questions.map((q, i) => (
            <ListeningQuestion
              key={q.question_id}
              question={q}
              index={i}
              value={answers[q.question_id] || ""}
              onChange={(v) => setAnswers((prev) => ({ ...prev, [q.question_id]: v }))}
            />
          ))}
          <Button onClick={handleSubmit} disabled={loading}>
            {loading ? "Submitting..." : "Submit answers"}
          </Button>
        </div>
      )}
      {result && <ListeningFeedback score={result.score} feedback={result.feedback} weakPoints={result.weak_points} />}
    </Card>
  );
}
