"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { supabase, isSupabaseConfigured } from "@/lib/supabase";
import { signOut } from "@/services/auth-service";
import type { User } from "@supabase/supabase-js";

export function AuthStatus() {
  const router = useRouter();
  const skipAuth = !isSupabaseConfigured || !supabase;
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(!skipAuth);

  useEffect(() => {
    if (skipAuth || !supabase) return;

    supabase.auth.getUser().then(({ data }) => {
      setUser(data.user);
      setLoading(false);
    });
    const { data: listener } = supabase.auth.onAuthStateChange((_, session) => {
      setUser(session?.user || null);
    });
    return () => listener.subscription.unsubscribe();
  }, [skipAuth]);

  if (skipAuth || loading) return null;

  async function handleSignOut() {
    await signOut();
    router.push("/login");
    router.refresh();
  }

  if (!user) return null;

  return (
    <div className="flex items-center gap-3 text-sm">
      <span className="text-gray-600">{user.email}</span>
      <button onClick={handleSignOut} className="text-gray-500 hover:text-gray-700">Sign out</button>
    </div>
  );
}
