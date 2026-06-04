"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { supabase, isSupabaseConfigured } from "@/lib/supabase";

interface AuthGuardProps {
  children: React.ReactNode;
}

export function AuthGuard({ children }: AuthGuardProps) {
  const router = useRouter();
  // If Supabase not configured, skip auth (dev mode)
  const skipAuth = !isSupabaseConfigured || !supabase;
  const [authorized, setAuthorized] = useState(skipAuth);
  const [checking, setChecking] = useState(!skipAuth);

  useEffect(() => {
    if (skipAuth || !supabase) return;

    supabase.auth.getUser().then(({ data }) => {
      if (data.user) {
        setAuthorized(true);
      } else {
        router.push("/login");
      }
      setChecking(false);
    });

    const { data: listener } = supabase.auth.onAuthStateChange((event) => {
      if (event === "SIGNED_OUT") {
        router.push("/login");
      }
    });

    return () => listener.subscription.unsubscribe();
  }, [router, skipAuth]);

  if (checking) {
    return <div className="flex items-center justify-center min-h-[200px] text-gray-500">Loading...</div>;
  }

  if (!authorized) return null;

  return <>{children}</>;
}
