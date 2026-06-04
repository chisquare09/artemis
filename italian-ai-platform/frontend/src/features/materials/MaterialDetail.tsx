"use client";
import { useState, useEffect } from "react";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { getMaterial } from "@/services/material-service";
import type { MaterialDetail as MaterialDetailType } from "@/types/material";

interface Props {
  materialId: string;
  onClose: () => void;
}

export function MaterialDetail({ materialId, onClose }: Props) {
  const [material, setMaterial] = useState<MaterialDetailType | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getMaterial(materialId).then(setMaterial).catch(() => setError("Could not load material."));
  }, [materialId]);

  if (error) return <Card><p className="text-red-500 text-sm">{error}</p><Button onClick={onClose}>Close</Button></Card>;
  if (!material) return <Card><p className="text-gray-500 text-sm">Loading...</p></Card>;

  return (
    <Card>
      <div className="flex justify-between items-start mb-4">
        <h4 className="font-semibold">{material.title}</h4>
        <Button onClick={onClose}>Close</Button>
      </div>
      <p className="text-sm text-gray-500 mb-4">{material.chunk_count} chunks</p>
      <div className="space-y-2 max-h-64 overflow-y-auto">
        {material.chunks.map((chunk) => (
          <div key={chunk.chunk_index} className="p-2 bg-gray-50 rounded text-sm">
            <span className="text-xs text-gray-400">#{chunk.chunk_index}</span>
            <p>{chunk.content}</p>
          </div>
        ))}
      </div>
    </Card>
  );
}
