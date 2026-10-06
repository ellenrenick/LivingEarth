# Claude Code for Teachers: Build Assessments, Lessons, and Canvas Content

This is the code-side companion to the chat-side tutorial. It walks through what was actually done in 16 Claude Code sessions (Sept 23 – Oct 5, 2026) for 9th-grade Living Earth (Biology), Earth Science, and Honors Geology, and it gives you a **better version of each prompt** so you can get the same result on the first try.

Every "Original prompt" below is the real prompt, lightly trimmed. Every "Better prompt" fixes what made Claude guess, ask, or build the wrong thing. Replace the `[brackets]` with your own details.

---

## Part 0. How to write a good prompt (the 6 patterns that fixed most problems)

Looking across all the sessions, almost every wasted turn came from one of six gaps:

| Gap | What happened | Fix |
|---|---|---|
| **Which course?** | "the sandbox" matched two sandboxes (CP and GATE); "put it in Canvas" gave no course. | Always give the course **name and ID**: `Living Earth CP Sandbox (course 330720)`. |
| **Which quiz type?** | "Canvas quiz" produced a Classic quiz; you had to ask for New Quizzes. | Say **"New Quizzes"** every time. |
| **Which file or chat?** | "the review", "the website", "the last session", "our last creations" were guessed from context. One guess grabbed a review for the wrong standard. | Name the **file, title, or standard code**: `the HS-LS2-5 review`, not `the review`. |
| **What state?** | Items arrived published, or unpublished, or only visible to overrides, without being asked. | State **published or unpublished** and where it goes (module name, position). |
| **Which tracker / what words mean** | "the mastery tracker", "LT", "CSA", "CFA" each needed a hunt or a clarifying question. | Define your terms once at the start (see the glossary prompt in Part 2). |
| **Don't touch live** | A write to the live course was blocked, then you had to say "Do not build units in the live course!" | Say **"sandbox only"** or **"live course OK"** in the prompt. |

A prompt that works well has: **(1) the task, (2) the course and ID, (3) the format or tool, (4) the standard, (5) the numbers (how many, how many points), (6) published or not.**

> **Template**
> *Using [source: file / standard / quiz], create [what] in [course name + ID] as [format, e.g., New Quizzes]. [Numbers: counts, points, DOK, time]. Put it in [module]. Leave it [unpublished]. [Anything to leave alone.]*

---

## Part 1. One-time setup

### 1.1 Create the Canvas access token (this was the biggest time sink)
Canvas uploads failed in four separate sessions with `401 – user authorization required`. Two of the sessions never finished the upload. Do this once, correctly:

1. In Canvas: **Account → Settings → Approved Integrations → + New Access Token**. Name it (for example "Claude"), set an expiry date, and copy the token.
2. **Do not paste the token into the chat.** Two tokens were pasted into chat in the first session; anything pasted in chat should be treated as exposed. If you did this, revoke the token in Canvas and make a new one.
3. In Claude Code on the web, open the **cloud environment menu** (title bar of the session) → **Edit**. Add the token as an **API credential** for your Canvas host (for example `yourschool.instructure.com`) or as an environment variable named `CANVAS_TOKEN`. If you are asked for a credential type, choose a **Bearer token** type.
4. **Start a new session.** A token you add to the environment is not visible to a session that is already running. This is why "I saved it as CANVAS_TOKEN" still failed in that same session.
5. Test it with a prompt like the one in the next section.

If Canvas ever returns 401 again, the token expired or was revoked. Repeat steps 1–4.

**Prompt: test access**
> Check whether you can reach Canvas. List my courses and tell me the names and IDs of the sandbox and live courses. Don't change anything.

### 1.2 Connect Google Drive, Sheets, and Slides (only if you use them)
Claude could read Drive and Sheets in these sessions, but **could not edit a Google Slides planner until the Slides connector was turned on** (claude.ai → Settings → Connectors → Google Slides). It also could not upload `.pptx` or PDF files through the Drive connector, only Docs, so slide decks came as a zip you drag into Drive. Claude **cannot edit a `.pptx` stored in Drive**; convert it to Google Slides first (File → Save as Google Slides).

