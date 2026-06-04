"use client";
import type { RoleplayTurn } from "@/types/speaking";
import { RoleplayMessage } from "./RoleplayMessage";

interface Props {
  turns: RoleplayTurn[];
}

export function RoleplayChat({ turns }: Props) {
  return (
    <div className="space-y-3 max-h-64 overflow-y-auto p-2 border rounded">
      {turns.map((turn, i) => <RoleplayMessage key={i} turn={turn} />)}
    </div>
  );
}
