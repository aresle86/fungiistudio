// POST /functions/v1/feedback-submit  { text, email?, context?, source?, hp? }
// Saves an improvement idea from a tool page (Shot Lab first) and emails it to the studio.
// Public endpoint (verify_jwt off): protected by honeypot, length limits and rate limits.
// Uses the same secrets as note-submit: RESEND_API_KEY, NOTIFY_TO, NOTIFY_FROM, IP_SALT, ALLOWED_ORIGINS
import { createClient } from "npm:@supabase/supabase-js@2";

const SB = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const ORIGINS = (Deno.env.get("ALLOWED_ORIGINS") ?? "https://fungiistudio.com,https://www.fungiistudio.com,https://aresle86.github.io").split(",").map((s) => s.trim());

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
// keeps line breaks in the idea text, strips other control characters
const clean = (v: unknown, max: number, multiline = false) =>
  typeof v === "string"
    ? (multiline ? v.replace(/\r\n?/g, "\n").replace(/[\u0000-\u0009\u000b-\u001f\u007f]/g, " ").replace(/\n{3,}/g, "\n\n") : v.replace(/[\u0000-\u001f\u007f]/g, " ").replace(/\s+/g, " ")).trim().slice(0, max)
    : "";
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
  const text = clean(b.text, 1000, true);
  if (text.length < 3) return json(req, { error: "empty" }, 400);
  const emailRaw = clean(b.email, 120);
  const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailRaw) ? emailRaw : null;
  const context = clean(b.context, 300) || null;
  const source = clean(b.source, 40).toLowerCase().replace(/[^a-z0-9-]/g, "") || "shotlab";

  // rate limit: 3 ideas per visitor per 10 minutes, 10 per day, 40 site-wide per hour
  const ip = (req.headers.get("x-forwarded-for") ?? "").split(",")[0].trim() || "unknown";
  const ip_hash = await sha(ip + (Deno.env.get("IP_SALT") ?? Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "fungii"));
  const since = (ms: number) => new Date(Date.now() - ms).toISOString();
  const [{ count: c10 }, { count: cDay }, { count: cAll }] = await Promise.all([
    SB.from("feedback").select("id", { count: "exact", head: true }).eq("ip_hash", ip_hash).gte("created_at", since(10 * 60e3)),
    SB.from("feedback").select("id", { count: "exact", head: true }).eq("ip_hash", ip_hash).gte("created_at", since(24 * 3600e3)),
    SB.from("feedback").select("id", { count: "exact", head: true }).gte("created_at", since(3600e3)),
  ]);
  if ((c10 ?? 0) >= 3 || (cDay ?? 0) >= 10 || (cAll ?? 0) >= 40) return json(req, { error: "slow_down" }, 429);

  const { data, error } = await SB.from("feedback").insert({ text, email, context, source, ip_hash }).select("id").single();
  if (error || !data) return json(req, { error: "save_failed" }, 500);

  // email the studio (a failed email never loses the idea: it stays in the table)
  const key = Deno.env.get("RESEND_API_KEY"), to = (Deno.env.get("NOTIFY_TO") || "ares.le@gmail.com").split(",").map((s) => s.trim()).filter(Boolean);
  if (key && to.length) {
    const html = `<div style="font-family:Georgia,serif;max-width:560px">
      <p style="font:12px monospace;letter-spacing:.08em">${esc(source.toUpperCase())} · NEW IDEA</p>
      <div style="background:#6EE8FF;border:2px solid #111;padding:18px;font:15px/1.5 monospace;white-space:pre-wrap">${esc(text)}</div>
      <p style="font:13px monospace">${email ? "From " + esc(email) + " (reply to this email to answer)" : "No email left"}</p>
      ${context ? `<p style="font:12px monospace;color:#666">Where they were: ${esc(context)}</p>` : ""}</div>`;
    await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: Deno.env.get("NOTIFY_FROM") ?? "Fungii <onboarding@resend.dev>",
        to, subject: `Shot Lab idea: “${text.replace(/\s+/g, " ").slice(0, 48)}${text.length > 48 ? "…" : ""}”`, html,
        ...(email ? { reply_to: email } : {}),
      }),
    }).then(async (r) => { if (!r.ok) console.error("resend failed", r.status, (await r.text()).slice(0, 300)); })
      .catch((e) => console.error("resend error", String(e)));
  } else console.warn("RESEND_API_KEY is not set: idea saved, no email sent");
  return json(req, { ok: true, id: data.id });
});