### 1.3 Add a "sandbox first" rule
Add a line to the repo's `CLAUDE.md` (Claude reads this at the start of every session):

> Build and test everything in the sandbox course first. Only write to the live course when I explicitly say so.

### 1.4 Know what Claude cannot do (so you ask for the workaround up front)
- **Cannot link New Quizzes questions to Outcomes through the API.** This came up in three sessions. The fix is the "Claude in Chrome" prompt in Recipe 6.
- **Cannot open real Word, or view slide images**, so it will tell you the output is untested. Skim it yourself.
- **Cannot upload large or binary files** through some connectors. Ask for a zip.

---

## Part 2. Start-of-project prompts

### Recipe A. Orient Claude to your project
*Original (Oct 1):* "what can i do in this session? Can you create lessons?"
That worked, but it cost a turn. A stronger opener gives Claude the lay of the land.

**Better prompt**
> I teach [course, grade]. Our standards are in [Google Sheet / workbook link]. We use Canvas at [host]. My sandbox course is [name + ID]; my live course is [name + ID]. Use New Quizzes. My gradebook is a 4-point scale: A = 3.5–4.0, B = 2.7–3.49, C = 1.8–2.69, D = 0.90–1.79, F = 0–0.89, so "below a B" means below 67.5%. Terms I use: **CSA** = common summative assessment, **CFA** = common formative assessment (one per learning target), **LT** = learning target. Work in the sandbox only unless I say "live." Tell me what you can and can't do with my tools before you start.

Why: the 75% vs 67.5% mistake (Unit 3 Mastery Paths) and the "mastery tracker" confusion (two sessions) both came from terms that were never defined.

---

## Part 3. Build an assessment

### Recipe 1. Summative assessment from a standard (HS-LS1-6)
*Original:* "I need an assessment for Canvas. It needs to be for 9th grade Living Earth (Biology) students. it should have 5-10 vocabulary matching question, several DOK 2 and 3 multiple choice questions, and a couple free response questions at DOK level3. Questions should be scenario based as much as possible. The priority standard is [HS-LS1-6 text]"

This was a good prompt, and Claude produced a QTI zip, a teacher key, and the generator code. Claude had to pick the counts and points itself (first 40 pts, later 36).

**Better prompt**
> Create a summative assessment for 9th grade Living Earth for standard [HS-LS1-6 + full text, including the clarification statement and assessment boundary]. Format: 8 vocabulary matching terms (DOK 1) plus 2 distractors; 10 scenario-based multiple choice (DOK 2 and 3, 2 points each); 2 free response (DOK 3, 4 points each, scored with a 4-point rubric). About 50 minutes. Give me (1) a Canvas-importable file, (2) a teacher key with answers, DOK levels, rubrics, grading notes, and a sample 4-point answer, and (3) the source files so I can edit questions later.

### Recipe 2. Add rubrics and grading notes
*Original:* "The free response questions should include grading notes in the form of a 4 point scale rubric"

**Better prompt**
> For each free-response question, add a 4-point rubric (4, 3, 2, 1, 0 with a descriptor for each), grading notes (what to look for, common errors), and an exemplar 4-point answer. Put the rubric, notes, and exemplar in the question's feedback or grading notes so I see them in SpeedGrader. Update the teacher key too.

### Recipe 3. Practice test plus review
*Original:* "I need a practice test on the same standard that can completed in about 20 minutes, and a review to do afterward to review for the summative test"

**Better prompt**
> Create a 20-minute practice test on [standard]: 6 matching, 6 multiple choice (DOK 2–3), 1 free response (DOK 3, 4-point rubric), with unlimited attempts and **all new scenarios** so it doesn't give away the summative. Then make a student review to do **after** the practice test. Map each practice question to a review section and include an answer key. Keep the review on [standard code only].

