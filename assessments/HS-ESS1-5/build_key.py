"""Write the teacher key for Unit 3.1 from the question bank (questions.py).

Usage: python3 build_key.py
"""

import html
import re
from pathlib import Path

import questions as Q

HERE = Path(__file__).parent
LETTERS = "ABCDEFG"


def text(s):
    s = re.sub(r"<(br|/p|/li|/h\d|/tr)[^>]*>", "\n", s)
    s = re.sub(r"</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(re.sub(r"\n\s*\n+", "\n", s)).strip()


def item_block(label, it):
    out = [f"**{label}** ({it['type']})", "", text(it["body"]), ""]
    if it["type"] in ("choice", "multi"):
        for n, c in enumerate(it["choices"]):
            right = n == it["answer"] if it["type"] == "choice" else n in it["answer"]
            out.append(f"- {LETTERS[n]}. {text(c)}" + ("  **(correct)**" if right else ""))
        out.append("")
    elif it["type"] == "tf":
        out += [f"- Answer: **{'True' if it['answer'] else 'False'}**", ""]
    else:
        out += ["Rubric and grading notes:", "", "> " + it["rubric"].replace(" - ", "\n> - ").replace("Grading notes:", "\n> Grading notes:"), ""]
    if it.get("feedback"):
        out += [f"Feedback shown to students: {text(it['feedback'])}", ""]
    return "\n".join(out)


def main():
    out = ["# Unit 3.1 Age of the Earth (HS-ESS1-5, HS-ESS1-6): teacher key", "",
           "Generated from `questions.py`. Do not share with students.", "",
           "## Schedule and Mastery Path", "",
           "| Target | CFA taken on | Review opens when |", "| --- | --- | --- |"]
    for code, (name, _) in Q.TARGETS.items():
        out.append(f"| {code} {name} | Day {Q.CFA_DAY[code]} | CFA score below 3 of 4 (fewer than 4 of 5 correct) |")
    out += ["", "Day 7 is a review day: any CFA that did not fit, absent students, Mastery Path reviews, and the Enrichment choice board all happen there. There is no practice test.", ""]

    out += ["## CFAs (5 questions each, auto-graded)", ""]
    for code, items in Q.CFAS.items():
        out += [f"### CFA {code}: {Q.TARGETS[code][0]}", "", f"*{Q.TARGETS[code][1]}*", ""]
        for n, it in enumerate(items, 1):
            out.append(item_block(f"{code}.{n}", it))

    out += ["## CSA (16 questions; Q14 and Q16 are teacher-graded, 4 points each)", ""]
    for n, (code, it) in enumerate(Q.CSA, 1):
        out.append(item_block(f"Q{n} · {code}", it))

    out += ["## Mastery Path review assignments (3 written questions each)", "",
            "Students answer in a text box or upload a photo. Pass/fail, 4 points. Suggested answers below.", ""]
    for code, rv in Q.REVIEWS.items():
        out += [f"### Review {code}: {Q.TARGETS[code][0]}", ""]
        for n, (q, a) in enumerate(zip(rv["questions"], rv["answers"]), 1):
            out += [f"{n}. {text(q)}", f"   - Suggested answer: {text(a)}"]
        out.append("")
    (HERE / "HS-ESS1-5_teacher_key.md").write_text("\n".join(out) + "\n")
    print("Wrote HS-ESS1-5_teacher_key.md")


if __name__ == "__main__":
    main()
