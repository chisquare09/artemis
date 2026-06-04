interface Props {
  unitCode: string;
  title: string;
  summary?: string;
}

export function LessonHeader({ unitCode, title, summary }: Props) {
  return (
    <div>
      <h1 className="text-2xl font-bold">{unitCode} — {title}</h1>
      {summary && <p className="text-gray-600 mt-2">{summary}</p>}
    </div>
  );
}