The "all new scenarios" line was Claude's own choice here; saying it yourself keeps it deliberate.

---

## Part 4. Put it in Canvas

### Recipe 4. Upload to Canvas
*Original:* "can you put this into canvas for me" → "Token [pasted]" → "https://…/courses/330720"

That took three more turns, plus network errors, before the upload worked. The reliable path is Part 1.1 first, then:

**Better prompt**
> Put the [HS-LS1-6 assessment, practice test, and review] into [sandbox course name, ID] as **New Quizzes** (the review as a Canvas Page). Leave everything unpublished. Settings: the assessment is a graded quiz with 1 attempt; the practice test is a practice quiz with a 20-minute limit and unlimited attempts. Put them in the module [Unit 1.3 – name]. Afterward, verify the counts (items and points) and send me the links.

Notes from the sessions:
- Re-running an uploader **creates duplicates**. Ask Claude to check for existing items first: "If an item with this title already exists, update or skip it."
- If an upload fails and Claude falls back to making a zip ("Can you just make the lessons downloadable"), that's fine, but ask for a `START_HERE` file with the import steps.

### Recipe 5. Convert an existing quiz or document into New Quizzes
*Original (Oct 5):* "Can you put this CFA into new quizzes in canvas course 342850 for unit 1.2. Include the answer key in the grading notes of the essay Qs" (with the .docx and the answer-sheet PDF attached)

This worked well. The only snags: vocabulary questions had to be short answer, and there was a 422 error before it succeeded.

**Better prompt**
> Convert the attached CFA (Word) and answer sheet (PDF) into a New Quiz in [course + ID], Unit [1.2] module, unpublished. Auto-grade the multiple choice and put the reasoning from the answer sheet in each question's feedback. For the essays, put the answer key and the 4-point rubric in the grading notes. If any question type can't be auto-graded, tell me which ones before you build.

---

## Part 5. Outcomes and the mastery tracker

### Recipe 6. Create outcomes from learning targets
*Original (Oct 1):* "Make each learning target an outcome, and link each question to its learning target outcome. Group the outcomes under the priority standard."

Claude created the outcome group and outcomes but **could not link questions** (no API for that). It took four more prompts to discover this.

*Original (Oct 5, whole course):* "Can you put all of the learning targets for the whole course into the Mastery tracker on the live course under the standard to which it belongs using Outcomes"

"The Mastery tracker" was not defined, so Claude searched the course, the sandboxes, and Drive before guessing. The result was correct (32 standard groups, 131 outcomes), but it cost time.

**Better prompt (create outcomes)**
> Read the learning targets from [Google Sheet name or link, tab name]. In [course name + ID], create one Outcome Group per standard (named "[HS-ESS1-3: short title]") and one Outcome per learning target inside its standard's group. Use a 0–4 scale, mastery at 3, and **highest score** as the calculation method. Include only the priority standards [list codes], or all standards [yes/no]. Run it in the sandbox first, then tell me the counts so I can approve the live run. Don't create units or modules.

**Better prompt (link questions to outcomes)**
> I know the API can't link New Quizzes questions to outcomes. For each CSA, CFA, and practice test in [course + ID], create a table of **question number → learning target**. Then write me a paste-ready prompt for Claude in Chrome that opens each quiz in the editor and links each question to its outcome, changes nothing else, and stops and asks me if a regrade dialog appears.

Claude in Chrome runs on your own computer (it needs the desktop app or a local session; the cloud session cannot reach your browser), so run that prompt there.

### Recipe 7. Highest-score grading on outcomes
*Original:* "Keep highest score"

Short prompts work when the context is clear. If you're starting a new session, spell it out: "Set the calculation method on all outcomes in [group] to highest score."

---

## Part 6. Intervention, enrichment, and Mastery Paths

