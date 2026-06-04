import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";

interface Props {
  overall: number;
  level: string;
  mode: string;
}

export function ProgressSummary({ overall, level, mode }: Props) {
  return (
    <Card>
      <h3 className="font-semibold mb-3">Overall Progress</h3>
      <ProgressBar label="Completion" value={overall} />
      <p className="text-sm text-gray-600 mt-2">Level: {level}</p>
      <p className="text-sm text-gray-600">Mode: {mode.replace("-", " ")}</p>
    </Card>
  );
}
