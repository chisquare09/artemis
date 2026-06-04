import { supabase, isSupabaseConfigured } from "@/lib/supabase";
import type { Session, User } from "@supabase/supabase-js";

export async function signIn(email: string, password: string): Promise<{ user: User | null; error: string | null }> {
  if (!supabase) return { user: null, error: "Supabase is not configured" };
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  return { user: data.user, error: error?.message || null };
}

export async function signUp(email: string, password: string): Promise<{ user: User | null; error: string | null }> {
  if (!supabase) return { user: null, error: "Supabase is not configured" };
  const { data, error } = await supabase.auth.signUp({ email, password });
  return { user: data.user, error: error?.message || null };
}

export async function signOut(): Promise<{ error: string | null }> {
  if (!supabase) return { error: "Supabase is not configured" };
  const { error } = await supabase.auth.signOut();
  return { error: error?.message || null };
}

export async function getSession(): Promise<Session | null> {
  if (!supabase) return null;
  const { data } = await supabase.auth.getSession();
  return data.session;
}

export async function getAccessToken(): Promise<string | null> {
  const session = await getSession();
  return session?.access_token || null;
}

export { isSupabaseConfigured };
