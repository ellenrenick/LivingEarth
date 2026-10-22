# Unit 2.2: Inherited Instructions (HS-LS3-2), Nov 9 to Dec 1, 2026

Built from the LE Planner and the Linked Workbook (tab "2.2 Inherited"). Eleven class days (Nov 11 and Nov 23 to 27 are off), in the
Unit 2.1 format: a daily deck (blue theme, orange accents), about 30 minutes of student work including the CFA, five CFAs
(one per priority target, 5 auto-graded questions each, below 4 of 5 opens a Mastery Path review), and a 13-question CSA
(19 raw points, graded out of 4).

| Day | Date | Deck | Targets | CFA |
| --- | --- | --- | --- | --- |
| 1 | Mon Nov 9 | [The Puppy Puzzle](https://docs.google.com/presentation/d/1jTmln-kX22vhyIaHH8Vvm-LBf_ZRH5bs0w13j3Af1PE/edit) | LS3-2.1 |  |
| 2 | Tue Nov 10 | [Mixing Information](https://docs.google.com/presentation/d/18HbEOI11iEdoNZcZcXkZtZJtzIPkXCFeYV-Cu9ADdII/edit) | LS3-2.1 | CFA LS3-2.1 |
| 3 | Thu Nov 12 | [Genetics Notes, Part 1: Genes and Alleles](https://docs.google.com/presentation/d/1IC_f8lutPWsxsGlG5-iVrVsglWzMSYDaQ0atsyISLu8/edit) | LS3-3.1 |  |
| 4 | Fri Nov 13 | [Genetics Notes, Part 2: Genotype, Phenotype, and Punnett Squares](https://docs.google.com/presentation/d/1gAb26s8KT0Z40GooPrW6WHfBVask6rYXE_hJT56IqOE/edit) | LS3-3.1 |  |
| 5 | Mon Nov 16 | [Monster Genetics, Part 1: Flip a Coin, Build a Monster](https://docs.google.com/presentation/d/1Kri9dIyUcI9-x3bondcwLxADO4mvzXYZrUQYNd7GO0I/edit) | LS3-3.1 |  |
| 6 | Tue Nov 17 | [Monster Genetics, Part 2: Predict the Baby](https://docs.google.com/presentation/d/1pvylnSWmZ_9o8MK58IWQc9LnnxtzZhTQB58gG45Krgc/edit) | LS3-2.2, LS3-3.2 | CFA LS3-2.2 |
| 7 | Wed Nov 18 | [When Copying Goes Wrong](https://docs.google.com/presentation/d/19s9J0PpjSDgS5A5qLXlImZH2nV7FYQjO3n8EOKljDH0/edit) | LS3-2.3 | CFA LS3-2.3 |
| 8 | Thu Nov 19 | [Where Did This Variation Come From?](https://docs.google.com/presentation/d/1VFPMRUcB2ByHd-Ytmnig-Sl-HxFfd1rk7tRwfYFMNBg/edit) | LS3-2.4 | CFA LS3-2.4 |
| 9 | Fri Nov 20 (2-hour early out) | [Back to the Puppies and Make-Up Work](https://docs.google.com/presentation/d/10C-DhJpXI-kyUrZlK_kTKfk9fhiZlC2qTweSIkc4Amo/edit) | LS3-2.5 |  |
| 10 | Mon Nov 30 | [Review Day: Prepare for the CSA](https://docs.google.com/presentation/d/1eSmpLJmecTzuc9kXqlkNH4ZxzBJP1sk3J_E7PWc8jlQ/edit) | LS3-2.1 to LS3-2.4 |  |
| 11 | Tue Dec 1 | [Unit 2.2 CSA](https://docs.google.com/presentation/d/1ol8Rcw0dPSvz9j8Ni4WB21q828fPH67IqoFHY7ZunW0/edit) | LS3-2.1, LS3-2.2, LS3-2.3, LS3-2.4, LS3-2.5 |  |

- Slides folder: https://drive.google.com/drive/folders/1ugbvDxgfiU_brW6tqWdNBPi08ZACn1WB
- Canvas sandbox (course 330720), unpublished: module and teacher module ids in `unit22/canvas_ids.json`.
- Keys: `HS-LS3-2_CFA_key.md`, `HS-LS3-2_CSA_key.md`; day-by-day plan: `Unit_2.2_plan.md`.

## Source files (`unit22/`)
- `content.py`: all lesson content (the single source). `cfas.py`: CFAs and CSA. `reviews.py`: Mastery Path reviews.
- `slides.py`: Google Slides request generator (`python3 slides.py deck N`). `canvas.py`: Canvas build (sandbox only, safe to rerun).
- `docs.py`: regenerates the markdown keys and plan.

## Printables and student notebook

Tables students would only copy from a slide are printed as glue-ins instead, which saves setup time. Build them with
`python3 unit22/printables.py`:

- `Unit22_Printables.pdf`: one cut-and-glue piece per table (13 pieces, days 1, 2, 4 to 10), 1 per student.
- `Unit22_Printables_Teacher_Key.pdf`: the same pieces with answers.
- `Unit22_Student_Notebook.pdf`: the left and right notebook pages for days 1 to 10, with a dashed "Glue in" box sized to each piece.

`unit22/nbslide.py` puts the same dashed boxes on each deck's notebook setup slide (`python3 nbslide.py <day> <old slide id>`), and the
content slides tell students to glue in the printable. Day 3 and the Day 11 CSA need no glue-ins.
