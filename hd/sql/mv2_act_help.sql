-- v107: đổi công "hái giùm" — mv2_act nhận thêm loại 'help' (tối đa 5 lần/ngày/vườn, như 'water').
-- Chủ vườn đọc sự kiện 'help' qua mv2_inbox như các loại khác; payload {id, k, n} do client ghi, client chủ vườn tự hái liếp đó.
-- Áp bằng Supabase MCP apply_migration (project zgfanxtjdvioxpgpbcke) TRƯỚC khi đưa v107 lên live. Chỉ đổi dòng v_max.
CREATE OR REPLACE FUNCTION public.mv2_act(p_code text, p_secret text, p_other text, p_kind text, p_payload jsonb)
 RETURNS json
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
declare v_me uuid := public.mv2_auth(p_code, p_secret); v_o uuid; v_n int; v_max int; v_day timestamptz := date_trunc('day', now() at time zone 'Asia/Ho_Chi_Minh') at time zone 'Asia/Ho_Chi_Minh';
begin
  if v_me is null then raise exception 'not allowed' using errcode = '42501'; end if;
  select id into v_o from public.mv2_farms where code = upper(trim(p_other));
  if v_o is null or v_o = v_me then raise exception 'no farm'; end if;
  if length(coalesce(p_payload, '{}'::jsonb)::text) > 2000 then raise exception 'bad payload'; end if;
  v_max := case p_kind when 'steal' then 5 when 'water' then 5 when 'help' then 5 when 'gift' then 1 when 'ask' then 1 when 'repay' then 1 when 'visit' then 50 else 0 end;
  if v_max = 0 then raise exception 'bad kind'; end if;
  if p_kind = 'repay' and not exists (select 1 from public.mv2_events where owner = v_me and visitor = v_o and kind = 'steal' and created_at > now() - interval '3 days') then
    return json_build_object('ok', false, 'left', 0);
  end if;
  select count(*) into v_n from public.mv2_events where visitor = v_me and owner = v_o and kind = p_kind and created_at >= v_day;
  if v_n >= v_max then return json_build_object('ok', false, 'left', 0); end if;
  if p_kind = 'visit' and exists (select 1 from public.mv2_events where visitor = v_me and owner = v_o and kind = 'visit' and created_at > now() - interval '20 minutes') then
    return json_build_object('ok', true, 'left', v_max - v_n);
  end if;
  insert into public.mv2_events (owner, visitor, kind, payload) values (v_o, v_me, p_kind, coalesce(p_payload, '{}'::jsonb));
  return json_build_object('ok', true, 'left', v_max - v_n - 1);
end $function$;
