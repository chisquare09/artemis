import { SectionHeader } from "@/components/ui/SectionHeader";
import { getProgressOverview } from "@/services/progress-service";
import {
  ProgressSummary,
  SkillProgressCard,
  WeakPointsList,
  ReviewRecommendationCard,
  RecentActivityList,
} from "@/features/progress";

export const dynamic = "force-dynamic";

export default async function ProgressPage() {
  let data;
  try {
    data = await getProgressOverview();
  } catch {
    return (
      <div className="text-center py-12">
        <h2 className="text-xl font-semibold text-gray-700">Could not load progress</h2>
        <p className="text-gray-500 mt-2">Please make sure the backend API is running.</p>
      </div>
    );
  }

  const isEmpty = data.overall_completion_percentage === 0 && data.recent_activity.length === 0;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Progress</h1>
      {isEmpty ? (
        <p className="text-gray-500">No progress yet. Complete an exercise to start tracking your learning.</p>
      ) : (
        <>
          <SectionHeader title="Overall" />
          <ProgressSummary overall={data.overall_completion_percentage} level={data.active_level} mode={data.active_mode} />
          <SectionHeader title="Skills" />
          <SkillProgressCard skills={data.skill_progress} />
          <SectionHeader title="Weak Points" />
          <WeakPointsList weakPoints={data.weak_points} />
          <SectionHeader title="Review Queue" />
          <ReviewRecommendationCard items={data.review_queue} />
          <SectionHeader title="Recent Activity" />
          <RecentActivityList activities={data.recent_activity} />
        </>
      )}
    </div>
  );
}
