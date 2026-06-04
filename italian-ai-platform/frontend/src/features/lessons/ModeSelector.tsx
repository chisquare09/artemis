import Link from "next/link";

interface Props {
  unitCode: string;
  currentMode: string;
}

export function ModeSelector({ unitCode, currentMode }: Props) {
  const isDaily = currentMode === "daily_communication";
  return (
    <div className="flex gap-2 text-sm">
      <Link
        href={`/units/${unitCode}?mode=daily_communication`}
        className={`px-3 py-1 rounded ${isDaily ? "bg-blue-600 text-white" : "bg-gray-100 text-gray-700"}`}
      >
        Daily Communication
      </Link>
      <Link
        href={`/units/${unitCode}?mode=academic_purpose`}
        className={`px-3 py-1 rounded ${!isDaily ? "bg-blue-600 text-white" : "bg-gray-100 text-gray-700"}`}
      >
        Academic Purpose
      </Link>
    </div>
  );
}
