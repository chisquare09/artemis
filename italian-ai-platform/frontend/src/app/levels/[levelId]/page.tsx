import Link from "next/link";
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";

const a1Units = [
  { code: "A1.1", title: "Sounds, Alphabet, and First Contact" },
  { code: "A1.2", title: "Identity and Personal Information" },
  { code: "A1.3", title: "Family and Description" },
  { code: "A1.4", title: "Daily Objects, House, and Location" },
  { code: "A1.5", title: "Food, Café, and Restaurant", available: true },
  { code: "A1.6", title: "Daily Routine" },
  { code: "A1.7", title: "City, Directions, and Transport" },
  { code: "A1.8", title: "Shopping and Clothing" },
  { code: "A1.9", title: "Free Time and Hobbies" },
  { code: "A1.10", title: "Review and A1 Survival Project" },
];

export default async function LevelPage({ params }: { params: Promise<{ levelId: string }> }) {
  const { levelId } = await params;

  if (levelId !== "A1") {
    return <div className="text-gray-600">This level will be added after the A1.5 vertical slice is complete.</div>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">A1 — Beginner / Breakthrough</h1>
        <p className="text-gray-600 mt-2">Handle very simple communication, introduce yourself, ask basic questions, understand slow speech, read signs/menus, and write short personal messages.</p>
      </div>
      <div className="space-y-3">
        {a1Units.map((u) => (
          <Card key={u.code} className={u.available ? "hover:border-blue-300" : "opacity-60"}>
            {u.available ? (
              <Link href={`/units/${u.code}`} className="block">
                <div className="flex justify-between items-center">
                  <span className="font-medium">{u.code} — {u.title}</span>
                  <Badge variant="success">Available</Badge>
                </div>
              </Link>
            ) : (
              <div className="flex justify-between items-center">
                <span className="font-medium">{u.code} — {u.title}</span>
                <Badge>Coming soon</Badge>
              </div>
            )}
          </Card>
        ))}
      </div>
    </div>
  );
}
