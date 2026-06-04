"use client";
import { Card } from "@/components/ui/Card";
import type { MaterialSummary } from "@/types/material";

interface Props {
  material: MaterialSummary;
  onSelect?: (id: string) => void;
}

export function MaterialCard({ material, onSelect }: Props) {
  return (
    <Card>
      <div className="cursor-pointer" onClick={() => onSelect?.(material.material_id)}>
        <h4 className="font-medium">{material.title}</h4>
        {material.description && <p className="text-sm text-gray-600 mt-1">{material.description}</p>}
        <div className="flex gap-2 mt-2 text-xs text-gray-500">
          <span>{material.source_type}</span>
          <span>•</span>
          <span>{material.language}</span>
          <span>•</span>
          <span>{material.chunk_count} chunks</span>
        </div>
        {material.tags.length > 0 && (
          <div className="flex gap-1 mt-2">
            {material.tags.map((tag) => (
              <span key={tag} className="px-2 py-0.5 bg-gray-100 rounded text-xs">{tag}</span>
            ))}
          </div>
        )}
      </div>
    </Card>
  );
}
