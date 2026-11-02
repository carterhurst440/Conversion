-- USERS: one public profile row per Supabase auth user.
-- Credentials live in auth.users; this table holds game-facing profile data.

create table public.users (
  id           uuid primary key references auth.users (id) on delete cascade,
  username     text not null,
  display_name text,
  avatar_url   text,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  constraint username_format check (username ~ '^[A-Za-z0-9_]{3,20}$')
);

-- Usernames are unique regardless of case ("Carter" and "carter" collide).
create unique index users_username_lower_key on public.users (lower(username));

alter table public.users enable row level security;

-- Profiles are visible to signed-in players (needed for lobbies, leaderboards).
create policy "Users are readable by signed-in players"
  on public.users for select
  to authenticated
  using (true);

-- Players can edit only their own row; id is fixed.
create policy "Users can update their own row"
  on public.users for update
  to authenticated
  using ((select auth.uid()) = id)
  with check ((select auth.uid()) = id);

-- Inserts happen only through the signup trigger below; no insert/delete policy.

create function public.set_updated_at()
returns trigger
language plpgsql
set search_path = ''
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger users_set_updated_at
  before update on public.users
  for each row execute function public.set_updated_at();

-- Create the profile row when someone signs up. The client passes the chosen
-- username in signUp({ options: { data: { username } } }).
create function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.users (id, username, display_name)
  values (
    new.id,
    new.raw_user_meta_data ->> 'username',
    coalesce(new.raw_user_meta_data ->> 'display_name', new.raw_user_meta_data ->> 'username')
  );
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- Lets the signup form check a username before creating the account.
create function public.username_available(name text)
returns boolean
language sql
stable
security definer
set search_path = ''
as $$
  select not exists (
    select 1 from public.users where lower(username) = lower(name)
  );
$$;

revoke execute on function public.username_available(text) from public;
grant execute on function public.username_available(text) to anon, authenticated;

revoke execute on function public.handle_new_user() from public, anon, authenticated;
