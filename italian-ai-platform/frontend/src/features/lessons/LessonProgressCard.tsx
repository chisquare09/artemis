import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import type { LessonProgress } from "@/types/lesson";

interface Props {
  progress: LessonProgress;
}

export function LessonProgressCard({ progress }: Props) {
  return (
    <Card>
      <h3 className="font-semibold mb-3">Progress</h3>
      <ProgressBar label="Completion" value={progress.completion_percentage} />
      <p className="text-sm text-gray-500 mt-2">
        Status: {progress.status.replace("_", " ")}
      </p>
    </Card>
  );
}
