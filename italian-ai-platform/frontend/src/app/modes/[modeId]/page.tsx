import Link from "next/link";
import { Card } from "@/components/ui/Card";
import { getLevels } from "@/services/curriculum-service";

export const dynamic = "force-dynamic";

const modes = {
  "daily-communication": { title: "Daily Communication", desc: "Practical Italian for everyday situations" },
  "academic-purpose": { title: "Academic Purpose", desc: "Italian for structured study and certification preparation" },
};
const fallbackLevels = ["A1", "A2", "B1", "B2"];

export default async function ModeDetailPage({ params }: { params: Promise<{ modeId: string }> }) {
  const { modeId } = await params;
  const mode = modes[modeId as keyof typeof modes];

  if (!mode) return <div className="text-gray-600">Mode not found</div>;

  let levels = fallbackLevels.map((code, index) => ({ code, name: code, order_index: index + 1 }));
  try {
    levels = await getLevels();
  } catch {
    // Keep fallback levels when backend is unavailable.
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">{mode.title}</h1>
        <p className="text-gray-600">{mode.desc}</p>
      </div>
      <h2 className="text-lg font-semibold">Levels</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {levels.sort((a, b) => a.order_index - b.order_index).map((level) => (
          <Link key={level.code} href={`/levels/${level.code}`}>
            <Card className="text-center hover:border-blue-300 cursor-pointer">
              <span className="font-semibold">{level.code}</span>
              <p className="text-xs text-gray-500 mt-1">{level.name}</p>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
