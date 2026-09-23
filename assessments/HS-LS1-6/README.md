# HS-LS1-6 Assessment: From Sugar to Building Blocks

Grade 9 Living Earth (Biology) assessment for **HS-LS1-6**: how carbon, hydrogen, and oxygen from sugar combine with other elements to form amino acids and other large carbon-based molecules.

| Part | Items | DOK | Points |
| --- | --- | --- | --- |
| Vocabulary matching | 8 terms (+2 distractors) | 1 | 8 |
| Multiple choice (scenario-based) | 10 | 2 and 3 | 20 |
| Free response (CER / revise an explanation), 4-point rubric | 2 | 3 | 8 |
| **Total** | | | **36** |

**Lessons:** the 7-lesson unit that leads into these assessments is in [`lessons/HS-LS1-6`](../../lessons/HS-LS1-6/README.md).

## Files

**Summative test** (about 50 minutes)
- `HS-LS1-6_canvas_qti.zip`: import this into Canvas.
- `HS-LS1-6_teacher_key.md`: all questions with the answer key, DOK levels, 4-point rubrics, grading notes, and sample answers.
- `questions.py`: the question bank.

**Practice test** (about 20 minutes, 22 points, unlimited attempts)
- `HS-LS1-6_practice_canvas_qti.zip`: import this into Canvas. It has 6 matching terms, 6 multiple-choice questions (DOK 2 and 3), and 1 free-response question (DOK 3, 4-point rubric). All scenarios are new, so the practice test doesn't give away the summative.
- `HS-LS1-6_practice_teacher_key.md`: answer key, rubric, and grading notes.
- `practice_questions.py`: the question bank.

**Review** (do after the practice test, about 30–40 minutes)
- `HS-LS1-6_review.html`: student review. It maps each practice question to a review section and includes vocabulary, atom accounting, energy vs. matter, tracing atoms, evidence matching, scoring sample answers, and revising an explanation. Open it in a browser to print. To use it as a Canvas Page, paste the part between `<body>` and `</body>` into the page's HTML editor.
- `HS-LS1-6_review_key.md`: answer key for the review.

To change a quiz, edit its question bank and run `python3 build.py`, which rebuilds both quizzes.

**Uploading straight to Canvas:** `CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com <course id>` builds both quizzes question by question through the Canvas API and creates the review page and the seven lesson handout pages (from `lessons/HS-LS1-6/handouts`). It doesn't need a file upload. Everything is created unpublished. Running it again creates duplicates, so if you already uploaded the quizzes and review, add `--only lessons` to create just the lesson pages. `--only` takes any of `quizzes`, `review`, `lessons`, separated by commas. Add `--dry-run` to list what would be created without touching Canvas.

## Importing into Canvas

1. In your course, go to **Settings → Import Course Content**.
2. Content Type: **QTI .zip file**. Choose `HS-LS1-6_canvas_qti.zip`.
3. Select **All content**, then click **Import**. When it finishes, the quiz shows up under **Quizzes**. Canvas creates it unpublished.
4. Before you publish, check the settings: time limit, availability dates, and whether students can see correct answers.
5. For the practice test, set **Quiz Type** to **Practice Quiz** so it doesn't count toward grades, and set the **Time Limit** to 20 minutes if you want one. The zip doesn't set these.

Notes:
- Canvas grades the matching and multiple-choice questions automatically. The 2 free-response questions are essays that you grade in SpeedGrader. Each essay's feedback holds its 4-point rubric, grading notes, and a sample answer. Canvas shows this feedback to students after they submit. To hide it, turn off **Let students see their quiz responses** in the quiz settings.
- If you use **New Quizzes**, import into Classic first and then migrate the quiz, or import the zip from inside New Quizzes. Check the data tables after migration.
