"""Write teacher_key.md: every reassessment question with its answer, rubric, and exemplar."""

import html
import re
from pathlib import Path

import questions

HERE = Path(__file__).parent
LETTERS = "ABCDEFGH"


def text(s):
    s = re.sub(r"</(p|li|tr|h3)>|<br>", "\n", s)
    s = re.sub(r"</t[dh]>", " | ", s)
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def render(bank):
    out = [f"## {bank['title']}", "", f"{round(sum(i['points'] for i in bank['items']), 2)} points", ""]
    for n, item in enumerate(bank["items"], 1):
        out += [f"### {n}. {item['title']} ({item['points']} pt)", "", text(item["prompt"]), ""]
        kind = item["type"]
        if kind in ("choice", "multi"):
            keys = [item["answer"]] if kind == "choice" else item["answers"]
            for i, c in enumerate(item["choices"]):
                out.append(f"- {LETTERS[i]}. {text(c)}{'  **(correct)**' if i in keys else ''}")
        elif kind == "truefalse":
            out.append(f"**Answer:** {item['answer']}")
        elif kind == "matching":
            out += [f"- {l} = {r}" for l, r in item["pairs"]]
            out.append(f"- Unused: {'; '.join(item['distractors'])}")
        else:
            out += [item["rubric"], "", f"**Exemplar:** {item['exemplar']}"]
        out.append("")
    return out


lines = ["# Reassessment teacher key", "",
         "Answer keys for the Unit 1.1, 1.2, and 1.3 reassessments (CP Living Earth). "
         "Each is worth 4.0 points. Regenerate with `python3 build_key.py`.", ""]
for bank in questions.REASSESSMENTS:
    lines += render(bank)
(HERE / "teacher_key.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote teacher_key.md")
