"use client";
import type { ListeningQuestion as LQ } from "@/types/listening";

interface Props {
  question: LQ;
  index: number;
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}

export function ListeningQuestion({ question, index, value, onChange, disabled }: Props) {
  return (
    <div className="space-y-2">
      <p className="font-medium text-sm">{index + 1}. {question.prompt}</p>
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
        placeholder="Type your answer..."
        className="w-full px-3 py-2 border rounded text-sm"
      />
    </div>
  );
}
