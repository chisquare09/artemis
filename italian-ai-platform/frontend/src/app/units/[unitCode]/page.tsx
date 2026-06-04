import { SectionHeader } from "@/components/ui/SectionHeader";
import { getLesson } from "@/services/lesson-service";
import { getUnitProgress } from "@/services/progress-service";
import {
  LessonHeader,
  LessonObjectives,
  LessonActivityList,
} from "@/features/lessons";
import { AITutorPanel } from "@/features/ai-chat";
import { ExerciseSet } from "@/features/exercises";
import { UnitProgressCard, WeakPointsList } from "@/features/progress";
import { ListeningActivity } from "@/features/listening";
import { SpeakingRoleplay } from "@/features/speaking";
import { MaterialList } from "@/features/materials";
import { ModeSelector } from "@/features/lessons/ModeSelector";
import { ModeGuidance } from "@/features/lessons/ModeGuidance";

interface PageProps {
  params: Promise<{ unitCode: string }>;
  searchParams: Promise<{ mode?: string }>;
}

export default async function UnitPage({ params, searchParams }: PageProps) {
  const { unitCode } = await params;
  const { mode } = await searchParams;
  const studyMode = mode === "academic_purpose" ? "academic_purpose" : "daily_communication";

  let lesson;
  try {
    lesson = await getLesson(unitCode, studyMode);
  } catch {
    return (
      <div className="text-center py-12">
        <h2 className="text-xl font-semibold text-gray-700">Could not load lesson data</h2>
        <p className="text-gray-500 mt-2">Please make sure the backend API is running.</p>
      </div>
    );
  }

  let unitProgress = null;
  if (lesson.unit_code === "A1.5") {
    try {
      unitProgress = await getUnitProgress(lesson.unit_code);
    } catch {
      // Progress fetch failed, continue without it
    }
  }

  return (
    <div className="grid lg:grid-cols-3 gap-6">
      <div className="lg:col-span-2 space-y-6">
        <LessonHeader
          unitCode={lesson.unit_code}
          title={lesson.title}
          summary={lesson.summary}
        />
        <ModeSelector unitCode={lesson.unit_code} currentMode={studyMode} />
        <ModeGuidance mode={studyMode} />
        <SectionHeader title="Objectives" />
        <LessonObjectives objectives={lesson.objectives} />
        <SectionHeader title="Activities" />
        <LessonActivityList activities={lesson.activities} />
        {lesson.unit_code === "A1.5" && (
          <>
            <SectionHeader title="Learning Materials" />
            <MaterialList unitCode={lesson.unit_code} />
            <SectionHeader title="Listening Practice" />
            <ListeningActivity unitCode={lesson.unit_code} />
            <SectionHeader title="Speaking Practice" />
            <SpeakingRoleplay unitCode={lesson.unit_code} />
            <SectionHeader title="Practice Quiz" />
            <ExerciseSet unitCode={lesson.unit_code} studyMode={studyMode} />
          </>
        )}
      </div>
      <div className="space-y-6">
        <AITutorPanel unitCode={lesson.unit_code} studyMode={studyMode} />
        {unitProgress ? (
          <>
            <UnitProgressCard progress={unitProgress} />
            <WeakPointsList weakPoints={unitProgress.weak_points} />
          </>
        ) : (
          <p className="text-sm text-gray-500">Progress tracking available for A1.5</p>
        )}
      </div>
    </div>
  );
}
