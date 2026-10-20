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
           "Targets follow the team workbook \"Renick Living Earth Standards and Learning Targets (26-27)\" (Targets tab).", "",
           "## Schedule and Mastery Path", "",
           "| Target | Tier | DOK | CFA taken on | On the CSA | Review opens when |", "| --- | --- | --- | --- | --- | --- |"]
    csa_codes = {c for c, _ in Q.CSA}
    for code, (name, _) in Q.TARGETS.items():
        tier, dok, _full = Q.TARGET_FULL[code]
        out.append(f"| {code} {name} | {tier} | {dok} | Day {Q.CFA_DAY[code]} | {'yes' if code in csa_codes else 'no'} | CFA score below 3 of 4 (fewer than 4 of 5 correct) |")
    out += ["", "Priority targets (ESS1-5) are assessed on the CSA. Supporting targets (ESS1-6) are taught and practiced with CFAs and reviews but never appear on the CSA.", "",
            "Each CFA is taken at the start of the class after its lesson. CFAs for ESS1-5.5 and ESS1-6.3 follow Day 6, so they are taken on the work day after Day 6 or at the start of Day 7. "
            "Day 7 is a review day: any CFA that did not fit, absent students, Mastery Path reviews, and the Enrichment choice board all happen there. There is no practice test.", ""]

    out += ["## CFAs (5 questions each, auto-graded)", ""]
    for code, items in Q.CFAS.items():
        out += [f"### CFA {code}: {Q.TARGETS[code][0]}", "", f"*{Q.TARGETS[code][1]}*", "",
                f"Workbook target ({Q.TARGET_FULL[code][0]}, DOK {Q.TARGET_FULL[code][1]}): {Q.TARGET_FULL[code][2]}", ""]
        for n, it in enumerate(items, 1):
            out.append(item_block(f"{code}.{n}", it))

    essays = [n for n, (_, it) in enumerate(Q.CSA, 1) if it["type"] == "essay"]
    out += [f"## CSA ({len(Q.CSA)} questions on the five priority targets; Q{' and Q'.join(map(str, essays))} are teacher-graded, 4 points each)", ""]
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
