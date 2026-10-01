"""Write Unit1.3_teacher_key.md from unit13_bank.py: alignment map plus answer key."""

import re
from pathlib import Path

import newquiz_upload as N
import unit13_bank as U

LETTERS = "ABCDEFG"


def text(h):
    h = re.sub(r"<sub>(.*?)</sub>", r"\1", h)
    h = re.sub(r"</(p|li|tr|blockquote)>|<br>", "\n", h)
    h = re.sub(r"</t[dh]>", " | ", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = h.replace("&rarr;", "→").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&mdash;", "—")
    return "\n".join(l.strip() for l in h.splitlines() if l.strip())


def answer(it, n_choice):
    t = it["type"]
    if t == "choice":
        choices, pos = N.place_key(it, n_choice)
        return LETTERS[pos], choices
    if t == "multi":
        return ", ".join(LETTERS[k] for k in it["answer"]), it["choices"]
    if t == "tf":
        return str(it["answer"]), None
    return "Teacher-graded (4-point rubric)", None


def main():
    out = ["# Unit 1.3 Sugar to Structures (HS-LS1-6): Outcomes, CFAs, Practice Test, CSA", "",
           "Generated from `unit13_bank.py` by `build_unit13_key.py`. Format follows Earth Science Unit 3.", "",
           "## Outcomes (4-point scale, mastery 3, highest score)", "",
           "| Outcome | DOK | Student \"I can\" |", "| --- | --- | --- |"]
    out += [f"| {tid}: {name} | {dok} | {ican} |" for tid, name, dok, ican in U.TARGETS]
    quizzes = N.all_quizzes()
    out += ["", "## Outcome alignment map", "",
            "Every question title starts with its number and target ID, so you can align it in the New Quizzes editor.", ""]
    for title, _instr, items in quizzes:
        lts = {it["lt"] for _, it in items}
        if len(lts) == 1:
            out.append(f"- **{title}**: all {len(items)} questions → {lts.pop()}")
        else:
            out.append(f"- **{title}**: " + "; ".join(f"{q.split(' · ')[0]} → {it['lt']}" for q, it in items))
    for title, instr, items in quizzes:
        out += ["", f"## {title}", "", text(instr), ""]
        n_choice = 0
        for q, it in items:
            key, choices = answer(it, n_choice)
            if it["type"] == "choice":
                n_choice += 1
            pts = 4 if it["type"] == "essay" else 1
            out += [f"### {q} ({pts} pt{'s' if pts > 1 else ''})", "", text(it["prompt"]), ""]
            if choices:
                out += [f"{LETTERS[i]}. {text(c)}" for i, c in enumerate(choices)] + [""]
            out.append(f"**Answer:** {key}")
            if it.get("feedback"):
                out.append(f"\n*Feedback:* {it['feedback']}")
            if it["type"] == "essay":
                out += ["", "| Score | Level | Descriptor |", "| --- | --- | --- |"]
                out += [f"| {s} | {lvl} | {d} |" for s, lvl, d in it["rubric"]]
                out += ["| 0 | No response | Blank or off-topic. |", "", "**Grading notes**", ""]
                out += [f"- {x}" for x in it["grading_notes"]]
                out += ["", f"**Exemplar (score 4):** {it['exemplar']}"]
            out.append("")
    Path(__file__).with_name("Unit1.3_teacher_key.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
