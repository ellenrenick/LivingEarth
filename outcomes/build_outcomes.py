"""Build the Canvas outcomes import CSV for Living Earth (26-27).

Each GROUP is a standard; each OUTCOME is a learning target under it.
Source: the "Living Earth Standards and Learning Targets (26-27)" sheet,
saved here as source_targets.csv (Targets tab) and source_pes.json (the
performance expectations from the Units tab).

Run: python3 build_outcomes.py   ->  LivingEarth_outcomes.csv
Import in Canvas: Outcomes > Import (course or account level).
"""
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RATINGS = [(4, "Advanced"), (3, "Proficient"), (2, "Developing"),
           (1, "Beginning"), (0, "No Evidence")]
CALC_METHOD, CALC_INT = "decaying_average", 65

def tier_label(t):
    return {"Priority": "Priority (on the unit test)",
            "Supporting": "Supporting (taught and practiced, not on the unit test)",
            "Thread": "Thread (taught and practiced, not on the unit test)"}[t]


with open(os.path.join(HERE, "source_targets.csv"), newline="", encoding="utf-8") as f:
    targets = list(csv.DictReader(f))
with open(os.path.join(HERE, "source_pes.json"), encoding="utf-8") as f:
    PES = json.load(f)

standards = {}  # standard -> (tier, unit, unit title, [targets]) in sheet order
for t in targets:
    s = standards.setdefault(t["Standard"], (t["Tier"], t["Unit"], t["Unit title"], []))
    s[3].append(t)

header = ["vendor_guid", "object_type", "title", "description", "display_name",
          "calculation_method", "calculation_int", "workflow_state",
          "parent_guids", "ratings"] + [""] * (len(RATINGS) * 2 - 1)
ratings = [x for pts, name in RATINGS for x in (pts, name)]

rows = [header]
for std, (tier, unit, utitle, lts) in standards.items():
    desc = PES.get(std, f"Taught in Unit {unit}: {utitle}.")
    rows.append([f"LE-{std}", "group", std, desc, "", "", "",
                 "active", "", ""] + [""] * (len(header) - 10))
    for t in lts:
        d = (f"{t['Learning target']} "
             f"[DOK {t['DOK']}; {tier_label(t['Tier'])}; Unit {t['Unit']}]")
        rows.append([f"LE-{t['ID']}", "outcome", t["ID"], d, t['Student "I can"'],
                     CALC_METHOD, CALC_INT, "active", f"LE-{std}"] + ratings)

with open(os.path.join(HERE, "LivingEarth_outcomes.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)