### Recipe 8. Practice test → intervention or enrichment
*Original (Oct 1):* "…a practice test that is similar, and an intervention/review piece for students who score below a 3 on the practice test, and an extension/enrichment piece for students who scored a 3 or 4 on the practice test. I want to put them as assignments in canvas that can be linked to the practice test through mastery paths"

Then: "My gradebook is a 4 point scale…" (the teacher had to correct Claude's 75% cutoff to 67.5%).

**Better prompt**
> For [Unit/standard], create: (1) a practice test (New Quiz) matching the CSA's question counts per learning target and DOK; (2) an **intervention** assignment (review) for students below a B; (3) an **enrichment/extension** assignment for a B or better. Our scale is 4-point and a B starts at 2.7, so the Mastery Path cutoff is 67.5%. Create the assignments as "only visible to Mastery Paths" and set up the Mastery Path rule on the practice test. **Do not assign to individual students.** Complete/incomplete, 10 points each. Unpublished.

What went wrong when this wasn't said (Oct 5, "Energy in Carbon"): Claude assigned the review directly to 25 named students by score, which wasn't wanted (you use Mastery Paths), and then had to undo it. Then "the intervention is the review" pulled in the HS-LS1-6 review, not the HS-LS2-5 one. Ask for **"the [standard] review"** and name the standard.

### Recipe 9. CFA per learning target with targeted intervention
*Original:* "New plan. I need a CFA per learning target linked to the outcomes. Each CFA needs its own intervention piece (this can be a review website) for targeted intervention. Anyone who scored below a B on the CFA needs to be directed to the intervention for that target via mastery paths"

"New plan" was unclear about whether the practice test setup from earlier stays. You had to add "keep this practice test set up we already did as well."

**Better prompt**
> Keep the existing practice test and its Mastery Path. **In addition**, create one CFA New Quiz per learning target for [standard] (5 questions each, auto-graded, tagged "Q# · LT-id" in the question title), and one targeted intervention page for each learning target. Create a Mastery Path rule on each CFA: below 67.5% opens that target's intervention. Unpublished. Give me an answer key and a table of question → LT.

---

## Part 7. Lessons and unit planning

### Recipe 10. Build a unit of lessons
*Original (Sept 23):* "Can you make a unit of lessons for the HS-LS1-6 unit from the previous session. It should be 7 45-minute classes (not including the practice assessment, review, or assessment day)"

"The previous session" was found by Claude reading the repo. That works only because the files were saved there. Name the folder or standard.

**Better prompt**
> Using the assessment files for [HS-LS1-6] in `assessments/HS-LS1-6/`, make a 7-lesson unit (45 minutes each, not counting the practice test, review, or CSA day). For each lesson, give me a teacher plan (objective, timing, materials, answer key), a student handout, and slides. Start with a phenomenon lesson.

*Original (Oct 1, Unit 3):* "Lets make lessons for the unit now. Slideshows/webpages, student facing with answer sheets or a notebook setup. Teacher pages for me as well."

Specify the **count and days** ("10 lessons, days 40–49") and where the practice test and CSA land.

### Recipe 11. Restructure to a fixed length
*Original:* "We already made lessons for this unit, lets revamp those a bit. I would like a phenomena/vocab/sketchnotes lesson at the beginning (can be two separate things), the CFAs applied where they fit best, and the practice test, review day, and CSA day added to them as well. The entire unit from launch to CSA should be 10 days"

**Better prompt**
> Rework the HS-LS1-6 lessons into a 10-day unit from launch to CSA: Day 1 phenomenon, Day 2 vocabulary with sketchnotes, Days 3–8 the existing lessons, each ending with that day's CFA, Day 9 practice test and review, Day 10 CSA. Update the Canvas module with "Day N" headers and tell me every tradeoff you made.

### Recipe 12. Add CFA slides to converted decks
*Original:* "I converted lessons 5-7 to Google Slides, add the CFA slides"

Good. It worked because the earlier session had set up the pattern. Convert any `.pptx` to Google Slides first, and say the deck names.

### Recipe 13. Put lessons into the planner (Google Slides)
*Original:* "Add the lessons to this planner starting October 8 [link]" and, for Unit 3, "…link each slideshow and teacher doc to the lesson title in the planner [link]"

**Better prompt**
> Add the 10 lessons to this planner starting Oct 8 [link]. Put each lesson in its day's cell: the lesson title linked to its slideshow, plus a "Teacher plan" link. Keep my existing text and style. Skip [Oct 16] (I'm out), and tell me which days look like conflicts before you write.

