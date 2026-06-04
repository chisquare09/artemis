import { Card } from "@/components/ui/Card";
import type { ReviewQueueItem } from "@/types/progress";

interface Props {
  items: ReviewQueueItem[];
}

export function ReviewRecommendationCard({ items }: Props) {
  if (items.length === 0) {
    return (
      <Card>
        <h3 className="font-semibold mb-2">Review Queue</h3>
        <p className="text-sm text-gray-500">No review items yet. Weak points will appear here after exercises.</p>
      </Card>
    );
  }
  return (
    <Card>
      <h3 className="font-semibold mb-2">Review Queue</h3>
      <ul className="text-sm space-y-1">
        {items.map((item, i) => (
          <li key={i} className="flex justify-between">
            <span>{item.target.replace("_", " ")}</span>
            <span className={`text-xs ${item.priority === "high" ? "text-red-500" : item.priority === "medium" ? "text-yellow-600" : "text-green-600"}`}>
              {item.priority}
            </span>
          </li>
        ))}
      </ul>
    </Card>
  );
}
