"use client";

interface Props {
  options: string[];
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}

export function MultipleChoiceQuestion({ options, value, onChange, disabled }: Props) {
  return (
    <div className="space-y-2">
      {options.map((opt) => (
        <label key={opt} className="flex items-center gap-2 cursor-pointer">
          <input
            type="radio"
            checked={value === opt}
            onChange={() => onChange(opt)}
            disabled={disabled}
            className="accent-blue-600"
          />
          <span className="text-sm">{opt}</span>
        </label>
      ))}
    </div>
  );
}
