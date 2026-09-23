"""Build the Canvas QTI 1.2 package and teacher copy from questions.py.

Usage: python3 build.py
Outputs (next to this file):
  HS-LS1-6_canvas_qti.zip  - import into Canvas (Settings > Import Course Content > QTI .zip)
  HS-LS1-6_teacher_key.md  - readable copy with answer key, DOK levels, and rubrics
"""

import html
import random
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import questions as q

HERE = Path(__file__).parent
ZIP_PATH = HERE / "HS-LS1-6_canvas_qti.zip"
KEY_PATH = HERE / "HS-LS1-6_teacher_key.md"
QUIZ_ID = "hs_ls1_6_sugar_to_building_blocks"
MC_POINTS = 2
LETTERS = "ABCDEFGH"
# Where the correct answer lands for each MC item (0 = A), balanced across letters.
KEY_POSITIONS = [1, 3, 0, 2, 1, 0, 3, 2, 0, 3]


def shuffled_mc():
    """Return MC items with choices shuffled deterministically."""
    rng = random.Random(16)
    items = []
    for n, item in enumerate(q.MULTIPLE_CHOICE):
        key = item["choices"][item["answer"]]
        others = [c for i, c in enumerate(item["choices"]) if i != item["answer"]]
        rng.shuffle(others)
        pos = KEY_POSITIONS[n % len(KEY_POSITIONS)]
        choices = others[:pos] + [key] + others[pos:]
        items.append({**item, "choices": choices, "answer": pos})
    return items


def metadata(qtype, points):
    return (
        "<itemmetadata><qtimetadata>"
        f"<qtimetadatafield><fieldlabel>question_type</fieldlabel><fieldentry>{qtype}</fieldentry></qtimetadatafield>"
        f"<qtimetadatafield><fieldlabel>points_possible</fieldlabel><fieldentry>{points}</fieldentry></qtimetadatafield>"
        "</qtimetadata></itemmetadata>"
    )


def mattext(content, is_html=True):
    kind = "text/html" if is_html else "text/plain"
    return f'<material><mattext texttype="{kind}">{escape(content)}</mattext></material>'


def general_feedback(text):
    return (
        '<itemfeedback ident="general_fb"><flow_mat>'
        f"{mattext('<p>' + text + '</p>')}"
        "</flow_mat></itemfeedback>"
    )


def matching_item():
    m = q.MATCHING
    rights = [d for _, d in m["pairs"]] + m["distractors"]
    rng = random.Random(9)
    rng.shuffle(rights)
    right_ids = {text: f"m_r{i}" for i, text in enumerate(rights)}
    labels = "".join(
        f'<response_label ident="{right_ids[t]}">{mattext(t, is_html=False)}</response_label>'
        for t in rights
    )
    responses, conditions = [], []
    share = 100 / len(m["pairs"])
    for i, (term, definition) in enumerate(m["pairs"]):
        rid = f"m_l{i}"
        responses.append(
            f'<response_lid ident="{rid}">{mattext(term, is_html=False)}'
            f"<render_choice>{labels}</render_choice></response_lid>"
        )
        conditions.append(
            f'<respcondition><conditionvar><varequal respident="{rid}">{right_ids[definition]}</varequal>'
            f'</conditionvar><setvar varname="SCORE" action="Add">{share:.2f}</setvar></respcondition>'
        )
    return (
        f'<item ident="{QUIZ_ID}_match" title="{escape(m["title"])}">'
        + metadata("matching_question", m["points"])
        + f"<presentation>{mattext(m['prompt'])}{''.join(responses)}</presentation>"
        + '<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>'
        + "".join(conditions)
        + "</resprocessing></item>"
    )


