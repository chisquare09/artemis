"use client";
import { Card } from "@/components/ui/Card";
import type { FinishRoleplayResponse } from "@/types/speaking";

interface Props {
  result: FinishRoleplayResponse;
}

export function RoleplayFeedback({ result }: Props) {
  return (
    <div className="space-y-4">
      <Card>
        <h4 className="font-semibold mb-2">Score: {result.score}%</h4>
        <p className="text-sm text-gray-600">{result.summary}</p>
        {result.weak_points.length > 0 && (
          <p className="text-sm text-gray-500 mt-2">Areas to review: {result.weak_points.join(", ")}</p>
        )}
        <p className="text-sm text-blue-600 mt-2">{result.next_suggested_action}</p>
      </Card>
    </div>
  );
}
