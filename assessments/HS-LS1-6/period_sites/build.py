"""Build one Unit 1.3 review site per class period from periods.json.  Run: python3 build.py"""
import html, json, sys
from pathlib import Path

HERE = Path(__file__).parent
RS = HERE.parent.parent / "review_sites"
sys.path.insert(0, str(RS))
import skills13 as S

css = (RS / "engine.css").read_text().replace("--accent:#1f5fbf;", "--accent:#7a4bb8;", 1)
css = css.replace("--accent:#7db0ff;", "--accent:#c3a2f0;")  # dark-theme accent (same hue)
js = (RS / "engine.js").read_text()
esc = lambda s: html.escape(s, quote=True)
OUT = HERE / "sites"

FIGURE = """<svg viewBox="0 0 640 230" role="img" aria-label="Flow from light, carbon dioxide and water to sugar, then sugar plus nitrogen to amino acids and proteins">
<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker></defs>
<g style="color:var(--fg)" font-family="system-ui,sans-serif" font-size="14" fill="var(--fg)">
<rect x="8" y="20" width="150" height="62" rx="10" fill="var(--accent-soft)" stroke="var(--line)"/><text x="83" y="46" text-anchor="middle" font-weight="700">CO₂ + H₂O</text><text x="83" y="66" text-anchor="middle" font-size="12" fill="var(--muted)">atoms from air and water</text>
<rect x="8" y="130" width="150" height="40" rx="10" fill="var(--warn-soft)" stroke="var(--line)"/><text x="83" y="155" text-anchor="middle" font-weight="700">Light energy</text>
<rect x="240" y="60" width="150" height="70" rx="10" fill="var(--good-soft)" stroke="var(--line)"/><text x="315" y="88" text-anchor="middle" font-weight="700">Sugar (glucose)</text><text x="315" y="108" text-anchor="middle" font-size="12" fill="var(--muted)">only C, H, and O</text>
<rect x="480" y="20" width="152" height="62" rx="10" fill="var(--accent-soft)" stroke="var(--line)"/><text x="556" y="46" text-anchor="middle" font-weight="700">Amino acids</text><text x="556" y="66" text-anchor="middle" font-size="12" fill="var(--muted)">C, H, O + N (and S)</text>
<rect x="480" y="130" width="152" height="62" rx="10" fill="var(--accent-soft)" stroke="var(--line)"/><text x="556" y="156" text-anchor="middle" font-weight="700">Fats, starch</text><text x="556" y="176" text-anchor="middle" font-size="12" fill="var(--muted)">only C, H, and O</text>
<rect x="400" y="196" width="232" height="30" rx="8" fill="var(--bg)" stroke="var(--line)"/><text x="516" y="216" text-anchor="middle" font-size="12">N, S, P come from outside the sugar</text>
<g stroke="currentColor" stroke-width="2.5" fill="none" marker-end="url(#ah)"><path d="M160 55 L238 85"/><path d="M160 150 C200 150 215 125 238 112"/><path d="M392 80 L478 55"/><path d="M392 112 L478 150"/></g>
<text x="436" y="58" text-anchor="middle" font-size="12" fill="var(--accent)" font-weight="700">+ N</text>
</g></svg>"""

IDEAS = [
    dict(t="Sugar is built from air and water.", d="In photosynthesis, light energy rearranges the atoms of CO₂ and water into sugar. Light is the energy. The atoms are the matter."),
    dict(t="Sugar has only carbon, hydrogen, and oxygen.", d="Fats are also only C, H, and O. Amino acids and proteins also contain nitrogen, and some contain sulfur."),
    dict(t="Other elements come from outside the sugar.", d="A cell combines atoms from sugar with nitrogen (and sulfur or phosphorus) from the soil or water to build amino acids and proteins."),
    dict(t="Atoms are rearranged, never created or destroyed.", d="When an animal eats, it breaks food into small pieces and rebuilds those atoms into its own molecules."),
    dict(t="Good explanations use evidence.", d="Use specific data, say what each result shows, and revise your explanation when new evidence does not fit."),
]
READY = {
    "6.1": "I can say which elements are in sugar, fats, and proteins.",
    "6.2": "I can explain where a plant’s matter comes from and count atoms in an equation.",
    "6.3": "I can explain why a plant with no nitrogen makes sugar but cannot grow.",
    "6.4": "I can trace atoms with a tracer or bead model and say what changes.",
    "6.5": "I can write a claim, evidence, and reasoning with at least two data points.",
    "6.6": "I can revise an explanation so it fits all of the evidence.",
}
tier = lambda p: "low" if p < 50 else "mid" if p < 70 else "hi"