def mc_item(n, item):
    ident = f"{QUIZ_ID}_mc{n}"
    labels = "".join(
        f'<response_label ident="{ident}_c{i}">{mattext(c)}</response_label>'
        for i, c in enumerate(item["choices"])
    )
    return (
        f'<item ident="{ident}" title="{escape(item["title"])} (DOK {item["dok"]})">'
        + metadata("multiple_choice_question", MC_POINTS)
        + f"<presentation>{mattext(item['prompt'])}"
        + f'<response_lid ident="response1" rcardinality="Single"><render_choice>{labels}</render_choice></response_lid>'
        + "</presentation>"
        + '<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>'
        + '<respcondition continue="Yes"><conditionvar><other/></conditionvar>'
        + '<displayfeedback feedbacktype="Response" linkrefid="general_fb"/></respcondition>'
        + f'<respcondition continue="No"><conditionvar><varequal respident="response1">{ident}_c{item["answer"]}</varequal></conditionvar>'
        + '<setvar action="Set" varname="SCORE">100</setvar></respcondition>'
        + "</resprocessing>"
        + general_feedback(item["feedback"])
        + "</item>"
    )


def essay_item(n, item):
    rows = "".join(
        f"<tr><td><strong>{score}</strong></td><td>{level}</td><td>{desc}</td></tr>"
        for score, level, desc in item["rubric"]
    )
    notes = "".join(f"<li>{n}</li>" for n in item["grading_notes"])
    fb = (
        "<strong>4-point scoring rubric</strong></p>"
        '<table border="1" cellpadding="4"><tr><th>Score</th><th>Level</th><th>Descriptor</th></tr>'
        f"{rows}<tr><td><strong>0</strong></td><td>No response</td><td>Blank or off-topic.</td></tr></table>"
        f"<p><strong>Grading notes</strong></p><ul>{notes}</ul>"
        f"<p><strong>Exemplar (score 4):</strong> {item['exemplar']}"
    )
    return (
        f'<item ident="{QUIZ_ID}_fr{n}" title="{escape(item["title"])} (DOK {item["dok"]})">'
        + metadata("essay_question", item["points"])
        + f"<presentation>{mattext(item['prompt'])}"
        + '<response_str ident="response1" rcardinality="Single"><render_fib><response_label ident="answer1" rshuffle="No"/></render_fib></response_str>'
        + "</presentation>"
        + '<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>'
        + '<respcondition continue="No"><conditionvar><other/></conditionvar></respcondition></resprocessing>'
        + general_feedback(fb)
        + "</item>"
    )


def section(ident, title, items):
    return f'<section ident="{ident}" title="{escape(title)}">{"".join(items)}</section>'


def build_qti(mc):
    total = q.MATCHING["points"] + MC_POINTS * len(mc) + sum(f["points"] for f in q.FREE_RESPONSE)
    body = (
        section("part1", q.MATCHING["title"], [matching_item()])
        + section("part2", "Part 2: Multiple Choice", [mc_item(i + 1, it) for i, it in enumerate(mc)])
        + section("part3", "Part 3: Free Response", [essay_item(i + 1, it) for i, it in enumerate(q.FREE_RESPONSE)])
    )
    assessment = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">'
        f'<assessment ident="{QUIZ_ID}" title="{escape(q.TITLE)}">'
        "<qtimetadata><qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry></qtimetadatafield></qtimetadata>"
        f'<section ident="root_section">{body}</section>'
        "</assessment></questestinterop>\n"
    )
    manifest = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<manifest identifier="{QUIZ_ID}_manifest" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1">'
        "<metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata>"
        "<organizations/>"
        f'<resources><resource identifier="{QUIZ_ID}" type="imsqti_xmlv1p2" href="{QUIZ_ID}.xml">'
        f'<file href="{QUIZ_ID}.xml"/></resource></resources>'
        "</manifest>\n"
    )
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest)
        z.writestr(f"{QUIZ_ID}.xml", assessment)
    return total


