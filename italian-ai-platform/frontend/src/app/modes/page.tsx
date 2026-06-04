import Link from "next/link";
import { Card } from "@/components/ui/Card";

export default function ModesPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Study Modes</h1>
      <div className="grid md:grid-cols-2 gap-4">
        <Link href="/modes/daily-communication">
          <Card className="hover:border-blue-300 cursor-pointer">
            <h3 className="font-semibold text-lg">Daily Communication</h3>
            <p className="text-sm text-gray-600 mt-2">Focus: listening, speaking, everyday conversation</p>
            <p className="text-sm text-gray-500 mt-2">Topics: café, directions, shopping, travel</p>
          </Card>
        </Link>
        <Link href="/modes/academic-purpose">
          <Card className="hover:border-blue-300 cursor-pointer">
            <h3 className="font-semibold text-lg">Academic Purpose</h3>
            <p className="text-sm text-gray-600 mt-2">Focus: reading, writing, grammar, certification</p>
            <p className="text-sm text-gray-500 mt-2">Tasks: exam-style reading, formal writing, grammar practice</p>
          </Card>
        </Link>
      </div>
    </div>
  );
}
