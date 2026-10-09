# Unit 1.3 Sugar to Structures (HS-LS1-6): 10-day sequence

Launch to CSA in 10 class days (45 minutes each). Each CFA closes the lesson that teaches its target. A score below a B (fewer than 4 of 5) opens that target's Mastery Path review.

| Day | Date | Lesson | Slides (Drive, Unit 1.3 folder) | CFA |
| --- | --- | --- | --- | --- |
| 1 | Thu Oct 8 | The Giant Pumpkin Mystery (phenomenon; the unit CER starts) | Lesson 1 | none |
| | Fri Oct 9 | Makeup work day (no Unit 1.3 lesson) | | |
| 2 | Mon Oct 12 | What Are Living Things Made Of? | Lesson 2 (CFA slide added) | LS1-6.1 |
| 3 | Tue Oct 13 | Building Sugar from Air and Water | Lesson 3 (CFA slide added) | LS1-6.2 |
| 4 | **Wed Oct 14, sub** | Vocabulary (one-page Frayer chart) and SketchNotes (5 big ideas, Pumpkin Path), notebook only | Day 4 Vocabulary and SketchNotes | none |
| 5 | Thu Oct 15 | From Sugar to Amino Acids (bead lab; uses Day 3's glucose bags) | Lesson 4 (CFA slide added) | LS1-6.3 |
| 6 | **Fri Oct 16, sub** | What's the Evidence? (jigsaw) | Lesson 6 (CFA slide added after the exit ticket) | LS1-6.5 |
| 7 | Mon Oct 19 | Small Pieces, Big Molecules | Lesson 5 (CFA slide added) | LS1-6.4 |
| 8 | Tue Oct 20 | Solving the Pumpkin Mystery (the unit CER is finished) | Lesson 7 (CFA slide added) | LS1-6.6 |
| 9 | Wed Oct 21 | Interventions: assigned CFA reviews, then review stations | Day 9 Interventions and Review | the CFA reviews each student was assigned |
| 10 | Thu Oct 22 | Unit 1.3 CSA | Day 10 Unit 1.3 CSA | |

There is no practice test; the six CFAs spread through the unit take its place, and Day 9 is for the reviews they assign. The practice test, its review, and the extension are still in Canvas (unpublished) but are no longer in the module. The two sub days get the lessons that need no lab materials, so Lesson 6 runs before Lesson 5 (its stations draw on Lessons 3 and 4). Unit 2.1 starts Fri Oct 23.

**Unit CER:** Students start it on Day 1 with the question "Where does a giant pumpkin's mass come from?" and a first claim. They add a row to an evidence log each day. They finish it on Day 8 as the explanation for the grower.

**Timing:** Each lesson day keeps the original lesson's activities. Minutes are trimmed to make room for the 6-minute CFA. The teacher pages give the adjusted agenda.

**Canvas (course 330720):**
- **Unit 1.3 module:** a "Day N" header for each day, then the student page, then that day's CFA and its review. Day 9 holds the intervention page (students work their assigned CFA reviews), and Day 10 holds the CSA. The practice test, its review, and the extension were removed from the module.
- **Teacher pages:** they're in the module "Unit 1.3 TEACHER PAGES (keep unpublished)". Each has the agenda, materials, teaching notes, answer key, and supports.

Files:
- `unit13_lessons.py`: the content of every day's pages.
- `canvas_lessons_upload.py`: `CANVAS_TOKEN=... python3 canvas_lessons_upload.py https://kernhigh.instructure.com 330720 1634113` creates or updates the pages and orders the module. It's safe to run again.
- `deck_requests.py`: Google Slides requests that built the Day 5, 9, and 10 decks (each a copy of the Lesson 2 deck).
- `cfa_slide_requests.py`: requests that added the CFA slide to the Lesson 2–7 Google decks.
- `planner_requests.py`: requests that wrote these days into the October page of the LE Planner 2026-2027 deck.
