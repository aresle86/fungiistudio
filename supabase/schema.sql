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

-- Shot Lab · feedback ideas from visitors (private: only the feedback-submit edge function reads or writes)
create table if not exists public.feedback (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  source      text not null default 'shotlab' check (char_length(source) <= 40),
  text        text not null check (char_length(text) between 1 and 1000),
  email       text check (email is null or char_length(email) <= 120),
  context     text check (context is null or char_length(context) <= 300),
  ip_hash     text
);
create index if not exists feedback_created on public.feedback (created_at desc);
create index if not exists feedback_ip_created on public.feedback (ip_hash, created_at desc);
alter table public.feedback enable row level security;
revoke all on public.feedback from anon, authenticated;

-- Miệt Vườn (fungiistudio.com/mietvuon): online farms, no login.
-- Each device registers an id + secret (only the sha256 of the secret is stored).
-- Reads are public; every write goes through the mv_* functions, which check the secret.
-- Friends (made with a farm code via mv_befriend) may write only plots/fps/inv/req/gifts of each other's farm.
create extension if not exists pgcrypto with schema extensions;
create table if not exists public.mv_farms (
  id uuid primary key default gen_random_uuid(), data jsonb,
  code text generated always as (upper(data->>'code')) stored,
  created_at timestamptz not null default now(), updated_at timestamptz not null default now());
create index if not exists mv_farms_code on public.mv_farms (code);
create table if not exists public.mv_keys (id uuid primary key references public.mv_farms(id) on delete cascade, secret_hash text not null, created_at timestamptz not null default now());
alter table public.mv_farms enable row level security;
alter table public.mv_keys enable row level security;
revoke all on public.mv_farms from anon, authenticated;
revoke all on public.mv_keys from anon, authenticated;
grant select on public.mv_farms to anon, authenticated;
drop policy if exists "farms are readable" on public.mv_farms;
create policy "farms are readable" on public.mv_farms for select to anon, authenticated using (true);
-- realtime: alter publication supabase_realtime add table public.mv_farms;
-- functions: mv_merge, mv_ok, mv_register, mv_set, mv_patch, mv_befriend, mv_xom (see migration "mietvuon_farms" in the Supabase dashboard)

-- Miệt Vườn 2.0 (mv2_*): bảng mv2_farms, mv2_follows, mv2_events + các hàm mv2_register, mv2_save, mv2_restore,
-- mv2_peek, mv2_follow, mv2_neighbors, mv2_act, mv2_inbox, mv2_ack. Đã áp dụng bằng migration "mv2_online_farms" (2026-10-29).
-- Bảng khoá RLS, không có policy: mọi truy cập đi qua hàm SECURITY DEFINER kiểm tra mã vườn + mã bí mật.
