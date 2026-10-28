"""Unit 3.1 (HS-ESS2-7) assessments: CFAs, reviews, CSA, and student assignments."""
from days import TARGETS, table, ol, ul

# ---- CFAs: 5 items each. (stem, [options], correct index or list of indexes, feedback)
CFAS = {
 "7.1": dict(title="Examples of Earth and life changing", items=[
  ("Which event is an example of <strong>Earth itself</strong> changing?",
   ["Plates move, and the continents drift apart and back together", "Cells begin to use photosynthesis", "Land plants spread across the continents", "The first animals appear in the oceans"], 0,
   "Moving plates and drifting continents change Earth. The other choices are changes in living things."),
  ("Which statement describes a change in <strong>life</strong> over Earth's history?",
   ["Simple single cells came first, and later many kinds of plants and animals evolved", "Ice sheets grew and shrank many times", "Sea level rose and fell", "Volcanoes released gases into the air"], 0,
   "Life changed from simple cells to many kinds of plants and animals. Ice sheets, sea level, and volcanoes are changes in Earth."),
  ("Select the <strong>TWO</strong> examples of how <strong>Earth</strong> has changed.",
   ["Ice ages came and went", "Sea level rose and fell", "Photosynthetic cells evolved", "Land plants appeared", "Animals with shells appeared"], [0, 1],
   "Ice ages and changing sea level are changes in Earth. Photosynthetic cells, land plants, and shells are changes in living things."),
  ("Which list shows events in order from <strong>oldest to newest</strong>?",
   ["First cells, oxygen builds up in the air, land plants, an asteroid ends the non-bird dinosaurs", "Land plants, first cells, oxygen builds up in the air, an asteroid ends the non-bird dinosaurs",
    "Oxygen builds up in the air, first cells, an asteroid ends the non-bird dinosaurs, land plants", "An asteroid ends the non-bird dinosaurs, first cells, land plants, oxygen builds up in the air"], 0,
   "First cells (about 3.5 billion years ago), then oxygen (starting about 2.4 billion), then land plants (about 470 million), then the asteroid (66 million)."),
  ("About how old is Earth, and about when did life first appear?",
   ["About 4.6 billion years old; life appeared at least 3.5 billion years ago", "About 4.6 billion years old; life appeared about 600 million years ago, with the first animals",
    "About 3.5 billion years old; life appeared when Earth formed", "About 600 million years old; life appeared 3.5 billion years ago"], 0,
   "Earth is about 4.6 billion years old. The first life, simple cells, appeared at least 3.5 billion years ago. The first animals came much later.")]),
 "7.2": dict(title="Earth changes life, life changes Earth", items=[
  ("A volcano erupts and its ash blocks sunlight for years. Many plants die. What kind of change is this?",
   ["Earth changed life", "Life changed Earth", "Nothing changed, because the ash is temporary", "Life changed life"], 0,
   "A change in Earth (ash and darkness) changed living things. This is Earth changing life."),
  ("Which example shows <strong>life changing Earth</strong>?",
   ["Lichens and roots break rock into soil", "An ice age spreads over a continent", "A shallow sea dries up", "An asteroid blocks sunlight"], 0,
   "Living things (lichens and roots) changed the rock by breaking it down into soil. The other choices are Earth changes."),
  ("Select the <strong>TWO</strong> examples of <strong>life changing Earth</strong>.",
   ["Cells use photosynthesis and add oxygen to the air", "Corals build reefs that change the shoreline", "Sea level falls and a sea dries up", "Volcanoes release gases", "An ice sheet melts"], [0, 1],
   "Oxygen from photosynthesis and reefs built by corals are changes made by living things."),
  ("Which statement gives <strong>one example in each direction</strong>?",
   ["Ash from a volcano kills plants (Earth changes life). Forests store carbon and cool the air (life changes Earth).",
    "Ash from a volcano kills plants. An asteroid darkens the sky.", "Forests store carbon. Corals build reefs.", "Sea level falls. An ice sheet grows."], 0,
   "The first sentence is Earth changing life. The second is life changing Earth. The other choices give two examples going the same way."),
  ("A student says, “Change only goes from Earth to life.” Which fact best shows the student is wrong?",
   ["Photosynthetic cells added oxygen to the oceans and air", "Ice ages happened many times", "Volcanoes erupt", "Mass extinctions have happened"], 0,
   "Oxygen from living cells changed the air and oceans, so life changed Earth too.")]),
 "7.3": dict(title="How events changed life and life changed Earth", items=[
  ("Photosynthetic cells added oxygen to the oceans for hundreds of millions of years. What happened to the iron dissolved in the water?",
   ["It rusted and sank, forming layers called banded iron formations", "It turned into photosynthetic cells", "It floated to the surface", "Nothing, because iron does not react with oxygen"], 0,
   "Oxygen reacts with dissolved iron to make rust. The rust sank and formed the banded iron layers."),
  ("After oxygen rose, some of it formed an <strong>ozone layer</strong>. How did the ozone layer change life?",
   ["It blocked harmful sunlight, so life could live on land", "It made the oceans colder, so life left the land", "It removed oxygen from the air", "It caused the first mass extinction"], 0,
   "Ozone blocks much of the Sun's harmful ultraviolet light. Life could then live on land."),
  ("Use the table. Which mass extinction killed the <strong>greatest percent</strong> of species?<br>" + table([["Mass extinction", "Species lost (approximate %)"], ["End-Ordovician", "85"], ["End-Permian", "96"], ["End-Cretaceous", "76"]]),
   ["End-Ordovician", "End-Permian", "End-Cretaceous", "They all lost the same percent"], 1,
   "96% is the largest number, so the End-Permian extinction killed the greatest percent."),
  ("After a mass extinction, many habitats are empty. What usually happens over the next millions of years?",
   ["Surviving groups spread into the empty habitats, and new groups evolve", "Life never recovers", "The same species return unchanged", "Oxygen disappears from the air"], 0,
   "Survivors spread out and new groups evolve. After the End-Cretaceous extinction, for example, mammals diversified."),
  ("Which sentence best describes a feedback between plants and Earth?",
   ["Plants make soil and take in carbon dioxide, which changes the soil and climate, which changes where plants can live",
    "Plants grow in sunlight", "Soil comes only from volcanoes", "Plants are not affected by climate"], 0,
   "Plants change the soil and the air, and those changes then affect where plants can live. That is a feedback.")]),
 "7.4": dict(title="Writing an argument with evidence", items=[
  ("Which is the best <strong>claim</strong> for an argument about oxygen in Earth's history?",
   ["Photosynthetic life added oxygen to the air and oceans, and that changed Earth", "Oxygen is a gas", "I like the story about oxygen", "Air is important"], 0,
   "A claim answers the question and can be backed up with evidence."),
  ("Which piece of evidence best supports the claim that <strong>life changed Earth's oceans</strong>?",
   ["Banded iron formations show iron rusted when oxygen reached the oceans, and photosynthetic cells were living then", "Many people like rocks", "Oceans are large", "Fish live in oceans"], 0,
   "Good evidence is a fact or data that you can check and that connects to the claim."),
  ("<strong>Evidence:</strong> Banded iron formations are layers of rust about 2.4 billion years old. Which <strong>reasoning</strong> sentence connects the evidence to the claim that life changed Earth?",
   ["Rust needs oxygen, and photosynthetic cells were the main source of that much oxygen, so living things must have changed the ocean", "The layers are red and gray", "The layers are 2.4 billion years old", "Many rocks have stripes"], 0,
   "Reasoning explains why the evidence supports the claim."),
  ("Select the <strong>TWO</strong> statements that are <strong>evidence</strong> (facts you can check), not opinions.",
   ["Stromatolite fossils are about 3.5 billion years old", "Oxygen was about 15% of the air 0.5 billion years ago", "Oxygen is the most interesting gas", "Everyone should learn about rocks", "Rocks are boring"], [0, 1],
   "Ages from fossils and measured oxygen levels can be checked. The others are opinions."),
  ("A skeptic says volcanoes made all of the oxygen. Which evidence best answers the skeptic?",
   ["Stromatolite fossils and a chemical signature in rocks show living things were releasing oxygen when the iron rusted", "Volcanoes are big", "Oxygen is a gas", "Many people agree with me"], 0,
   "Evidence from fossils and rock chemistry points to living things as the source of the oxygen.")]),
 "7.5": dict(title="Combining kinds of evidence", items=[
  ("Which pair of evidence makes an argument stronger because it uses <strong>two different kinds</strong>?",
   ["A banded iron formation (rock) and stromatolites (fossils)", "Two photos of the same banded iron formation", "Two textbook sentences that say the same thing", "Two people's opinions"], 0,
   "A rock and a fossil are different kinds of evidence. Together they are harder to explain away."),
  ("Why does combining several kinds of evidence make an argument stronger?",
   ["If different kinds of evidence point to the same story, it is harder to explain them away", "It makes the argument longer", "One kind of evidence is always wrong", "Evidence is never wrong"], 0,
   "When separate kinds of evidence agree, the claim is more likely to be correct."),
  ("Fossils show land plants about 470 million years ago. Rock layers show thick soils soon after. Chemical data show carbon dioxide in the air falling over the next 100 million years. Which statement is <strong>best supported</strong>?",
   ["Spreading land plants helped make soil and lowered carbon dioxide", "Soil caused land plants to evolve", "Falling carbon dioxide caused plants to die", "Plants had no effect on the air"], 0,
   "The fossils, rocks, and data agree in time and in direction. They support plants changing the soil and the air."),
  ("Which piece of evidence is the <strong>weakest</strong>?",
   ["A story that says “the air was always the same,” with no data", "Chemical measurements of ancient rock", "Fossils of microbes", "A banded iron formation you can see and touch"], 0,
   "A story with no data cannot be checked. The other choices can be measured, seen, or repeated."),
  ("A group argues that coral reefs changed ancient coastlines. Select the <strong>TWO</strong> pieces of evidence that add the most <strong>different kinds</strong>.",
   ["Limestone reef rock mapped along an ancient shoreline", "Fossil corals found in the limestone", "A second map of the same limestone", "An opinion that reefs are pretty", "A repeat of the first map"], [0, 1],
   "Rock (the limestone) and fossils (the corals) are two kinds. Repeated maps or opinions add nothing new.")]),
 "7.6": dict(title="Earth and life changing together", items=[
  ("What does it mean that Earth's systems and life changed <strong>together</strong>?",
   ["Changes in the air, rock, and oceans changed life, and changes in life changed the air, rock, and oceans", "Life changed, but Earth stayed the same", "Earth changed, but life stayed the same", "They changed at the same time by coincidence"], 0,
   "Change went both ways and linked together over time."),
  ("Use the table.<br>" + table([["Time", "Event"], ["2.4 billion years ago", "Oxygen in the air rises"], ["600 million years ago", "First animals appear"], ["470 million years ago", "Land plants spread"], ["350 million years ago", "Forests bury carbon"]]) + "<br>Which statement is <strong>best supported</strong>?",
   ["Rising oxygen came before the first animals, and plants later changed the air again", "Animals caused oxygen to rise", "Land plants came before oxygen", "Forests had no effect on the air"], 0,
   "Oxygen rose first, animals came later, and forests later changed the air by burying carbon."),
  ("Plants spread on land and make soil. Soil lets larger plants grow, and those plants make more soil. This is an example of…",
   ["a loop in which life changes Earth and Earth changes life", "Earth changing life only", "a mass extinction", "an ice age"], 0,
   "Each change leads to another that feeds back to the first. That is a loop."),
  ("Which new evidence would <strong>weaken</strong> the argument that life changed Earth's atmosphere?",
   ["Rocks show the oxygen rise happened with no living things anywhere on Earth", "Fossils of microbes from the same time", "Rust layers in ocean rocks", "Stromatolites"], 0,
   "If oxygen rose with no life at all, then life could not be the cause."),
  ("Select the <strong>TWO</strong> links that show <strong>life changing a non-living Earth system</strong>.",
   ["Plants and roots break rock and make soil", "Forests bury carbon and lower carbon dioxide in the air", "Volcanoes release gases", "An asteroid darkens the sky", "Ice ages change sea level"], [0, 1],
   "Plants changed the rock and soil, and forests changed the air. The others are Earth changes.")]),
}


