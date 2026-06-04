import { Card } from "@/components/ui/Card";
import type { LessonActivity } from "@/types/lesson";

interface Props {
  activities: LessonActivity[];
}

export function LessonActivityList({ activities }: Props) {
  const sorted = [...activities].sort((a, b) => a.order_index - b.order_index);
  return (
    <Card>
      <ul className="space-y-2">
        {sorted.map((a, i) => (
          <li key={a.order_index} className="text-sm text-gray-700">
            {i + 1}. {a.title}
          </li>
        ))}
      </ul>
    </Card>
  );
}
