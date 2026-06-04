import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import type { SkillProgress } from "@/types/progress";

interface Props {
  skills: SkillProgress;
}

export function SkillProgressCard({ skills }: Props) {
  return (
    <Card>
      <h3 className="font-semibold mb-3">Skills</h3>
      <div className="space-y-2">
        <ProgressBar label="Listening" value={skills.listening} />
        <ProgressBar label="Reading" value={skills.reading} />
        <ProgressBar label="Writing" value={skills.writing} />
        <ProgressBar label="Speaking" value={skills.speaking} />
      </div>
    </Card>
  );
}