# ---- Reviews (Mastery Path): intro sections with check-your-answer, then 3 questions
def details(q, a):
    return f"<p><strong>Try it:</strong> {q}</p><details><summary>Check your answer</summary><p>{a}</p></details>"


REVIEWS = {
 "7.1": dict(use="Use: your Day 1 card sort and timeline strip.", sections=[
   ("Earth changes and life changes", "Earth has changed many times: plates moved and continents drifted, ice ages came and went, sea level rose and fell, and volcanoes and asteroids shook the planet. Life has changed too: simple cells came first, then cells that use photosynthesis, then animals, plants on land, and many other groups.",
    details("Is an ice age a change in Earth or in life?", "Earth. It is a change in climate and ice.")),
   ("A timeline of big events", "Earth formed about 4.6 billion years ago. The first cells appeared at least 3.5 billion years ago. Oxygen began to build up about 2.4 billion years ago. The first animals appeared about 600 million years ago, and land plants spread about 470 million years ago. The asteroid that ended the non-bird dinosaurs struck 66 million years ago.",
    details("Which came first, land plants or the first animals?", "The first animals (about 600 million years ago). Land plants came later (about 470 million years ago).")),
   ("Events that are both", "Some events changed Earth and life together. When photosynthetic cells added oxygen to the air, life changed the air. That was a change in life and in Earth.",
    details("Why is “oxygen builds up in the air” marked both?", "Living cells made the oxygen (life), and the air changed (Earth)."))],
   qs=["Name two ways Earth has changed and two ways life has changed.", "Put these in order from oldest to newest: first animals, first cells, land plants, Earth forms.", "Explain why one event on the timeline can be both an Earth change and a life change."]),
 "7.2": dict(use="Use: your Day 2 cause-and-effect cards and your two diagrams.", sections=[
   ("Two directions", "Earth can change life. Ash from volcanoes can block sunlight and kill plants. Ice ages change climate. Sea level changes can take away habitat. Life can change Earth. Photosynthetic cells added oxygen to the air. Lichens and roots make soil. Corals build reefs.",
    details("Photosynthetic cells added oxygen. Which direction is that?", "Life changed Earth (L→E).")),
   ("Reading an arrow", "An arrow shows what changed what. “Ash cloud → plants die” is Earth changing life (E→L). “Roots → soil forms” is life changing Earth (L→E).",
    details("Write an arrow for: a sea dries up and its animals lose their home.", "Sea dries up → animals lose habitat (E→L).")),
   ("Both ways in one story", "Often the story has both. Plants make soil (L→E). The soil lets larger plants grow (E→L).",
    details("What is the first change in that story, and what is the second?", "First, plants change the ground by making soil. Second, the soil changes which plants can grow."))],
   qs=["Give one example of Earth changing life and one example of life changing Earth.", "Draw and label two boxes and an arrow for each example.", "A friend says change only goes one way. Explain why your friend is wrong."]),
 "7.3": dict(use="Use: your Day 3 graph and chain, and your Day 4 three-case table.", sections=[
   ("The oxygen chain", "Photosynthetic cells released oxygen. The oxygen rusted iron in the oceans, which formed banded iron formations. Later, oxygen built up in the air and an ozone layer formed. The ozone layer blocked harmful sunlight, so life could live on land.",
    details("What did the ozone layer let life do?", "Live on land.")),
   ("Mass extinctions and recovery", "Earth events, like huge volcanic eruptions or an asteroid, changed climate and oceans. Many species died out. Survivors spread into empty habitats and new groups evolved.",
    details("What usually follows a mass extinction?", "Survivors spread out and new groups of living things evolve.")),
   ("Feedback", "A feedback is when a change leads back to the first thing. Plants make soil and take in carbon dioxide. That changes the soil and climate, which changes where plants can live.",
    details("Why is this a feedback?", "Plants change the soil and air, and the changed soil and air then affect plants."))],
   qs=["Write the oxygen chain in four steps. Mark which steps are life changing Earth and which are Earth changing life.", "Explain what happens to life after a mass extinction.", "Explain one feedback between plants and Earth."]),
 "7.4": dict(use="Use: your Day 5 evidence bank and your CER argument.", sections=[
   ("Claim, evidence, reasoning", "A claim answers the question. Evidence is a fact or data you can check. Reasoning explains why the evidence supports the claim.",
    details("Which part says why? Claim, evidence, or reasoning?", "Reasoning.")),
   ("Evidence that works", "Good evidence has a number, a place, or a name. “Banded iron formations are about 2.4 billion years old” is evidence. “Rocks are cool” is not.",
    details("Is “oxygen was about 15% of the air 0.5 billion years ago” evidence?", "Yes. It is a measured number.")),
   ("A counterclaim", "A counterclaim is what a skeptic might say. You answer it with evidence. A skeptic says volcanoes made the oxygen. You answer with stromatolites and rock chemistry that show living things made it.",
    details("What evidence answers “volcanoes made the oxygen”?", "Stromatolite fossils and rock chemistry that point to living things."))],
   qs=["Write a claim about how life and Earth changed each other.", "Give two pieces of evidence for your claim. Include a number.", "Write one reasoning sentence that starts with “This shows … because …”."]),
 "7.5": dict(use="Use: your Day 6 Evidence Court table.", sections=[
   ("Kinds of evidence", "Rock evidence: a banded iron formation. Fossil evidence: stromatolites. Chemical data: measurements of ancient rock chemistry. A model: a computer simulation. A story with no data is not evidence.",
    details("What kind of evidence is a stromatolite?", "A fossil.")),
   ("What makes evidence strong", "Strong evidence is direct, checkable, and agrees with other kinds of evidence.",
    details("Why is a story with no data weak?", "It cannot be checked.")),
   ("Combine to convince", "If a rock, a fossil, and chemical data all tell the same story, it is hard to explain them away. This is why we use several kinds.",
    details("Why are three kinds better than one?", "If different kinds agree, one mistake cannot break the claim."))],
   qs=["Name three different kinds of evidence and give an example of each.", "Rank a rock, a model, and a story with no data from strongest to weakest and explain.", "Explain why combining kinds of evidence makes an argument stronger."]),
 "7.6": dict(use="Use: your Day 7 web and your Day 8 timeline and argument.", sections=[
   ("Earth's systems", "Earth's systems are the geosphere (rock), hydrosphere (water), atmosphere (air), and biosphere (living things). They are linked. A change in one can change the others.",
    details("Which system do living things belong to?", "The biosphere.")),
   ("Loops over time", "Microbes add oxygen to the air. Oxygen forms ozone. Ozone lets plants live on land. Plants make soil and change the air. Each step changes the next.",
    details("What did the ozone layer let plants do?", "Live on land.")),
   ("Arguing together", "To argue that Earth and life changed together, use at least three events, include one loop, and say how each event changed the next.",
    details("What is a loop?", "A change that leads back to the first thing, like plants making soil that helps more plants grow."))],
   qs=["Explain what it means that Earth's systems and life changed together.", "Use two timeline events to describe one loop.", "A friend says life only reacts to Earth. Respond with evidence."]),
}


