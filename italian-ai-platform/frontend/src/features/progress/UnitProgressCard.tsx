import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import type { UnitProgress } from "@/types/progress";

interface Props {
  progress: UnitProgress;
}

export function UnitProgressCard({ progress }: Props) {
  return (
    <Card>
      <h3 className="font-semibold mb-3">Unit Progress</h3>
      <ProgressBar label="Completion" value={progress.completion_percentage} />
      <p className="text-sm text-gray-600 mt-2">
        Activities: {progress.completed_activities}/{progress.total_activities}
      </p>
      {progress.mastery_score !== null && (
        <p className="text-sm text-gray-600">Mastery: {progress.mastery_score}%</p>
      )}
      <p className="text-sm text-gray-500 mt-1">Status: {progress.status.replace("_", " ")}</p>
    </Card>
  );
}
