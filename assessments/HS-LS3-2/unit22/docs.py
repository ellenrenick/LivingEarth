"""Markdown files for Unit 2.2: CFA keys, CSA key, and the day-by-day plan.

  python3 docs.py            # writes ../HS-LS3-2_CFA_key.md, ../HS-LS3-2_CSA_key.md, ../Unit_2.2_plan.md
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "HS-LS1-6"))
import cfas as Q  # noqa: E402
import content as U  # noqa: E402
import newquiz_upload as N  # noqa: E402

L = "ABCDEFGH"


def _md_table(t):
    rows = re.findall(r"<tr>(.*?)</tr>", t, flags=re.S)
    cells = [[re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, flags=re.S)] for r in rows]
    out = ["| " + " | ".join(cells[0]) + " |", "| " + " | ".join("---" for _ in cells[0]) + " |"]
    return "\n".join(out + ["| " + " | ".join(r) + " |" for r in cells[1:]])


def md(s):
    s = re.sub(r"<table.*?</table>", lambda m: "\n\n" + _md_table(m.group(0)) + "\n\n", s, flags=re.S)
    s = re.sub(r"</?(strong|b)>", "**", s)
    s = re.sub(r"</?em>", "*", s)
    s = re.sub(r"</p>\s*<p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[ \t]+", " ", s.replace("&rarr;", "→").replace("&nbsp;", " ")).strip()


def question(n, it, pos_index):
    out = [f"**Question {n}.** {md(it['prompt'])}\n"]
    key = ""
    if it["type"] == "choice":
        ch, pos = N.place_key(it, pos_index)
        out.append("\n".join(f"- {L[i]}. {md(x)}" for i, x in enumerate(ch)) + "\n")
        key = L[pos]
    elif it["type"] == "multi":
        out.append("\n".join(f"- {L[i]}. {md(x)}" for i, x in enumerate(it["choices"])) + "\n")
        key = " and ".join(L[i] for i in it["answer"])
    elif it["type"] == "tf":
        key = "True" if it["answer"] else "False"
    return "\n".join(out), key


def cfa_doc():
    out = [f"# {U.STANDARD} CFAs: {U.UNIT_NAME}\n",
           "One CFA per priority target (LS3-2.1 to LS3-2.5): 5 one-point auto-graded questions, taken from memory at the end of the "
           "lesson. Below a B (fewer than 4 of 5) opens that target's review (Mastery Path). Canvas shuffles questions and answer "
           "choices; the letters here follow this file.\n",
           "| CFA | Target | DOK | Given on |", "| --- | --- | --- | --- |"]
    given = {d["cfa"]: d for d in U.DAYS if d["cfa"]}
    for tid in Q.CFAS:
        t = U.TARGET[tid]
        out.append(f"| {tid} | {t[3]} | {t[2]} | Day {given[tid]['day']} ({given[tid]['date']}) |")
    out.append("")
    for tid, items in Q.CFAS.items():
        out.append(f"\n## {Q.CFA_TITLE[tid]}\n\n**Target:** {U.TARGET[tid][3]}\n")
        key, n_choice = [], 0
        for n, it in enumerate(items, 1):
            text, k = question(n, it, n_choice)
            out.append(text)
            n_choice += it["type"] == "choice"
            key.append(f"| {n} | {k} | {it['feedback']} |")
        out.append("**Answer key**\n\n| Question | Answer | Why |\n| --- | --- | --- |\n" + "\n".join(key) + "\n")
    return "\n".join(out)


def csa_doc():
    out = [f"# {Q.CSA_TITLE}\n",
           "13 questions on the 5 priority targets, graded out of 4 (19 raw points). Items for DOK 1 and 2 targets are 1 point each, "
           "auto-graded; each DOK 3 target has 1 multiple-choice question and 1 four-point written response that you grade. "
           "Mastery is 3 of 4. Full period.\n"]
    key, n_choice = [], 0
    for n, (tid, it) in enumerate(Q.CSA, 1):
        text, k = question(n, it, n_choice)
        n_choice += it["type"] == "choice"
        out.append(f"### {tid}\n\n{text}")
        if it["type"] == "essay":
            out.append("**Rubric (4 points)**\n\n| Score | Level | Description |\n| --- | --- | --- |\n" +
                       "\n".join(f"| {s} | {lvl} | {d} |" for s, lvl, d in it["rubric"]) + "\n| 0 | Blank or off-topic | |\n")
            out.append("**Grading notes**\n\n" + "\n".join(f"- {g}" for g in it["grading_notes"]) + f"\n\n**Exemplar (score 4):** {it['exemplar']}\n")
            key.append(f"| {n} | {tid} | Rubric |")
        else:
            key.append(f"| {n} | {tid} | {k} |")
    out.append("## Answer key\n\n| Question | Target | Answer |\n| --- | --- | --- |\n" + "\n".join(key) + "\n")
    return "\n".join(out)


def plan_doc():
    out = [f"# {U.UNIT}: {U.UNIT_NAME} ({U.STANDARD}) · day-by-day plan\n",
           f"**Anchoring phenomenon:** {U.MYSTERY}. {U.DRIVING_Q}\n", f"**Performance expectation:** {U.PE}\n",
           f"**Boundary:** {U.BOUNDARY}\n", "## Learning targets\n", "| Target | Tier | DOK | I can |", "| --- | --- | --- | --- |"]
    out += [f"| {t[0]} | {t[4]} | {t[2]} | {t[3]} |" for t in U.TARGETS]
    out += ["\n## Days (LE Planner, Mon Nov 9 to Tue Dec 1)\n", "| Day | Date | Lesson | Targets | CFA | Student minutes |",
            "| --- | --- | --- | --- | --- | --- |"]
    for d in U.DAYS:
        m = U.minutes(d)
        out.append(f"| {d['day']} | {d['date']} | {d['title']} | {', '.join(d['targets'])} | "
                   f"{'CFA ' + d['cfa'] if d['cfa'] else 'none'} | {m if m else 'full period'} |")
    out += ["\n## How this fits the workbook\n",
            "The workbook tab \"2.2 Inherited\" plans 15 days (course days 52 to 66). The LE Planner has 11 class days between Nov 9 and "
            "Dec 1 (Nov 11 Veterans Day and Nov 23 to 27 Fall Break are off), so the unit is compressed the way Unit 2.1 was (13 days to 8):\n",
            "- Every priority target keeps its CFA and one class period (LS3-2.3, 2.4, and 2.5 get one day instead of two or three).",
            "- The supporting standard LS3-3 (Punnett squares, chances and real counts) is taught through the planner's four linked "
            "resources: Genetics Notes (Nov 12, 13) and Monster Genetics (Nov 16, 17). LS3-3.3 is a short enrichment on Nov 20. None of it is on the CSA.",
            "- LS3-2.2 (sex cells and fertilization) is taught on Nov 17, right where Monster Genetics' Punnett squares need it.",
            "- The Nov 20 Catch Up Day keeps its job: CFA reviews (Mastery Paths) and make-up work, then the CSA is Dec 1.",
            "- Nothing on the CSA is removed.\n", "## Lessons\n"]
    for d in U.DAYS:
        out.append(f"### Day {d['day']} · {d['date']} · {d['title']}\n")
        out.append(f"**Focus question:** {d['focus']}\n")
        if d["kind"] != "csa":
            out.append("| Min | Section | What happens |\n| --- | --- | --- |")
            out.append("| 2 | Notebook setup | Students copy slide 2. |" if d["kind"] != "review" or True else "")
            for s in d["sections"]:
                out.append(f"| {s['minutes'] + s.get('minutes_frame', 0)} | {s['title']} | {s['teacher']} |")
            if d["cfa"]:
                out.append(f"| 6 | CFA {d['cfa']} | On their own, from memory. Below 4 of 5 opens the review. |")
        else:
            out.append(d["sections"][0]["teacher"])
        out.append("")
        for n in d.get("notes", []):
            out.append(f"- {n}")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    (HERE.parent / "HS-LS3-2_CFA_key.md").write_text(cfa_doc())
    (HERE.parent / "HS-LS3-2_CSA_key.md").write_text(csa_doc())
    (HERE.parent / "Unit_2.2_plan.md").write_text(plan_doc())
    print("wrote CFA key, CSA key, plan")
