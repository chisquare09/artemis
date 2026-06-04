"use client";
import type { RoleplayTurn } from "@/types/speaking";

interface Props {
  turn: RoleplayTurn;
}

export function RoleplayMessage({ turn }: Props) {
  const isWaiter = turn.speaker === "waiter";
  return (
    <div className={`flex ${isWaiter ? "justify-start" : "justify-end"}`}>
      <div className={`max-w-[80%] px-3 py-2 rounded-lg text-sm ${isWaiter ? "bg-gray-100" : "bg-blue-100"}`}>
        <span className="text-xs text-gray-500 block mb-1">{isWaiter ? "Cameriere" : "You"}</span>
        {turn.text}
      </div>
    </div>
  );
}
