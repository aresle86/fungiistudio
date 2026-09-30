// POST /functions/v1/note-submit  { text, name?, city?, email?, paper?, hp? }
// Saves a visitor note as "pending" and emails the studio an approve / reject link.
// Secrets (Supabase → Edge Functions → Secrets): RESEND_API_KEY, NOTIFY_TO (comma-separated), IP_SALT
// Optional: NOTIFY_FROM (defaults to Resend's test sender until the domain is verified), ALLOWED_ORIGINS, SITE_URL
import { createClient } from "npm:@supabase/supabase-js@2";

const SB = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const ORIGINS = (Deno.env.get("ALLOWED_ORIGINS") ?? "https://aresle86.github.io").split(",").map((s) => s.trim());

function cors(req: Request) {
  const o = req.headers.get("origin") ?? "";
  const ok = ORIGINS.includes(o) || o.startsWith("http://localhost");
  return {
    "Access-Control-Allow-Origin": ok ? o : ORIGINS[0],
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type, apikey, authorization, x-client-info",
    "Vary": "Origin",
  };
}
const json = (req: Request, body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...cors(req), "content-type": "application/json" } });
const clean = (v: unknown, max: number) =>
  typeof v === "string" ? v.replace(/[\u0000-\u001f\u007f]/g, " ").replace(/\s+/g, " ").trim().slice(0, max) : "";
const esc = (s: string) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));

async function sha(s: string) {
  const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return Array.from(new Uint8Array(b)).map((x) => x.toString(16).padStart(2, "0")).join("");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors(req) });
  if (req.method !== "POST") return json(req, { error: "method" }, 405);
  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return json(req, { error: "bad_json" }, 400); }

  if (clean(b.hp, 100)) return json(req, { ok: true });            // honeypot filled → a bot; pretend it worked
  const text = clean(b.text, 160);
  if (!text) return json(req, { error: "empty" }, 400);
  const name = clean(b.name, 40) || null, city = clean(b.city, 40) || null;
  const emailRaw = clean(b.email, 120);
  const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailRaw) ? emailRaw : null;
  const paper = Math.min(4, Math.max(0, Number(b.paper) | 0));

  // rate limit: at most 3 notes per visitor per 10 minutes, 20 per day
  const ip = (req.headers.get("x-forwarded-for") ?? "").split(",")[0].trim() || "unknown";
  const ip_hash = await sha(ip + (Deno.env.get("IP_SALT") ?? "fungii"));
  const since = (ms: number) => new Date(Date.now() - ms).toISOString();
  const [{ count: c10 }, { count: cDay }] = await Promise.all([
    SB.from("notes").select("id", { count: "exact", head: true }).eq("ip_hash", ip_hash).gte("created_at", since(10 * 60e3)),
    SB.from("notes").select("id", { count: "exact", head: true }).eq("ip_hash", ip_hash).gte("created_at", since(24 * 3600e3)),
  ]);
  if ((c10 ?? 0) >= 3 || (cDay ?? 0) >= 20) return json(req, { error: "slow_down" }, 429);

  const { data, error } = await SB.from("notes")
    .insert({ text, name, city, email, paper, ip_hash })
    .select("id, token").single();
  if (error || !data) return json(req, { error: "save_failed" }, 500);

  // email the studio (a failed email never loses the note: it stays pending in the table)
  const key = Deno.env.get("RESEND_API_KEY"), to = (Deno.env.get("NOTIFY_TO") ?? "").split(",").map((s) => s.trim()).filter(Boolean);
  if (key && to.length) {
    const site = (Deno.env.get("SITE_URL") ?? "https://aresle86.github.io/fungiistudio/").replace(/\/?$/, "/");
    const base = `${site}moderate.html?id=${data.id}&t=${data.token}`;
    const btn = (href: string, label: string, bg: string) =>
      `<a href="${href}" style="display:inline-block;padding:12px 18px;margin-right:8px;background:${bg};color:#111;border:2px solid #111;font:bold 14px monospace;text-decoration:none">${label}</a>`;
    const html = `<div style="font-family:Georgia,serif;max-width:520px">
      <p style="font:12px monospace;letter-spacing:.08em">THE WALL · NEW NOTE</p>
      <div style="background:#F2FFA0;border:2px solid #111;padding:18px;font:16px/1.45 monospace">${esc(text)}</div>
      <p style="font:13px monospace">— ${esc(name ?? "Anonymous")}${city ? ", " + esc(city) : ""}${email ? " · reply to " + esc(email) : ""}</p>
      <p>${btn(base + "&a=approve", "APPROVE ✓", "#2BD1B0")}${btn(base + "&a=reject", "REJECT ✕", "#FFB8B0")}</p>
      <p style="font:11px monospace;color:#666">Nothing is published until you approve it.</p></div>`;
    await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: Deno.env.get("NOTIFY_FROM") ?? "Fungii wall <onboarding@resend.dev>",
        to, subject: `New note on the wall: “${text.slice(0, 40)}${text.length > 40 ? "…" : ""}”`, html,
        ...(email ? { reply_to: email } : {}),
      }),
    }).catch(() => {});
  }
  return json(req, { ok: true, id: data.id });
});