def review_html(k):
    r = REVIEWS[k]
    h = f"<p><strong>Learning target ESS2-{k}:</strong> {TARGETS[k]}</p>"
    h += "<p>Your CFA score was below a 3 out of 4, so this page walks you back through the target. Read each section, try the checks, then answer the 3 questions at the bottom.</p>"
    h += f"<p><em>{r['use']}</em></p>"
    for i, (head, body, chk) in enumerate(r["sections"], 1):
        h += f"<h3>{i}. {head}</h3><p>{body}</p>{chk}"
    h += "<h3>Show what you know</h3><p>Answer all 3 questions in the text box or upload a photo of your written answers. Use complete sentences.</p>" + ol(r["qs"])
    return h


# ---- Student assignments
LESSON1 = ("<p><strong>Lesson 1: Rusty Stripes</strong> · Unit 3.1: Changing Earth, Changing Life (HS-ESS2-7)</p>"
           "<p>Take a clear photo of your <strong>D1 Rusty Stripes</strong> notebook pages and upload it. Your pages should show your warm-up questions, the pre-check, your Earth and life sort, and your timeline strip.</p>"
           + table([["Score", "What it looks like"], ["4", "All four parts, neat, with each event placed on the timeline and marked E, L, or B."], ["3", "All four parts, but one is incomplete."], ["2", "Two or three parts."], ["1", "Only one part or hard to read."]]))
