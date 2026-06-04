"use client";
import { useState } from "react";
import { Button } from "@/components/ui/Button";

interface Props {
  onSubmit: (question: string) => void;
  disabled?: boolean;
}

export function LessonQuestionInput({ onSubmit, disabled }: Props) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (question.trim()) {
      onSubmit(question.trim());
      setQuestion("");
    }
  };

  return (
    <div className="flex gap-2">
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about this lesson..."
        className="flex-1 px-3 py-2 border rounded text-sm"
        disabled={disabled}
        onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
      />
      <Button onClick={handleSubmit} disabled={disabled || !question.trim()}>
        Ask
      </Button>
    </div>
  );
}