def short(s, n=170):
    s = " ".join(s.replace('.,"', ". ").replace('"', "").split())
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def snapshot(P, ranked, focus, level):
    items = S.CP_ITEMS if level == "CP" else S.GATE_ITEMS
    bars = "".join(
        f'<li><span class="nm">{esc(S.SKILLS[k]["name"])}</span><span class="tr"><i class="t-{tier(v)}" style="width:{max(v,2)}%"></i></span><span class="pc">{v}%</span></li>'
        for k, v in ranked if k in S.SKILLS)
    out = f'<div class="stats"><div><b>{P["n"]}</b><span>students tested</span></div><div><b>{P["avg_pct"]}%</b><span>class average</span></div><div><b>{esc(S.SKILLS[focus[0]]["short"])}</b><span>biggest target</span></div></div>'
    out += '<p class="sub">Percent of points your class earned on each skill, weakest first.</p><ul class="bars">' + bars + '</ul>'
    out += '<p class="legend">Red: under 50% (reteach). Gold: 50–69% (practice). Green: 70% and up (keep sharp).</p>'
    note = [e for e in P["items"] if e["unscored"]]
    if note:
        out += '<p class="legend">The written answer on test question ' + ", ".join(str(e["q"]) for e in note) + ' was not scored yet, so it is left out of these numbers.</p>'
    out += '<h3 style="margin-top:22px">Your top 3 targets</h3>'
    for rank, k in enumerate(focus, 1):
        rows = ""
        for e in sorted((e for e in P["items"] if e["skill"] == k and e["pct"] is not None and not e["unscored"]), key=lambda e: e["pct"]):
            lab, idea = items.get(e["q"], ("Question " + str(e["q"]), ""))
            wr = ""
            if e.get("wrong"):
                txt, c = e["wrong"][0]
                wr = f'<div class="wr">Most common wrong answer ({c} of {P["n"]} students): “{esc(short(txt))}”</div>'
            rows += f'<tr><td class="n">{e["pct"]}%</td><td><b>Q{e["q"]}.</b> {esc(lab)}<div class="wr">Know this: {esc(idea)}</div>{wr}</td></tr>'
        out += f'<div class="prio"><div class="rk">Target {rank}</div><h3>{esc(S.SKILLS[k]["name"])} · {P["skills"][k]}%</h3><div class="scroll"><table><tr><th>Class got</th><th>Test question</th></tr>{rows}</table></div></div>'
    return out


def unit(P):
    level, ps = P["level"], P["skills"]
    skills = sorted((k for k in ps if k in S.SKILLS), key=lambda k: ps[k])
    ranked = [(k, ps[k]) for k in skills]
    focus = skills[:3]
    rest = skills[3:]
    groups = []
    for i, k in enumerate(skills):
        sk = S.SKILLS[k]
        qs = sk["qs"] if k in focus else sk["qs"][:2]
        tag = f'Target {i+1}' if k in focus else 'Quick check'
        groups.append(dict(title=f'{sk["name"]} ({ps[k]}%)', sub=("Your class’s " + tag.lower() + ". Read the mini-lesson, then try the questions.") if k in focus else "Your class did well here. Two quick questions to stay sharp.",
                           open=(i == 0), teach=f'{sk["teach"]}<div class="fix">{sk["fix"]}</div>', qs=qs))
    writes = []
    for k in skills:
        w = S.SKILLS[k].get("write")
        if w:
            writes.append(dict(w, ctx=w["ctx"]))
    vocab = S.VOCAB_CP if level == "CP" else S.VOCAB_GATE
    D = dict(code=f"LS1-6-{P['teacher']}-{level}-P{P['period']}", eyebrow=f"Unit 1.3 · HS-LS1-6 · {P['teacher']} · Period {P['period']} {level}",
             title="Sugar to Structures: your class’s review",
             lede="Built from your class’s results on the Unit 1.3 CSA. Start with the top 3 targets, then practice before your reassessment.",
             footer="Living Earth (Biology) · Unit 1.3 review for one class period. Class results only, no individual scores. Your progress saves in this browser.",
             pre=snapshot(P, ranked, focus, level), preTitle="Your class results", preNav="Your class",
             ideas=IDEAS, ideasSub="The big picture for every class.", figure=FIGURE, figureCaption="Sugar has only C, H, and O. Other elements join in to build amino acids and proteins.",
             vocab=[list(v) for v in vocab], vocabQuiz=[S.VOCAB_QUIZ_GATE] if level == "GATE" else [],
             groups=groups, rubric=[["4", "Correct and complete. Specific data, correct science words, and reasoning that explains WHY."], ["3", "Mostly correct. One piece is missing."], ["2", "Partly correct. Names ideas but does not connect them or use data."], ["1", "Major mistake or does not answer the question."]],
             write=writes, ready=[READY[k] for k in skills])
    return D, skills, focus


def build(P):
    D, skills, focus = unit(P)
    data = json.dumps(D).replace("</", "<\\/")
    title = f"Unit 1.3 Review {P['teacher']} P{P['period']}"
    return title, f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">
<style>
{css}
</style>
</head>
<body>
<div class="wrap" id="app"></div>
<script>window.UNIT={data};</script>
<script>
{js}
</script>
</body>
</html>
"""


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    index = []
    for P in json.load(open(HERE / "periods.json")):
        title, page = build(P)
        name = f"HS-LS1-6_review_{P['teacher']}_{P['level']}_P{P['period']}.html"
        (OUT / name).write_text(page)
        index.append((P["teacher"], P["level"], P["period"], P["n"], name))
        print("wrote", name, len(page))
