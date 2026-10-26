# Unit 3.1 Age of the Earth assessments (HS-ESS1-5, supporting HS-ESS1-6)

Grade 9 Living Earth. Five CFAs (one per priority target ESS1-5.1 to 5.5; the supporting ESS1-6 targets have none), one CSA on the same five targets, and five Mastery Path review assignments, built as Canvas New Quizzes. See `../../units/HS-ESS1-5/unit_plan.md` for the unit.

| Piece | Items | Notes |
| --- | --- | --- |
| CFA ESS1-5.1 (plates, boundaries, and crust) | 5 | Auto-graded, 4-point scale |
| CFA ESS1-5.2 (reading rock ages) | 5 | Auto-graded |
| CFA ESS1-5.3 (why ocean crust is young and continents are old) | 5 | Auto-graded |
| CFA ESS1-5.4 (evidence for moving crust) | 5 | Auto-graded |
| CFA ESS1-5.5 (how well plate tectonics explains rock ages) | 5 | Auto-graded |
| CSA | 12 | Priority targets ESS1-5.1 to 5.5 only (supporting targets are never on the CSA). 10 auto-graded; Q10 (evaluate evidence) and Q12 (evaluate plate tectonics with data) teacher-graded with 4-point rubrics |
| Mastery Path reviews | 5 | One per CFA. Opens when the CFA score is below 3 of 4 (fewer than 4 of 5 correct). Pass/fail, 4 points, 3 written questions |

Targets and tiers come from the team workbook "Renick Living Earth Standards and Learning Targets (26-27)" (Targets tab).

## Files

- `questions.py`: the question bank (CFAs, CSA, reviews). Answer order is shuffled with a fixed seed.
- `canvas_upload.py`: builds the CFAs, CSA, reviews, and Mastery Path rules in a Canvas course through the API.
- `lessons.py`: the student pages, teacher pages, and extra assignments (Lesson 1, Lesson 4 SketchNotes, CER, Enrichment).
- `slides_spec.py`, `make_requests.py`, `lines.py`: generate the eight Google Slides lesson decks (see the unit plan).
- `canvas_lessons.py`: builds the pages and assignments and replaces the simple module with the full day-by-day module plus a teacher module.
- `build_key.py` and `HS-ESS1-5_teacher_key.md`: the teacher key, generated from the bank.
- `canvas_ids.json`: IDs created in the last upload, used by `--cleanup`.

## Using it

```
python3 canvas_upload.py https://kernhigh.instructure.com <course id> --dry-run   # check only
python3 canvas_upload.py https://kernhigh.instructure.com <course id>             # build quizzes, reviews, rules
python3 canvas_lessons.py https://kernhigh.instructure.com <course id>            # then build pages, assignments, modules
python3 canvas_lessons.py https://kernhigh.instructure.com <course id> --cleanup  # remove pages, extra assignments, teacher module
python3 canvas_upload.py https://kernhigh.instructure.com <course id> --cleanup   # remove what the last run built
python3 build_key.py                                                              # rebuild the teacher key
```

Run `canvas_upload.py` first, then `canvas_lessons.py`. To start over, run both `--cleanup` options.

Set `CANVAS_TOKEN` when running outside the cloud sandbox. Everything is created unpublished, in a module with one subheader per day. Running the upload twice makes duplicates, so run `--cleanup` first.

To change a question, edit `questions.py`, run `build_key.py`, and rebuild in Canvas.

## Built so far

Built in the **26-27 CP Living Earth Sandbox** (course 330720) only. Not yet in the GATE sandbox or any teaching course.

The Enrichment choice board is unpublished and hidden from all students. Use **Assign To** for the students you pick, then publish it.
