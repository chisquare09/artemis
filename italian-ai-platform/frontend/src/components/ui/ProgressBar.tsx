interface ProgressBarProps {
  value: number;
  label?: string;
  className?: string;
}

export function ProgressBar({ value, label, className = "" }: ProgressBarProps) {
  return (
    <div className={className}>
      {label && <div className="text-sm text-gray-600 mb-1">{label}</div>}
      <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
        <div className="h-full bg-blue-600 rounded-full" style={{ width: `${value}%` }} />
      </div>
    </div>
  );
}
