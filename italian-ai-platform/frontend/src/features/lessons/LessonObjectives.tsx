import { Card } from "@/components/ui/Card";

const CATEGORY_LABELS: Record<string, string> = {
  communicative_goal: "Communicative Goals",
  grammar: "Grammar",
  vocabulary: "Vocabulary",
  listening: "Listening",
  speaking: "Speaking",
  reading: "Reading",
  writing: "Writing",
  culture: "Culture",
};

interface Props {
  objectives: Record<string, string[]>;
}

export function LessonObjectives({ objectives }: Props) {
  return (
    <div className="grid md:grid-cols-2 gap-4">
      {Object.entries(objectives).map(([key, items]) => (
        <Card key={key}>
          <h4 className="font-semibold text-sm mb-2">{CATEGORY_LABELS[key] || key}</h4>
          <ul className="text-sm text-gray-600 space-y-1">
            {items.map((item) => <li key={item}>• {item}</li>)}
          </ul>
        </Card>
      ))}
    </div>
  );
}
