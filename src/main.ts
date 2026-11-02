import './style.css';
import type { Session } from '@supabase/supabase-js';
import { supabase } from './supabase';
import { fetchProfile, signIn, signOut, signUp } from './auth';

const app = document.querySelector<HTMLDivElement>('#app')!;

type AuthMode = 'signin' | 'signup';

function escapeHtml(text: string) {
  return text.replace(/[&<>"']/g, (c) => `&#${c.charCodeAt(0)};`);
}

function renderAuth(mode: AuthMode, message = '') {
  const isSignup = mode === 'signup';
  app.innerHTML = `
    <main class="screen">
      <h1 class="logo">CONVERSION</h1>
      <form class="card" id="auth-form" novalidate>
        <div class="tabs">
          <button type="button" class="tab ${!isSignup ? 'active' : ''}" data-mode="signin">Sign in</button>
          <button type="button" class="tab ${isSignup ? 'active' : ''}" data-mode="signup">Create account</button>
        </div>
        ${
          isSignup
            ? `<label>Username
                 <input name="username" autocomplete="username" autocapitalize="off" required
                        minlength="3" maxlength="20" pattern="[A-Za-z0-9_]{3,20}" />
               </label>`
            : ''
        }
        <label>Email
          <input name="email" type="email" autocomplete="email" autocapitalize="off" required />
        </label>
        <label>Password
          <input name="password" type="password" minlength="6" required
                 autocomplete="${isSignup ? 'new-password' : 'current-password'}" />
        </label>
        <p class="message" id="message">${escapeHtml(message)}</p>
        <button type="submit" class="primary">${isSignup ? 'Create account' : 'Sign in'}</button>
      </form>
    </main>
  `;

  app.querySelectorAll<HTMLButtonElement>('.tab').forEach((tab) => {
    tab.addEventListener('click', () => renderAuth(tab.dataset.mode as AuthMode));
  });

  const form = app.querySelector<HTMLFormElement>('#auth-form')!;
  const messageEl = app.querySelector<HTMLParagraphElement>('#message')!;
  const submit = form.querySelector<HTMLButtonElement>('button[type="submit"]')!;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const email = String(data.get('email') ?? '').trim();
    const password = String(data.get('password') ?? '');
    const username = String(data.get('username') ?? '').trim();

    messageEl.textContent = '';
    messageEl.classList.remove('success');
    submit.disabled = true;
    try {
      if (isSignup) {
        const { needsConfirmation } = await signUp(email, password, username);
        if (needsConfirmation) {
          renderAuth('signin', `Check ${email} for a confirmation link, then sign in.`);
          app.querySelector('#message')?.classList.add('success');
        }
      } else {
        await signIn(email, password);
      }
      // A successful sign-in triggers onAuthStateChange, which renders home.
    } catch (err) {
      messageEl.textContent = err instanceof Error ? err.message : 'Something went wrong.';
    } finally {
      submit.disabled = false;
    }
  });
}

async function renderHome(session: Session) {
  app.innerHTML = `<main class="screen"><p class="muted">Loading…</p></main>`;
  const profile = await fetchProfile(session.user.id).catch(() => null);
  const name = profile?.display_name ?? profile?.username ?? session.user.email ?? 'Commander';

  app.innerHTML = `
    <main class="screen">
      <h1 class="logo">CONVERSION</h1>
      <section class="card">
        <p class="muted">Signed in as</p>
        <h2>${escapeHtml(name)}</h2>
        ${profile ? `<p class="muted">@${escapeHtml(profile.username)}</p>` : ''}
        <a class="primary button" href="/game/index.html">Play</a>
        <button class="secondary" id="sign-out">Sign out</button>
      </section>
    </main>
  `;

  app.querySelector('#sign-out')!.addEventListener('click', () => {
    signOut().catch((err) => alert(err.message));
  });
}

let currentUserId: string | null | undefined;

function render(session: Session | null) {
  const userId = session?.user.id ?? null;
  if (userId === currentUserId) return; // ignore token refreshes
  currentUserId = userId;
  if (session) renderHome(session);
  else renderAuth('signin');
}

supabase.auth.onAuthStateChange((_event, session) => {
  // Defer so we don't call Supabase from inside its own auth callback.
  setTimeout(() => render(session), 0);
});
