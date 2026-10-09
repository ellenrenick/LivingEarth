"""Turn a day's slide spec into update_presentation arguments.

Usage:
  python3 make_requests.py SPEC_DIR DAY REVISION_ID [--only 1,2,4] [--index] [--delete DEFAULT_SLIDE_ID]

Runs slides_helper.py build, then adds slide backgrounds (dark title slide, cream content slides).
--only builds just those slide numbers; --index inserts each at position (number - 1);
--delete removes the blank default slide. Prints compact JSON for update_presentation.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HELPER = next(Path("/root/.claude/skills/synced").glob("*/google-workspace/scripts/slides_helper.py"))
CREAM, GREEN = (0.984, 0.969, 0.937), (0.137, 0.224, 0.173)


def round_floats(o):
    if isinstance(o, float):
        return round(o, 3)
    if isinstance(o, list):
        return [round_floats(x) for x in o]
    if isinstance(o, dict):
        return {k: round_floats(v) for k, v in o.items()}
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir"); ap.add_argument("day"); ap.add_argument("revision")
    ap.add_argument("--only"); ap.add_argument("--index", action="store_true"); ap.add_argument("--delete"); ap.add_argument("--fix-fonts")
    a = ap.parse_args()
    d = Path(a.dir)
    spec = json.loads((d / f"day{a.day}_spec.json").read_text())
    meta = json.loads((d / f"day{a.day}_meta.json").read_text())
    want = {int(x) for x in a.only.split(",")} if a.only else None
    slides = []
    for s in spec["slides"]:
        n = int(s["id"].rsplit("_s", 1)[1])
        if want is None or n in want:
            if a.index:
                s["index"] = n - 1
            slides.append(s)
    keep = {s["id"] for s in slides}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"slides": slides}, f)
    out = subprocess.run([sys.executable, str(HELPER), "build", f.name, "--revision", a.revision],
                         capture_output=True, text=True, check=True)
    if out.stderr.strip():
        print(out.stderr, file=sys.stderr)
    call = json.loads(out.stdout)
    reqs = [r for r in call["requests"] if not (
        "updateParagraphStyle" in r and r["updateParagraphStyle"].get("style") == {"alignment": "START"})]
    for r in reqs:
        u = r.get("updateTextStyle")
        if u and "cellLocation" in u:
            u["style"]["fontFamily"] = "Nunito Sans"
            u["fields"] += ",fontFamily"
    for fx in (a.fix_fonts.split(",") if a.fix_fonts else []):
        for sl in spec["slides"]:
            if sl["id"].endswith(f"_s{fx}"):
                for el in sl["elements"]:
                    if el["type"] == "table":
                        for ri, row in enumerate(el["rows"]):
                            for ci in range(len(row)):
                                reqs.append({"updateTextStyle": {"objectId": el["id"], "cellLocation": {"rowIndex": ri, "columnIndex": ci},
                                             "textRange": {"type": "ALL"}, "style": {"fontFamily": "Nunito Sans"}, "fields": "fontFamily"}})
    for s in meta["slides"]:
        if s["id"] in keep:
            r, g, b = GREEN if s["dark"] else CREAM
            reqs.append({"updatePageProperties": {"objectId": s["id"], "fields": "pageBackgroundFill.solidFill.color",
                         "pageProperties": {"pageBackgroundFill": {"solidFill": {"color": {"rgbColor": {"red": r, "green": g, "blue": b}}}}}}})
    if a.delete:
        reqs.append({"deleteObject": {"objectId": a.delete}})
    call["requests"] = reqs
    print(json.dumps(round_floats(call), separators=(",", ":")))


if __name__ == "__main__":
    main()
