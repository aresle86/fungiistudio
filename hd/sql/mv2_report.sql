-- Báo lỗi trong game. Bảng khóa RLS, không ai đọc trực tiếp; game chỉ gọi hàm gửi; trang đọc cần khóa quản trị.
create table if not exists public.mv2_reports (
  id bigserial primary key,
  created_at timestamptz not null default now(),
  code text, verified boolean not null default false,
  kind text not null, msg text, shot text, meta jsonb,
  done boolean not null default false
);
create index if not exists mv2_reports_code_at on public.mv2_reports (code, created_at desc);
create index if not exists mv2_reports_at on public.mv2_reports (created_at desc);
alter table public.mv2_reports enable row level security;

create table if not exists public.mv2_errs (
  sig text primary key,
  msg text, stack text, build text, meta jsonb,
  n int not null default 1,
  first_at timestamptz not null default now(),
  last_at timestamptz not null default now(),
  done boolean not null default false
);
alter table public.mv2_errs enable row level security;

create or replace function public.mv2_report(p_code text, p_secret text, p_kind text, p_msg text, p_shot text, p_meta jsonb)
returns json language plpgsql security definer set search_path to 'public', 'extensions' as $$
declare v_ok boolean; v_code text; v_shot text;
begin
  if p_kind not in ('ket','matdo','hinh','gopy') then raise exception 'bad kind'; end if;
  v_ok := p_code is not null and public.mv2_auth(p_code, p_secret) is not null;
  v_code := case when p_code is null then null else upper(trim(left(p_code, 16))) end;
  if v_ok and (select count(*) from public.mv2_reports where code = v_code and created_at > now() - interval '1 day') >= 5 then raise exception 'limit'; end if;
  if (select count(*) from public.mv2_reports where created_at > now() - interval '1 hour') >= (case when v_ok then 100 else 20 end) then raise exception 'busy'; end if;
  v_shot := case when p_shot like 'data:image/jpeg;base64,%' and length(p_shot) <= 250000 then p_shot end;
  if length(coalesce(p_meta::text, '')) > 4000 then p_meta := null; end if;
  insert into public.mv2_reports (code, verified, kind, msg, shot, meta) values (v_code, v_ok, p_kind, left(p_msg, 600), v_shot, p_meta);
  update public.mv2_reports set shot = null where shot is not null and created_at < now() - interval '60 days';
  return json_build_object('ok', true);
end $$;

create or replace function public.mv2_err(p_sig text, p_msg text, p_stack text, p_build text, p_meta jsonb)
returns void language plpgsql security definer set search_path to 'public', 'extensions' as $$
begin
  if (select count(*) from public.mv2_errs where last_at > now() - interval '1 minute') > 60 then return; end if;
  if (select count(*) from public.mv2_errs) > 2000 and not exists (select 1 from public.mv2_errs where sig = left(p_sig, 120)) then return; end if;
  if length(coalesce(p_meta::text, '')) > 1500 then p_meta := null; end if;
  insert into public.mv2_errs (sig, msg, stack, build, meta) values (left(p_sig, 120), left(p_msg, 300), left(p_stack, 1500), left(p_build, 16), p_meta)
  on conflict (sig) do update set n = public.mv2_errs.n + 1, last_at = now(), build = excluded.build, meta = excluded.meta, done = false;
end $$;

create or replace function public.mv2_admin_ok(p_key text) returns boolean language sql immutable security definer set search_path to 'public', 'extensions' as $$
  select encode(extensions.digest(coalesce(p_key, ''), 'sha256'), 'hex') = '1682ef270abf3c0eb8f7d17ed190bd324bb4fdd740856cfe0cb35788e4e5e004'
$$;

create or replace function public.mv2_admin_list(p_key text) returns json language plpgsql stable security definer set search_path to 'public', 'extensions' as $$
begin
  if not public.mv2_admin_ok(p_key) then raise exception 'denied'; end if;
  return json_build_object(
    'reports', (select coalesce(json_agg(r), '[]') from (select id, created_at, code, verified, kind, msg, shot, meta, done from public.mv2_reports order by done, created_at desc limit 100) r),
    'errs', (select coalesce(json_agg(e), '[]') from (select sig, msg, stack, build, meta, n, first_at, last_at, done from public.mv2_errs order by done, last_at desc limit 100) e));
end $$;

create or replace function public.mv2_admin_done(p_key text, p_tbl text, p_id text, p_done boolean) returns void language plpgsql security definer set search_path to 'public', 'extensions' as $$
begin
  if not public.mv2_admin_ok(p_key) then raise exception 'denied'; end if;
  if p_tbl = 'reports' then update public.mv2_reports set done = p_done where id = p_id::bigint;
  elsif p_tbl = 'errs' then update public.mv2_errs set done = p_done where sig = p_id; end if;
end $$;