### Recipe 14. Handle a substitute day
*Original:* "October 14th is a sub day, please shift"

"Shift" didn't say what to move, so Claude moved Vocabulary/SketchNotes to cover the sub day, which broke your earlier request that vocabulary come right after the phenomenon.

**Better prompt**
> Oct 14 and Oct 16 are sub days. Reorder the unit so those days have sub-friendly lessons (no lab, no teacher-led demo). Keep [vocabulary right after the phenomenon]. Don't change the CSA date. Add a sub plan to those days' teacher pages and mark "SUB DAY" in the planner. Tell me what you moved.

---

## Part 8. Student-facing websites and assignments

### Recipe 15. Make a better interactive website plus a matching quiz
*Original:* "In my Geology class 342801 there is a lesson called 'LAB Volcanic Materials Identification' that has students use the website linked to identify volcanic materials. Can you make a better website for this and matching 'quiz' in new quizzes for them to fill in Canvas?"

This produced 15 specimens, a hand-lens view, and a 15-item New Quiz. It worked, but **scope was entirely Claude's choice** ("better" and "matching").

**Better prompt**
> Build a replacement for the website linked in [lesson name, course + ID]: [N specimens], students identify [what]. Include [a check-your-answers button / a reference guide / a lab sheet]. Make a matching New Quiz in [course + module] with [dropdown blanks per specimen, 1 point each], unpublished. Host the site so students can open it without signing in.

Follow-ups that worked as short prompts:
- "can you add to the website a 'check your answers' button that tells them if they are correct like the old version." Add what "correct" feedback should look like.
- "Can you give more information for how they know if it pyroclastic or lava flow origin in the guide and specimen card? That is unclear." Name **which cards** are unclear.
- "Remove the float test row from the card." Clear and specific, which is why it worked.

**A Canvas detail worth knowing:** Claude couldn't edit a New Quizzes item in place; each change meant creating a new item and deleting the old one. If you only need small text edits, tell it to do them in one pass.

### Recipe 16. Test question from a real sample
*Original:* "Make me a test question with a real rock sample of pumice (I will provide it) that i can add to a test bank in Canvas for their quiz. Provide a specimen card for pumice and the same quiz question format as this one, do not include the ID guide as they are demonstrating their ability to identify it on their own."

Claude assumed a sample size (under 6.4 cm). **Include the measurement**, the density or float result if you want it used, and the answer key.

### Recipe 17. Create an assignment plus link the lesson website
*Original:* "Create an assignment for the Blow Your Top: Volcano Types, Magma and Mayhem in canvas course 342801" → "Add the link to the website please" → "please make the website and assignment match with the 5 types" → "remove the demo/warm up too" → "where is the student doc to download"

Five prompts were needed because the deliverables (the Canvas assignment, the website, and the student guide) drifted apart.

**Better prompt**
> Create an assignment "[Blow Your Top: Volcano Types]" in [course + ID], in the [Unit 1.4] module after the lab, unpublished, [points]. It must match the lesson website "[title]" and the student guide "[title]" exactly. The five types are: shield, cinder cone, composite, lava dome, and caldera. There is **no warm-up or demo**. Add links to the website and the student guide. When I change one of the three, update the other two.