CER = ("<p><strong>Unit 3.1 CER: Earth and life changed each other</strong></p>"
       "<p><strong>Question:</strong> Did Earth and life change each other over Earth's history?</p>"
       "<p>Write one paragraph of 8 to 10 sentences. Use at least <strong>three</strong> pieces of evidence from the Day 5 evidence bank, name the <strong>kind</strong> of each, include a number, and use the word <strong>because</strong> at least twice. Type it in the text box or upload your notebook page.</p>"
       + ul(["<strong>Claim:</strong> Earth and life changed each other because ______.", "<strong>Evidence 1 (life changed Earth):</strong> ______.", "<strong>Evidence 2 (Earth changed life):</strong> ______.", "<strong>Evidence 3:</strong> ______.",
             "<strong>Reasoning:</strong> This shows ______ because ______.", "<strong>Counterclaim:</strong> Someone might say ______. That does not fit because ______."])
       + "<h3>Scoring (4 points)</h3>" + table([["Score", "What it looks like"],
          ["4", "A clear claim that goes both ways. Three pieces of evidence with numbers, from at least two kinds. Reasoning that explains why each piece supports the claim. A fair counterclaim with a reply."],
          ["3", "A clear claim and two or three pieces of evidence. Reasoning is there but one piece is missing or general."],
          ["2", "A claim and some evidence, but little reasoning, or the claim goes only one way."], ["1", "A claim with little or no evidence, or a major mistake."]]))
