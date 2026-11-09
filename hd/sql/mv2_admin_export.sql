-- Sao lưu: xuất nguyên một bảng (hoặc định nghĩa hàm, cấu trúc cột) ra JSON.
-- Chỉ đọc. Cần khóa quản trị (hd/.baoloi-key), giống mv2_admin_stats.
-- Gọi từ hd/saoluu.py.
create or replace function public.mv2_admin_export(p_key text, p_tbl text)
returns json
language plpgsql
stable security definer
set search_path to 'public', 'extensions'
as $$
declare r json;
begin
  if not public.mv2_admin_ok(p_key) then
    raise exception 'not allowed' using errcode = '42501';
  end if;

  if p_tbl = '_functions' then
    select coalesce(json_agg(json_build_object(
             'name', p.proname,
             'args', pg_get_function_identity_arguments(p.oid),
             'def',  pg_get_functiondef(p.oid)) order by p.proname), '[]'::json)
      into r
      from pg_proc p join pg_namespace n on n.oid = p.pronamespace
     where n.nspname = 'public' and p.prokind = 'f';
    return r;
  end if;

  if p_tbl = '_schema' then
    select coalesce(json_agg(json_build_object(
             'table', table_name, 'column', column_name, 'type', data_type,
             'nullable', is_nullable, 'default', column_default)
             order by table_name, ordinal_position), '[]'::json)
      into r
      from information_schema.columns
     where table_schema = 'public';
    return r;
  end if;

  if p_tbl not in ('mv2_farms', 'mv2_events', 'mv2_steps', 'mv2_reports', 'mv2_days',
                   'mv2_errs', 'mv2_follows', 'feedback', 'notes', 'mv_farms', 'mv_keys') then
    raise exception 'bad table';
  end if;

  execute format('select coalesce(json_agg(t), ''[]''::json) from public.%I t', p_tbl) into r;
  return r;
end $$;

revoke all on function public.mv2_admin_export(text, text) from public;
grant execute on function public.mv2_admin_export(text, text) to anon, authenticated;