def to_md(fragment):
    """Rough HTML -> Markdown for the teacher copy."""
    s = fragment
    s = re.sub(r"<table[^>]*>", "\n\n", s)
    s = s.replace("</table>", "\n\n")
    s = re.sub(r"<tr>(.*?)</tr>", lambda m: "| " + " | ".join(re.findall(r"<t[hd]>(.*?)</t[hd]>", m.group(1))) + " |\n"
               + ("| " + " | ".join("---" for _ in re.findall(r"<th>", m.group(1))) + " |\n" if "<th>" in m.group(1) else ""), s)
    s = re.sub(r"<blockquote>(.*?)</blockquote>", r"\n> \1\n\n", s)
    s = re.sub(r"</?(strong)>", "**", s)
    s = re.sub(r"</?(em)>", "*", s)
    s = re.sub(r"<sub>(.*?)</sub>", r"\1", s)
    s = re.sub(r"<li>", "\n- ", s)
    s = re.sub(r"</p>\s*<p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def build_key(mc, total):
    out = [f"# {q.TITLE}", "", "**Course:** Living Earth (Biology), Grade 9  ",
           "**Priority standard:** HS-LS1-6  ", f"**Total points:** {total}", "",
           "| Part | Items | DOK | Points |", "| --- | --- | --- | --- |",
           f"| 1. Vocabulary matching | {len(q.MATCHING['pairs'])} terms | 1 | {q.MATCHING['points']} |",
           f"| 2. Multiple choice | {len(mc)} | " + ", ".join(sorted({str(i['dok']) for i in mc})) + f" | {MC_POINTS * len(mc)} |",
           f"| 3. Free response | {len(q.FREE_RESPONSE)} | 3 | {sum(f['points'] for f in q.FREE_RESPONSE)} |",
           "", "---", "", f"## {q.MATCHING['title']}", "", to_md(q.MATCHING["prompt"]), "",
           "| Term | Correct definition |", "| --- | --- |"]
    out += [f"| {t} | {d} |" for t, d in q.MATCHING["pairs"]]
    out += ["", "*Distractors (unused):* " + "; ".join(q.MATCHING["distractors"]), "", "---", "",
            "## Part 2: Multiple Choice", ""]
    for i, item in enumerate(mc, 1):
        out += [f"### {i}. {item['title'].split(' - ', 1)[1]} (DOK {item['dok']})", "", to_md(item["prompt"]), ""]
        out += [f"{LETTERS[j]}. {html.unescape(c)}" + ("  ✅" if j == item["answer"] else "") + "  " for j, c in enumerate(item["choices"])]
        out += ["", f"**Answer: {LETTERS[item['answer']]}** — {item['feedback']}", ""]
    out += ["---", "", "## Part 3: Free Response", ""]
    for i, item in enumerate(q.FREE_RESPONSE, 1):
        out += [f"### {i}. {item['title'].split(' - ', 1)[1]} (DOK {item['dok']}, {item['points']} pts)", "",
                to_md(item["prompt"]), "", "**4-point scoring rubric**", "",
                "| Score | Level | Descriptor |", "| --- | --- | --- |"]
        out += [f"| {score} | {level} | {desc} |" for score, level, desc in item["rubric"]]
        out += ["| 0 | No response | Blank or off-topic. |", "", "**Grading notes**", ""]
        out += [f"- {n}" for n in item["grading_notes"]]
        out += ["", f"**Exemplar response (score 4):** {item['exemplar']}", ""]
    out += ["---", "", "## Quick answer key", "",
            "| MC # | " + " | ".join(str(i) for i in range(1, len(mc) + 1)) + " |",
            "| --- | " + " | ".join("---" for _ in mc) + " |",
            "| Answer | " + " | ".join(LETTERS[m["answer"]] for m in mc) + " |", ""]
    KEY_PATH.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    mc = shuffled_mc()
    total = build_qti(mc)
    build_key(mc, total)
    print(f"Wrote {ZIP_PATH.name} and {KEY_PATH.name} ({total} points)")