SKETCH = ("<p><strong>Lesson 7: SketchNotes: Earth's systems and life</strong></p>"
          "<p>Make a sketchnote of your Earth's Systems Web. Include the <strong>four elements</strong>: <strong>color</strong>, <strong>picture</strong>, <strong>text</strong>, and a <strong>template</strong>. Use about equal amounts of pictures and text (the 50/50 rule). Upload a photo.</p>"
          + table([["Score", "What it looks like"], ["4", "All four elements, about 50/50 pictures and text, all four Earth systems, and at least 5 labeled links."], ["3", "All four elements, but the balance or the number of links is off."], ["2", "Missing one element or several systems."], ["1", "Missing several elements or hard to read."]]))
ENRICH = ("<p><strong>Unit 3.1 Enrichment: Choice Board</strong></p>"
          "<p>You showed you understand the targets. Choose <strong>ONE</strong> option. Use at least two numbers or facts from this unit.</p>"
          "<h3>Option 1: Reef Builders</h3><p>Corals built reefs that changed shorelines and gave new homes to many species. Draw a labeled before-and-after diagram of a shoreline. Write 4 sentences about how the reef changed Earth and how the changed shoreline changed life. Include one number.</p>"
          "<h3>Option 2: A Diary from the Great Oxidation</h3><p>Write a diary entry by a photosynthetic microbe 2.4 billion years ago. Describe the ocean, the rust forming, and why the microbe's own waste, oxygen, is about to change the world. Include two facts from this unit.</p>"
          "<h3>Option 3: Coal and Climate</h3><p>Forests that spread about 350 million years ago buried carbon as coal. Make a flow chart that follows one carbon atom from the air into a tree, into coal, and back into the air when the coal is burned today. Explain in 3 sentences how this connects the past to climate now.</p>"
          "<h3>Option 4: After the Crash</h3><p>Use the five mass extinctions table from Day 3. Make a bar graph of species lost. Then predict: after which extinction did a famous group of animals diversify, and why? Use evidence.</p>")

