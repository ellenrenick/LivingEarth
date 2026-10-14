# HS-LS1-6 Assessment: From Sugar to Building Blocks

Grade 9 Living Earth (Biology) assessment for **HS-LS1-6**: how carbon, hydrogen, and oxygen from sugar combine with other elements to form amino acids and other large carbon-based molecules.

| Part | Items | DOK | Points |
| --- | --- | --- | --- |
| Vocabulary matching | 8 terms (+2 distractors) | 1 | 8 |
| Multiple choice (scenario-based) | 10 | 2 and 3 | 20 |
| Free response (CER / revise an explanation), 4-point rubric | 2 | 3 | 8 |
| **Total** | | | **36** |

## Files

**Summative test** (about 50 minutes)
- `HS-LS1-6_canvas_qti.zip`: import this into Canvas.
- `HS-LS1-6_teacher_key.md`: all questions with the answer key, DOK levels, 4-point rubrics, grading notes, and sample answers.
- `questions.py`: the question bank.

**CFAs** (one 6-point exit ticket per priority learning target, replacing a practice test)
- `HS-LS1-6_CFA_canvas_qti.zip`: one Canvas quiz per CFA. `HS-LS1-6_CFA_key.md`: answers and scoring guides.
- `cfa.py`: the CFA bank. Rebuild with `python3 ../build_unit.py HS-LS1-6`.

**Review** (done on the review day, after the CFAs and before the CSA, about 30 to 40 minutes)
- `HS-LS1-6_review.html`: student review. Students use their CFA scores (below 4 of 6) to pick sections; everyone does Vocabulary and Write It. Open in a browser to print, or paste the part between `<body>` and `</body>` into a Canvas Page's HTML editor.
- `HS-LS1-6_review_key.md`: answer key and model answer.
- `review.py`: the review bank.

To change the CSA, edit `questions.py` and run `python3 build.py`.

**Uploading straight to Canvas:** `CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com <course id>` builds the CSA question by question through the Canvas API and creates the review page. It doesn't need a file upload. Everything is created unpublished. Running it again creates duplicates.

## Importing into Canvas

1. In your course, go to **Settings → Import Course Content**.
2. Content Type: **QTI .zip file**. Choose `HS-LS1-6_canvas_qti.zip`.
3. Select **All content**, then click **Import**. When it finishes, the quiz shows up under **Quizzes**. Canvas creates it unpublished.
4. Before you publish, check the settings: time limit, availability dates, and whether students can see correct answers.
5. For the practice test, set **Quiz Type** to **Practice Quiz** so it doesn't count toward grades, and set the **Time Limit** to 20 minutes if you want one. The zip doesn't set these.

Notes:
- Canvas grades the matching and multiple-choice questions automatically. The 2 free-response questions are essays that you grade in SpeedGrader. Each essay's feedback holds its 4-point rubric, grading notes, and a sample answer. Canvas shows this feedback to students after they submit. To hide it, turn off **Let students see their quiz responses** in the quiz settings.
- If you use **New Quizzes**, import into Classic first and then migrate the quiz, or import the zip from inside New Quizzes. Check the data tables after migration.
