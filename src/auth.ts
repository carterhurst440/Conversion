import { Capacitor } from '@capacitor/core';
import { supabase, type UserProfile } from './supabase';

export const USERNAME_PATTERN = /^[A-Za-z0-9_]{3,20}$/;

// Where email links (confirmation, later password reset) send people. On the
// web that's the site they signed up on; the iOS app's own origin
// (capacitor://localhost) can't be opened from an email, so use the public site.
function emailRedirectUrl() {
  return Capacitor.isNativePlatform()
    ? import.meta.env.VITE_SITE_URL
    : window.location.origin;
}

export async function signUp(email: string, password: string, username: string) {
  if (!USERNAME_PATTERN.test(username)) {
    throw new Error('Username must be 3–20 letters, numbers or underscores.');
  }

  const { data: available, error: checkError } = await supabase.rpc('username_available', {
    name: username,
  });
  if (checkError) throw checkError;
  if (!available) throw new Error('That username is taken.');

  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: { data: { username }, emailRedirectTo: emailRedirectUrl() },
  });
  if (error) throw error;

  // With email confirmation on, there is no session until the link is clicked.
  return { needsConfirmation: !data.session };
}

export async function signIn(email: string, password: string) {
  const { error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) throw error;
}

export async function signOut() {
  const { error } = await supabase.auth.signOut();
  if (error) throw error;
}

export async function fetchProfile(userId: string): Promise<UserProfile | null> {
  const { data, error } = await supabase
    .from('users')
    .select('id, username, display_name, avatar_url, created_at')
    .eq('id', userId)
    .maybeSingle();
  if (error) throw error;
  return data;
}
