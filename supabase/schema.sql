-- Fungii · the wall (visitor notes)
-- Run once in Supabase → SQL Editor. Safe to re-run.

create extension if not exists pgcrypto;

create table if not exists public.notes (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  text        text not null check (char_length(text) between 1 and 160),
  name        text check (name is null or char_length(name) <= 40),
  city        text check (city is null or char_length(city) <= 40),
  email       text check (email is null or char_length(email) <= 120),   -- private: never exposed to the site
  paper       smallint not null default 0 check (paper between 0 and 4),
  status      text not null default 'pending' check (status in ('pending','approved','rejected')),
  token       uuid not null default gen_random_uuid(),                   -- private: signs the approve/reject link
  ip_hash     text,                                                      -- private: salted hash, for rate limiting only
  decided_at  timestamptz
);
create index if not exists notes_status_created on public.notes (status, created_at desc);
create index if not exists notes_ip_created on public.notes (ip_hash, created_at desc);

alter table public.notes enable row level security;

-- the website (anon / publishable key) may read ONLY approved notes, and ONLY the public columns.
-- all writes go through the edge functions, which use the service role.
revoke all on public.notes from anon, authenticated;
grant select (id, created_at, text, name, city, paper) on public.notes to anon, authenticated;

drop policy if exists "approved notes are public" on public.notes;
create policy "approved notes are public" on public.notes
  for select to anon, authenticated
  using (status = 'approved');
