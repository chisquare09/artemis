"use client";
import { useState } from "react";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { startRoleplay, respondRoleplay, finishRoleplay } from "@/services/speaking-service";
import { RoleplayChat } from "./RoleplayChat";
import { RoleplayFeedback } from "./RoleplayFeedback";
import type { RoleplayTurn, FinishRoleplayResponse, RoleplayFeedback as Feedback } from "@/types/speaking";

interface Props {
  unitCode: string;
}

export function SpeakingRoleplay({ unitCode }: Props) {
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [turns, setTurns] = useState<RoleplayTurn[]>([]);
  const [message, setMessage] = useState("");
  const [lastFeedback, setLastFeedback] = useState<Feedback | null>(null);
  const [result, setResult] = useState<FinishRoleplayResponse | null>(null);
  const [isComplete, setIsComplete] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleStart = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await startRoleplay(unitCode);
      setSessionId(data.session_id);
      setTurns(data.turns);
    } catch {
      setError("Could not start speaking roleplay.");
    } finally {
      setLoading(false);
    }
  };

  const handleSend = async () => {
    if (!sessionId || !message.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const data = await respondRoleplay(sessionId, message.trim());
      setLastFeedback(data.feedback);
      setTurns((prev) => [...prev, { speaker: "learner", text: message.trim() }, ...(data.next_turn ? [data.next_turn] : [])]);
      setMessage("");
      setIsComplete(data.is_complete);
    } catch {
      setError("Could not send your response.");
    } finally {
      setLoading(false);
    }
  };

  const handleFinish = async () => {
    if (!sessionId) return;
    setLoading(true);
    try {
      const data = await finishRoleplay(sessionId);
      setResult(data);
    } catch {
      setError("Could not finish roleplay.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card>
      <h3 className="font-semibold mb-2">Speaking Roleplay</h3>
      <p className="text-sm text-gray-500 mb-2">{unitCode === "A1.5" ? "Practice ordering at an Italian café." : "Practice a short Italian conversation for this unit."}</p>
      <p className="text-xs text-gray-400 mb-4">Voice practice will be added later. For now, this is text-based speaking roleplay.</p>
      {error && <p className="text-sm text-red-500 mb-4">{error}</p>}
      {!sessionId && !result && (
        <Button onClick={handleStart} disabled={loading}>{loading ? "Starting..." : "Start roleplay"}</Button>
      )}
      {sessionId && !result && (
        <div className="space-y-4">
          <RoleplayChat turns={turns} />
          {lastFeedback && (
            <p className={`text-sm ${lastFeedback.is_appropriate ? "text-green-600" : "text-yellow-600"}`}>{lastFeedback.message}</p>
          )}
          {!isComplete && (
            <div className="flex gap-2">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type your response in Italian..."
                className="flex-1 px-3 py-2 border rounded text-sm"
                onKeyDown={(e) => e.key === "Enter" && handleSend()}
              />
              <Button onClick={handleSend} disabled={loading || !message.trim()}>Send</Button>
            </div>
          )}
          {isComplete && <Button onClick={handleFinish} disabled={loading}>Finish roleplay</Button>}
        </div>
      )}
      {result && <RoleplayFeedback result={result} />}
    </Card>
  );
}
