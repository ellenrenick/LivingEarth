"""Create one plain Canvas page per review site, each with a button to the interactive site.

Usage: CANVAS_TOKEN=... python3 canvas_pages.py https://kernhigh.instructure.com 330720
Pages are created unpublished (or updated if a page with the same title exists) and added to the
"Review Sites" module. Canvas strips scripts, so the pages hold the content as plain HTML with
answers in collapsible sections. The interactive version is one click away.
"""
import html, json, os, re, ssl, sys, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "HS-LS1-6" / "period_sites"))
import skills13 as S
import build as b13
from units import UNITS

ART = "https://claude.ai/artifact/"
LINKS = {"BOOTCAMP": "LQChiLbgpBaCmCjZSEkuXY", "HS-LS1-2": "8d3xTGiuNvuRgMN4Sf3cUx", "HS-LS2-5": "LGatBgqEsmTPbqLiDHzaJ6",
         ("Renick", "CP", 5): "4fTc7aG4hQxdwAJNtUCrP6", ("Renick", "CP", 7): "MZEHvkJvoc92Gnhg7z2m2E", ("Leapley", "CP", 7): "T85n573o6xiuvL6nFpfJps",
         ("Leapley", "GATE", 5): "GZBEQJQQVuvyhR9MFJvMif", ("Leapley", "GATE", 6): "5sta5YEAimmVdKTVkzangq", ("Boyles", "GATE", 1): "Cy5EkmzuBRjZgDj2vSbDSm",
         ("Boyles", "GATE", 2): "SHZN4s7HjN2Ar2UtJTQE7r", ("Bogner", "CP", 1): "9U7DGUpqUi9mYYR3oaCE5r", ("Bogner", "CP", 2): "SM4uABJ6VKzxAzoSRLcbdB",
         ("Bogner", "CP", 3): "541W1ELwSYXz35aCehwWeC", ("Bogner", "CP", 6): "86QNtp7qcwUMhjFkQuFamG", ("Bogner", "CP", 7): "YKSW81t2Tjh9rZvNpCWdoH"}
# Canvas strips SVG, so each diagram is described in words or a table instead.
FIGS = {
 "BOOTCAMP": "<table border='1' cellpadding='6'><tr><th>Bean plants, 14 days</th><th>Height (cm)</th></tr><tr><td>Sunny window</td><td>15</td></tr><tr><td>Dark closet</td><td>4</td></tr></table>",
 "HS-LS2-5": "<p>Arrows show carbon moving between spheres. Read the start and the end of each arrow.</p><table border='1' cellpadding='6'><tr><th>Arrow</th><th>From</th><th>To</th></tr><tr><td>A</td><td>Atmosphere</td><td>Biosphere</td></tr><tr><td>B</td><td>Biosphere</td><td>Atmosphere</td></tr><tr><td>C</td><td>Atmosphere</td><td>Hydrosphere</td></tr><tr><td>D</td><td>Hydrosphere</td><td>Biosphere</td></tr><tr><td>E</td><td>Biosphere</td><td>Geosphere (rock, soil, coal, oil)</td></tr><tr><td>F</td><td>Geosphere</td><td>Atmosphere</td></tr></table>",
 "13": "<p><b>CO₂ + H₂O + light energy → sugar (only C, H, O) → add N (and S, P) from outside the sugar → amino acids and proteins.</b> Fats and starch are also only C, H, and O.</p>",
}
LET = "ABCDEFGH"
ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt") if os.path.exists("/root/.ccr/ca-bundle.crt") else ssl.create_default_context()


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def question(n, q):
    out = f"<p><b>{n}.</b> {q.get('ctx', '')} {q['q']}</p>"
    ans = ""
    if q.get("type") == "match" or "pairs" in q:
        rights = sorted({p[1] for p in q["pairs"]} | set(q.get("extra", [])))
        out += "<table border='1' cellpadding='6'><tr><th>Item</th><th>Your match</th></tr>" + "".join(f"<tr><td>{l}</td><td>&nbsp;</td></tr>" for l, _ in q["pairs"]) + "</table>"
        out += "<p><b>Choices:</b></p><ul>" + "".join(f"<li>{r}</li>" for r in rights) + "</ul>"
        ans = "<ul>" + "".join(f"<li>{l} → {r}</li>" for l, r in q["pairs"]) + "</ul>"
    else:
        out += "<ol type='A'>" + "".join(f"<li>{o}</li>" for o in q["opts"]) + "</ol>"
        idx = q["a"] if isinstance(q["a"], list) else [q["a"]]
        ans = "<p><b>Answer:</b> " + ", ".join(f"{LET[i]}. {q['opts'][i]}" for i in idx) + "</p>"
    if q.get("type") == "multi":
        out = out.replace("</p>", f" <i>(Choose {len(q['a'])}.)</i></p>", 1)
    return out + f"<details><summary>Show answer</summary>{ans}<p>{q.get('why', '')}</p></details>"


