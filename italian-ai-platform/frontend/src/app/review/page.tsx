import { getProgressOverview } from "@/services/progress-service";
import { ReviewRecommendationCard, WeakPointsList } from "@/features/progress";

export const dynamic = "force-dynamic";

export default async function ReviewPage() {
  let data;
  try {
    data = await getProgressOverview();
  } catch {
    return (
      <div className="text-center py-12">
        <h2 className="text-xl font-semibold text-gray-700">Could not load review data</h2>
        <p className="text-gray-500 mt-2">Please make sure the backend API is running.</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Review</h1>
      <ReviewRecommendationCard items={data.review_queue} />
      <WeakPointsList weakPoints={data.weak_points} />
    </div>
  );
}
