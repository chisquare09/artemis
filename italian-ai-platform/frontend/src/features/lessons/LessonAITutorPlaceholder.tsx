import { Card } from "@/components/ui/Card";
import type { LessonAIHelperContext } from "@/types/lesson";

interface Props {
  context: LessonAIHelperContext;
}

export function LessonAITutorPlaceholder({ context }: Props) {
  return (
    <Card>
      <h3 className="font-semibold mb-3">AI Tutor Panel</h3>
      <p className="text-sm text-gray-500">{context.note}</p>
    </Card>
  );
}
