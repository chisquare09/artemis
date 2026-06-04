interface SectionHeaderProps {
  title: string;
  subtitle?: string;
}

export function SectionHeader({ title, subtitle }: SectionHeaderProps) {
  return (
    <div className="mb-4">
      <h2 className="text-xl font-semibold text-gray-900">{title}</h2>
      {subtitle && <p className="text-gray-600 mt-1">{subtitle}</p>}
    </div>
  );
}
