import Link from "next/link";
import { Card } from "@/components/ui/Card";

const modes = {
  "daily-communication": { title: "Daily Communication", desc: "Practical Italian for everyday situations" },
  "academic-purpose": { title: "Academic Purpose", desc: "Italian for structured study and certification preparation" },
};
const levels = ["A1", "A2", "B1", "B2"];

export default async function ModeDetailPage({ params }: { params: Promise<{ modeId: string }> }) {
  const { modeId } = await params;
  const mode = modes[modeId as keyof typeof modes];

  if (!mode) return <div className="text-gray-600">Mode not found</div>;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">{mode.title}</h1>
        <p className="text-gray-600">{mode.desc}</p>
      </div>
      <h2 className="text-lg font-semibold">Levels</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {levels.map((l) => (
          <Link key={l} href={`/levels/${l}`}>
            <Card className="text-center hover:border-blue-300 cursor-pointer">
              <span className="font-semibold">{l}</span>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
