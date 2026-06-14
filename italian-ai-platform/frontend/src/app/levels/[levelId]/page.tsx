import Link from "next/link";
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { getLevel, getLevelUnits } from "@/services/curriculum-service";

export const dynamic = "force-dynamic";

export default async function LevelPage({ params }: { params: Promise<{ levelId: string }> }) {
  const { levelId } = await params;

  let level;
  let units = [];
  try {
    [level, units] = await Promise.all([getLevel(levelId), getLevelUnits(levelId)]);
  } catch {
    return (
      <div className="text-gray-600">
        Could not load {levelId}. Please make sure the backend API is running and the curriculum is imported.
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">{level.code} — {level.name}</h1>
        {level.goal && <p className="text-gray-600 mt-2">{level.goal}</p>}
      </div>

      {level.exit_outcomes.length > 0 && (
        <Card>
          <h2 className="font-semibold mb-3">Exit outcomes</h2>
          <ul className="list-disc pl-5 text-sm text-gray-600 space-y-1">
            {level.exit_outcomes.map((outcome) => <li key={outcome}>{outcome}</li>)}
          </ul>
        </Card>
      )}

      <div className="space-y-3">
        {units.map((unit) => (
          <Card key={unit.code} className="hover:border-blue-300">
            <Link href={`/units/${unit.code}`} className="block">
              <div className="flex justify-between gap-4 items-start">
                <div>
                  <span className="font-medium">{unit.code} — {unit.title}</span>
                  {unit.summary && <p className="text-sm text-gray-500 mt-1">{unit.summary}</p>}
                </div>
                <Badge variant="success">Available</Badge>
              </div>
            </Link>
          </Card>
        ))}
      </div>
    </div>
  );
}
