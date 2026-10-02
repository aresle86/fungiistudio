// The approve / reject API behind moderate.html (Supabase can't serve HTML pages itself).
// GET  ?id=…&t=…                → { text, name, city, status }   (the link in the email opens moderate.html,
// POST { id, t, a }             → applies "approve" | "reject"     which calls this; mail scanners can't approve)
import { createClient } from "npm:@supabase/supabase-js@2";
const SB = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const ORIGINS = (Deno.env.get("ALLOWED_ORIGINS") ?? "https://fungiistudio.com,https://www.fungiistudio.com,https://aresle86.github.io").split(",").map((s) => s.trim());
const cors = (req: Request) => {
  const o = req.headers.get("origin") ?? "";
  return { "Access-Control-Allow-Origin": ORIGINS.includes(o) || o.startsWith("http://localhost") ? o : ORIGINS[0],
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS", "Access-Control-Allow-Headers": "content-type, apikey, authorization, x-client-info", "Vary": "Origin" };
};
const json = (req: Request, b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors(req), "content-type": "application/json" } });
const UUID = /^[0-9a-f-]{36}$/i;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors(req) });
  let id = "", t = "", a = "";
  if (req.method === "GET") { const u = new URL(req.url); id = u.searchParams.get("id") ?? ""; t = u.searchParams.get("t") ?? ""; }
  else if (req.method === "POST") { try { const b = await req.json(); id = String(b.id ?? ""); t = String(b.t ?? ""); a = String(b.a ?? ""); } catch { return json(req, { error: "bad_json" }, 400); } }
  else return json(req, { error: "method" }, 405);
  if (!UUID.test(id) || !UUID.test(t)) return json(req, { error: "invalid" }, 400);

  const { data: n } = await SB.from("notes").select("id, text, name, city, paper, status, token").eq("id", id).maybeSingle();
  if (!n || n.token !== t) return json(req, { error: "not_found" }, 404);
  if (req.method === "GET") return json(req, { text: n.text, name: n.name, city: n.city, paper: n.paper, status: n.status });

  if (a !== "approve" && a !== "reject") return json(req, { error: "invalid" }, 400);
  const status = a === "approve" ? "approved" : "rejected";
  const { error } = await SB.from("notes").update({ status, decided_at: new Date().toISOString() }).eq("id", id);
  return error ? json(req, { error: "save_failed" }, 500) : json(req, { ok: true, status });
});
