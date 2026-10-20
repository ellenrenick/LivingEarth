# Living Earth course materials

## Rules for every CFA and CSA

1. **Every CFA and CSA is a New Quiz.** Never build one as a classic quiz. To convert an
   existing classic quiz, use `assessments/HS-LS1-6/classic_to_newquiz.py` (keeps questions,
   points, module spot, and Mastery Path rule; leaves the classic quiz renamed "OLD classic: …"
   and unpublished).
2. **Every CFA and CSA uses these quiz settings:**
   - Shuffle questions: on
   - Shuffle answers: on
   - Restrict student result view ("hide results"): on, with **no** other toggle under it
     selected (no points awarded, points possible, items, responses, correctness, correct
     answers, or feedback).

   In code these are `CFA_CSA_SETTINGS` in `assessments/HS-LS1-6/newquiz_upload.py`; pass them
   in `quiz_settings` when creating a quiz. To re-apply them to a whole course, run
   `python3 assessments/HS-LS1-6/cfa_csa_settings.py https://kernhigh.instructure.com <course_id>`.

## Rule for every lesson: pace and style

Model every new or revised lesson on Unit 1.3 Short Lessons A and B
(`assessments/HS-LS1-6/lessons/short_lessons.py`). The teacher says their pace and content style work for her classes.

- **Pace:** Short A and B run about 30 minutes of student work, including the CFAs. Every lesson stays within 10
  minutes of that, so 20 to 40 minutes in total, counting CFAs. Plan the minutes on the slides and the teacher
  page, and make sure they add up. A lab or CSA day may use the full period.
- **Style:**
  - Each activity is short: about 2 to 8 minutes, and the mini-lesson is about 5 minutes.
  - Every notebook section has its own slide, in the same order as the notebook setup.
  - Every fill-in has a sentence frame and a word bank. Word banks are always scrambled, never in answer order.
  - Show one worked example, then let students do the rest.
  - The evidence is a small data table with real numbers.
  - The lesson ends with the CFA(s), taken from memory.
  - A short animation or simulation reviews the key idea, where it helps.

Courses: live 342850, sandbox 330720.
