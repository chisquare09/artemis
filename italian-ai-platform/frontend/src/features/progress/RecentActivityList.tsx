import { Card } from "@/components/ui/Card";

interface Props {
  activities: string[];
}

export function RecentActivityList({ activities }: Props) {
  if (activities.length === 0) return null;
  return (
    <Card>
      <h3 className="font-semibold mb-2">Recent Activity</h3>
      <ul className="text-sm text-gray-600 space-y-1">
        {activities.map((a, i) => <li key={i}>• {a}</li>)}
      </ul>
    </Card>
  );
}
