# Unit 1.3 Sugar to Structures (HS-LS1-6): 10-day sequence

Launch to CSA in 10 class days (45 minutes each). Each CFA closes the lesson that teaches its target. A score below a B (fewer than 4 of 5) opens that target's Mastery Path review.

| Day | Date | Lesson | Slides (Drive, Unit 1.3 folder) | CFA |
| --- | --- | --- | --- | --- |
| 1 | Thu Oct 8 | The Giant Pumpkin Mystery (phenomenon; the unit CER starts) | Lesson 1 | none |
| 2 | Fri Oct 9 | What Are Living Things Made Of? | Lesson 2 (CFA slide added) | LS1-6.1 |
| 3 | Mon Oct 12 | Building Sugar from Air and Water | Lesson 3 (CFA slide added) | LS1-6.2 |
| 4 | Tue Oct 13 | From Sugar to Amino Acids (bead lab, the day after Day 3's beads) | Lesson 4 (CFA slide added) | LS1-6.3 |
| 5 | **Wed Oct 14, sub** | Vocabulary (10 Frayer models) and SketchNotes (5 big ideas, Pumpkin Path), notebook only | Day 5 Vocabulary and SketchNotes | none |
| 6 | Thu Oct 15 | Small Pieces, Big Molecules | Lesson 5 (CFA slide added) | LS1-6.4 |
| 7 | **Fri Oct 16, sub** | What's the Evidence? (jigsaw) | Lesson 6 (CFA slide added after the exit ticket) | LS1-6.5 |
| 8 | Mon Oct 19 | Solving the Pumpkin Mystery (the unit CER is finished) | Lesson 7 (CFA slide added) | LS1-6.6 |
| 9 | Tue Oct 20 | Practice test and review stations | Day 9 Practice Test and Review | practice test → review or extension |
| 10 | Wed Oct 21 | Unit 1.3 CSA | Day 10 Unit 1.3 CSA | |

The two sub days get the lessons that need no lab materials. Unit 2.1 starts Thu Oct 22.

**Unit CER:** Students start it on Day 1 with the question "Where does a giant pumpkin's mass come from?" and a first claim. They add a row to an evidence log each day. They finish it on Day 8 as the explanation for the grower.

**Timing:** Each lesson day keeps the original lesson's activities. Minutes are trimmed to make room for the 6-minute CFA. The teacher pages give the adjusted agenda.

**Canvas (course 330720):**
- **Unit 1.3 module:** a "Day N" header for each day, then the student page, then that day's CFA and its review. Day 9 holds the practice test, review, and extension, and Day 10 holds the CSA.
- **Teacher pages:** they're in the module "Unit 1.3 TEACHER PAGES (keep unpublished)". Each has the agenda, materials, teaching notes, answer key, and supports.

Files:
- `unit13_lessons.py`: the content of every day's pages.
- `canvas_lessons_upload.py`: `CANVAS_TOKEN=... python3 canvas_lessons_upload.py https://kernhigh.instructure.com 330720 1634113` creates or updates the pages and orders the module. It's safe to run again.
- `deck_requests.py`: Google Slides requests that built the Day 5, 9, and 10 decks (each a copy of the Lesson 2 deck).
- `cfa_slide_requests.py`: requests that added the CFA slide to the Lesson 2–7 Google decks.
- `planner_requests.py`: requests that wrote these days into the October page of the LE Planner 2026-2027 deck.
