import { Card } from "@/components/ui/Card";

interface Props {
  weakPoints: string[];
}

export function WeakPointsList({ weakPoints }: Props) {
  if (weakPoints.length === 0) return null;
  return (
    <Card>
      <h3 className="font-semibold mb-2">Areas to Review</h3>
      <ul className="text-sm text-gray-600 space-y-1">
        {weakPoints.map((wp) => <li key={wp}>• {wp.replace("_", " ")}</li>)}
      </ul>
    </Card>
  );
}
