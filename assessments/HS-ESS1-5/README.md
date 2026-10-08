# Unit 3.1 Age of the Earth assessments (HS-ESS1-5, supporting HS-ESS1-6)

Grade 9 Living Earth. Five CFAs, one CSA, and five Mastery Path review assignments, built as Canvas New Quizzes. See `../../units/HS-ESS1-5/unit_plan.md` for the unit.

| Piece | Items | Notes |
| --- | --- | --- |
| CFA ESS1-5.1 (continental drift evidence) | 5 | Auto-graded, 4-point scale |
| CFA ESS1-5.2 (seafloor spreading and age pattern) | 5 | Auto-graded |
| CFA ESS1-5.3 (plate boundaries and subduction) | 5 | Auto-graded |
| CFA ESS1-6.1 (radiometric dating) | 5 | Auto-graded |
| CFA ESS1-5.4 (building the argument) | 5 | Auto-graded |
| CSA | 16 | 14 auto-graded, Q14 (CER) and Q16 (revise an explanation) teacher-graded with 4-point rubrics |
| Mastery Path reviews | 5 | One per CFA. Opens when the CFA score is below 3 of 4 (fewer than 4 of 5 correct). Pass/fail, 4 points, 3 written questions |

## Files

- `questions.py`: the question bank (CFAs, CSA, reviews). Answer order is shuffled with a fixed seed.
- `canvas_upload.py`: builds everything in a Canvas course through the API.
- `build_key.py` and `HS-ESS1-5_teacher_key.md`: the teacher key, generated from the bank.
- `canvas_ids.json`: IDs created in the last upload, used by `--cleanup`.

## Using it

```
python3 canvas_upload.py https://kernhigh.instructure.com <course id> --dry-run   # check only
python3 canvas_upload.py https://kernhigh.instructure.com <course id>             # build
python3 canvas_upload.py https://kernhigh.instructure.com <course id> --cleanup   # remove what the last run built
python3 build_key.py                                                              # rebuild the teacher key
```

Set `CANVAS_TOKEN` when running outside the cloud sandbox. Everything is created unpublished, in a module with one subheader per day. Running the upload twice makes duplicates, so run `--cleanup` first.

To change a question, edit `questions.py`, run `build_key.py`, and rebuild in Canvas.

## Built so far

Built in the **26-27 CP Living Earth Sandbox** (course 330720) only. Not yet in the GATE sandbox or any teaching course.