# ---- CSA (30 points: matching 6, eight multiple-choice at 2 each, two written at 4 each)
CSA_MATCH = [("Atmosphere", "The layer of gases around Earth"), ("Biosphere", "All of the living things on Earth"),
             ("Photosynthesis", "The process cells use to make sugar and release oxygen"), ("Mass extinction", "A time when a very large share of species die out"),
             ("Ozone layer", "A layer high in the air that blocks harmful sunlight"), ("Banded iron formation", "Rock layers of rusted iron that formed when oxygen reached the oceans")]
CSA_EXTRA = ["The slow movement of Earth's plates", "The solid outer layer of Earth"]
CSA_MC = [  # (target, stem, options, correct, feedback)
 ("7.1", "Which list shows events from <strong>oldest to newest</strong>?",
  ["Earth forms, first cells, oxygen builds up, first animals, land plants", "First cells, Earth forms, first animals, oxygen builds up, land plants", "Earth forms, oxygen builds up, first cells, land plants, first animals", "First animals, first cells, Earth forms, land plants, oxygen builds up"], 0,
  "Earth formed first, then the first cells, then oxygen began to build up, then the first animals, and later land plants."),
 ("7.2", "Corals build a reef that changes a shoreline. Later, sea level drops, the reef dries out, and many corals die. Which statement gives the <strong>direction</strong> of each change?",
  ["Life changed Earth first (the reef), then Earth changed life (sea level and the dying corals)", "Earth changed life first (the reef), then life changed Earth (the drying)", "Both changes were life changing Earth", "Both changes were Earth changing life"], 0,
  "Corals (life) built the reef that changed the shore. Falling sea level (Earth) then killed the corals."),
 ("7.3", "Which chain of events is in the correct order and direction?",
  ["Photosynthetic cells release oxygen, iron in the ocean rusts, oxygen builds up in the air, an ozone layer forms, life can live on land", "An ozone layer forms, photosynthetic cells release oxygen, iron rusts, life moves to land", "Life moves to land, an ozone layer forms, oxygen builds up, iron rusts", "Iron rusts, an ozone layer forms, cells release oxygen, life moves to land"], 0,
  "Oxygen from cells came first. It rusted iron, built up in the air, and formed ozone, which let life live on land."),
 ("7.3", "Use the table.<br>" + table([["Mass extinction", "Time", "Species lost (approximate %)", "What happened next"], ["End-Permian", "252 million years ago", "96", "New groups, including early dinosaurs, evolved over millions of years"], ["End-Cretaceous", "66 million years ago", "76", "Mammals spread and diversified"]]) + "<br>Which conclusion is <strong>best supported</strong>?",
  ["Large losses of species were followed by new groups spreading into empty habitats", "Mass extinctions end all life", "New groups appeared before the extinctions", "Extinctions only happened to dinosaurs"], 0,
  "In both rows, survivors and new groups spread after the loss."),
 ("7.4", "<strong>Claim:</strong> Life changed the oceans. <strong>Evidence:</strong> Banded iron formations are layers of rust about 2.4 billion years old. Which <strong>reasoning</strong> best connects the evidence to the claim?",
  ["Rust needs oxygen, and photosynthetic cells were the main source of that much oxygen, so living things must have changed the ocean", "The layers are red and gray, so the claim is true", "The layers are old, so life must be old", "Many rocks have stripes, so oxygen is common"], 0,
  "Good reasoning explains why the evidence supports the claim, using the idea that rust needs oxygen and life made the oxygen."),
 ("7.5", "Which set makes the <strong>strongest</strong> argument that land plants changed Earth?",
  ["Fossil plants, ancient soil layers, and chemical data showing carbon dioxide fell", "Three photos of the same fossil", "A story and an opinion", "Two sentences from the same textbook paragraph"], 0,
  "Three different kinds of evidence that agree make the strongest argument."),
 ("7.5", "Which finding would most <strong>weaken</strong> the claim that photosynthetic microbes caused the rise in oxygen?",
  ["Evidence that the oxygen rise happened before any photosynthetic microbes existed", "Stromatolite fossils from the time of the oxygen rise", "Rust layers in ocean rocks from the time of the oxygen rise", "Rock chemistry showing living things were active"], 0,
  "If the oxygen rise came before any microbes, the microbes could not be the cause."),
 ("7.6", "Which statement best summarizes the evidence that Earth's systems and life changed <strong>together</strong>?",
  ["Changes in the air, rock, and oceans changed life, and changes in life changed the air, rock, and oceans over billions of years", "Life changed, but Earth stayed the same", "Earth changed, but life did not respond", "Earth and life changed at the same time by coincidence"], 0,
  "The evidence shows links that went both ways between living and non-living systems.")]