def write_q(i, w):
    o = f"<p><b>{i}.</b> {w.get('ctx', '')}</p><p>{w['q']}</p>"
    if w.get("frames"):
        o += "<ul>" + "".join(f"<li>{f}</li>" for f in w["frames"]) + "</ul>"
    o += "<p><b>Check your own answer:</b></p><ul>" + "".join(f"<li>☐ {c}</li>" for c in w["check"]) + "</ul>"
    return o + f"<details><summary>Show a sample answer (about a 4)</summary><p>{w['sample']}</p></details>"


def button(code):
    u = ART + code
    return (f"<p><a class='Button Button--primary' href='{u}' target='_blank' rel='noopener noreferrer'><b>Open the interactive review site</b></a></p>"
            f"<p>The interactive site checks your answers right away and saves your progress. This page has the same content to read or print. Answers are hidden under “Show answer.”</p>")


def snapshot13(P, D):
    skills = sorted((k for k in P["skills"] if k in S.SKILLS), key=lambda k: P["skills"][k])
    rows = "".join(f"<tr><td>{S.SKILLS[k]['name']}</td><td>{P['skills'][k]}%</td><td>{'▓' * round(P['skills'][k] / 5)}</td><td>{'Reteach' if P['skills'][k] < 50 else 'Practice' if P['skills'][k] < 70 else 'Keep sharp'}</td></tr>" for k in skills)
    out = f"<p><b>{P['n']}</b> students tested · class average <b>{P['avg_pct']}%</b></p><table border='1' cellpadding='6'><tr><th>Skill</th><th>Class got</th><th></th><th>Plan</th></tr>{rows}</table>"
    if any(e["unscored"] for e in P["items"]):
        out += "<p><i>The written answer on test question " + ", ".join(str(e["q"]) for e in P["items"] if e["unscored"]) + " was not scored yet, so it is left out.</i></p>"
    items = S.CP_ITEMS if P["level"] == "CP" else S.GATE_ITEMS
    out += "<h3>Your top 3 targets</h3>"
    for rank, k in enumerate(skills[:3], 1):
        out += f"<h4>Target {rank}: {S.SKILLS[k]['name']} ({P['skills'][k]}%)</h4><ul>"
        for e in sorted((e for e in P["items"] if e["skill"] == k and e["pct"] is not None and not e["unscored"]), key=lambda e: e["pct"]):
            lab, idea = items.get(e["q"], ("Question %d" % e["q"], ""))
            wr = ""
            if e.get("wrong"):
                wr = f" Most common wrong answer ({e['wrong'][0][1]} of {P['n']} students): “{html.escape(b13.short(e['wrong'][0][0]))}”"
            out += f"<li><b>{e['pct']}%</b> · Q{e['q']}. {html.escape(lab)}<br><i>Know this:</i> {html.escape(idea)}{wr}</li>"
        out += "</ul>"
    return out


