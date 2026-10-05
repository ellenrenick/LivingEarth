"""Create the Energy Through Carbon CFA (Unit 1.2, HS-LS2-5) as a Canvas New Quiz.

Questions and answer key come from Energy_through_Carbon_CFA.docx and its answer sheet.
The quiz is created unpublished, in the Assignments group, and added to the Unit 1.2 module.

Usage:
  python3 energy_through_carbon_cfa.py https://kernhigh.instructure.com 342850
(CANVAS_TOKEN is used if set; in Claude cloud sessions the proxy adds it.)
"""

import json
import os
import ssl
import sys
import urllib.request
import uuid

TITLE = "Energy Through Carbon CFA"
ASSIGNMENT_GROUP = 647725  # Assignments
MODULE = 1632748  # Unit 1.2 Cell Energy & Carbon HS-LS2-5

INSTRUCTIONS = (
    "<p>Choose the best answer for multiple-choice questions. Type complete answers for the "
    "vocabulary and short-response questions. Use scientific terms and explain the direction "
    "carbon moves when asked.</p>"
)

# (prompt, choices, correct index, reason from answer sheet)
MC = [
    ("A plant uses carbon dioxide from the air to make glucose. Which process is happening?",
     ["Cellular respiration", "Photosynthesis", "Combustion", "Decomposition"], 1,
     "Photosynthesis moves carbon dioxide from the atmosphere into plant molecules."),
    ("A car burns gasoline. Which process releases carbon dioxide into the atmosphere?",
     ["Ocean uptake", "Sedimentation", "Combustion", "Consumption"], 2,
     "Combustion releases stored carbon as carbon dioxide."),
    ("Which statement about plants is correct?",
     ["Plants only carry out photosynthesis.", "Plants only carry out respiration at night.",
      "Plants carry out both photosynthesis and respiration.", "Plants do not release carbon dioxide."], 2,
     "Plants carry out both photosynthesis and cellular respiration."),
    ("Which arrow shows ocean uptake?",
     ["Ocean &rarr; atmosphere", "Atmosphere &rarr; ocean", "Plant &rarr; atmosphere", "Soil &rarr; plant"], 1,
     "Ocean uptake moves carbon from the atmosphere into ocean water."),
    ("A fallen leaf is broken down by fungi and bacteria. What happens to the carbon?",
     ["It disappears completely.", "It moves into soil, decomposers, or the air.",
      "It changes into sunlight.", "It can only move into an animal."], 1,
     "Decomposition moves carbon into soil, decomposers, and sometimes the atmosphere."),
    ("A rabbit eats a plant. How does carbon move?",
     ["From the plant to the rabbit through consumption", "From the rabbit to the plant through combustion",
      "From the atmosphere to the rabbit through sedimentation",
      "From the geosphere to the rabbit through ocean uptake"], 0,
     "Consumption moves carbon from the plant to the rabbit."),
    ("Which statement best compares carbon and energy in an ecosystem?",
     ["Carbon cycles, while energy flows through the system.",
      "Carbon and energy both disappear after respiration.",
      "Energy cycles, while carbon only moves once.", "Carbon enters ecosystems only through animals."], 0,
     "Carbon cycles; energy flows through the ecosystem."),
    ("Carbon dioxide dissolves in seawater. Which two Earth systems are connected?",
     ["Atmosphere and hydrosphere", "Biosphere and geosphere", "Geosphere and atmosphere",
      "Biosphere and hydrosphere"], 0,
     "Air is the atmosphere and seawater is the hydrosphere."),
]

# (prompt, accepted answers)
VOCAB = [
    ("Type the process that moves carbon dioxide from the atmosphere into plants.",
     ["Photosynthesis"]),
    ("Type the process that breaks down glucose and releases usable ATP energy.",
     ["Cellular respiration", "Respiration"]),
]

RUBRIC = """4-POINT RUBRIC (score holistically)
4 Advanced Understanding: Accurately explains carbon movement, uses several scientific terms, shows correct arrow directions, and connects processes to the four Earth systems.
3 Meets the Standard: Correctly explains the main carbon pathways and uses most scientific terms. Model or explanation is mostly complete.
2 Developing Understanding: Shows part of the idea, but some terms, process descriptions, or arrow directions are incomplete or inaccurate.
1 Beginning Understanding: Needs more practice identifying the Earth systems, carbon processes, and directions of carbon movement.
A 3 means the student has met the standard even if a minor vocabulary or arrow-direction error remains. A 4 requires accurate relationships, clear scientific vocabulary, and connected reasoning."""

