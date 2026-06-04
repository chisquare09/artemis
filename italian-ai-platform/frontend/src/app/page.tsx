import Link from "next/link";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { SectionHeader } from "@/components/ui/SectionHeader";

export default function Dashboard() {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Welcome back</h1>
        <p className="text-gray-600">Continue your Italian learning journey</p>
      </div>

      <Card>
        <h3 className="font-semibold text-lg">A1.5 — Food, Café, and Restaurant</h3>
        <p className="text-gray-600 text-sm mt-1">Vertical slice coming soon</p>
        <Link href="/units/A1.5"><Button className="mt-4">Continue lesson</Button></Link>
      </Card>

      <SectionHeader title="Study Modes" />
      <div className="grid md:grid-cols-2 gap-4">
        <Link href="/modes/daily-communication">
          <Card className="hover:border-blue-300 cursor-pointer">
            <h3 className="font-semibold">Daily Communication</h3>
            <p className="text-sm text-gray-600 mt-1">Practical Italian for everyday situations</p>
          </Card>
        </Link>
        <Link href="/modes/academic-purpose">
          <Card className="hover:border-blue-300 cursor-pointer">
            <h3 className="font-semibold">Academic Purpose</h3>
            <p className="text-sm text-gray-600 mt-1">Structured study and certification preparation</p>
          </Card>
        </Link>
      </div>

      <SectionHeader title="Skill Progress" />
      <Card>
        <div className="space-y-3">
          <ProgressBar label="Listening" value={0} />
          <ProgressBar label="Reading" value={0} />
          <ProgressBar label="Writing" value={0} />
          <ProgressBar label="Speaking" value={0} />
        </div>
      </Card>

      <SectionHeader title="Review" />
      <Card><p className="text-gray-500 text-sm">No review items yet</p></Card>
    </div>
  );
}
