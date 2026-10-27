"""Create the Bootcamp reassessment (a New Quiz) in a Canvas course.

Usage: CANVAS_TOKEN=... python3 bootcamp_reassessment.py https://kernhigh.instructure.com <course id>
Matches the other reassessments: simplified wording, word help, 4 points, results hidden, unpublished.
It goes in the same assignment group as the course's Unit 1.1 Reassessment. Running it twice makes two quizzes.
"""
import json, os, ssl, sys, urllib.parse, urllib.request, uuid

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
base, course = sys.argv[1].rstrip("/"), sys.argv[2]
tok = os.environ["CANVAS_TOKEN"]
TITLE = "Bootcamp Reassessment: Science Skills"

INSTRUCTIONS = ("<p><strong>Bootcamp Reassessment: Science Skills</strong></p>"
    "<p>Show what you know about asking science questions, living things, writing a CER, and taking notes. Read each question slowly. You can read it twice.</p>"
    "<p><strong>Word help:</strong></p><ul>"
    "<li><strong>Claim</strong> = the answer to the question.</li>"
    "<li><strong>Evidence</strong> = data (numbers) from the investigation that supports the claim.</li>"
    "<li><strong>Reasoning</strong> = explains WHY the evidence supports the claim.</li>"
    "<li><strong>Organism</strong> = a whole living thing.</li></ul>")

SETTINGS = {"calculator_type": "none", "filter_ip_address": False, "filters": {}, "one_at_a_time_type": "none", "allow_backtracking": True,
            "shuffle_answers": True, "shuffle_questions": True, "require_student_access_code": False, "student_access_code": None,
            "has_time_limit": False, "session_time_limit_in_seconds": 0, "multiple_attempts": {},
            "result_view_settings": {"display_items": False, "display_item_feedback": False, "display_item_response": False, "display_points_awarded": False,
                                     "result_view_restricted": True, "display_points_possible": False, "display_item_correct_answer": False,
                                     "display_item_response_correctness": False}}

# (title, question, options, index of correct option), 0.25 points each
MC = [
    ("Best scientific question", "Which question can be tested in an investigation?",
     ["Which flavor of ice cream is best?", "How does the amount of water change how tall a bean plant grows?", "Why is summer fun?", "Are dogs better than cats?"], 1),
    ("Shared by all living things", "Which is true for ALL living things?",
     ["They can move from place to place.", "They are made of cells.", "They live on land.", "They have green parts."], 1),
    ("Responding to the environment", "Which example BEST shows a living thing responding to its environment?",
     ["Ice melting on a warm day", "Wind blowing sand into a pile", "A sunflower turning its flower to face the sun", "A stone rolling down a hill"], 2),
    ("Sketchnote elements", "According to the Sketchnote Bootcamp, which list has the FOUR elements of sketchnoting?",
     ["Reading, Writing, Testing, Memorizing", "Notes, Homework, Labs, Quizzes", "Highlighting, Typing, Copying, Coloring", "Color, Picture, Text, Template"], 3),
    ("50/50 rule", "What does the 50/50 rule of sketchnoting mean?",
     ["Half of the page is left blank.", "Your notes have about equal amounts of pictures and text.", "You use 50 words and 50 pictures.", "You only draw pictures."], 1),
    ("Focused notes", "Which action is part of focused note-taking?",
     ["Copy every word from the board.", "Skip the parts that are confusing.", "Highlight key words and write a question about the notes.", "Use only one color so the page looks neat."], 2),
]
MATCH = ("Match words", "<p><strong>Match each word to its meaning.</strong> One meaning will not be used.</p>",
         [("Claim", "The answer to the question"), ("Evidence", "Data from the investigation that supports the claim"),
          ("Reasoning", "Explains WHY the evidence supports the claim"), ("Organism", "A whole living thing"),
          ("Sketchnote", "Notes that use pictures, text, color, and a template")], ["A guess made with no data"])
ESSAY_BODY = ("<p><strong>Scenario:</strong> A class investigated whether bean seeds sprout better in warm soil or in cold soil. Each group had 10 seeds.</p>"
    "<p>Seeds in warm soil (24 °C): 9 of 10 seeds sprouted.<br>Seeds in cold soil (10 °C): 3 of 10 seeds sprouted.</p>"
    "<p><strong>Write a CER response.</strong></p><p><strong>Claim:</strong> Which condition helped the seeds sprout better?<br>"
    "<strong>Evidence:</strong> Use numbers from the investigation.<br><strong>Reasoning:</strong> Explain WHY the evidence supports your claim. Use biology!</p>"
    "<p>Sentence starters: <em>My claim is ... The evidence is ... This supports my claim because ...</em></p>")