# (prompt, answer key)
ESSAYS = [
    ("A forest fire releases carbon dioxide. Explain why the carbon does not disappear and name one "
     "process that could later remove some carbon dioxide from the atmosphere.",
     "ANSWER KEY - Sample response: The carbon does not disappear during a forest fire. Combustion moves "
     "carbon from trees into the atmosphere as carbon dioxide. Photosynthesis could later remove some of "
     "that carbon dioxide as new plants grow. Ocean uptake could also move carbon dioxide into ocean water."),
    ("Explain one way carbon can move through at least three Earth systems. Use arrows or words to show "
     "the direction of movement.",
     "ANSWER KEY - Sample response: Atmosphere -> biosphere by photosynthesis; biosphere -> geosphere through "
     "decomposition and soil storage; geosphere -> atmosphere through combustion or a volcanic eruption. "
     "Other scientifically accurate pathways should receive credit."),
]

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()


class Canvas:
    def __init__(self, base, course):
        self.base, self.course = base.rstrip("/"), course
        self.token = os.environ.get("CANVAS_TOKEN")

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=CTX) as r:
            return json.loads(r.read() or "null")

    def quiz_api(self, method, path, body=None):
        return self.call(method, f"/api/quiz/v1/courses/{self.course}/quizzes{path}", body)


def item(position, points, title, entry):
    return {"item": {"position": position, "points_possible": points,
                     "entry_type": "Item", "entry": {"title": title, **entry}}}


def choice(n, prompt, choices, answer, reason):
    ids = [str(uuid.uuid4()) for _ in choices]
    return item(n, 1, f"Question {n}", {
        "item_body": f"<p>{prompt}</p>",
        "interaction_type_slug": "choice",
        "interaction_data": {"choices": [
            {"id": i, "position": p, "item_body": f"<p>{c}</p>"}
            for p, (i, c) in enumerate(zip(ids, choices), 1)]},
        "properties": {"shuffle_rules": {"choices": {"shuffled": False}}, "vary_points_by_answer": False},
        "scoring_data": {"value": ids[answer]},
        "scoring_algorithm": "Equivalence",
        "feedback": {"neutral": f"<p>{reason}</p>"},
    })


def fill_blank(n, prompt, answers):
    bid = str(uuid.uuid4())
    if len(answers) == 1:
        algorithm = "TextCloseEnough"  # forgives one typo
        scoring = {"value": answers[0], "blank_text": answers[0], "edit_distance": 1}
    else:
        algorithm = "TextInChoices"
        variants = list(dict.fromkeys(v for a in answers for v in (a, a.lower(), a.title())))
        scoring = {"value": variants, "blank_text": answers[0]}
    return item(n, 1, f"Question {n}", {
        "item_body": f'<p>{prompt}</p><p><span id="blank_{bid}"></span></p>',
        "interaction_type_slug": "rich-fill-blank",
        "interaction_data": {"blanks": [{"id": bid, "answer_type": "openEntry"}],
                             "reuse_word_bank_choices": False, "word_bank_choices": []},
        "properties": {"shuffle_rules": {"blanks": {"children": {"0": {"children": None}}}}},
        "scoring_data": {
            "value": [{"id": bid, "scoring_algorithm": algorithm, "scoring_data": scoring}],
            "working_item_body": f"<p>{prompt}</p><p>`{answers[0]}`</p>",
        },
        "scoring_algorithm": "MultipleMethods",
    })


def essay(n, prompt, key):
    return item(n, 4, f"Question {n}", {
        "item_body": f"<p>{prompt}</p>",
        "interaction_type_slug": "essay",
        "interaction_data": {"rce": True, "essay": None, "word_count": False, "file_upload": False,
                             "spell_check": True, "word_limit_max": None, "word_limit_min": None,
                             "word_limit_enabled": False},
        "properties": {},
        "scoring_data": {"value": f"{key}\n\n{RUBRIC}"},
        "scoring_algorithm": "None",
    })


def build_items():
    items, n = [], 0
    for q in MC:
        n += 1
        items.append(choice(n, *q))
    for q in VOCAB:
        n += 1
        items.append(fill_blank(n, *q))
    for q in ESSAYS:
        n += 1
        items.append(essay(n, *q))
    return items


if __name__ == "__main__":
    api = Canvas(sys.argv[1], sys.argv[2])
    quiz = api.quiz_api("POST", "", {"quiz": {
        "title": TITLE, "instructions": INSTRUCTIONS,
        "assignment_group_id": str(ASSIGNMENT_GROUP), "published": False, "grading_type": "points",
    }})
    items = build_items()
    for it in items:
        api.quiz_api("POST", f"/{quiz['id']}/items", it)
    # New Quizzes doesn't total item points on its own until the quiz is opened in the editor.
    total = sum(it["item"]["points_possible"] for it in items)
    api.quiz_api("PATCH", f"/{quiz['id']}", {"quiz": {"points_possible": total}})
    api.call("POST", f"/api/v1/courses/{api.course}/modules/{MODULE}/items",
             {"module_item": {"type": "Assignment", "content_id": int(quiz["id"])}})
    quiz = api.quiz_api("GET", f"/{quiz['id']}")
    print(f"{quiz['title']}: id {quiz['id']}, {quiz['points_possible']} pts")
    print(f"{api.base}/courses/{api.course}/assignments/{quiz['id']}")
