-- Shot Lab · anonymous usage counters. One row per day per event, holding only a number.
-- No visitor id, no IP, no user agent. Private: only the shotlab-count edge function writes.
-- Applied 25/11/2026 as migration "shotlab_counts". Kept apart from schema.sql, which the game also edits.
create table if not exists public.shotlab_counts (
  day    date not null,
  event  text not null check (event ~ '^[a-z0-9_]{1,24}$'),
  n      integer not null default 0 check (n >= 0),
  primary key (day, event)
);
alter table public.shotlab_counts enable row level security;
revoke all on public.shotlab_counts from anon, authenticated;

-- Adds one to today's counter (Vietnam date) for each event name given. Capped per event per day.
create or replace function public.shotlab_bump(p_events text[])
returns void language sql security definer set search_path = '' as $$
  insert into public.shotlab_counts (day, event, n)
  select (now() at time zone 'Asia/Ho_Chi_Minh')::date, e, 1
  from (select distinct unnest(p_events) as e) s
  where e ~ '^[a-z0-9_]{1,24}$'
  on conflict (day, event) do update set n = public.shotlab_counts.n + 1
  where public.shotlab_counts.n < 200000;
$$;
revoke all on function public.shotlab_bump(text[]) from public, anon, authenticated;
grant execute on function public.shotlab_bump(text[]) to service_role;

-- Reading the numbers:
--   select day, event, n from public.shotlab_counts order by day desc, n desc;
