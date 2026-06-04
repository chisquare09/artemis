"use client";
import { Card } from "@/components/ui/Card";

interface Props {
  type: "explanation" | "answer";
  content: string;
  provider: string;
}

export function AIResponseCard({ type, content, provider }: Props) {
  return (
    <Card>
      <div className="text-xs text-gray-400 mb-2">
        {type === "explanation" ? "Lesson Explanation" : "Answer"} · Provider: {provider}
      </div>
      <p className="text-sm text-gray-700 whitespace-pre-wrap">{content}</p>
    </Card>
  );
}
