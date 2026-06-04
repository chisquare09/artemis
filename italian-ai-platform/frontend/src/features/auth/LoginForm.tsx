"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { signIn, signUp, isSupabaseConfigured } from "@/services/auth-service";
import { Button } from "@/components/ui/Button";

export function LoginForm() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSignUp, setIsSignUp] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (!isSupabaseConfigured) {
    return (
      <div className="p-4 bg-yellow-50 border border-yellow-200 rounded text-yellow-800">
        <p className="font-medium">Supabase not configured</p>
        <p className="text-sm mt-1">Set NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY in your environment.</p>
      </div>
    );
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    const fn = isSignUp ? signUp : signIn;
    const { error } = await fn(email, password);
    setLoading(false);
    if (error) {
      setError(error);
    } else {
      router.push("/");
      router.refresh();
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {error && <div className="p-3 bg-red-50 border border-red-200 text-red-700 text-sm rounded">{error}</div>}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required
          className="w-full px-3 py-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required minLength={6}
          className="w-full px-3 py-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
      </div>
      <Button type="submit" disabled={loading} className="w-full">
        {loading ? "Loading..." : isSignUp ? "Sign Up" : "Sign In"}
      </Button>
      <button type="button" onClick={() => setIsSignUp(!isSignUp)} className="w-full text-sm text-blue-600 hover:underline">
        {isSignUp ? "Already have an account? Sign In" : "Need an account? Sign Up"}
      </button>
    </form>
  );
}