FR1 = ("7.4", "<strong>Land plants and Earth.</strong> Use the evidence.<br>" + table([["Kind", "Evidence"],
        ["Fossil", "Fossils of the first land plants are about 470 million years old."], ["Rock", "Thick soils appear in rock layers about 450 million years ago, soon after the first land plants."],
        ["Data", "Carbon dioxide in the air fell from about 4,000 ppm to about 400 ppm between 450 and 300 million years ago, while forests spread and coal formed. (Values are simplified.)"]]) +
       "<br><strong>Construct an argument:</strong> Argue that land plants changed Earth <em>and</em> that these changes then changed life. Use at least two pieces of evidence and explain how they support your claim.",
       "Rubric (4 pts) - 4: Clear claim that goes both ways (plants changed soil and air; changed soil and air let more or larger plants live). Uses at least two pieces of evidence with the specific values (470 million years, soils at about 450 million years, carbon dioxide from about 4,000 to 400 ppm). Reasoning explains why each piece supports the claim (roots and plants break down rock and make soil; plants take in carbon dioxide and bury carbon in coal). 3: Proficient. Claim and two pieces of evidence with reasoning, but one direction or one reasoning is missing. 2: Developing. Lists evidence with little explanation, or the claim goes one way. 1: Beginning. Little evidence or a major mistake. 0: blank or off-topic. Grading notes: Accept 'Earth changed life' as the soil letting larger plants grow or as lower carbon dioxide cooling climate. Do not take off for spelling. Exemplar: Land plants changed Earth, and the changed Earth changed life. Fossils show land plants about 470 million years ago, and soils appear in rock about 450 million years ago, so plants helped make soil by breaking down rock with roots. Carbon dioxide fell from about 4,000 ppm to 400 ppm while forests spread, because plants took in carbon dioxide and buried carbon as coal. The thicker soil and cooler climate then let larger plants and forests grow, which changed life too.")
