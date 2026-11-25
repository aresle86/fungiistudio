// POST /functions/v1/shotlab-count  { e: string[] }
// Anonymous usage counter for Shot Lab. Adds one to today's number for each known event name.
// Stores a date, an event name and a number. It does not read, store or log the visitor's IP,
// user agent or any id. Public endpoint (verify_jwt off): only known event names from the
// site's own pages are counted, and each counter is capped per day.
import { createClient } from "npm:@supabase/supabase-js@2";

const SB = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const ORIGINS = (Deno.env.get("ALLOWED_ORIGINS") ?? "https://fungiistudio.com,https://www.fungiistudio.com,https://aresle86.github.io").split(",").map((s) => s.trim());
const EVENTS = new Set([
  "open", "use",                                   // page loaded · first touch of any control
  "l2", "l3", "l4",                                // a lesson opened
  "l1_out", "l2_end", "l3_end", "l4_end",          // reached the last step of a lesson
  "copy_prompt", "copy_row", "copy_mapref", "save_map", // lesson 01 outputs
  "l2_copy", "l3_copy", "l4_copy",                 // a lesson's text copied
  "kit_on",                                        // the film's lens kit switched on for lesson 01
  "idea_open", "tip",                              // idea form opened · Ko-fi link clicked
]);

function cors(req: Request) {
  const o = req.headers.get("origin") ?? "";
  return {
    "Access-Control-Allow-Origin": ORIGINS.includes(o) ? o : ORIGINS[0],
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type, apikey, authorization, x-client-info",
    "Vary": "Origin",
  };
}
const done = (req: Request, status = 200) =>
  new Response(JSON.stringify({ ok: status === 200 }), { status, headers: { ...cors(req), "content-type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors(req) });
  if (req.method !== "POST") return done(req, 405);
  if (!ORIGINS.includes(req.headers.get("origin") ?? "")) return done(req);   // not from the site: say ok, count nothing
  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return done(req, 400); }
  const list = Array.isArray(b.e) ? b.e : [b.e];
  const events = [...new Set(list.filter((x): x is string => typeof x === "string" && EVENTS.has(x)))].slice(0, 8);
  if (!events.length) return done(req);
  const { error } = await SB.rpc("shotlab_bump", { p_events: events });
  if (error) { console.error("shotlab_bump failed", error.message); return done(req, 500); }
  return done(req);
});
