"use client";

interface Props {
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}

export function FillBlankQuestion({ value, onChange, disabled }: Props) {
  return (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      disabled={disabled}
      placeholder="Type your answer..."
      className="w-full px-3 py-2 border rounded text-sm"
    />
  );
}
