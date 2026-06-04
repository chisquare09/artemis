"use client";
import { useState, useEffect, useCallback } from "react";
import { getUnitMaterials } from "@/services/material-service";
import { MaterialCard } from "./MaterialCard";
import { MaterialDetail } from "./MaterialDetail";
import { AddManualMaterialForm } from "./AddManualMaterialForm";
import type { MaterialSummary } from "@/types/material";

interface Props {
  unitCode: string;
}

export function MaterialList({ unitCode }: Props) {
  const [materials, setMaterials] = useState<MaterialSummary[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const loadMaterials = useCallback(() => {
    getUnitMaterials(unitCode).then((data) => setMaterials(data.materials)).catch(() => setError("Could not load materials."));
  }, [unitCode]);

  useEffect(() => { loadMaterials(); }, [loadMaterials]);

  if (error) return <p className="text-sm text-red-500">{error}</p>;

  return (
    <div className="space-y-4">
      <AddManualMaterialForm unitCode={unitCode} onCreated={loadMaterials} />
      {selectedId && <MaterialDetail materialId={selectedId} onClose={() => setSelectedId(null)} />}
      {materials.length === 0 ? (
        <p className="text-sm text-gray-500">No materials yet.</p>
      ) : (
        <div className="space-y-2">
          {materials.map((m) => <MaterialCard key={m.material_id} material={m} onSelect={setSelectedId} />)}
        </div>
      )}
    </div>
  );
}
