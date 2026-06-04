interface Props {
  mode: string;
}

export function ModeGuidance({ mode }: Props) {
  const isAcademic = mode === "academic_purpose";
  return (
    <p className="text-sm text-gray-500 italic">
      {isAcademic
        ? "Academic mode emphasizes structured grammar, reading comprehension, and writing accuracy."
        : "Daily mode emphasizes practical listening, speaking, and real-life interaction."}
    </p>
  );
}
