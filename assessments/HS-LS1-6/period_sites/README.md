# Unit 1.3 CSA: review sites by class period

One interactive review site per class period, built from that class's results on the Unit 1.3 CSA (HS-LS1-6). Each site opens with the class snapshot (percent of points earned on each of the six skills, weakest first) and the top 3 targets with the test questions behind them. Below that are mini-lessons and fresh practice questions for every skill, ordered weakest to strongest, plus written-answer practice and a ready check.

Sites are in `sites/`, named `HS-LS1-6_review_<Teacher>_<CP|GATE>_P<period>.html`. They show class results only, with no student names or individual scores.

| Teacher | Test | Periods |
| --- | --- | --- |
| Renick | CP | 5, 7 |
| Leapley | CP | 7 |
| Leapley | GATE | 5, 6 |
| Boyles | GATE | 1, 2 |
| Bogner | CP | 1, 2, 3, 6, 7 |

## Notes on the data

- First attempts only.
- The CP test has official skill tags (LS1-6.1 to 6.6). The GATE test does not, so its questions are mapped to skills by what they ask (see `GATE_MAP` in `analyze.py`). GATE question 1 (vocabulary) is reported separately.
- The CP written answer on question 16 (LS1-6.6) shows full marks for nearly everyone in every file, so it looks unscored. It is left out, and the 6.6 number rests on question 15 alone. Re-export after scoring and rebuild.
- Blank cells (not attempted or not graded) are left out of an item's percent.

## Rebuilding, or adding a teacher (for example Silva)

1. Export the New Quizzes **Student Analysis Report** CSV for each teacher into a local folder. Keep the raw CSVs out of the repo, since they have student names.
2. `python3 analyze.py <folder>` writes `periods.json` (class-level numbers only).
3. `python3 build.py` rebuilds every site in `sites/`.

The look and behavior come from `../../review_sites/engine.css` and `engine.js`. The skill lessons and practice questions are in `../../review_sites/skills13.py`. The practice questions are new scenarios so they do not repeat the CSA items.
