"use client";

interface Props {
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}

export function WritingQuestion({ value, onChange, disabled }: Props) {
  return (
    <textarea
      value={value}
      onChange={(e) => onChange(e.target.value)}
      disabled={disabled}
      placeholder="Write your answer..."
      rows={3}
      className="w-full px-3 py-2 border rounded text-sm"
    />
  );
}
