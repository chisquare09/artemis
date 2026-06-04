"use client";
import type { ExerciseItem } from "@/types/exercise";
import { MultipleChoiceQuestion } from "./MultipleChoiceQuestion";
import { FillBlankQuestion } from "./FillBlankQuestion";
import { ShortAnswerQuestion } from "./ShortAnswerQuestion";
import { WritingQuestion } from "./WritingQuestion";

interface Props {
  item: ExerciseItem;
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}

export function ExerciseQuestion({ item, value, onChange, disabled }: Props) {
  return (
    <div className="space-y-2">
      <p className="font-medium text-sm">{item.order_index}. {item.prompt}</p>
      {item.item_type === "multiple_choice" && item.options && (
        <MultipleChoiceQuestion options={item.options} value={value} onChange={onChange} disabled={disabled} />
      )}
      {item.item_type === "fill_blank" && (
        <FillBlankQuestion value={value} onChange={onChange} disabled={disabled} />
      )}
      {item.item_type === "short_answer" && (
        <ShortAnswerQuestion value={value} onChange={onChange} disabled={disabled} />
      )}
      {item.item_type === "short_writing" && (
        <WritingQuestion value={value} onChange={onChange} disabled={disabled} />
      )}
    </div>
  );
}