ESSAY_SCORE = ("Scoring (2 pts, 4-level CER rubric): 2.0 = Mastery. Clear claim (warm soil), evidence with specific numbers from BOTH groups (9 of 10 and 3 of 10), and reasoning that explains WHY using biology (for example: seeds need warmth for the cell processes that use stored food and energy to start growing, so cold slows those processes). "
    "1.5 = Proficient. Clear claim and numbers from the data, but the reasoning is missing or only restates the data. "
    "1.0 = Developing. Claim and some data, but the data is not used to prove the claim, or the numbers are vague (for example, 'more seeds sprouted'). "
    "0.5 = Emerging. Some ideas or vocabulary, but the claim or evidence is missing or wrong. 0 = Blank or off-topic. "
    "Grading notes: Accept everyday wording in the reasoning. Do not take off points for spelling. Accept 90% and 30% for the numbers. A common mistake is a claim with no numbers, or evidence with no explanation of why. "
    "Exemplar (full credit): My claim is that seeds sprout better in warm soil. The evidence is that 9 of 10 seeds sprouted in warm soil (24 °C), but only 3 of 10 sprouted in cold soil (10 °C). This supports my claim because seeds need warmth for the cell processes that use their stored food and energy to start growing, and cold slows those processes down.")


def api(method, path, body=None):
    req = urllib.request.Request(base + path, data=json.dumps(body).encode() if body is not None else None, method=method)
    req.add_header("Authorization", "Bearer " + tok); req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, context=CTX) as r:
        return json.loads(r.read() or "null")


# same assignment group as the course's Unit 1.1 Reassessment (if there is one)
q = urllib.parse.urlencode({"search_term": "Unit 1.1 Reassessment"})
found = api("GET", f"/api/v1/courses/{course}/assignments?{q}")
group = found[0]["assignment_group_id"] if found else None
quiz_body = {"title": TITLE, "instructions": INSTRUCTIONS, "points_possible": 4, "quiz_settings": SETTINGS}
if group:
    quiz_body["assignment_group_id"] = str(group)
quiz = api("POST", f"/api/quiz/v1/courses/{course}/quizzes", {"quiz": quiz_body})
qid = quiz["id"]
print("quiz", qid, quiz.get("title"))


def item(pos, pts, entry):
    return api("POST", f"/api/quiz/v1/courses/{course}/quizzes/{qid}/items", {"item": {"position": pos, "points_possible": pts, "entry_type": "Item", "entry": dict(entry, calculator_type="none")}})


pos = 0
for title, text, opts, ok in MC:
    pos += 1
    ids = [str(uuid.uuid4()) for _ in opts]
    item(pos, 0.25, {"title": title, "item_body": f"<p><strong>{text}</strong></p>", "interaction_type_slug": "choice",
        "interaction_data": {"choices": [{"id": i, "position": n + 1, "item_body": f"<p>{o}</p>"} for n, (i, o) in enumerate(zip(ids, opts))]},
        "properties": {"shuffle_rules": {"choices": {"shuffled": True}}, "vary_points_by_answer": False},
        "scoring_data": {"value": ids[ok]}, "scoring_algorithm": "Equivalence"})
pos += 1
title, body, pairs, extra = MATCH
qids = [str(uuid.uuid4()) for _ in pairs]
item(pos, 0.5, {"title": title, "item_body": body, "interaction_type_slug": "matching",
    "interaction_data": {"answers": [p[1] for p in pairs] + extra, "questions": [{"id": i, "item_body": p[0]} for i, p in zip(qids, pairs)]},
    "properties": {"shuffle_rules": {"questions": {"shuffled": False}}},
    "scoring_data": {"value": {i: p[1] for i, p in zip(qids, pairs)},
                     "edit_data": {"matches": [{"answer_body": p[1], "question_id": i, "question_body": p[0]} for i, p in zip(qids, pairs)], "distractors": extra}},
    "scoring_algorithm": "PartialDeep"})
pos += 1
item(pos, 2.0, {"title": "Scenario: CER", "item_body": ESSAY_BODY, "interaction_type_slug": "essay",
    "interaction_data": {"rce": True, "essay": None, "word_count": True, "file_upload": False, "spell_check": True, "word_limit_enabled": False},
    "properties": {"word_limit": False, "spell_check": False, "word_limit_max": 0, "word_limit_min": 0, "show_word_count": False, "rich_content_editor": False},
    "scoring_data": {"value": ESSAY_SCORE}, "scoring_algorithm": "None"})
print("items", pos, "assignment group", group)
