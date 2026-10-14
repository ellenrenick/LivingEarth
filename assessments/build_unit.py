"""Build the CSA and CFA packages for a unit.

Usage: python3 build_unit.py HS-LS1-2 [HS-LS2-5 ...]   (or: python3 build_unit.py all)

Each unit folder holds:
  questions.py  the 45-minute CSA (same layout as HS-LS1-6/questions.py)
  cfa.py        one short CFA per priority learning target
It writes, next to those files:
  <STD>_canvas_qti.zip, <STD>_teacher_key.md          (CSA)
  <STD>_CFA_canvas_qti.zip, <STD>_CFA_key.md          (one quiz per CFA)
"""

import html
import importlib.util
import json
import random
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "HS-LS1-6"))
import build  # noqa: E402  (the HS-LS1-6 builder, reused for the CSA)

LETTERS = "ABCD"
PACING = json.loads((ROOT / "pacing.json").read_text(encoding="utf-8"))
CFA_MC_POINTS = 2


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cfa_items(cfa):
    """Shuffle MC choices deterministically; the key is written first in the bank."""
    rng = random.Random(cfa["id"])
    out = []
    for n, it in enumerate(cfa["items"]):
        if "choices" not in it:
            out.append(it)
            continue
        key, others = it["choices"][0], it["choices"][1:]
        rng.shuffle(others)
        pos = (n + len(cfa["id"])) % 4
        out.append({**it, "choices": others[:pos] + [key] + others[pos:], "answer": pos})
    return out


def cfa_item_xml(ident, n, it):
    if "choices" in it:
        labels = "".join(
            f'<response_label ident="{ident}_c{i}">{build.mattext(c)}</response_label>'
            for i, c in enumerate(it["choices"])
        )
        return (
            f'<item ident="{ident}_q{n}" title="Q{n}">'
            + build.metadata("multiple_choice_question", CFA_MC_POINTS)
            + f"<presentation>{build.mattext(it['prompt'])}"
            + f'<response_lid ident="response1" rcardinality="Single"><render_choice>{labels}</render_choice></response_lid>'
            + "</presentation>"
            + '<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>'
            + '<respcondition continue="Yes"><conditionvar><other/></conditionvar>'
            + '<displayfeedback feedbacktype="Response" linkrefid="general_fb"/></respcondition>'
            + f'<respcondition continue="No"><conditionvar><varequal respident="response1">{ident}_c{it["answer"]}</varequal></conditionvar>'
            + '<setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing>'
            + build.general_feedback(it["feedback"])
            + "</item>"
        )
    rows = "".join(f"<tr><td><strong>{s}</strong></td><td>{d}</td></tr>" for s, d in it["criteria"])
    fb = (
        '<strong>Scoring</strong></p><table border="1" cellpadding="4"><tr><th>Score</th><th>Criteria</th></tr>'
        f"{rows}</table><p><strong>Model answer:</strong> {it['exemplar']}"
    )
    return (
        f'<item ident="{ident}_q{n}" title="Q{n}">'
        + build.metadata("essay_question", it["points"])
        + f"<presentation>{build.mattext(it['prompt'])}"
        + '<response_str ident="response1" rcardinality="Single"><render_fib><response_label ident="answer1" rshuffle="No"/></render_fib></response_str>'
        + "</presentation>"
        + '<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>'
        + '<respcondition continue="No"><conditionvar><other/></conditionvar></respcondition></resprocessing>'
        + build.general_feedback(fb)
        + "</item>"
    )


def cfa_points(items):
    return sum(CFA_MC_POINTS if "choices" in i else i["points"] for i in items)


def build_cfa(unit_dir, cfa_mod):
    std = cfa_mod.STANDARD
    resources, files = [], {}
    keys = [f"# {std} CFAs: {cfa_mod.UNIT_TITLE}", "",
            "**Course:** Living Earth (Biology), Grade 9  ",
            f"**Unit:** {cfa_mod.UNIT}  ", f"**Priority standard:** {std}  ",
            "**Format:** one short check per priority learning target, given as an exit ticket in the last 5 to 7 minutes of the class that closes the target. Mastery is 4 of 6 points; below that, reteach before the CSA.", "",
            "| CFA | Learning target | DOK | Points | Given on |", "| --- | --- | --- | --- | --- |"]
    sections = []
    for cfa in cfa_mod.CFAS:
        items = cfa_items(cfa)
        ident = "cfa_" + cfa["id"].replace("-", "_").replace(".", "_")
        pts = cfa_points(items)
        ud = PACING[std]["cfa_unit_day"].get(cfa["id"])
        cd = PACING[std]["start"] + ud - 1 if ud else None
        given = f"Unit day {ud} (course day {cd})" if ud else "Review day"
        keys.append(f"| {cfa['id']} | {cfa['lt']} | {cfa['dok']} | {pts} | {given} |")
        body = "".join(cfa_item_xml(ident, n, it) for n, it in enumerate(items, 1))
        xml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2">'
            f'<assessment ident="{ident}" title="{escape("CFA " + cfa["id"] + ": " + cfa["lt"])}">'
            '<qtimetadata><qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry></qtimetadatafield></qtimetadata>'
            f'<section ident="root_section">{body}</section></assessment></questestinterop>\n'
        )
        files[f"{ident}.xml"] = xml
        resources.append(f'<resource identifier="{ident}" type="imsqti_xmlv1p2" href="{ident}.xml"><file href="{ident}.xml"/></resource>')
        sec = ["", "---", "", f"## {cfa['id']} (DOK {cfa['dok']}, {pts} points)", "", f"**Learning target:** {cfa['lt']}", ""]
        for n, it in enumerate(items, 1):
            sec += [f"**Q{n}.** " + build.to_md(it["prompt"]), ""]
            if "choices" in it:
                sec += [f"{LETTERS[j]}. {html.unescape(c)}" + ("  ✅" if j == it["answer"] else "") + "  " for j, c in enumerate(it["choices"])]
                sec += ["", f"*Answer {LETTERS[it['answer']]}.* {it['feedback']}", ""]
            else:
                sec += ["| Score | Criteria |", "| --- | --- |"] + [f"| {s} | {d} |" for s, d in it["criteria"]]
                sec += ["", f"*Model answer:* {it['exemplar']}", ""]
        sections += sec
    manifest = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<manifest identifier="{std}_cfa_manifest" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1">'
        "<metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata><organizations/>"
        f"<resources>{''.join(resources)}</resources></manifest>\n"
    )
    with zipfile.ZipFile(unit_dir / f"{std}_CFA_canvas_qti.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest)
        for name, xml in files.items():
            z.writestr(name, xml)
    (unit_dir / f"{std}_CFA_key.md").write_text("\n".join(keys + sections) + "\n", encoding="utf-8")
    return len(cfa_mod.CFAS)


def build_unit(std):
    unit_dir = ROOT / std
    build.HERE = unit_dir
    q = load(unit_dir / "questions.py", f"q_{std}")
    mc = build.shuffled_mc(q)
    total = build.build_qti(q, mc)
    build.build_key(q, mc, total)
    n = build_cfa(unit_dir, load(unit_dir / "cfa.py", f"c_{std}"))
    print(f"{std}: CSA {total} points, {n} CFAs")


if __name__ == "__main__":
    names = sys.argv[1:] or ["all"]
    if names == ["all"]:
        names = sorted(p.parent.name for p in ROOT.glob("HS-*/cfa.py"))
    for name in names:
        build_unit(name)
