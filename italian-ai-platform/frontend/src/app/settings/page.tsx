import { Card } from "@/components/ui/Card";

export default function SettingsPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Settings</h1>
      <Card>
        <div className="space-y-4">
          <div><span className="text-sm text-gray-600">Active level:</span> <span className="font-medium">A1</span></div>
          <div><span className="text-sm text-gray-600">Active mode:</span> <span className="font-medium">Daily Communication</span></div>
          <div><span className="text-sm text-gray-600">Preferred explanation language:</span> <span className="font-medium">English</span></div>
          <div><span className="text-sm text-gray-600">AI provider:</span> <span className="font-medium text-gray-400">Not configured yet</span></div>
        </div>
      </Card>
    </div>
  );
}
