# Living Earth assessments

One folder per priority standard (one per unit). Each holds a 45-minute CSA and one CFA per priority learning target.

| Unit | Folder | CSA | CFAs |
| --- | --- | --- | --- |
| 1.1 Organization in Organisms | `HS-LS1-2` | 30 pts, 45 min | 6 |
| 1.2 Energy Through Carbon | `HS-LS2-5` | 30 pts, 45 min | 6 |
| 1.3 Sugar to Structures | `HS-LS1-6` | 36 pts, about 50 min (built first; see its README) | 6 |
| 2.1 DNA to Proteins | `HS-LS1-1` | 30 pts, 45 min | 6 |
| 2.2 Inherited Instructions | `HS-LS3-2` | 30 pts, 45 min | 6 |
| 3.1 Age of the Earth | `HS-ESS1-5` | 30 pts, 45 min | 6 |
| 3.2 Changing Earth, Changing Life | `HS-ESS2-7` | 30 pts, 45 min | 6 |
| 3.3 Patterns of the Past | `HS-LS4-1` | 30 pts, 45 min | 4 (LS4-1.1 is a pre-assessment prompt) |
| 3.4 Evolution by Selection | `HS-LS4-4` | 30 pts, 45 min | 4 |
| 4.1 Cycles of Life | `HS-LS2-4` | 30 pts, 45 min | 6 |
| 4.2 Patterns in Populations | `HS-LS2-2` | 30 pts, 45 min | 6 |
| 4.3 Earth Shaping Humanity | `HS-ESS3-1` | 30 pts, 45 min | 6 |
| 4.4 Solutions for Sustainability | `HS-LS2-7` | 30 pts, 45 min | 5 |

## CSA format (45 minutes, 30 points)
6 vocabulary matches (6 pts), 8 multiple choice (16 pts, DOK 2 and 3), 2 free response with 4-point rubrics (8 pts). Items stay at or below DOK 3 and respect each standard's assessment boundary.

## CFA format
One exit ticket (5 to 7 minutes, 6 points) per priority learning target. DOK 1 targets get 3 multiple-choice items; higher targets get 2 multiple-choice items and 1 short response with a 0 to 2 scoring guide. Mastery is 4 of 6. Each CFA is placed on the class that closes its target (see `pacing.json` and the unit tabs in the workbook).

## Files in each folder
- `questions.py`: the CSA bank. `cfa.py`: the CFA bank.
- `<STD>_canvas_qti.zip` and `<STD>_teacher_key.md`: CSA for Canvas and the teacher key.
- `<STD>_CFA_canvas_qti.zip` and `<STD>_CFA_key.md`: one Canvas quiz per CFA (import once, get all of them) and the key.

## Rebuilding
`python3 build_unit.py HS-LS1-2` (one unit) or `python3 build_unit.py all`. `HS-LS1-6` only rebuilds its CFAs here; its CSA is built by `HS-LS1-6/build.py`.

`pacing.json` holds the day-by-day plan used by the workbook (priority targets get the most time, supporting and thread targets are compressed, every unit ends with a review day and a CSA day).
