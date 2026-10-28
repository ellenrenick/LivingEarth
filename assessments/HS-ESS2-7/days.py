"""Unit 3.1 Changing Earth, Changing Life (HS-ESS2-7): daily lesson content (student and teacher pages)."""

BLUE = '<div style="background:#eef5fb;border-left:5px solid #2b6cb0;padding:10px 14px;margin:12px 0">'
ORANGE = '<div style="background:#fff7e6;border-left:5px solid #c05621;padding:10px 14px;margin:12px 0">'
TBL = '<table border="1" cellpadding="6" style="border-collapse:collapse"><tbody>'
UNIT_LABEL = "Unit 3.1: Changing Earth, Changing Life (HS-ESS2-7)"


def table(rows, head=True):
    out = TBL
    for i, r in enumerate(rows):
        tag = "th" if head and i == 0 else "td"
        out += "<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in r) + "</tr>"
    return out + "</tbody></table>"


def ol(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"
def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


TARGETS = {
    "7.1": "I can name examples of how Earth has changed and how life has changed.",
    "7.2": "I can describe one way Earth changed life and one way life changed Earth.",
    "7.3": "I can explain how events in Earth's history changed life, and how life in turn changed Earth.",
    "7.4": "I can write an argument, with evidence, that Earth and life changed each other.",
    "7.5": "I can combine several kinds of evidence into one strong argument about Earth and life.",
    "7.6": "I can argue from evidence that Earth's systems and life have changed together over time.",
}

# Notebook helper text reused on several pages
LOG = "<strong>Unit CER evidence log:</strong> a two-page table in the back of your notebook with the columns Evidence | Kind (rock, fossil, data, model) | What it shows."

EVENTS = [
    ["A", "Earth forms", "about 4.6 billion years ago", "Earth", "1"],
    ["B", "Oceans of liquid water form", "about 4 billion years ago", "Earth", "4"],
    ["C", "First simple cells (microbes)", "about 3.5 billion years ago", "Life", "6"],
    ["D", "Cells that use photosynthesis spread", "at least 2.7 billion years ago", "Life", "10"],
    ["E", "Oxygen builds up in the air and oceans", "starting about 2.4 billion years ago", "Both", "11"],
    ["F", "First animals", "about 600 million years ago", "Life", "20"],
    ["G", "Land plants spread", "about 470 million years ago", "Life", "21"],
    ["H", "Continents join into the supercontinent Pangaea", "about 300 million years ago", "Earth", "22"],
    ["I", "Largest mass extinction (end of the Permian)", "252 million years ago", "Both", "22"],
    ["J", "Asteroid strike; non-bird dinosaurs go extinct", "66 million years ago", "Both", "23"],
    ["K", "Ice ages come and go", "many times; the last ended about 12,000 years ago", "Earth", "23"],
    ["L", "Humans appear", "about 300,000 years ago", "Life", "23"],
]

OXYGEN = [["Time (billions of years ago)", "Oxygen in the air (% of air, simplified)"],
          ["4.0", "0"], ["3.0", "0 (a trace)"], ["2.5", "0 (a trace)"], ["2.0", "2"], ["1.0", "3"], ["0.5", "15"], ["0.3", "30"], ["0 (today)", "21"]]
EXTINCT = [["Mass extinction", "Time (million years ago)", "Species lost (approximate %)"],
           ["End-Ordovician", "445", "85"], ["Late Devonian", "375", "75"], ["End-Permian", "252", "96"], ["End-Triassic", "201", "80"], ["End-Cretaceous", "66", "76"]]

TIMELINE_ROWS = [
    ["1", "3.5 billion years ago", "Oceans and shallow seas exist", "First cells build layered mounds (stromatolites)", ""],
    ["2", "2.7 to 2.4 billion years ago", "Iron dissolved in the oceans rusts; the air starts to gain oxygen", "Photosynthetic cells spread", ""],
    ["3", "2.4 to 1.8 billion years ago", "Oxygen rises in oceans and air; rusty iron layers settle on the seafloor", "New kinds of cells that use oxygen evolve", ""],
    ["4", "600 million years ago", "More oxygen in the air and oceans; an ozone layer forms", "First animals appear", ""],
    ["5", "470 million years ago", "The ozone layer blocks most harmful sunlight on land", "Plants spread onto land; soils form", ""],
    ["6", "350 to 300 million years ago", "Forests bury carbon; oxygen is high and carbon dioxide falls", "Giant insects and the first large land animals", ""],
    ["7", "252 million years ago", "Huge volcanic eruptions warm the climate; ocean oxygen drops", "About 96% of ocean species go extinct", ""],
    ["8", "66 million years ago", "An asteroid strike darkens the sky and cools the climate", "Non-bird dinosaurs go extinct; mammals diversify", ""],
]


def student(n, title, targets, driving, focus, reading, nb, parts, wrap, absent_extra=""):
    t = "".join(f"<li><strong>ESS2-{k}</strong> {TARGETS[k]}</li>" for k in targets)
    h = (f"{BLUE}<p><strong>Day {n}</strong> · {UNIT_LABEL}</p><p><strong>Driving question:</strong> {driving}</p>"
         f"<p><strong>Focus question:</strong> {focus}</p><p><strong>Learning target:</strong></p><ul>{t}</ul></div>")
    h += f"<h2>Notebook setup</h2>{BLUE}<p><strong>Before the lesson:</strong></p>{ol(nb)}<p><em>Your notebook is your answer sheet for this lesson. Keep it neat; your teacher will check it.</em></p></div>"
    for i, (head, body) in enumerate(parts, 1):
        h += f"<hr><h2>Part {i}: {head}</h2>{body}"
    h += f"<hr><h2>Part {len(parts)+1}: Wrap-up</h2>{wrap}"
    h += f"<hr><p><strong>If you were absent:</strong> complete the notebook pages above using this page{absent_extra}. Your teacher will tell you which materials to borrow.</p>"
    return h


def teacher(n, student_url, targets, glance, materials, agenda, notes, key, supports):
    h = (f"{ORANGE}<p><strong>Teacher page · keep unpublished.</strong> Students never see this page.</p>"
         f"<p><strong>Day {n}</strong> · Targets: {targets} · <a href=\"{student_url}\">Student page</a></p></div>")
    h += f"<h2>At a glance</h2><p>{glance}</p><h2>Materials</h2>{ul(materials)}<h2>Agenda (45 minutes)</h2>{table([['Min','What happens']] + agenda)}"
    h += f"<h2>Teaching notes</h2>{ul(notes)}<h2>Answer key</h2>{ul(key)}<h2>Supports</h2><p>{supports}</p>"
    return h


DAYS = []

# ---------------------------------------------------------------- Day 1
DAYS.append(dict(
    n=1, title="Rusty Stripes", short="Launch: Rusty Stripes", targets=["7.1"], cfa="7.1",
    s=dict(
        driving="Some of the oldest rocks on Earth have red and gray stripes of rust. How could tiny living things have changed the whole planet, and how did the planet change life in return?",
        focus="What are examples of how Earth has changed and how life has changed?",
        reading="Textbook: Lesson 8.3 Earth and Life Evolve Together (pp. 226–235)",
        nb=["Title: <strong>D1 Rusty Stripes</strong>. Add it to your table of contents.",
            "Leave room for a short pre-check, a two-column chart, and a timeline strip across the width of a page.",
            "Start your " + LOG],
        parts=[
            ("Warm-up: a rock with stripes (5 min)",
             "<p>Your teacher shows a photo of a <strong>banded iron formation</strong>: a rock about 2.4 billion years old with red bands of rust and gray bands of rock.</p>" + ol([
                 "Iron rusts when it meets oxygen. What does the rust in this rock tell you about the air or water that touched it long ago?",
                 "Write two questions you have about this rock."])),
            ("Pre-check (5 min, not graded)",
             "<p>Answer in your notebook. It is OK to guess. We will come back to these at the end of the unit.</p>" + ol([
                 "About how old is Earth?",
                 "Name one way Earth has changed over its history.",
                 "Name one way life has changed over Earth's history.",
                 "Do you think living things ever changed the air or the rocks? Explain."])),
            ("Card sort: how Earth and life changed (15 min)",
             "<p><strong>Sort and place 12 events · 15 min · with a partner</strong></p><p><strong>Materials:</strong> event cards (or the table below), a ruler, a pencil</p>" + ol([
                 "Draw a strip of <strong>23 boxes</strong> across your page. Each box is <strong>200 million years</strong>. Label the left end <strong>4.6 billion years ago</strong> and the right end <strong>today</strong>.",
                 "For each event, decide: did <strong>Earth</strong> change, did <strong>life</strong> change, or <strong>both</strong>? Write E, L, or B.",
                 "Write each event's letter in the box where it belongs on the timeline."]) +
             table([["Card", "Event", "When"]] + [[e[0], e[1], e[2]] for e in EVENTS]) + ol([
                 "Which cards did you mark <strong>both</strong>? Why could both be true?",
                 "Where on your timeline do most of the cards crowd together? What does that say about how fast things changed late in Earth's history?"])),
            ("Preview the unit (5 min)",
             "<p>Read the six learning targets for this unit. Put a star next to the one you think will be hardest.</p>" + ul([f"<strong>ESS2-{k}</strong> {v}" for k, v in TARGETS.items()])),
            ("Exit ticket: CFA ESS2-7.1 (6 min)",
             "<p>Take this CFA on Canvas now (5 questions):</p><ul><li><strong>Unit 3.1 CFA ESS2-7.1: Examples of Earth and life changing</strong></li></ul><p>If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
        ],
        wrap="<p>Take a photo of your D1 notebook pages and submit it on Canvas: <strong>Lesson 1: Rusty Stripes</strong>.</p><p>Tomorrow: you will find out whether the changes go in one direction or both. Look at your two-column chart and think of one event that changed both Earth and life.</p>"),
    t=dict(
        glance="Launch day. Students observe a banded iron formation, take a short ungraded pre-check, sort 12 events into Earth changes, life changes, or both, and place them on a 23-box timeline. The CFA for ESS2-7.1 is the exit ticket.",
        materials=["Photo of a banded iron formation (for example, from the USGS or a museum collection) to project", "Event cards (the 12 rows of the table, printed and cut apart)", "Rulers and pencils", "Chromebooks for the CFA"],
        agenda=[["0–5", "Warm-up: banded iron formation"], ["5–10", "Pre-check (not graded)"], ["10–25", "Card sort and timeline strip"], ["25–35", "Preview the six targets"], ["35–45", "Exit ticket: CFA ESS2-7.1 and wrap-up"]],
        notes=["The pre-check is for you. Do not grade it. Keep it to compare with the Day 9 review and the CSA.",
               "Ages are rounded for 9th grade. Scientists' estimates vary a little by source.",
               "Do not explain how the rock formed yet. The question stays open until Day 3.",
               "Reading support: read each direction aloud. Pairs may sort orally first and then write."],
        key=["Rust needs oxygen. The rock suggests oxygen was in the water or air that touched iron.",
             "Earth changed: A (Earth forms), B (oceans), H (Pangaea), K (ice ages). Life changed: C, D, F, G, L. Both: E (life added oxygen to the air, an Earth change), I (volcanic eruptions and the extinction), J (asteroid and the extinction).",
             "Timeline boxes (each = 200 million years, box 1 is the oldest): A 1, B 4, C 6, D 10, E 11, F 20, G 21, H 22, I 22, J 23, K 23, L 23.",
             "Most cards crowd in the last few boxes. Large, fast changes to life happened late in Earth's history."],
        supports="Give a partly filled timeline with the box numbers marked. Let students color-code E, L, and B. Pair a student who needs reading support with a strong reader.")))

# ---------------------------------------------------------------- Day 2
DAYS.append(dict(
    n=2, title="A Two-Way Street", short="A Two-Way Street", targets=["7.2"], cfa="7.2",
    s=dict(
        driving="If living things changed the air, did the changed air change living things in return? Does change go in only one direction?",
        focus="How did Earth change life, and how did life change Earth?",
        reading="Textbook: Lesson 8.2 Life's Early History (pp. 219–225)",
        nb=["Title: <strong>D2 A Two-Way Street</strong>. Add it to your table of contents.",
            "Leave room for a sorting chart (8 rows) and two small diagrams.",
            "Keep your " + LOG],
        parts=[
            ("Warm-up (4 min)",
             ol(["An ice sheet creeps across a region for thousands of years. What happens to the plants and animals that live there?",
                 "A lichen (a tiny living thing) grows on bare rock for many years. What might happen to the rock?"])),
            ("Cause-and-effect cards (15 min)",
             "<p><strong>Which way did the change go? · 15 min · with a partner</strong></p><p>For each card, write <strong>E→L</strong> if <strong>Earth changed life</strong>, or <strong>L→E</strong> if <strong>life changed Earth</strong>. Then write what changed.</p>" +
             table([["Card", "What happened"],
                    ["1", "Cells that use photosynthesis release oxygen into the oceans and air."],
                    ["2", "Volcanoes throw ash into the sky. The ash blocks sunlight for years, and many plants die."],
                    ["3", "Lichens and plant roots break rock into tiny pieces that become soil."],
                    ["4", "Sea level drops and a shallow sea dries up. Its animals lose their habitat."],
                    ["5", "Corals build reefs that slow waves and protect the shore."],
                    ["6", "An ice age spreads cold climate. Some animals evolve thick fur."],
                    ["7", "Forests take in carbon dioxide and store carbon in wood, and later in coal."],
                    ["8", "An asteroid strikes. Dust darkens the sky, and many species go extinct."]]) +
             ol(["How many cards are E→L? How many are L→E?", "Finish the sentence: Change between Earth and life goes in ______ directions."])),
            ("Draw your own pair (10 min)",
             "<p>Pick <strong>one E→L card</strong> and <strong>one L→E card</strong>. For each, draw two boxes joined by an arrow and label them (for example: <em>Ash cloud</em> → <em>Plants die</em>). Under each diagram, write one sentence that starts with “First, … so …”.</p>"),
            ("Find it in the reading (6 min)",
             "<p>Skim <strong>Lesson 8.2, Life's Early History (pp. 219–225)</strong>. Find one sentence that shows <strong>life changing Earth</strong>. Copy it and write the page number. Add one row to your evidence log.</p>"),
            ("Exit ticket: CFA ESS2-7.2 (6 min)",
             "<p>Take this CFA on Canvas now (5 questions):</p><ul><li><strong>Unit 3.1 CFA ESS2-7.2: Earth changes life, life changes Earth</strong></li></ul><p>If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
        ],
        wrap="<p>Tomorrow you will follow one famous chain of events: how oxygen got into the air. Bring your two diagrams.</p>"),
    t=dict(
        glance="Students decide whether each of 8 changes ran from Earth to life or from life to Earth, then draw one pair of their own and find supporting text in the reading. The CFA for ESS2-7.2 is the exit ticket.",
        materials=["Cards 1 to 8 (printed or projected)", "Textbook, Lesson 8.2 (pp. 219–225)", "Chromebooks for the CFA"],
        agenda=[["0–4", "Warm-up"], ["4–19", "Cause-and-effect card sort"], ["19–29", "Draw your own pair"], ["29–35", "Find it in the reading"], ["35–45", "Exit ticket: CFA ESS2-7.2 and wrap-up"]],
        notes=["The target is one example each way. Do not push the feedback idea until Day 3.",
               "Cards 1, 3, 5, 7 are life changing Earth. Cards 2, 4, 6, 8 are Earth changing life. That makes 4 and 4.",
               "Some students will see that card 1 is also an Earth change. Praise that and tell them to hold on to it for tomorrow."],
        key=["Warm-up: plants and animals that cannot move or adapt die or move away; lichens break rock down and start soil.",
             "Card sort: 1 L→E, 2 E→L, 3 L→E, 4 E→L, 5 L→E, 6 E→L, 7 L→E, 8 E→L. Four of each. Change goes in both directions.",
             "Reading: accept any sentence from pp. 219–225 about early life changing the air, oceans, or rock."],
        supports="Give a sentence frame: “___ changed because ___.” Allow students to color-code the arrows. Provide the card sort with the two columns already drawn.")))

# ---------------------------------------------------------------- Day 3
DAYS.append(dict(
    n=3, title="The Oxygen Story", short="The Oxygen Story", targets=["7.3"], cfa=None,
    s=dict(
        driving="Early Earth had almost no oxygen in the air. Where did the oxygen come from, and what did it do to Earth and to life?",
        focus="How can one event in Earth's history change life, and how can life change Earth in return?",
        reading="Textbook: Analyzing Data, Extinction Through Time (p. 231)",
        nb=["Title: <strong>D3 The Oxygen Story</strong>. Add it to your table of contents.",
            "Leave room for a data table, a line graph, and a chain of five boxes.",
            "Keep your " + LOG],
        parts=[
            ("Warm-up (4 min)",
             "<p>Think back to the striped rock from Day 1. Rust needs oxygen. What do you predict about oxygen in the air and ocean when the rust stripes formed?</p>"),
            ("Graph the oxygen story (12 min)",
             "<p><strong>Line graph · 12 min · with your group</strong></p><p><strong>Materials:</strong> graph paper, a ruler, a pencil</p>" + ol([
                 "Put <strong>time</strong> on the x-axis. Start at 4.0 billion years ago on the left and end at 0 (today) on the right. Put <strong>oxygen (% of air)</strong> on the y-axis from 0 to 30.",
                 "Plot the points from the table and connect them. (The values are simplified. Scientists' estimates vary.)"]) + table(OXYGEN) + ol([
                 "About when does oxygen first rise above a trace? Label that spot <strong>Great Oxidation Event</strong>.",
                 "What process made this oxygen? Which living things did it first (cyanobacteria)?",
                 "When is oxygen higher than it is today? What do you think happened to it afterward?"])),
            ("The rust record (6 min)",
             "<p>Iron dissolved in ancient ocean water. When oxygen from photosynthesis reached it, the iron <strong>rusted</strong> and sank to the seafloor in layers. These layers are the <strong>banded iron formations</strong>.</p>" + ol([
                 "Which came first: oxygen from living things, or the rust layers? Explain.",
                 "Is this an example of life changing Earth, or Earth changing life? Why?"])),
            ("Mass extinctions: reading the data (8 min)",
             "<p>Open the textbook to <strong>Analyzing Data, Extinction Through Time (p. 231)</strong>. Then use the table.</p>" + table(EXTINCT) + ol([
                 "Which extinction killed the greatest percent of species?",
                 "Many of these were caused by Earth events, such as volcanoes or an asteroid. Explain how an Earth event changes life.",
                 "Predict: what happens to the living things that survive an extinction?"])),
            ("Build a chain (8 min)",
             "<p>Fill in the empty boxes with what happened next. Mark each arrow <strong>E→L</strong> or <strong>L→E</strong>.</p><p>Cells use <strong>photosynthesis</strong> → <strong>______</strong> → iron in the ocean <strong>______</strong> → oxygen builds up in the <strong>air</strong> → an <strong>ozone layer</strong> forms and <strong>______</strong></p>"),
        ],
        wrap="<p>Write one sentence: “Because ______ happened, ______ changed, which led to ______.” Tomorrow you will check three other cases to see if they follow the same pattern. There is no CFA today; the CFA for this target is tomorrow.</p>"),
    t=dict(
        glance="Students graph an approximate history of oxygen in the air, connect it to banded iron, read the extinction data, and build a first cause-and-effect chain. The ESS2-7.3 CFA is tomorrow.",
        materials=["Graph paper and rulers", "Photo of a banded iron formation (from Day 1)", "Textbook p. 231 (Analyzing Data, Extinction Through Time)", "Optional: iron nail in water to show rust"],
        agenda=[["0–4", "Warm-up prediction"], ["4–16", "Graph the oxygen story"], ["16–22", "The rust record"], ["22–30", "Mass extinction data"], ["30–38", "Build a chain"], ["38–45", "Wrap-up sentence"]],
        notes=["Oxygen values are simplified classroom values (about 0 before 2.4 billion years ago, about 2% by 2.0, 15% by 0.5, a peak near 30% about 300 million years ago, 21% today). Say so out loud.",
               "The target is the explanation of events changing life and life changing Earth. Push for the word because.",
               "Save the deeper feedback talk (plants, soil, carbon dioxide) for Day 4."],
        key=["Prediction: little or no oxygen at first; the rust shows some oxygen later.",
             "Oxygen first rises above a trace about 2.4 billion years ago (the Great Oxidation Event). It was made by photosynthetic cells (cyanobacteria). It peaks near 30% about 300 million years ago, then falls to 21%.",
             "Rust record: oxygen from living things came first and then rusted the iron. Life changed Earth (L→E).",
             "Extinctions: End-Permian (about 96%). An Earth event (volcanoes or an asteroid) changes climate or ocean conditions, so many living things die. Survivors spread into empty habitats and diversify.",
             "Chain: photosynthesis → oxygen released into water and air (L→E) → iron in the ocean rusts → oxygen builds up in the air → an ozone layer forms and shields life so organisms can live on land (E→L)."],
        supports="Provide a pre-drawn axis and a table with the plotted values already marked. Give the chain with the first two boxes filled in.")))

# ---------------------------------------------------------------- Day 4
DAYS.append(dict(
    n=4, title="Three Case Files", short="Three Case Files", targets=["7.3"], cfa="7.3",
    s=dict(
        driving="Does the oxygen story show a pattern? Do other big events work the same way?",
        focus="How do events in Earth's history change life, and how does life change Earth in return?",
        reading="Textbook: Lesson 8.3 Earth and Life Evolve Together (pp. 226–235), second read",
        nb=["Title: <strong>D4 Three Case Files</strong>. Add it to your table of contents.",
            "Leave room for a 3-row table with four columns.",
            "Keep your " + LOG],
        parts=[
            ("Warm-up (3 min)",
             "<p>Look at your chain from yesterday. Which arrow shows <strong>life changing Earth</strong>? Which arrow shows <strong>Earth changing life</strong>? Tell a partner.</p>"),
            ("Station rotation: three case files (27 min, 9 min each)",
             "<p>Read each case. In your table, write <strong>Event</strong>, <strong>Effect on life</strong>, <strong>Effect back on Earth</strong>, and the <strong>direction</strong> of each arrow.</p>" +
             "<h3>Case A: Oxygen, ozone, and land</h3><p>Oxygen from photosynthesis rose in the air. Some oxygen became <strong>ozone</strong>, a layer high in the air that blocks much of the Sun's harmful ultraviolet light. Before the ozone layer, life lived mostly in water. After it, plants and animals could live on land.</p>" +
             "<h3>Case B: Soil and the first forests</h3><p>Microbes, lichens, and then plants spread on bare rock about 470 million years ago. They broke rock down and added dead matter, so <strong>soil</strong> formed. Deep soil let larger plants grow. Roots broke rock further and plants took in carbon dioxide. As forests spread, carbon was buried as coal and the air's carbon dioxide fell, which helped cool the climate.</p>" +
             "<h3>Case C: The end-Permian mass extinction</h3><p>About 252 million years ago, huge volcanic eruptions released carbon dioxide and other gases. The climate warmed and the oceans lost oxygen. About 96% of ocean species died. Over the next several million years, survivors spread into empty habitats and new groups, including early dinosaurs, evolved.</p>" +
             table([["Case", "Event", "Effect on life", "Effect back on Earth"], ["A", "", "", ""], ["B", "", "", ""], ["C", "", "", ""]]) +
             "<p>After you finish the three rows, answer: What do all three cases have in common?</p>"),
            ("Quick write (6 min)",
             "<p>Pick one case. Write 3 sentences that include the word <strong>because</strong> and tell how Earth changed life <em>and</em> how life changed Earth.</p>"),
            ("Exit ticket: CFA ESS2-7.3 (6 min)",
             "<p>Take this CFA on Canvas now (5 questions):</p><ul><li><strong>Unit 3.1 CFA ESS2-7.3: How events changed life and life changed Earth</strong></li></ul><p>If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
        ],
        wrap="<p>Tomorrow you write a full argument. Look at your three cases and circle the strongest fact you could use as evidence.</p>"),
    t=dict(
        glance="Three stations (oxygen and ozone, soil and forests, the end-Permian extinction) apply Day 3's pattern. Students complete a 3-row table and a quick write. The CFA for ESS2-7.3 is the exit ticket.",
        materials=["Three case cards, one per station (print the text)", "Chromebooks for the CFA", "Timer for 9-minute rotations"],
        agenda=[["0–3", "Warm-up"], ["3–30", "Three stations (9 min each)"], ["30–36", "Quick write"], ["36–45", "Exit ticket: CFA ESS2-7.3 and wrap-up"]],
        notes=["If time is short, run two stations and have groups share the third.",
               "Case A: oxygen → ozone layer. Life changed Earth (oxygen), and Earth changed life (ozone shield lets life live on land).",
               "Case B is the clearest feedback loop: plants make soil and cool the climate, which changes where plants can live."],
        key=["Case A: Event: oxygen rises. Effect on life: new oxygen-using cells; ozone shields land. Effect back on Earth: more oxygen in the air; ozone layer forms.",
             "Case B: Event: plants spread on land. Effect on life: more plants and animals can live on land. Effect back on Earth: soil forms, rock breaks down, carbon dioxide falls, climate cools.",
             "Case C: Event: huge volcanoes. Effect on life: about 96% of ocean species die; survivors diversify. Effect back on Earth: fewer living things changes ocean and air chemistry for a time.",
             "In common: a change in one part (air, land, climate) changes living things, and living things change the air, soil, or oceans in return."],
        supports="Supply the table with one cell per case already filled. Allow oral rehearsal with a partner before writing.")))

# ---------------------------------------------------------------- Day 5
DAYS.append(dict(
    n=5, title="Make the Argument", short="Make the Argument", targets=["7.4"], cfa="7.4",
    s=dict(
        driving="Can you prove that Earth and life changed each other? What would a careful scientist need to see?",
        focus="How do I write an argument with a claim, evidence, and reasoning?",
        reading="Textbook: reread Lessons 8.2 and 8.3 (pp. 219–235) for evidence to use in the argument",
        nb=["Title: <strong>D5 Make the Argument</strong>. Add it to your table of contents.",
            "Leave a full page for your written argument and half a page for the peer check.",
            "Add three rows to your " + LOG],
        parts=[
            ("Warm-up (3 min)",
             "<p>A friend says, “Earth changed life, but life never changed Earth.” Do you agree? Write one sentence and give one reason.</p>"),
            ("The evidence bank (8 min)",
             "<p>Read the six pieces of evidence. Add three of them to your evidence log and mark the kind.</p>" +
             table([["Card", "Evidence", "Kind", "What it shows"],
                    ["E1", "Banded iron formations: layers of rusty iron rock formed about 2.5 to 1.8 billion years ago.", "Rock", "Oxygen reached the oceans and rusted iron."],
                    ["E2", "Stromatolites: layered rock mounds made by cyanobacteria, found from 3.5 billion years ago to today.", "Fossil", "Photosynthetic life existed very early."],
                    ["E3", "Oxygen data: about 0% before 2.4 billion years ago, about 2% by 2.0 billion, and about 15% by 0.5 billion.", "Data", "Oxygen in the air rose over time."],
                    ["E4", "Fossils of the first land plants (about 470 million years old); ancient soils appear after them.", "Fossil and rock", "Plants changed the land and made soil."],
                    ["E5", "Five mass extinctions in the last 450 million years; after each, new groups of animals spread within millions of years.", "Data", "Earth events change life, and survivors change the living world."],
                    ["E6", "Reef limestone built by corals stretches for hundreds of kilometers; shorelines behind reefs erode less.", "Rock", "Living things change coasts."]])),
            ("Plan with the frames (6 min)",
             "<p>Use these frames to plan. Fill in your notebook.</p>" + ul([
                 "<strong>Claim:</strong> Earth and life changed each other because ______.",
                 "<strong>Evidence 1:</strong> (Life changed Earth) ______ (use a number or a place).",
                 "<strong>Evidence 2:</strong> (Earth changed life) ______ (use a number or a place).",
                 "<strong>Evidence 3:</strong> ______.",
                 "<strong>Reasoning:</strong> This evidence shows ______ because ______.",
                 "<strong>Counterclaim:</strong> Someone might say ______. That does not fit because ______."])),
            ("Write your argument (14 min)",
             "<p>Write one paragraph of 8 to 10 sentences. Use <strong>at least three</strong> pieces of evidence from the bank. Include a number, name the <strong>kind</strong> of each piece of evidence, and use the word <strong>because</strong> at least twice.</p><p>Turn it in on Canvas: <strong>Unit 3.1 CER: Earth and life changed each other</strong> (type it in the text box or upload your notebook page).</p>"),
            ("Peer check (6 min)",
             "<p>Swap with a partner. Score your partner using the scale. Write one star (something strong) and one step (something to add).</p>" +
             table([["Score", "What it looks like"],
                    ["4", "A clear claim that goes both ways. Three pieces of evidence, with numbers, from at least two kinds. Reasoning that explains why each piece supports the claim. A fair counterclaim."],
                    ["3", "A clear claim and two or three pieces of evidence. Reasoning is there but one piece is missing or general."],
                    ["2", "A claim and some evidence, but little reasoning, or the claim goes only one way."],
                    ["1", "A claim with little or no evidence, or a major mistake."]])),
            ("Exit ticket: CFA ESS2-7.4 (6 min)",
             "<p>Take this CFA on Canvas now (5 questions):</p><ul><li><strong>Unit 3.1 CFA ESS2-7.4: Writing an argument with evidence</strong></li></ul><p>If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
        ],
        wrap="<p>Fix one thing your partner suggested. Tomorrow you will judge how strong different kinds of evidence are.</p>"),
    t=dict(
        glance="Students use a bank of six pieces of evidence to write their first full argument, then peer score it with a 4-point scale. They submit the CER on Canvas. The CFA for ESS2-7.4 is the exit ticket.",
        materials=["Evidence bank (the table, printed or projected)", "Sentence frames (on the page)", "Chromebooks for the CER submission and the CFA"],
        agenda=[["0–3", "Warm-up"], ["3–11", "Evidence bank"], ["11–17", "Plan with frames"], ["17–31", "Write the argument"], ["31–37", "Peer check"], ["37–45", "Exit ticket: CFA ESS2-7.4"]],
        notes=["Score the CER with the 4-point scale on the page. Do not grade grammar.",
               "A common error is a claim that only goes one way (Earth to life). Ask: where is life changing Earth in your argument?",
               "A second common error is evidence with no number or place. Ask: what could I check?"],
        key=["Warm-up: students should disagree and give an example such as oxygen, soil, or reefs.",
             "Model claim: Earth and life changed each other because photosynthetic life added oxygen to the air and oceans, and the changed air then shaped later life.",
             "Model evidence: E1 (banded iron layers show oxygen rusted ocean iron), E3 (oxygen rose from about 0% to about 15%), E5 (after each mass extinction new groups spread).",
             "Model reasoning: Oxygen could only reach the rock record if living things made it, so life changed Earth. Extinctions and later oxygen changes changed which living things could survive, so Earth changed life.",
             "Counterclaim: Volcanoes made all the oxygen. Answer: the iron layers and stromatolites point to photosynthesis, and volcanoes do not release large amounts of free oxygen."],
        supports="Give the six frames as a fill-in table. Allow students to dictate the first draft to a partner. Provide a word bank: because, shows, so, therefore.")))

# ---------------------------------------------------------------- Day 6
DAYS.append(dict(
    n=6, title="Evidence Court", short="Evidence Court", targets=["7.5"], cfa="7.5",
    s=dict(
        driving="You have a story about Earth and life. A skeptic asks: how do you know? Which evidence could convince them?",
        focus="How do different kinds of evidence work together to make one strong argument?",
        reading="Use your evidence log and the evidence cards below",
        nb=["Title: <strong>D6 Evidence Court</strong>. Add it to your table of contents.",
            "Leave room for a sorting table with 8 rows and a paragraph.",
            "Open your " + LOG],
        parts=[
            ("Warm-up (3 min)",
             "<p>Would you believe a story told by only one witness? What would make you trust it more? Write 2 sentences.</p>"),
            ("Sort and rate the evidence (14 min)",
             "<p><strong>Evidence Court · 14 min · with a partner</strong></p><p>For each card write the <strong>kind</strong> (rock, fossil, chemical data, model, or story) and a <strong>strength score from 1 to 3</strong>. Strong evidence is <strong>direct</strong> (you can touch or measure it), <strong>checkable</strong> (others can repeat it), and <strong>agrees with other kinds</strong> of evidence.</p>" +
             table([["Card", "Evidence", "Kind", "Strength (1–3) and why"],
                    ["C1", "Banded iron formation: layers of rusty rock, about 2.4 billion years old.", "", ""],
                    ["C2", "Measurements of ancient rock chemistry show the oceans and air held very little oxygen before 2.4 billion years ago.", "", ""],
                    ["C3", "Stromatolites: fossil mounds built by photosynthetic microbes, 3.5 billion years old.", "", ""],
                    ["C4", "A computer model that shows oxygen rising when photosynthetic microbes spread.", "", ""],
                    ["C5", "Fossils of the first animals appear after oxygen rose.", "", ""],
                    ["C6", "Ancient soil layers beneath fossil forests.", "", ""],
                    ["C7", "Carbon in rocks has a chemical signature made by living things.", "", ""],
                    ["C8", "A short story in an old book saying “the air was always the same.” (No data.)", "", ""]])),
            ("Build one argument from several kinds (12 min)",
             "<p>Write a paragraph that uses <strong>at least three kinds</strong> of evidence from the cards to argue that <strong>life changed Earth's air and oceans</strong>.</p>" + ul([
                 "<strong>Claim:</strong> ______.",
                 "<strong>Evidence:</strong> a rock ______, a fossil ______, and chemical data or a model ______.",
                 "<strong>Why they agree:</strong> These different kinds of evidence point to the same story because ______.",
                 "<strong>Skeptic:</strong> A skeptic says ______. This evidence answers because ______."])),
            ("Challenge: go further (8 min, GATE and anyone ready)",
             "<p><strong>Depth challenge (DOK 4).</strong> Pick <strong>two</strong> prompts. Write 4 to 5 sentences for each.</p>" + ul([
                 "<strong>Different perspectives:</strong> How would a geologist and an ecologist tell this story differently? What does each notice?",
                 "<strong>Over time:</strong> How did the same event look at the start of the story compared with the end?",
                 "<strong>Unanswered questions:</strong> What would you still like to know? What evidence would answer it?",
                 "<strong>Big idea:</strong> State one idea that works for oxygen, soil, and reefs. Where might it not work?"])),
            ("Exit ticket: CFA ESS2-7.5 (6 min)",
             "<p>Take this CFA on Canvas now (5 questions):</p><ul><li><strong>Unit 3.1 CFA ESS2-7.5: Combining kinds of evidence</strong></li></ul><p>If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
        ],
        wrap="<p>Circle the single strongest piece of evidence in your sorting table. Tomorrow you zoom out to Earth's whole system.</p>"),
    t=dict(
        glance="Students sort and rate eight pieces of evidence, build one argument from several kinds, and (for students who are ready) complete a depth challenge with Kaplan-style prompts. This is the DOK 4 depth day; the CSA stops at DOK 3. The CFA for ESS2-7.5 is the exit ticket.",
        materials=["Evidence cards C1 to C8", "Chromebooks for the CFA", "Depth challenge prompts for GATE compaction"],
        agenda=[["0–3", "Warm-up"], ["3–17", "Sort and rate the evidence"], ["17–29", "Build one argument"], ["29–37", "Depth challenge"], ["37–45", "Exit ticket: CFA ESS2-7.5"]],
        notes=["The CFA asks students to combine kinds of evidence at DOK 3. The depth challenge is optional and reaches DOK 4.",
               "For GATE, use the challenge as the main task and compact the sorting table to a short discussion.",
               "Do not tell students which card is strongest. Make them use the three tests: direct, checkable, agrees with other kinds."],
        key=["Kinds: C1 rock, C2 chemical data, C3 fossil, C4 model, C5 fossil, C6 rock, C7 chemical data, C8 story.",
             "Strength: C1 (3, direct and checkable), C2 (3, measured, repeated), C3 (3, direct sign of microbes), C4 (2, a model depends on assumptions), C5 (2, timing only), C6 (3, direct), C7 (2, needs interpretation), C8 (1, no data).",
             "Good argument: banded iron layers (rock), stromatolites (fossil), and ancient rock chemistry (data) all point to oxygen from living things at about the same time. When different kinds agree, the argument is stronger.",
             "Skeptic: “Volcanoes made the oxygen.” Answer: stromatolites and the carbon signature point to living things, and the rust layers appear where photosynthetic life lived."],
        supports="Give a one-page card with the three strength tests. Provide the argument paragraph as a partly filled frame. Pair students for the sorting task.")))

# ---------------------------------------------------------------- Day 7
DAYS.append(dict(
    n=7, title="Earth's Systems Web", short="Earth's Systems Web", targets=["7.6"], cfa=None,
    s=dict(
        driving="Earth is made of rock, water, air, and living things. When one changes, do the others change too?",
        focus="How are Earth's systems and life connected over time?",
        reading="Textbook: Lesson 8.1 Earth's Origin (pp. 206–218). Read in chunks; finish on Day 8.",
        nb=["Title: <strong>D7 Earth's Systems Web</strong>. Add it to your table of contents.",
            "Leave a full page for the web and half a page for reading notes.",
            "Keep your " + LOG],
        parts=[
            ("Warm-up (3 min)",
             "<p>Write the four Earth systems and one example in each: <strong>geosphere</strong> (rock), <strong>hydrosphere</strong> (water), <strong>atmosphere</strong> (air), <strong>biosphere</strong> (living things).</p>"),
            ("Reading notes (12 min)",
             "<p>Read <strong>Lesson 8.1, Earth's Origin (pp. 206–218)</strong>. Make a chart with two columns, <em>Stage of Earth</em> and <em>Which system changed</em>. Add at least four rows (for example: hot early Earth, oceans form, first life, oxygen builds up).</p>"),
            ("Build the web (20 min)",
             "<p><strong>Systems web · 20 min · with a partner</strong></p>" + ol([
                 "Draw four boxes: Geosphere, Hydrosphere, Atmosphere, Biosphere. Put one in each corner of your page.",
                 "Draw an arrow for each link below. Label every arrow with a short phrase. Mark each arrow with a star if it is a link where living things changed a non-living system.",
                 "Add <strong>two links of your own</strong>."]) + table([["Link", "What happens"],
                    ["1", "Volcanoes release gases into the air (geosphere to atmosphere)."],
                    ["2", "Rain falls and fills the oceans (atmosphere to hydrosphere)."],
                    ["3", "Photosynthetic cells release oxygen (biosphere to atmosphere)."],
                    ["4", "Oxygen rusts iron dissolved in the ocean (atmosphere to hydrosphere and geosphere)."],
                    ["5", "Ozone blocks harmful sunlight so life can live on land (atmosphere to biosphere)."],
                    ["6", "Plants and roots break rock and make soil (biosphere to geosphere)."],
                    ["7", "Forests take in carbon dioxide and bury carbon as coal (biosphere to atmosphere and geosphere)."],
                    ["8", "Ice ages change sea level and where life can live (atmosphere and hydrosphere to biosphere)."],
                    ["9", "Corals build reefs that change the shore (biosphere to geosphere)."],
                    ["10", "Mass extinctions change which living things survive (geosphere and atmosphere to biosphere)."]])),
            ("Sketchnote (7 min, finish for homework)",
             "<p>Make a sketchnote of your web with <strong>color, picture, text, and a template</strong>, using about equal amounts of pictures and text. Submit it on Canvas: <strong>Lesson 7: SketchNotes: Earth's systems and life</strong>.</p>"),
        ],
        wrap="<p>Which system has the most arrows pointing out of it? Which has the most pointing in? Write your answers. Tomorrow you will use the web to argue that Earth and life changed together. There is no CFA today.</p>",
        absent_extra=""),
    t=dict(
        glance="Students read Lesson 8.1 and build a four-system web with ten linked events. They begin a sketchnote. The CFA for ESS2-7.6 is tomorrow.",
        materials=["Textbook Lesson 8.1 (pp. 206–218)", "Colored pencils", "The web link table (printed or projected)"],
        agenda=[["0–3", "Warm-up"], ["3–15", "Reading notes"], ["15–35", "Build the web"], ["35–42", "Sketchnote start"], ["42–45", "Wrap-up"]],
        notes=["Lesson 8.1 is long. Chunk it: pp. 206–210 (hot early Earth), 211–214 (oceans and the first cells), 215–218 (oxygen and the ozone layer).",
               "The star marks links where life changed a non-living system. Expect links 3, 4 (by effect), 6, 7, and 9.",
               "Each link is one row of the Day 8 timeline. Keep student webs for tomorrow."],
        key=["Warm-up examples: geosphere, rocks; hydrosphere, oceans; atmosphere, air; biosphere, plants and animals.",
             "Stars (life changed a non-living system): 3, 6, 7, 9 (and 4 through the oxygen life made).",
             "Most arrows out of: biosphere. Most arrows in: depends on the student's own links; accept any answer supported by the web."],
        supports="Provide a pre-drawn web with the four boxes. Let students color each arrow by the system it starts in.")))

# ---------------------------------------------------------------- Day 8
DAYS.append(dict(
    n=8, title="Argue Together", short="Argue Together", targets=["7.6"], cfa="7.6",
    s=dict(
        driving="Did Earth and life change together over 3.5 billion years, or did each change on its own?",
        focus="Can I argue from evidence that Earth's systems and life changed together over time?",
        reading="Use your Day 7 web and the timeline table below",
        nb=["Title: <strong>D8 Argue Together</strong>. Add it to your table of contents.",
            "Leave room for the timeline table and one paragraph.",
            "Keep your " + LOG],
        parts=[
            ("Warm-up (3 min)",
             "<p>Look at your web from yesterday. Pick the arrow that you think matters most. Tell a partner why.</p>"),
            ("The timeline (12 min)",
             "<p>Read the eight rows. In the last column write <strong>how Earth and life are linked</strong> in that row. Circle two rows that form a <strong>loop</strong> (life changes Earth, then Earth changes life).</p>" +
             table([["Row", "When", "What happened to Earth", "What happened to life", "How they are linked"]] + TIMELINE_ROWS)),
            ("Write your argument (15 min)",
             "<p>Write one paragraph (8 to 10 sentences) that argues <strong>Earth's systems and life changed together over time</strong>. Use the frames.</p>" + ul([
                 "<strong>Claim:</strong> Earth's systems and life changed together because ______.",
                 "<strong>Evidence:</strong> Use <strong>at least three rows</strong> from the table. Include one loop. Name the kind of evidence (rock, fossil, data) when you can.",
                 "<strong>Reasoning:</strong> These rows show ______ because ______.",
                 "<strong>Counterclaim:</strong> Someone says life only <em>reacts</em> to Earth. Use two rows to respond."])),
            ("Share and fix (5 min)",
             "<p>Read your argument to a partner. Check for: a claim that goes both ways, three rows with numbers, and the word <strong>because</strong>. Fix one thing.</p>"),
            ("Exit ticket: CFA ESS2-7.6 (6 min)",
             "<p>Take this CFA on Canvas now (5 questions):</p><ul><li><strong>Unit 3.1 CFA ESS2-7.6: Earth and life changing together</strong></li></ul><p>If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
        ],
        wrap="<p>Tomorrow is the review day. Look at your six CFA scores and plan which reviews you need.</p>"),
    t=dict(
        glance="Students use an eight-row timeline to write a final argument that Earth's systems and life changed together, including a loop and a counterclaim. The CFA for ESS2-7.6 is the exit ticket.",
        materials=["Timeline table (printed or projected)", "Day 7 webs", "Chromebooks for the CFA"],
        agenda=[["0–3", "Warm-up"], ["3–15", "The timeline"], ["15–30", "Write the argument"], ["30–35", "Share and fix"], ["35–45", "Exit ticket: CFA ESS2-7.6"]],
        notes=["This is the capstone argument for the CSA's free response. Score it with the Day 5 four-point scale.",
               "Loops to accept: row 2 to 3 (microbes release oxygen, which changes the oceans, which changes later cells), row 4 to 5 (oxygen, ozone, land plants), row 5 to 6 (plants, soil, carbon dioxide, climate).",
               "A response to “life only reacts” should name a row where life changed Earth (rows 2, 3, 5, 6)."],
        key=["Row links: 1 early oceans and microbes, 2 life adds oxygen, 3 oxygen changes ocean chemistry and later cells, 4 oxygen and ozone allow animals, 5 ozone lets plants live on land and plants make soil, 6 forests change the air and climate, 7 Earth event and mass extinction, 8 Earth event and mass extinction.",
             "Loops: rows 2 to 3, 4 to 5, 5 to 6.",
             "Model claim: Earth's systems and life changed together because each change in the air, rock, or oceans changed which living things could live, and living things in turn changed the air, rock, and oceans."],
        supports="Provide the paragraph frame as a table with sentence starters. Allow oral drafting before writing. Give a two-row model of a loop.")))

# ---------------------------------------------------------------- Day 9
REVIEW_BODY = (
    "<p><strong>Do the sections for any CFA under 4 of 5 correct (3 of 4 points). Everyone does Vocabulary (Section A) and Write It (Section F).</strong></p>"
    + table([["Section", "Target", "What it practices"],
             ["A", "All", "Vocabulary"], ["B", "ESS2-7.1", "Examples of how Earth changed and how life changed"], ["C", "ESS2-7.2 and 7.3", "Direction of change and cause chains"],
             ["D", "ESS2-7.4 and 7.5", "Evidence and its kinds"], ["E", "ESS2-7.4 to 7.6", "Score it yourself"], ["F", "ESS2-7.6", "Write It: one argument"]])
    + "<h2>Section A: Vocabulary</h2><p><strong>Word bank:</strong> atmosphere, biosphere, geosphere, hydrosphere, photosynthesis, ozone layer, mass extinction, banded iron formation, stromatolite, evidence, argument, feedback</p>"
    + ol(["Cells use ______ to make sugar and release oxygen.", "A layer of oxygen high in the air that blocks harmful sunlight is the ______.",
          "A time when a very large share of species die out is a ______.", "Layers of rusty iron rock formed when oxygen reached the oceans: ______.",
          "Layered mounds built by microbes and found as fossils: ______.", "The living things on Earth are the ______; the air is the ______.",
          "When a change in one part leads to a change back in the first part, we call it ______.", "Facts or data that support a claim are ______."])
    + "<h2>Section B: Earth changed or life changed?</h2><p>Write E, L, or B for each: ice ages come and go; photosynthetic cells spread; Pangaea breaks apart; land plants spread; oxygen builds up in the air; the first animals appear. Then name one example of each kind from memory.</p>"
    + "<h2>Section C: Which way, and what next?</h2>" + ol([
        "Corals build a reef. Which way did the change go? What happens next to the shore?",
        "A volcano blocks sunlight for years. Which way did the change go? Write a chain of three events that follows.",
        "Plants spread on land. Name one thing they change in the air and one thing they change in the soil."])
    + "<h2>Section D: Kinds of evidence</h2><p>Sort these: a banded iron formation; ancient rock chemistry; stromatolite fossils; a computer model; a story with no data. Write the kind of each (rock, fossil, data, model, story) and rank them from strongest to weakest. Why does combining kinds make a claim stronger?</p>"
    + "<h2>Section E: Score it yourself</h2><p>Use the Day 5 four-point scale. Question: <em>Did life change Earth, or only Earth change life?</em></p>"
    + "<p><strong>Student A:</strong> “Life changed Earth because there was a lot of life.”</p>"
    + "<p><strong>Student B:</strong> “Life changed Earth. Stromatolite fossils show photosynthetic cells lived 3.5 billion years ago, and the rusty banded iron layers about 2.4 billion years old show oxygen reached the ocean. Rust needs oxygen, so living things that make oxygen must have changed the ocean and air. Oxygen then rose to about 15% of the air by 0.5 billion years ago, which let animals evolve. Someone might say volcanoes made the oxygen, but the fossils and layers point to living things.”</p>"
    + "<p><strong>Student C:</strong> “Oxygen went up, so life changed Earth.”</p>"
    + ol(["Score each response from 1 to 4 and explain.", "Rewrite Student C's answer so it earns a 4."])
    + "<h2>Section F: Write It</h2><p>Write one paragraph (8 to 10 sentences) arguing that <strong>Earth's systems and life changed together over time</strong>. Use at least three pieces of evidence from at least two kinds, one loop, and one counterclaim.</p>"
    + "<h2>Before the CSA: Can you…</h2>" + ul(["name examples of how Earth and life each changed?", "say which direction a change went and what came next?",
                                              "explain the oxygen story with two cause-and-effect links?", "write an argument with a claim, evidence, and reasoning?",
                                              "explain why several kinds of evidence are stronger than one?", "argue that Earth's systems and life changed together?"]))

DAYS.append(dict(
    n=9, title="Review and Reteach", short="Interventions and Review", targets=["7.1", "7.2", "7.3", "7.4", "7.5", "7.6"], cfa=None,
    s=dict(
        driving="You have learned a lot of pieces. Which pieces do you still need before the CSA?",
        focus="What do I still need to practice for the CSA?",
        reading="Your CFA scores, your reviews, and your evidence log",
        nb=["Title: <strong>D9 Review</strong>. Add it to your table of contents.",
            "List your six CFA scores (ESS2-7.1 to 7.6). Circle any under 4 of 5 correct (3 of 4 points)."],
        parts=[
            ("Check where you are (5 min)",
             "<p>Open Canvas. Look at your six CFAs. If you scored below 3 out of 4 on a CFA, its <strong>Review (Mastery Path)</strong> has opened. Finish any review you have not done.</p>"),
            ("Review work time (35 min)", REVIEW_BODY),
        ],
        wrap="<p>Put a check next to each “Can you…” you are sure of. Bring questions about the others tomorrow. Tomorrow is the <strong>Unit 3.1 CSA</strong> (45 minutes). Sleep well and bring a pencil.</p>"),
    t=dict(
        glance="Review and reteach. Students with any CFA under 4 of 5 correct complete the matching review and the sections for that target. All students complete Vocabulary and Write It. Pull a small group for reteaching from the CFA data.",
        materials=["CFA results (Canvas gradebook or the item report)", "Review page for each target", "Chromebooks"],
        agenda=[["0–5", "Check scores; plan"], ["5–25", "Sections for the targets under mastery"], ["25–38", "Vocabulary and Write It"], ["38–45", "“Can you…” check and CSA preview"]],
        notes=["Reteach the two lowest CFA targets with a small group while others work.",
               "Use the pre-check from Day 1 to show growth.",
               "Remind students that the CSA stops at DOK 3 and does not include the Day 6 depth challenge."],
        key=["Vocabulary: photosynthesis; ozone layer; mass extinction; banded iron formation; stromatolite; biosphere and atmosphere; feedback; evidence.",
             "B: ice ages E; photosynthetic cells L; Pangaea breaks apart E; land plants L; oxygen builds up B; first animals L.",
             "C: (1) life changed Earth; reefs protect the shore and change erosion. (2) Earth changed life; ash blocks sunlight, plants die, animals that eat them lose food, the ecosystem changes. (3) Plants take in carbon dioxide and make soil.",
             "D: rock, data, fossil, model, story. Strongest to weakest: banded iron formation and rock chemistry and fossils, then model, then story. Several kinds that agree make a claim harder to doubt.",
             "E: A = 1 (no evidence); B = 4; C = 2 (one fact, no kind or reasoning). A 4 for C adds the fossils or rust layers, a number, and reasoning that oxygen came from living things.",
             "F: Score with the four-point scale."],
        supports="Provide a checklist for each review. Offer oral explanations for Write It. Provide the Day 8 table as a model.")))

# ---------------------------------------------------------------- Day 10
DAYS.append(dict(
    n=10, title="Unit 3.1 CSA", short="Unit 3.1 CSA", targets=["7.1", "7.2", "7.3", "7.4", "7.5", "7.6"], cfa=None,
    s=dict(
        driving="Show what you know about how Earth and life have changed each other.",
        focus="Can I show I have met the targets for this unit?",
        reading="No notes. Your teacher will tell you what is allowed.",
        nb=["Clear your desk. You may have a pencil."],
        parts=[
            ("Before you start (2 min)",
             "<ul><li>You have <strong>45 minutes</strong>.</li><li>The CSA has 6 matching terms, 8 multiple-choice questions, and 2 written responses (30 points in all).</li><li>Read each question twice.</li><li>For the written responses, use a claim, evidence, and reasoning.</li></ul>"),
            ("Take the CSA (43 min)",
             "<p>Open Canvas and take: <strong>Unit 3.1 CSA: Changing Earth, Changing Life (HS-ESS2-7)</strong></p>"),
        ],
        wrap="<p>When you finish, check your written responses, then read quietly. Students who are done early may work on the enrichment choice board.</p>"),
    t=dict(
        glance="Unit CSA. Students take the 45-minute Canvas test. Some questions are scored by Canvas; the two written responses are scored by hand with the four-point scoring notes in each question.",
        materials=["Chromebooks (Respondus LockDown Browser if your team uses it)", "Pencils"],
        agenda=[["0–2", "Directions"], ["2–45", "CSA"]],
        notes=["Allow the full 45 minutes.", "Score the two written responses within two days. The scoring notes are in SpeedGrader for each question.",
               "After the CSA, use the Reassessment plan for students under mastery."],
        key=["CSA key: see the CSA scoring notes in Canvas SpeedGrader and the CSA key file in the repository (assessments/HS-ESS2-7/)."],
        supports="Offer a quiet space, extra time per IEP/504, and read-aloud of the stems for eligible students.")))
