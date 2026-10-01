# Unit 1.3 Sugar to Structures (HS-LS1-6): 10-day sequence

Launch to CSA in 10 class days (45 minutes each). Each CFA closes the lesson that teaches its target. A score below a B (fewer than 4 of 5) opens that target's Mastery Path review.

| Day | Lesson | Slides (Drive, Unit 1.3 folder) | CFA |
| --- | --- | --- | --- |
| 1 | The Giant Pumpkin Mystery (phenomenon; the unit CER starts) | Lesson 1 | none |
| 2 | **New:** Vocabulary (10 Frayer models) and SketchNotes (5 big ideas, Pumpkin Path sensemaking page) | Day 2 Vocabulary and SketchNotes | none |
| 3 | What Are Living Things Made Of? | Lesson 2 (CFA slide added) | LS1-6.1 |
| 4 | Building Sugar from Air and Water | Lesson 3 (CFA slide added) | LS1-6.2 |
| 5 | From Sugar to Amino Acids | Lesson 4 (CFA slide added) | LS1-6.3 |
| 6 | Small Pieces, Big Molecules | Lesson 5 (pptx) | LS1-6.4 |
| 7 | What's the Evidence? (jigsaw) | Lesson 6 (pptx) | LS1-6.5 |
| 8 | Solving the Pumpkin Mystery (the unit CER is finished) | Lesson 7 (pptx) | LS1-6.6 |
| 9 | Practice test and review stations | Day 9 Practice Test and Review | practice test → review or extension |
| 10 | Unit 1.3 CSA | Day 10 Unit 1.3 CSA | |

**Unit CER:** Students start it on Day 1 with the question "Where does a giant pumpkin's mass come from?" and a first claim. They add a row to an evidence log each day. They finish it on Day 8 as the explanation for the grower.

**Timing:** Each lesson day keeps the original lesson's activities. Minutes are trimmed to make room for the 6-minute CFA. The teacher pages give the adjusted agenda.

**Canvas (course 330720):**
- **Unit 1.3 module:** a "Day N" header for each day, then the student page, then that day's CFA and its review. Day 9 holds the practice test, review, and extension, and Day 10 holds the CSA.
- **Teacher pages:** they're in the module "Unit 1.3 TEACHER PAGES (keep unpublished)". Each has the agenda, materials, teaching notes, answer key, and supports.

Files:
- `unit13_lessons.py`: the content of every day's pages.
- `canvas_lessons_upload.py`: `CANVAS_TOKEN=... python3 canvas_lessons_upload.py https://kernhigh.instructure.com 330720 1634113` creates or updates the pages and orders the module. It's safe to run again.
- `deck_requests.py`: Google Slides requests that built the Day 2, 9, and 10 decks (each a copy of the Lesson 2 deck).
- `cfa_slide_requests.py`: requests that added the CFA slide to the Lesson 2–4 Google decks.