def render(D, link, fig=None, snap=None, groups=None):
    body = f"<h1>{D['title']}</h1><p><b>{D['eyebrow']}</b></p><p>{D['lede']}</p>" + button(link)
    if snap:
        body += "<h2>Your class results</h2>" + snap
    body += "<h2>Key ideas</h2>"
    if fig:
        body += fig
    body += "<ol>" + "".join(f"<li><b>{i['t']}</b> {i['d']}{('<br><b>' + i['eq'] + '</b>') if i.get('eq') else ''}</li>" for i in D["ideas"]) + "</ol>"
    if D.get("vocab"):
        body += "<h2>Vocabulary</h2><table border='1' cellpadding='6'><tr><th>Word</th><th>Meaning</th></tr>" + "".join(f"<tr><td><b>{w}</b></td><td>{m}</td></tr>" for w, m in D["vocab"]) + "</table>"
        for q in D.get("vocabQuiz", []):
            body += question("V", q)
    n = 0
    body += "<h2>Practice</h2>"
    for q in D.get("practice", []):
        n += 1
        body += question(n, q)
    for g in D.get("groups", []):
        body += f"<h3>{g['title']}</h3><div style='background:#eef3fb;padding:10px 14px;border-radius:6px'>{g['teach']}</div>"
        for q in g["qs"]:
            n += 1
            body += question(n, q)
    if D.get("model"):
        m = D["model"]
        body += f"<h2>{m['title']}</h2><p>{m['sub']}</p>" + (FIGS.get(D["code"]) or m["figure"]) + f"<p><i>{m['caption']}</i></p>"
        for q in m["qs"]:
            n += 1
            body += question(n, q)
    body += "<h2>Explain it</h2><table border='1' cellpadding='6'><tr><th>Score</th><th>What it looks like</th></tr>" + "".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td></tr>" for r in D["rubric"]) + "</table>"
    for i, w in enumerate(D["write"], 1):
        body += write_q(i, w)
    body += "<h2>Ready check</h2><ul>" + "".join(f"<li>☐ {r}</li>" for r in D["ready"]) + "</ul>" + button(link) + f"<p><i>{D['footer']}</i></p>"
    return body


def pages():
    for u in UNITS:
        D = {k: u[k] for k in ("code", "eyebrow", "title", "lede", "footer", "ideas", "vocab", "vocabQuiz", "practice", "model", "rubric", "write", "ready")}
        label = {"BOOTCAMP": "Bootcamp", "HS-LS1-2": "Unit 1.1", "HS-LS2-5": "Unit 1.2"}[u["code"]]
        yield f"{label} Review Site: {u['title']}", render(D, LINKS[u["code"]], fig=None), u["code"]
    for P in json.load(open(HERE.parent / "HS-LS1-6" / "period_sites" / "periods.json")):
        D, skills, focus = b13.unit(P)
        key = (P["teacher"], P["level"], P["period"])
        yield (f"Unit 1.3 Review: {P['teacher']} P{P['period']} ({P['level']})",
               render(D, LINKS[key], fig=FIGS["13"], snap=snapshot13(P, D)), key)


if __name__ == "__main__":
    base, course = sys.argv[1].rstrip("/"), sys.argv[2]
    tok = os.environ.get("CANVAS_TOKEN")
    if "--dump" in sys.argv:
        out = HERE / "canvas_pages_preview"
        out.mkdir(exist_ok=True)
        for t, body, _ in pages():
            (out / (re.sub(r"\W+", "_", t) + ".html")).write_text(body)
        sys.exit()

    def api(method, path, body=None):
        req = urllib.request.Request(base + path, data=json.dumps(body).encode() if body is not None else None, method=method)
        req.add_header("Authorization", "Bearer " + tok); req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=ctx) as r:
            return json.loads(r.read() or "null")
    C = f"/api/v1/courses/{course}"
    existing = {p["title"]: p for p in api("GET", C + "/pages?per_page=100")}
    mod = next(m for m in api("GET", C + "/modules?per_page=50") if m["name"].startswith("Review Sites"))
    items = api("GET", f"{C}/modules/{mod['id']}/items?per_page=100")
    have = {i.get("page_url") for i in items}
    heads = {i["title"] for i in items if i["type"] == "SubHeader"}

    def head(title):
        if title not in heads:
            api("POST", f"{C}/modules/{mod['id']}/items", {"module_item": {"title": title, "type": "SubHeader"}})
            heads.add(title)
    for t, body, key in pages():
        if t in existing:
            pg = api("PUT", f"{C}/pages/{existing[t]['url']}", {"wiki_page": {"body": body}})
        else:
            pg = api("POST", C + "/pages", {"wiki_page": {"title": t, "body": body, "published": False}})
        head("Unit 1.3 CSA Review by Class Period (HS-LS1-6)" if isinstance(key, tuple) else "Unit Reviews: Bootcamp, Unit 1.1, Unit 1.2")
        if pg["url"] not in have:
            api("POST", f"{C}/modules/{mod['id']}/items", {"module_item": {"title": t, "type": "Page", "page_url": pg["url"], "indent": 1 if isinstance(key, tuple) else 0}})
        print("ok", t)
