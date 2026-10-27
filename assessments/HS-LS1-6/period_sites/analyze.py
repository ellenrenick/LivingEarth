"""Summarize Unit 1.3 CSA Student Analysis Reports (Canvas New Quizzes CSV) by class period.

Usage: python3 analyze.py <folder with the *.csv exports>
Writes periods.json. It holds class-level numbers only (no student names or IDs),
so it is safe to commit. Keep the raw CSVs out of the repo.

Handles both versions of the test: the CP test (16-17 items) and the GATE test (14 items).
Adding a teacher (for example Silva): drop her CSV in the folder and run this again.
"""
import collections, csv, html, json, re, sys
from pathlib import Path

CP_MAP = {1: "6.1", 2: "6.1", 3: "6.1", 4: "6.2", 5: "6.2", 6: "6.2", 7: "6.3", 8: "6.3", 9: "6.3",
          10: "6.4", 11: "6.4", 12: "6.4", 13: "6.5", 14: "6.5", 15: "6.6", 16: "6.6", 17: "6.3"}
# GATE items have no official skill tags. Mapped by what each item asks (see skills13.GATE_ITEMS).
GATE_MAP = {1: "vocab", 2: "6.2", 3: "6.3", 4: "6.2", 5: "6.3", 6: "6.4", 7: "6.5", 8: "6.5", 9: "6.3",
            10: "6.6", 11: "6.6", 12: "6.6", 13: "6.5", 14: "6.6"}


def clean(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def load(path):
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    h = rows[0]
    items = []
    for j, c in enumerate(h):
        if c == "ItemType":
            items.append(dict(col=j + 1, type=rows[1][j], text=h[j + 1], earn=j + 2))
    for it in items:
        it["max"] = max(float(r[it["earn"]]) for r in rows[1:] if len(r) > it["earn"] and r[it["earn"]] != "")
    return rows, h, items


def analyze(folder):
    out = []
    for path in sorted(Path(folder).glob("*.csv")):
        if "Student Analysis" not in path.name:
            continue
        rows, h, items = load(path)
        si, ai = h.index("SectionNames"), h.index("Attempt")
        level = "CP" if items[0]["text"].startswith("A protein in a bean seed") else "GATE"
        mp = CP_MAP if level == "CP" else GATE_MAP
        data = [r for r in rows[1:] if len(r) > si and r[ai] == "1"]  # first attempt only
        for it in items:
            vals = [float(r[it["earn"]]) for r in data if len(r) > it["earn"] and r[it["earn"]] != ""]
            # an essay where nearly everyone has full marks has not been scored yet
            it["unscored"] = it["type"] == "essay" and bool(vals) and sum(v == it["max"] for v in vals) >= 0.9 * len(vals)
        poss = float(data[0][h.index("PointsPossible")])
        for sec in sorted({r[si] for r in data}):
            sd = [r for r in data if r[si] == sec]
            period = int(re.search(r"P(\d\d)", sec).group(1))
            teacher = sec.rsplit("-", 1)[-1]
            P = dict(teacher=teacher, level=level, period=period, n=len(sd), items=[])
            for q, it in enumerate(items, 1):
                vals = [float(r[it["earn"]]) / it["max"] for r in sd if it["max"] and r[it["earn"]] != ""]
                e = dict(q=q, type=it["type"], skill=mp.get(q), unscored=it["unscored"],
                         pct=round(100 * sum(vals) / len(vals)) if vals else None, answered=len(vals))
                if it["type"] in ("choice", "multi-answer", "true-false") and level == "CP":
                    wc = collections.Counter(clean(r[it["col"]]) for r in sd
                                             if r[it["earn"]] != "" and float(r[it["earn"]]) < it["max"])
                    e["wrong"] = wc.most_common(1)
                P["items"].append(e)
            sk = collections.defaultdict(list)
            for e in P["items"]:
                if e["skill"] and e["pct"] is not None and not e["unscored"]:
                    sk[e["skill"]].append(e["pct"])
            P["skills"] = {k: round(sum(v) / len(v)) for k, v in sorted(sk.items())}
            P["avg_pct"] = round(100 * sum(float(r[h.index("OverallScore")] or 0) for r in sd) / len(sd) / poss)
            out.append(P)
    return out


if __name__ == "__main__":
    res = analyze(sys.argv[1])
    json.dump(res, open(Path(__file__).parent / "periods.json", "w"), indent=1)
    for P in sorted(res, key=lambda p: (p["teacher"], p["level"], p["period"])):
        print(P["teacher"], P["level"], f"P{P['period']}", "n =", P["n"], "avg", P["avg_pct"], P["skills"])
