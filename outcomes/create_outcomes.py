"""Load the Living Earth learning targets into a Canvas course as Outcomes.

One outcome group per standard (ordered by unit), one outcome per learning target,
so the targets show up in the Learning Mastery Gradebook under their standard.
Uses the same 4-point scale as the sandbox outcomes. Safe to re-run: groups and
outcomes that already exist (matched by title) are skipped.

Source: "Living Earth Standards and Learning Targets (26-27)" sheet, Targets tab,
saved as learning_targets_26-27.json.

Usage:
  python3 create_outcomes.py https://kernhigh.instructure.com 342850
"""

import html
import json
import os
import ssl
import sys
import urllib.request
from pathlib import Path

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

ICAN = 'Student "I can"'

RATINGS = [
    {"description": "Mastered", "points": 4},
    {"description": "Proficient", "points": 3},
    {"description": "Approaching", "points": 2},
    {"description": "Not yet meeting", "points": 1},
    {"description": "Insufficient evidence", "points": 0},
]


class Canvas:
    def __init__(self, base, course):
        self.root = f"{base.rstrip('/')}/api/v1/courses/{course}"
        self.token = os.environ.get("CANVAS_TOKEN")

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(path if path.startswith("http") else self.root + path, data=data, method=method)
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=CTX) as r:
            return json.loads(r.read() or "null")


def group_title(t):
    return f"HS-{t['Standard']} · Unit {t['Unit']}: {t['Unit title']} ({t['Tier']})"


def outcome(t):
    e = html.escape
    i_can = t[ICAN]
    desc = (
        f"<p>{e(i_can)}</p>"
        f"<p><strong>Learning target:</strong> {e(t['Learning target'])}</p>"
        f"<p>HS-{e(t['Standard'])} · {e(t['Tier'])} · DOK {e(t['DOK'])} · Unit {e(t['Unit'])}</p>"
    )
    return {
        "title": f"{t['ID']}: {i_can}",
        "display_name": t["ID"],
        "description": desc,
        "mastery_points": 3,
        "ratings": RATINGS,
        "calculation_method": "highest",
    }


def main(base, course):
    api = Canvas(base, course)
    targets = json.loads((Path(__file__).parent / "learning_targets_26-27.json").read_text())
    root = api.call("GET", "/root_outcome_group")
    groups = {g["title"]: g for g in api.call("GET", f"/outcome_groups/{root['id']}/subgroups?per_page=100")}
    made = skipped = 0
    for t in targets:
        title = group_title(t)
        if title not in groups:
            groups[title] = api.call("POST", f"/outcome_groups/{root['id']}/subgroups", {"title": title})
            groups[title]["_existing"] = set()
        g = groups[title]
        if "_existing" not in g:
            links = api.call("GET", f"/outcome_groups/{g['id']}/outcomes?per_page=100")
            g["_existing"] = {l["outcome"]["title"] for l in links}
        o = outcome(t)
        if o["title"] in g["_existing"]:
            skipped += 1
            continue
        api.call("POST", f"/outcome_groups/{g['id']}/outcomes", o)
        g["_existing"].add(o["title"])
        made += 1
    print(f"{len(groups)} standard groups; {made} outcomes created, {skipped} already there")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
