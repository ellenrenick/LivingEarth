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

Courses: live 342850, sandbox 330720.