FR2 = ("7.5", "<strong>Earth and life together.</strong> Use the table.<br>" + table([["Time", "What happened to Earth", "What happened to life", "Kind of evidence"],
        ["2.4 billion years ago", "Oxygen begins to build up; iron rusts in the oceans", "Photosynthetic cells are common", "Rock (banded iron) and fossils (stromatolites)"],
        ["600 million years ago", "Oxygen is higher and an ozone layer has formed", "First animals appear", "Chemical data and fossils"],
        ["470 million years ago", "Ozone blocks harmful sunlight on land", "Plants spread onto land and soils form", "Fossils and rock"],
        ["350 million years ago", "Forests bury carbon; carbon dioxide falls and the climate cools", "Large forests and land animals", "Data and fossils"]]) +
       "<br><strong>Argue from evidence</strong> that Earth's systems and life changed together over time. Use at least three rows, include one loop (life changing Earth and then Earth changing life), name at least two kinds of evidence, and answer a student who says, “Life only reacts to Earth; it never changes it.”",
       "Rubric (4 pts) - 4: A claim that Earth's systems and life changed together. Uses at least three rows with the specific times or events. Explains one loop (for example, photosynthetic cells add oxygen to the air, oxygen forms ozone, ozone lets plants live on land, plants make soil and change the air). Names at least two kinds of evidence (rock, fossil, data) and says why agreement among kinds makes the argument stronger. Answers the counterclaim using a row where life changed Earth (rows 1, 3, or 4). 3: Proficient. Claim, three rows, and a loop, but the kinds of evidence or the counterclaim reply is missing or general. 2: Developing. Lists rows with little linking, or no loop. 1: Beginning. Little evidence or a major mistake. 0: blank or off-topic. Grading notes: Accept any correct loop. Credit the kinds of evidence if named from the right column. Exemplar: Earth's systems and life changed together. About 2.4 billion years ago, banded iron rock and stromatolite fossils show that photosynthetic cells added oxygen to the oceans, so life changed Earth. By 600 million years ago, more oxygen and an ozone layer let the first animals live, and by 470 million years ago the ozone layer let plants live on land, where they made soil, so Earth changed life. Forests then buried carbon and lowered carbon dioxide, which changed the climate again. A rock, a fossil, and chemical data all agree, which makes the argument stronger. Someone might say life only reacts to Earth, but the oxygen and the carbon dioxide changes were caused by life.")