Reminder: a private website link won't open for students. Set sharing to "anyone with the link" before you publish.

---

## Part 9. Copy between courses

### Recipe 18. Sandbox ↔ live
*Original:* "Take the intervention and enrichment, Practice test, and CSA assignments for unit 1.2 in the live course and put them in the sandbox"

Claude had to ask which sandbox (CP or GATE) and whether to replace the existing CSA. It then deleted the old CSA, **and the copies arrived published**.

**Better prompt**
> Copy these four items from the live course [name + ID] to the **CP sandbox [name + ID]**: Intervention, Extension, Practice Test, CSA (Unit 1.2). Replace the sandbox's existing Unit 1.2 CSA. Keep them **unpublished**, and keep the module order the same as live: [Practice Test, Intervention, Extension, CSA]. Verify that the New Quiz questions copied and tell me what you checked.

---

## Part 10. Downloads and documents

### Recipe 19. Word docs and downloads
*Original:* "make the teacher plans Word docs too"; "make these into slideshows and docs for me to download/put in google drive as well with links to the websites"; "add everything to this google drive folder when it is ready [link]"

Claude chose which files to convert. It also could not open the Word files, and Drive could not take `.pptx`/PDF.

**Better prompt**
> Make Word (.docx) versions of the teacher plans **and** the student answer sheets for [unit]. Put the Docs in this Drive folder [link] as native Google Docs with subfolders per lesson, and give me a zip of anything the connector can't upload (slide decks, PDFs). Tell me which files you couldn't test in Word.

---

## Part 11. Checklist before you hit enter

- [ ] Course **name and ID** (sandbox or live)
- [ ] **New Quizzes** (not Classic)
- [ ] **Standard code** (HS-LS2-5), not "the review" or "the last session"
- [ ] **Counts and points** (how many questions, DOK, points per item)
- [ ] **Published or unpublished**, and the **module** and position
- [ ] Mastery Path cutoff in **%** (67.5% = B on a 4-point scale) and "no per-student assignments"
- [ ] Your **terms** are defined (CSA, CFA, LT, tracker)
- [ ] Token is stored in the **environment**, not pasted in chat; start a **new session** after changing it
- [ ] If you need outcome links on New Quizzes questions, ask for the **Claude in Chrome prompt**

## Appendix. What was built, by session

| Date | Session | Result |
|---|---|---|
| Sep 23 | Canvas Biology assessment (HS-LS1-6) | Summative QTI + key, 4-point rubrics, 20-min practice test, review page, Canvas REST uploader |
| Sep 23–30 | HS-LS1-6 lesson unit | 7 lessons (plans + handouts), lessons zip, Word plans; Canvas upload blocked by 401 |
| Sep 23, 30 | Upload retries / Canvas access check | Blocked by expired token; fixed by replacing the token in the environment |
| Oct 1 | Earth Science Unit 3 CSA | CSA, outcomes, practice test with Mastery Paths, 5 CFAs + reviews, 10 lessons, Drive upload, planner |
| Oct 1 | Unit 1.3 Sugar to Structures | Outcomes, CFAs, practice test, new CSA, Mastery Paths, 10-day restructure, planner, sub-day shift |
| Oct 2 | Earth science quiz conversion | Unit 2 quizzes, review/enrichment assignments, module, outcomes |
| Oct 2 | Volcanic materials website | ID lab site, New Quiz, pumice question, Ch 4 quiz |
| Oct 5 | Learning-target tracker | 65 outcomes in 12 standard groups (live and sandbox) |
| Oct 5 | CFA to Canvas (Unit 1.2) | CFA New Quiz; 131 outcomes in 32 groups for the whole course |
| Oct 5 | Volcano Types assignment | Assignment, website, and student guide aligned |
| Oct 5 | Energy in Carbon intervention/enrichment | Review and extension on HS-LS2-5 |
| Oct 5 | Unit 1.2 to sandbox | Four assignments copied to the CP sandbox |
