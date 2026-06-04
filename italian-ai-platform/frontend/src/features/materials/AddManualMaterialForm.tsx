"use client";
import { useState } from "react";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { createMaterial } from "@/services/material-service";

interface Props {
  unitCode: string;
  onCreated: () => void;
}

export function AddManualMaterialForm({ unitCode, onCreated }: Props) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [rawText, setRawText] = useState("");
  const [tags, setTags] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !rawText.trim()) return;
    setLoading(true);
    setError(null);
    try {
      await createMaterial({
        title: title.trim(),
        description: description.trim() || undefined,
        source_type: "manual_text",
        raw_text: rawText.trim(),
        language: "Italian",
        unit_code: unitCode,
        tags: tags.split(",").map((t) => t.trim()).filter(Boolean),
      });
      setTitle("");
      setDescription("");
      setRawText("");
      setTags("");
      onCreated();
    } catch {
      setError("Could not create material.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card>
      <h4 className="font-medium mb-2">Add Manual Material</h4>
      <p className="text-xs text-gray-400 mb-4">Manual text is supported now. PDF, webpage, and YouTube transcript extraction will be added later.</p>
      {error && <p className="text-sm text-red-500 mb-2">{error}</p>}
      <form onSubmit={handleSubmit} className="space-y-3">
        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" className="w-full px-3 py-2 border rounded text-sm" required />
        <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description (optional)" className="w-full px-3 py-2 border rounded text-sm" />
        <textarea value={rawText} onChange={(e) => setRawText(e.target.value)} placeholder="Italian text content" className="w-full px-3 py-2 border rounded text-sm h-24" required />
        <input type="text" value={tags} onChange={(e) => setTags(e.target.value)} placeholder="Tags (comma-separated)" className="w-full px-3 py-2 border rounded text-sm" />
        <Button type="submit" disabled={loading || !title.trim() || !rawText.trim()}>{loading ? "Adding..." : "Add material"}</Button>
      </form>
    </Card>
  );
}
