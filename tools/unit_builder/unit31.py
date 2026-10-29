# -*- coding: utf-8 -*-
"""Unit 3.1 Changing Earth, Changing Life (HS-ESS2-7)."""
from lib import *

T = {
    1: 'ESS2-7.1: I can name examples of how Earth has changed and how life has changed.',
    2: 'ESS2-7.2: I can describe one way Earth changed life and one way life changed Earth.',
    3: 'ESS2-7.3: I can explain how events in Earth\'s history changed life, and how life in turn changed Earth.',
    4: 'ESS2-7.4: I can write an argument, with evidence, that Earth and life changed each other.',
    5: 'ESS2-7.5: I can combine several kinds of evidence into one strong argument about Earth and life.',
    6: 'ESS2-7.6: I can argue from evidence that Earth\'s systems and life have changed together over time.',
}
ILLUS = 'Illustrative data: simplified numbers for class, not from a single study.'
SRC_TIME = ('Sources: Earth\'s age, USGS "Age of the Earth" (about 4.54 billion years); oxygen rise, Lyons, Reinhard and Planavsky (2014), Nature 506:307-315; '
            'first animals, Narbonne (2005), Annual Review of Earth and Planetary Sciences 33:421-442; land plants, Rubinstein et al. (2010), New Phytologist 188:365-369; '
            'end-Permian extinction, Burgess, Bowring and Shen (2014), PNAS 111:3316-3321; end-Cretaceous impact, Renne et al. (2013), Science 339:684-687; '
            'earliest Homo sapiens fossils, Hublin et al. (2017), Nature 546:289-292. Dates are rounded; scientists revise them as new evidence arrives.')


def tb(header, rows, cols=None, rowh=None):
    return ('table', {'header': header, 'rows': rows, 'cols': cols, 'rowh': rowh})


def item(lesson, title, kicker, use, copies, body, key):
    return dict(lesson=lesson, title=title, kicker=kicker, use=use, copies=copies, body=body, key=key)


EV = [('A', 'Earth forms', 'about 4.6 billion years ago'), ('B', 'Oceans of liquid water form', 'about 4 billion years ago'),
      ('C', 'First simple cells (microbes)', 'about 3.5 billion years ago'), ('D', 'Cells that use photosynthesis spread', 'at least 2.7 billion years ago'),
      ('E', 'Oxygen builds up in the air and oceans', 'starting about 2.4 billion years ago'), ('F', 'First animals', 'about 600 million years ago'),
      ('G', 'Land plants spread', 'about 470 million years ago'), ('H', 'Continents join into the supercontinent Pangaea', 'about 300 million years ago'),
      ('I', 'Largest mass extinction (end of the Permian)', '252 million years ago'), ('J', 'Asteroid strike; non-bird dinosaurs go extinct', '66 million years ago'),
      ('K', 'Ice ages come and go', 'many times; the last ended about 12,000 years ago'), ('L', 'Humans appear', 'about 300,000 years ago')]
items = []

# ---- Lesson 1
items.append(item(1, 'Card sort: 12 events in Earth and life history', 'Card sort', 'Cut apart; pairs sort the cards', 'One set per pair',
    [('p', 'Cut out the 12 cards. For each event decide: did Earth change, did life change, or both? Then place each card on your timeline strip.'),
     ('cards', ['%s · %s · %s' % e for e in EV], 3, 0.92), ('note', SRC_TIME)],
    [('p', 'Cards are the same 12 events listed on the printable. Answers for E, L or B are on the "Timeline strip and E / L / B chart" key.')]))
items.append(item(1, 'Timeline strip and E / L / B chart', 'Card sort', 'Glue under "Card sort" in the notebook', 'One per student',
    [('p', 'Each box is 200 million years. The left end is 4.6 billion years ago and the right end is today. Write each card\'s letter in the box where it belongs.'),
     tb(None, [[str(i) for i in range(1, 24)]], [1] * 23, 0.5),
     ('note', 'Box 1 = 4.6 to 4.4 billion years ago. Box 23 = the most recent 200 million years to today.'),
     tb(['Card', 'Event', 'E, L or B?', 'Box'], [[e[0], e[1], '', ''] for e in EV], [0.6, 4, 1.2, 0.9], rowh=0.3),
     ('p', 'Which cards did you mark both? Why could both be true? ______________________________________________'),
     ('p', 'Where do most of the cards crowd together? What does that say about how fast things changed late in Earth\'s history? ________________________')],
    [tb(['Card', 'E, L or B', 'Box', 'Why'],
        [['A', 'E', '1', 'Earth formed (no life yet)'], ['B', 'E', '3', 'Oceans form'], ['C', 'L', '6', 'Life begins'], ['D', 'L', '10', 'Photosynthesis spreads'],
         ['E', 'B', '11', 'Life made oxygen (L to E), which changed air and ocean chemistry'], ['F', 'L', '20', 'First animals; life changes'],
         ['G', 'B', '21', 'Plants change land and soil (L to E) and need land to live on'], ['H', 'E', '22', 'Pangaea: Earth change'],
         ['I', 'B', '22', 'Earth event (volcanoes) caused extinction of life; Earth conditions changed too'], ['J', 'B', '23', 'Asteroid (E) then extinctions (L)'],
         ['K', 'B', '23', 'Climate change affects life; life affects carbon dioxide'], ['L', 'L', '23', 'A new living thing appears']], [0.7, 1, 0.7, 5]),
     ('p', 'Accept any reasoned answer for E, L or B. Cards in boxes 20 to 23 (F to L) crowd together: more events are known from recent history because the evidence is better preserved, and life and Earth changed fast late in the record.')]))
items.append(item(1, 'Unit CER evidence log', 'Evidence log', 'Glue into the back of the notebook; add rows all unit', 'One per student',
    [('p', 'Add one row each time you find evidence about how Earth and life changed each other. Kind: rock, fossil, data, or model.'),
     tb(['Evidence', 'Kind (rock, fossil, data, model)', 'What it shows'], [['', '', '']] * 13, [3, 2, 3.4], 0.5)],
    [('p', 'Rows will fill in over the unit. Example rows: Banded iron formation, rock, oxygen reached the oceans (about 2.4 billion years ago). Stromatolites, fossil, photosynthetic life existed early (3.5 billion years ago). Oxygen data, data, oxygen in the air rose over time.')]))

# ---- Lesson 2
CARDS2 = ['1 · Cells that use photosynthesis release oxygen into the oceans and air.',
          '2 · Volcanoes throw ash into the sky. The ash blocks sunlight for years, and many plants die.',
          '3 · Lichens and plant roots break rock into tiny pieces that become soil.',
          '4 · Sea level drops and a shallow sea dries up. Its animals lose their habitat.',
          '5 · Corals build reefs that slow waves and protect the shore.',
          '6 · An ice age spreads cold climate. Some animals evolve thick fur.',
          '7 · Forests take in carbon dioxide and store carbon in wood, and later in coal.',
          '8 · An asteroid strikes. Dust darkens the sky, and many species go extinct.']
items.append(item(2, 'Cause-and-effect cards', 'Cause-and-effect cards', 'Cut apart; pairs sort the cards', 'One set per pair',
    [('p', 'For each card write E→L if Earth changed life, or L→E if life changed Earth, then write what changed.'),
     ('cards', CARDS2, 2, 1.0), ('note', 'Examples are standard textbook cases; no data.')],
    [('p', 'Answers are on the sorting chart key.')]))
items.append(item(2, 'Sorting chart and diagrams', 'Cause-and-effect cards', 'Glue under "Sort" in the notebook', 'One per student',
    [tb(['Card', 'E→L or L→E', 'What changed'], [[str(i), '', ''] for i in range(1, 9)], [0.7, 1.5, 5], 0.38),
     ('p', 'How many cards are E→L? ____  How many are L→E? ____   Change between Earth and life goes in ______ directions.'),
     ('h', 'Draw your own pair: one E→L card and one L→E card. Two boxes joined by an arrow, labeled (example: Ash cloud → Plants die).'),
     ('box', 1.1, 'Diagram 1'), ('box', 1.1, 'Diagram 2'),
     ('p', 'Under each: First, ______________ so ______________.')],
    [tb(['Card', 'Direction', 'What changed'],
        [['1', 'L→E', 'Oxygen enters the air and oceans'], ['2', 'E→L', 'Ash blocks sunlight and plants die'], ['3', 'L→E', 'Rock becomes soil'],
         ['4', 'E→L', 'Habitat is lost for animals'], ['5', 'L→E', 'Reefs change the shoreline'], ['6', 'E→L', 'Climate changes and animals evolve thick fur'],
         ['7', 'L→E', 'Carbon dioxide is stored as carbon'], ['8', 'E→L', 'Dust darkens the sky and species go extinct']], [0.7, 1, 4.5]),
     ('p', '4 are E→L and 4 are L→E. Change between Earth and life goes in <b>both</b> directions. Diagrams vary: look for two labeled boxes, an arrow, and a "First, ... so ..." sentence.')]))

# ---- Lesson 3
items.append(item(3, 'Oxygen story: data table and graph grid', 'The Oxygen Story', 'Glue under "Graph" in the notebook', 'One per student',
    [('p', 'Graph the oxygen story. Put time on the x-axis (4.0 billion years ago on the left, 0 today on the right). Put oxygen (% of air) on the y-axis from 0 to 30. Plot and connect the points.'),
     tb(['Time (billions of years ago)', 'Oxygen in the air (% of air, simplified)'],
        [['4.0', '0'], ['3.0', '0 (a trace)'], ['2.5', '0 (a trace)'], ['2.0', '2'], ['1.0', '3'], ['0.5', '15'], ['0.3', '30'], ['0 (today)', '21']], [3, 3.4], 0.28),
     ('box', 2.3, 'Graph area (draw your axes)'),
     ('p', 'About when does oxygen first rise above a trace? Label that spot Great Oxidation Event. What process made this oxygen? ______________'),
     ('p', 'When is oxygen higher than it is today? What do you think happened to it afterward? ______________'),
     ('note', 'Values are simplified from published reconstructions: Lyons, Reinhard and Planavsky (2014), Nature 506:307-315 (rise of oxygen); Berner (2009), Geochimica et Cosmochimica Acta 73:5-23 (Phanerozoic oxygen model). Estimates vary widely; treat the numbers as a teaching model.')],
    [('p', 'Oxygen first rises above a trace between about 2.5 and 2.0 billion years ago (label near 2.4 billion years ago, the Great Oxidation Event). It was made by photosynthesis by cyanobacteria. Oxygen is highest (about 30%) around 0.3 billion years ago, higher than today (21%); afterward it fell (model-based estimates; students might say it was used up or changed as forests were buried and climates shifted).'),
     ('p', 'Points: (4.0, 0), (3.0, 0), (2.5, 0), (2.0, 2), (1.0, 3), (0.5, 15), (0.3, 30), (0, 21).')]))
items.append(item(3, 'Mass extinction data and the rust record', 'The Oxygen Story', 'Glue under "Mass extinctions" in the notebook', 'One per student',
    [('h', 'The rust record'),
     ('p', 'Iron dissolved in ancient ocean water. When oxygen from photosynthesis reached it, the iron rusted and sank to the seafloor in layers. These layers are banded iron formations.'),
     ('p', 'Which came first: oxygen from living things, or the rust layers? Explain. ______________________________'),
     ('p', 'Is this an example of life changing Earth, or Earth changing life? Why? ______________________________'),
     ('h', 'Mass extinctions: reading the data'),
     tb(['Mass extinction', 'Time (million years ago)', 'Species lost (approximate %)'],
        [['End-Ordovician', '445', '85'], ['Late Devonian', '375', '75'], ['End-Permian', '252', '96'], ['End-Triassic', '201', '80'], ['End-Cretaceous', '66', '76']], [3, 2.5, 2.8], 0.3),
     ('p', 'Which extinction killed the greatest percent of species? ______________'),
     ('p', 'Many of these were caused by Earth events, such as volcanoes or an asteroid. Explain how an Earth event changes life. ______________'),
     ('p', 'Predict: what happens to the living things that survive an extinction? ______________'),
     ('note', 'Source: Barnosky et al. (2011), Nature 471:51-57, "Has the Earth\'s sixth mass extinction already arrived?" (approximate percent of species lost in each of the "Big Five"; ranges vary by study and are rounded).')],
    [('p', 'The oxygen from living things came first: the iron could only rust after oxygen reached the water. This is life changing Earth (L→E): photosynthetic cells changed ocean and air chemistry.'),
     ('p', 'End-Permian killed the greatest percent (about 96%). Earth events (eruptions, an asteroid) change climate, light, or oceans, so many species cannot survive; survivors spread into empty habitats and new groups evolve.')]))
items.append(item(3, 'Build a chain', 'Build a chain', 'Glue under "Build a chain" in the notebook', 'One per student',
    [('p', 'Fill in the empty boxes with what happened next. Mark each arrow E→L or L→E.'),
     tb(None, [['Cells use photosynthesis', '→', '', '→', 'Iron in the ocean', '→', 'Oxygen builds up in the air', '→', 'An ozone layer forms and']], [2, 0.4, 2, 0.4, 2, 0.4, 2.4, 0.4, 2], 0.9),
     ('p', 'Fill in: box 2 ______________; box 3 iron in the ocean ______________; box 5 and ______________.'),
     ('p', 'Write one sentence: "Because ______ happened, ______ changed, which led to ______."'), ('lines', 3)],
    [('p', 'Chain: Cells use photosynthesis (L) → <b>release oxygen</b> → iron in the ocean <b>rusts and sinks</b> → oxygen builds up in the air → an ozone layer forms and <b>life can live on land</b>. Arrow marks: photosynthesis to oxygen L→E; oxygen to rusting E (chemical) shown as part of L→E; ozone to life on land E→L.'),
     ('p', 'Sample sentence: Because cells began using photosynthesis, the ocean and air changed, which led to the ozone layer and life on land.')]))

# ---- Lesson 4
items.append(item(4, 'Three case files', 'Three case files', 'Station reading and table; glue under "Case files"', 'One per student',
    [('h', 'Case A: Oxygen, ozone, and land'),
     ('p', 'Oxygen from photosynthesis rose in the air. Some oxygen became ozone, a layer high in the air that blocks much of the Sun\'s harmful ultraviolet light. Before the ozone layer, life lived mostly in water. After it, plants and animals could live on land.'),
     ('h', 'Case B: Soil and the first forests'),
     ('p', 'Microbes, lichens, and then plants spread on bare rock about 470 million years ago. They broke rock down and added dead matter, so soil formed. Deep soil let larger plants grow. Roots broke rock further and plants took in carbon dioxide. As forests spread, carbon was buried as coal and the air\'s carbon dioxide fell, which helped cool the climate.'),
     ('h', 'Case C: The end-Permian mass extinction'),
     ('p', 'About 252 million years ago, huge volcanic eruptions released carbon dioxide and other gases. The climate warmed and the oceans lost oxygen. About 96% of ocean species died. Over the next several million years, survivors spread into empty habitats and new groups, including early dinosaurs, evolved.'),
     tb(['Case', 'Event', 'Effect on life', 'Effect back on Earth', 'Arrow directions'], [['A', '', '', '', ''], ['B', '', '', '', ''], ['C', '', '', '', '']], [0.6, 2, 2.2, 2.2, 1.4], 0.55),
     ('p', 'What do all three cases have in common? ______________________________'),
     ('note', 'Sources: Algeo and Scheckler (1998), Phil. Trans. R. Soc. B 353:113-130 (land plants, weathering, and ocean oxygen); Burgess, Bowring and Shen (2014), PNAS 111:3316-3321 (end-Permian timing); percent extinction as in Barnosky et al. (2011), Nature 471:51-57.')],
    [tb(['Case', 'Event', 'Effect on life', 'Effect back on Earth', 'Arrows'],
        [['A', 'Oxygen from photosynthesis rises', 'Ozone lets life move onto land', 'Ozone layer forms; oxygen builds up', 'L→E then E→L'],
         ['B', 'Plants spread on land', 'Larger plants grow in deep soil', 'Soil forms; carbon buried as coal; CO₂ falls; climate cools', 'L→E, then E→L, then L→E'],
         ['C', 'Huge eruptions release gases', 'About 96% of ocean species die; survivors spread; new groups evolve', 'Warmer climate; oceans lose oxygen', 'E→L, then life refills Earth']], [0.5, 1.7, 2, 2.2, 1.6]),
     ('p', 'In common: each case is a chain of changes where an event in one system (air, rock, or life) causes changes in another, and the effect comes back.')]))

# ---- Lesson 5
EVB = [('E1', 'Banded iron formations: layers of rusty iron rock formed about 2.5 to 1.8 billion years ago.', 'Rock', 'Oxygen reached the oceans and rusted iron.'),
       ('E2', 'Stromatolites: layered rock mounds made by cyanobacteria, found from 3.5 billion years ago to today.', 'Fossil', 'Photosynthetic life existed very early.'),
       ('E3', 'Oxygen data: about 0% before 2.4 billion years ago, about 2% by 2.0 billion, and about 15% by 0.5 billion.', 'Data', 'Oxygen in the air rose over time.'),
       ('E4', 'Fossils of the first land plants (about 470 million years old); ancient soils appear after them.', 'Fossil and rock', 'Plants changed the land and made soil.'),
       ('E5', 'Five mass extinctions in the last 450 million years; after each, new groups of animals spread within millions of years.', 'Data', 'Earth events change life, and survivors change the living world.'),
       ('E6', 'Reef limestone built by corals stretches for hundreds of kilometers; shorelines behind reefs erode less.', 'Rock', 'Living things change coasts.')]
items.append(item(5, 'Evidence bank: six cards', 'Evidence bank', 'Cut apart; add three to the evidence log', 'One set per student',
    [('p', 'Read the six pieces of evidence. Add three of them to your evidence log and mark the kind.'),
     ('cards', ['%s · %s · Kind: %s · Shows: %s' % e for e in EVB], 2, 1.35),
     ('note', 'Sources: Bekker et al. (2010), Economic Geology 105:467-508 (banded iron formations); Allwood et al. (2006), Nature 441:714-718 (3.5 billion-year-old stromatolites); '
              'Rubinstein et al. (2010), New Phytologist 188:365-369 (early land plants); Barnosky et al. (2011), Nature 471:51-57 (extinctions). Oxygen values are simplified.')],
    [('p', 'Any three cards are acceptable for the evidence log. Kinds: E1 rock; E2 fossil; E3 data; E4 fossil and rock; E5 data; E6 rock.')]))
items.append(item(5, 'Argument planner and peer-check scale', 'Plan with the frames', 'Glue under "Plan" in the notebook', 'One per student',
    [('h', 'Plan with the frames'),
     ('p', 'Claim: Earth and life changed each other because ______________________________.'),
     ('p', 'Evidence 1 (life changed Earth): ______________________ (use a number or a place).'),
     ('p', 'Evidence 2 (Earth changed life): ______________________ (use a number or a place).'),
     ('p', 'Evidence 3: ______________________________.'),
     ('p', 'Reasoning: This evidence shows ______________ because ______________.'),
     ('p', 'Counterclaim: Someone might say ______________. That does not fit because ______________.'),
     ('h', 'Peer check: score your partner 1 to 4'),
     tb(['Score', 'What it looks like'],
        [['4', 'A clear claim that goes both ways. Three pieces of evidence, with numbers, from at least two kinds. Reasoning that explains why each piece supports the claim. A fair counterclaim.'],
         ['3', 'A clear claim and two or three pieces of evidence. Reasoning is there but one piece is missing or general.'],
         ['2', 'A claim and some evidence, but little reasoning, or the claim goes only one way.'],
         ['1', 'A claim with little or no evidence, or a major mistake.']], [0.7, 6.5]),
     ('p', 'One star (something strong): ______________________   One step (something to add): ______________________')],
    [('p', 'Sample plan: Claim: Earth and life changed each other because living things changed the air and the changed air changed living things. Evidence 1 (L→E): Banded iron formations about 2.4 billion years old show oxygen reached the ocean (rock). Evidence 2 (E→L): Five mass extinctions, such as the end-Permian, killed up to 96% of species after Earth events (data). Evidence 3: Oxygen rose from about 0% to 15% by 0.5 billion years ago, and the first animals appeared (data and fossil). Reasoning: Rust needs oxygen, so living things that make oxygen must have changed the ocean and air. Counterclaim: Volcanoes made the oxygen. That does not fit because stromatolite fossils show oxygen-making life existed.'),
     ('p', 'Peer-check scores vary. A 4 needs a claim that goes both ways, three pieces of evidence with numbers from two or more kinds, reasoning, and a counterclaim.')]))

# ---- Lesson 6
EVC = [('C1', 'Banded iron formation: layers of rusty rock, about 2.4 billion years old.'),
       ('C2', 'Measurements of ancient rock chemistry show the oceans and air held very little oxygen before 2.4 billion years ago.'),
       ('C3', 'Stromatolites: fossil mounds built by photosynthetic microbes, 3.5 billion years old.'),
       ('C4', 'A computer model that shows oxygen rising when photosynthetic microbes spread.'),
       ('C5', 'Fossils of the first animals appear after oxygen rose.'),
       ('C6', 'Ancient soil layers beneath fossil forests.'),
       ('C7', 'Carbon in rocks has a chemical signature made by living things.'),
       ('C8', 'A short story in an old book saying "the air was always the same." (No data.)')]
items.append(item(6, 'Evidence Court: eight evidence cards', 'Evidence Court', 'Cut apart; pairs sort and rate', 'One set per pair',
    [('p', 'For each card write the kind (rock, fossil, chemical data, model, or story) and a strength score from 1 to 3. Strong evidence is direct (you can touch or measure it), checkable (others can repeat it), and agrees with other kinds of evidence.'),
     ('cards', ['%s · %s' % c for c in EVC], 2, 0.95),
     ('note', 'Cards summarize evidence discussed in Bekker et al. (2010), Economic Geology 105:467-508; Allwood et al. (2006), Nature 441:714-718; Lyons, Reinhard and Planavsky (2014), Nature 506:307-315.')],
    [('p', 'Ratings are on the rating table key.')]))
items.append(item(6, 'Rating table and argument frames', 'Evidence Court', 'Glue under "Sort and rate" in the notebook', 'One per student',
    [tb(['Card', 'Kind', 'Strength (1 to 3) and why'], [['C%d' % i, '', ''] for i in range(1, 9)], [0.7, 1.8, 5], 0.4),
     ('h', 'Build one argument from several kinds of evidence'),
     ('p', 'Claim: ______________________.   Evidence: a rock ______, a fossil ______, and chemical data or a model ______.'),
     ('p', 'Why they agree: These different kinds of evidence point to the same story because ______________.'),
     ('p', 'Skeptic: A skeptic says ______________. This evidence answers because ______________.'),
     ('lines', 3)],
    [tb(['Card', 'Kind', 'Strength and why (sample)'],
        [['C1', 'Rock', '3: direct, checkable, agrees with C2 and C7'], ['C2', 'Chemical data', '3: measured and repeatable'], ['C3', 'Fossil', '3: direct evidence of early photosynthetic life'],
         ['C4', 'Model', '2: useful but depends on assumptions; strong only if it matches rock data'], ['C5', 'Fossil', '2: shows timing; does not show cause alone'],
         ['C6', 'Rock', '3: direct evidence of soil under forests'], ['C7', 'Chemical data', '3: measured signature of life'], ['C8', 'Story', '1: no data and cannot be checked']], [0.7, 1.4, 5]),
     ('p', 'Sample argument: Claim: Life changed Earth\'s air and oceans. Evidence: banded iron formations (rock) show oxygen reached the oceans; stromatolites (fossil) show photosynthetic life 3.5 billion years ago; ancient rock chemistry (data) shows oxygen was nearly absent before 2.4 billion years ago. They agree because rust needs oxygen and living cells make it. Skeptic: the air was always the same (C8). That has no data, while the rocks do.')]))

# ---- Lesson 7
LINKS = [('1', 'Volcanoes release gases into the air (geosphere to atmosphere).'), ('2', 'Rain falls and fills the oceans (atmosphere to hydrosphere).'),
         ('3', 'Photosynthetic cells release oxygen (biosphere to atmosphere).'), ('4', 'Oxygen rusts iron dissolved in the ocean (atmosphere to hydrosphere and geosphere).'),
         ('5', 'Ozone blocks harmful sunlight so life can live on land (atmosphere to biosphere).'), ('6', 'Plants and roots break rock and make soil (biosphere to geosphere).'),
         ('7', 'Forests take in carbon dioxide and bury carbon as coal (biosphere to atmosphere and geosphere).'), ('8', 'Ice ages change sea level and where life can live (atmosphere and hydrosphere to biosphere).'),
         ('9', 'Corals build reefs that change the shore (biosphere to geosphere).'), ('10', 'Mass extinctions change which living things survive (geosphere and atmosphere to biosphere).')]
items.append(item(7, 'Earth\'s systems web: link cards', 'Systems web', 'Cut apart; pairs build the web', 'One set per pair',
    [('p', 'Draw four boxes in your notebook: Geosphere, Hydrosphere, Atmosphere, Biosphere (one in each corner). Draw an arrow for each link card and label it with a short phrase. Put a star on each arrow where living things changed a non-living system. Add two links of your own.'),
     ('cards', ['%s · %s' % l for l in LINKS], 2, 0.78)],
    [('p', 'Arrows with a star (biosphere changing a non-living system): links 3, 4, 6, 7, 9. Link 4 is an atmosphere effect on water and rock, but the oxygen came from life. Arrows are on the web key. Most arrows pointing out of the biosphere: 3, 6, 7, 9.')]))
items.append(item(7, 'Earth\'s systems web: template and reading chart', 'Systems web', 'Glue under "Systems web" in the notebook', 'One per student',
    [tb(['Geosphere (rock)', 'Hydrosphere (water)'], [['', ''], ['', '']], [1, 1], 1.2),
     tb(['Atmosphere (air)', 'Biosphere (living things)'], [['', ''], ['', '']], [1, 1], 1.2),
     ('h', 'Reading notes: Lesson 8.1, Earth\'s Origin (pp. 206-218)'),
     tb(['Stage of Earth', 'Which system changed'], [['', ''], ['', ''], ['', ''], ['', '']], [3, 3.4], 0.4),
     ('p', 'Which system has the most arrows pointing out of it? ________  Which has the most pointing in? ________')],
    [('p', 'Sample reading chart: hot early Earth → geosphere; oceans form → hydrosphere; first life → biosphere; oxygen builds up → atmosphere (changed by biosphere).'),
     ('p', 'Most arrows out: the biosphere (links 3, 6, 7, 9 and the starred link 4). Most arrows in: the atmosphere or biosphere, depending on the student\'s extra links. Accept any count that matches the student\'s web.')]))

# ---- Lesson 8
items.append(item(8, 'The timeline: eight rows', 'Argue together', 'Glue under "The timeline" in the notebook', 'One per student',
    [('p', 'Read the eight rows. In the last column write how Earth and life are linked in that row. Circle two rows that form a loop (life changes Earth, then Earth changes life).'),
     tb(['Row', 'When', 'What happened to Earth', 'What happened to life', 'How they are linked'],
        [['1', '3.5 billion years ago', 'Oceans and shallow seas exist', 'First cells build layered mounds (stromatolites)', ''],
         ['2', '2.7 to 2.4 billion years ago', 'Iron dissolved in the oceans rusts; the air starts to gain oxygen', 'Photosynthetic cells spread', ''],
         ['3', '2.4 to 1.8 billion years ago', 'Oxygen rises in oceans and air; rusty iron layers settle on the seafloor', 'New kinds of cells that use oxygen evolve', ''],
         ['4', '600 million years ago', 'More oxygen in the air and oceans; an ozone layer forms', 'First animals appear', ''],
         ['5', '470 million years ago', 'The ozone layer blocks most harmful sunlight on land', 'Plants spread onto land; soils form', ''],
         ['6', '350 to 300 million years ago', 'Forests bury carbon; oxygen is high and carbon dioxide falls', 'Giant insects and the first large land animals', ''],
         ['7', '252 million years ago', 'Huge volcanic eruptions warm the climate; ocean oxygen drops', 'About 96% of ocean species go extinct', ''],
         ['8', '66 million years ago', 'An asteroid strike darkens the sky and cools the climate', 'Non-bird dinosaurs go extinct; mammals diversify', '']], [0.5, 1.4, 2.2, 2.2, 1.9], 0.62),
     ('note', SRC_TIME + ' Giant insects and carbon burial: Berner (2009).'),
     ('h', 'Write your argument frames'), ('p', 'Claim: Earth\'s systems and life changed together because ______.   Counterclaim: Someone says life only reacts to Earth. Use two rows to respond.')],
    [tb(['Row', 'How they are linked (sample)'],
        [['1', 'Oceans gave a home for first cells (E→L); the cells built mounds in the water (L→E).'], ['2', 'Cells made oxygen that rusted ocean iron (L→E).'],
         ['3', 'Oxygen rose, so cells that use oxygen evolved (E→L).'], ['4', 'More oxygen and ozone allowed first animals (E→L).'],
         ['5', 'Ozone let plants move to land (E→L), and plants made soil (L→E).'], ['6', 'Forests buried carbon (L→E); high oxygen supported giant insects (E→L).'],
         ['7', 'Eruptions changed the climate and ocean oxygen (E→L), killing 96% of ocean species.'], ['8', 'Asteroid changed climate (E→L); extinctions let mammals diversify (L→E in the living world).']], [0.7, 6.5]),
     ('p', 'Loops (life changes Earth, then Earth changes life): rows 2 and 3 (oxygen then new cells) or rows 5 and 6. Accept any pair where the effect comes back.')]))

# ---- Lesson 9
items.append(item(9, 'Review packet A to C', 'Review work time', 'Sections for CFAs under mastery; everyone does Section A', 'One per student',
    [('h', 'Section A: Vocabulary (everyone)'),
     ('p', 'Word bank: atmosphere, biosphere, geosphere, hydrosphere, photosynthesis, ozone layer, mass extinction, banded iron formation, stromatolite, evidence, argument, feedback'),
     ('p', '1. Cells use ______________ to make sugar and release oxygen.   2. A layer of oxygen high in the air that blocks harmful sunlight is the ______________.   3. A time when a very large share of species die out is a ______________.   4. Layers of rusty iron rock formed when oxygen reached the oceans: ______________.   5. Layered mounds built by microbes and found as fossils: ______________.   6. The living things on Earth are the ______________; the air is the ______________.   7. When a change in one part leads to a change back in the first part, we call it ______________.   8. Facts or data that support a claim are ______________.'),
     ('h', 'Section B: Earth changed or life changed? (ESS2-7.1)'),
     ('p', 'Write E, L, or B for each: ice ages come and go ___; photosynthetic cells spread ___; Pangaea breaks apart ___; land plants spread ___; oxygen builds up in the air ___; the first animals appear ___.'),
     ('p', 'Name one example of each kind from memory. E: ______________  L: ______________  B: ______________'),
     ('h', 'Section C: Which way, and what next? (ESS2-7.2 and 7.3)'),
     ('p', '1. Corals build a reef. Which way did the change go? ______ What happens next to the shore? ______________'),
     ('p', '2. A volcano blocks sunlight for years. Which way? ______ Write a chain of three events that follows. ______________________'),
     ('p', '3. Plants spread on land. Name one thing they change in the air ______________ and one thing in the soil ______________.')],
    [('p', 'A: 1 photosynthesis; 2 ozone layer; 3 mass extinction; 4 banded iron formation; 5 stromatolite; 6 biosphere, atmosphere; 7 feedback; 8 evidence.'),
     ('p', 'B: ice ages B (or E); photosynthetic cells spread L; Pangaea breaks apart E; land plants spread B (L with effects on soil); oxygen builds up B (L→E); first animals L. Examples vary.'),
     ('p', 'C: 1 L→E (reefs change the shore); waves are slowed and the shore erodes less. 2 E→L; sample chain: ash blocks sunlight → plants die → plant-eating animals starve. 3 They take in carbon dioxide / add oxygen; they break rock and add matter to make soil.')]))
items.append(item(9, 'Review packet D to F', 'Review work time', 'Sections for CFAs under mastery; everyone does Section F', 'One per student',
    [('h', 'Section D: Kinds of evidence (ESS2-7.4 and 7.5)'),
     ('p', 'Sort these: a banded iron formation; ancient rock chemistry; stromatolite fossils; a computer model; a story with no data. Write the kind of each (rock, fossil, data, model, story) and rank them strongest to weakest. Why does combining kinds make a claim stronger?'), ('lines', 4),
     ('h', 'Section E: Score it yourself (ESS2-7.4 to 7.6)'),
     ('p', 'Use the four-point scale from Lesson 5. Question: Did life change Earth, or only Earth change life?'),
     ('p', 'Student A: "Life changed Earth because there was a lot of life."  Score: ___ Why? ______________'),
     ('p', 'Student B: "Life changed Earth. Stromatolite fossils show photosynthetic cells lived 3.5 billion years ago, and the rusty banded iron layers about 2.4 billion years old show oxygen reached the ocean. Rust needs oxygen, so living things that make oxygen must have changed the ocean and air. Oxygen then rose to about 15% of the air by 0.5 billion years ago, which let animals evolve. Someone might say volcanoes made the oxygen, but the fossils and layers point to living things."  Score: ___ Why? ______________'),
     ('p', 'Student C: "Oxygen went up, so life changed Earth."  Score: ___ Why? ______________'),
     ('p', 'Rewrite Student C\'s answer so it earns a 4:'), ('lines', 3),
     ('h', 'Section F: Write It (ESS2-7.6)'),
     ('p', 'One paragraph (8 to 10 sentences) arguing that Earth\'s systems and life changed together. Use at least three pieces of evidence from at least two kinds, one loop, and one counterclaim.'), ('lines', 4)],
    [('p', 'D: banded iron formation (rock), ancient rock chemistry (data), stromatolite fossils (fossil), computer model (model), story with no data (story). Sample ranking: chemistry and rock formation and fossils strongest (direct and checkable), model (depends on assumptions), story weakest. Combining kinds is stronger because independent evidence that agrees is harder to explain away.'),
     ('p', 'E: Student A = 1 (a claim with no evidence). Student B = 4 (clear claim, evidence from fossil and rock and data with numbers, reasoning, and a counterclaim). Student C = 2 (a claim and some evidence but little reasoning). Rewrite sample: Life changed Earth. Banded iron formations about 2.4 billion years old (rock) and oxygen data rising from about 0% to 15% by 0.5 billion years ago (data) show oxygen increased. Because stromatolite fossils show oxygen-making cells existed, living things must have caused the rise. Someone might say volcanoes made it, but the fossils point to life.'),
     ('p', 'F: Look for a claim that goes both ways, three pieces of evidence from two kinds, one loop (life changes Earth, then Earth changes life), and a counterclaim answered with evidence.')]))

# ---------- Lessons ----------
L = []


def lesson(n, title, focus, tl, objective, agenda, moves, misc, check, diff, nb, warmup, exit_, materials=None, key_nb=None):
    L.append(dict(n=n, title=title, focus=focus, target_labels=[T[k] for k in tl], objective=objective, agenda=agenda, moves=moves, misc=misc,
                  check=check, diff=diff, nb=nb, warmup=warmup, exit=exit_, materials=materials or [], key_nb=key_nb, tl=tl))


def p2(focus, reading, vocab, warm, ex):
    return dict(focus=focus,
                left=[('Reading: ' + reading, 'Biology: The Living Earth. Annotate: underline new terms, star the main idea.', 1.3, 'lines'),
                      ('Vocabulary', 'Word | my definition | example (' + vocab + ')', 3.0, 'box')],
                right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                       ('Connect it', 'Sketch one example from the reading of Earth changing life or life changing Earth.', 1.8, 'box')],
                warmup=('Warm-up', warm), exit=('Exit ticket', ex))


lesson(1, 'Rusty Stripes', 'What are examples of how Earth has changed and how life has changed?', [1],
       'Students notice how a banded iron formation records change, sort twelve events into Earth, life, or both on a timeline, and preview the unit targets.',
       [('5', 'Warm-up', 'Banded iron formation: what does rust tell you?'), ('5', 'Pre-check', 'Four ungraded questions'), ('15', 'Card sort', 'Sort 12 events; place on the timeline strip'),
        ('10', 'Preview', 'Read the six targets; star the hardest'), ('10', 'Exit ticket', 'CFA ESS2-7.1 in Canvas, then wrap-up')],
       ['Show the banded iron photo and let students wonder before you name it.', 'Do not grade the pre-check; keep it to compare at the end of the unit.', 'Start the Unit CER evidence log together.'],
       ['"Earth is only a few thousand years old."', '"Life only changes; Earth stays the same."'],
       'CFA ESS2-7.1 (below 3 of 4 opens a review).', 'Reteach: sort only cards A to F first. Extend: add three more events of your own to the timeline.',
       dict(left=[('Pre-check', 'About how old is Earth? Name one way Earth has changed. Name one way life has changed. Did living things ever change the air or the rocks?', 1.5, 'lines'),
                  ('Card sort', 'Glue in: Card sort chart and timeline strip', 3.0, 'glue')],
            right=[('Unit CER evidence log', 'Glue in: Unit CER evidence log (or start it in the back of your notebook)', 2.2, 'glue'),
                   ('Preview the unit', 'Star the target you think will be hardest.', 1.2, 'lines')],
            part2=p2('How did Earth and life evolve together?', 'Lesson 8.3 Earth and Life Evolve Together (pp. 226-235)', 'coevolution, extinction, fossil record', 'Skim the headings. What do you predict?', 'One new idea from the reading is ____.')),
       ('Warm-up', 'Iron rusts when it meets oxygen. What does the rust in a banded iron formation tell you about the air or water that touched it long ago? Write two questions.'),
       ('Exit ticket', 'Name one way Earth changed and one way life changed.'), materials=['Banded iron formation photo (slides)'])
lesson(2, 'A Two-Way Street', 'How did Earth change life, and how did life change Earth?', [2],
       'Students sort eight events by direction of change and draw their own cause-and-effect pair.',
       [('4', 'Warm-up', 'Ice sheet and lichen'), ('15', 'Card sort', 'E→L or L→E for eight cards'), ('10', 'Draw your own pair', 'Two labeled diagrams'),
        ('6', 'Reading', 'Find one sentence in Lesson 8.2'), ('10', 'Exit ticket', 'CFA ESS2-7.2 in Canvas')],
       ['Have pairs defend each arrow aloud.', 'Point out that change goes in both directions.'],
       ['"Only Earth changes life."', 'Students mislabel direction by naming the effect, not the cause.'],
       'CFA ESS2-7.2.', 'Reteach: use cards 1, 2, 3 only. Extend: add a third arrow back (a loop).',
       dict(left=[('Sort', 'Glue in: Sorting chart and diagrams', 3.4, 'glue'), ('Find it in the reading', 'Copy one sentence that shows life changing Earth and write the page number. Add one row to your evidence log.', 1.5, 'lines')],
            right=[('Draw your own pair', 'One E→L and one L→E: two boxes joined by an arrow. Under each write "First, ... so ...".', 3.0, 'box'),
                   ('Change goes in ___ directions', '', 0.8, 'lines')],
            part2=p2('How did early life change Earth?', 'Lesson 8.2 Life\'s Early History (pp. 219-225)', 'photosynthesis, stromatolite, oxygen', 'What do you know about early life?', 'Early life changed Earth by ____.')),
       ('Warm-up', 'An ice sheet creeps across a region. What happens to plants and animals? A lichen grows on bare rock for many years. What might happen to the rock?'),
       ('Exit ticket', 'One way Earth changed life: ____. One way life changed Earth: ____.'))
lesson(3, 'The Oxygen Story', 'How can one event in Earth\'s history change life, and how can life change Earth in return?', [3],
       'Students graph the history of oxygen, read the rust record and mass-extinction data, and build a cause-and-effect chain.',
       [('4', 'Warm-up', 'Predict oxygen when the rust formed'), ('12', 'Graph', 'Plot oxygen over time'), ('6', 'Rust record', 'Which came first, oxygen or the layers?'),
        ('8', 'Data', 'Mass extinction table'), ('8', 'Chain', 'Build a chain of five boxes'), ('7', 'Wrap-up', 'Write a "Because ... happened" sentence')],
       ['No CFA today; the CFA for this target is Lesson 4.', 'Connect the graph to the Lesson 1 rock.'],
       ['"Oxygen has always been 21%."', 'Students plot time in the wrong direction.'],
       'Wrap-up sentence with cause, change, and effect.', 'Reteach: plot only the first four points. Extend: explain the 30% peak.',
       dict(left=[('Graph', 'Glue in: Oxygen story: data table and graph grid', 3.4, 'glue'), ('The rust record', 'Which came first: oxygen from living things, or the rust layers?', 1.2, 'lines')],
            right=[('Mass extinctions', 'Glue in: Mass extinction data and the rust record', 2.6, 'glue'), ('Build a chain', 'Glue in: Build a chain', 1.6, 'glue'),
                   ('Wrap-up', 'Because ______ happened, ______ changed, which led to ______.', 0.9, 'lines')]),
       ('Warm-up', 'Rust needs oxygen. What do you predict about oxygen in the air and ocean when the rust stripes formed?'),
       ('Exit ticket', 'Because ____ happened, ____ changed, which led to ____.'), materials=['Graph paper, ruler, pencil'])
lesson(4, 'Three Case Files', 'How do events in Earth\'s history change life, and how does life change Earth in return?', [3],
       'Students read three cases at stations, fill a four-column table, and write about the pattern they share.',
       [('3', 'Warm-up', 'Look back at the oxygen chain'), ('27', 'Stations', 'Three cases, 9 minutes each'), ('6', 'Quick write', 'Three sentences with "because"'), ('9', 'Exit ticket', 'CFA ESS2-7.3 in Canvas')],
       ['Rotate stations on a timer.', 'Require "because" in the quick write.'],
       ['Students record only one direction per case.', 'Students copy the case instead of paraphrasing the effect.'],
       'CFA ESS2-7.3.', 'Reteach: do Case A together. Extend: find a fourth case from Lesson 8.3.',
       dict(left=[('Case files', 'Glue in: Three case files', 4.8, 'glue')],
            right=[('What do all three cases have in common?', '', 1.3, 'lines'), ('Quick write', 'Pick one case. Write 3 sentences with the word because that tell how Earth changed life and how life changed Earth.', 2.2, 'lines')]),
       ('Warm-up', 'Look at your chain from yesterday. Which arrow shows life changing Earth? Which shows Earth changing life? Tell a partner.'),
       ('Exit ticket', 'Choose the case you understand best and describe the loop in one sentence.'))
lesson(5, 'Make the Argument', 'How do I write an argument with a claim, evidence, and reasoning?', [4],
       'Students choose evidence, plan with frames, write an argument paragraph, and peer-check with a four-point scale.',
       [('3', 'Warm-up', 'Agree or disagree with a friend'), ('8', 'Evidence bank', 'Six cards; add three to the log'), ('6', 'Plan', 'Frames'), ('14', 'Write', 'One paragraph of 8 to 10 sentences'),
        ('6', 'Peer check', 'Score and star-and-step'), ('8', 'Exit ticket', 'CFA ESS2-7.4 in Canvas')],
       ['Model one frame sentence aloud.', 'Turn in the paragraph on Canvas: Unit 3.1 CER: Earth and life changed each other.'],
       ['Claim goes only one way.', 'Evidence has no numbers.'],
       'CFA ESS2-7.4.', 'Reteach: use the sentence frames only. Extend: add a second counterclaim.',
       dict(left=[('Evidence bank', 'Glue in: Evidence bank cards you chose (or list E-numbers) and add three rows to your evidence log.', 2.2, 'glue'), ('Plan', 'Glue in: Argument planner and peer-check scale', 3.2, 'glue')],
            right=[('Write your argument', 'One paragraph of 8 to 10 sentences. Use at least three pieces of evidence, include a number, name the kind, use because twice.', 4.0, 'lines'), ('Peer check', 'Score: ___  Star: ___  Step: ___', 0.9, 'lines')]),
       ('Warm-up', 'A friend says, "Earth changed life, but life never changed Earth." Do you agree? One sentence and one reason.'),
       ('Exit ticket', 'One thing my partner suggested that I will fix: ____.'))
lesson(6, 'Evidence Court', 'How do different kinds of evidence work together to make one strong argument?', [5],
       'Students rate the kind and strength of eight pieces of evidence and combine several kinds into one argument.',
       [('3', 'Warm-up', 'One witness or many?'), ('14', 'Sort and rate', 'Eight cards: kind and strength'), ('12', 'Build an argument', 'Three kinds of evidence'), ('8', 'Depth challenge', 'DOK 4 prompts'), ('8', 'Exit ticket', 'CFA ESS2-7.5 in Canvas')],
       ['Define strong evidence as direct, checkable, and agreeing with other kinds.', 'Use the depth challenge for GATE compaction.'],
       ['Students rate by length, not strength.', 'Students rank the story card above data.'],
       'CFA ESS2-7.5.', 'Reteach: rate C1 to C4 only. Extend: pick two depth prompts and write 4 to 5 sentences each.',
       dict(left=[('Sort and rate', 'Glue in: Rating table and argument frames', 4.2, 'glue'), ('Why do different kinds make a claim stronger?', '', 1.0, 'lines')],
            right=[('Build one argument', 'Write the paragraph using the frames.', 3.2, 'lines'), ('Depth challenge (choose two)', 'Different perspectives; Over time; Unanswered questions; Big idea.', 2.4, 'lines')]),
       ('Warm-up', 'Would you believe a story told by only one witness? What would make you trust it more? Write 2 sentences.'),
       ('Exit ticket', 'The strongest piece of evidence in my table is ____ because ____.'))
lesson(7, 'Earth\'s Systems Web', 'How are Earth\'s systems and life connected over time?', [6],
       'Students read about Earth\'s origin, build a web of arrows linking four Earth systems, and begin a sketchnote.',
       [('3', 'Warm-up', 'Four systems and an example in each'), ('12', 'Reading notes', 'Lesson 8.1 two-column chart'), ('20', 'Build the web', 'Link cards and your own links'), ('7', 'Sketchnote', 'Color, picture, text'), ('3', 'Wrap-up', 'Most arrows out and in')],
       ['No CFA today; Lesson 8 holds the CFA for this target.', 'Remind students to star links where life changed a non-living system.'],
       ['Students draw arrows between boxes without labels.', 'Students leave out the biosphere as a cause.'],
       'Web with labeled arrows and starred links.', 'Reteach: build the web with links 1 to 5 only. Extend: add feedback loops.',
       dict(left=[('Warm-up systems', 'Geosphere (rock): ... Hydrosphere (water): ... Atmosphere (air): ... Biosphere (living things): ...', 1.2, 'lines'),
                  ('Systems web', 'Glue in: Earth\'s systems web template and reading chart', 4.2, 'glue')],
            right=[('Sketchnote', 'Make a sketchnote of your web with color, picture, text, and a template (about equal pictures and text).', 4.2, 'box'),
                   ('Which system has the most arrows out? In?', '', 0.9, 'lines')],
            part2=p2('How did Earth form and change?', 'Lesson 8.1 Earth\'s Origin (pp. 206-218)', 'geosphere, hydrosphere, atmosphere, biosphere', 'Skim the headings. What system is each about?', 'One new idea about early Earth is ____.')),
       ('Warm-up', 'Write the four Earth systems and one example in each.'), ('Exit ticket', 'Which system has the most arrows pointing out of it? Which has the most pointing in?'))
lesson(8, 'Argue Together', 'Can I argue from evidence that Earth\'s systems and life changed together over time?', [6],
       'Students use a timeline of eight rows to write an argument that Earth\'s systems and life changed together.',
       [('3', 'Warm-up', 'Pick the arrow that matters most'), ('12', 'The timeline', 'Eight rows; circle a loop'), ('15', 'Write the argument', 'Frames'), ('5', 'Share and fix', 'Read aloud and fix one thing'), ('10', 'Exit ticket', 'CFA ESS2-7.6 in Canvas')],
       ['Check for a claim that goes both ways, three rows with numbers, and because.', 'Collect the paragraph with the notebook photo.'],
       ['Students pick rows from one direction only.', 'Students skip the counterclaim.'],
       'CFA ESS2-7.6.', 'Reteach: choose rows 2 and 3 as a loop, then add one more. Extend: add a row of your own from Lesson 8.1.',
       dict(left=[('The timeline', 'Glue in: The timeline: eight rows', 4.4, 'glue')],
            right=[('Write your argument', 'One paragraph (8 to 10 sentences).', 3.8, 'lines'), ('Share and fix', 'Check: claim both ways, three rows with numbers, because. One thing I fixed: ____', 1.2, 'lines')]),
       ('Warm-up', 'Look at your web from Lesson 7. Pick the arrow you think matters most. Why?'), ('Exit ticket', 'One loop in Earth\'s history is ____.'))
lesson(9, 'Review and Reteach', 'What do I still need to practice for the CSA?', [1, 2, 3, 4, 5, 6],
       'Students check CFA scores, complete review sections for targets under mastery, and finish Vocabulary and Write It.',
       [('5', 'Check scores', 'Open Canvas; plan'), ('20', 'Review sections', 'Sections for CFAs under 4 of 5'), ('13', 'Vocabulary and Write It', 'Sections A and F'), ('7', 'Can you...? check', 'Self-check and CSA preview')],
       ['Pull small groups by target.', 'Everyone does Section A and Section F.'],
       ['Students skip sections they believe they know.', 'Students copy answers from a partner.'],
       'Can you... checklist and review packet.', 'Reteach: pull a group on ESS2-7.4 and 7.5. Extend: enrichment choice board.',
       dict(left=[('My CFA scores', 'List ESS2-7.1 to 7.6. Circle any under 4 of 5 correct (3 of 4 points).', 1.8, 'lines'), ('Review work', 'Glue in: Review packet A to C', 3.8, 'glue')],
            right=[('Review work', 'Glue in: Review packet D to F', 3.8, 'glue'), ('Can you...?', 'Put a check next to each target you are sure of.', 1.6, 'lines')]),
       ('Warm-up', 'List your six CFA scores (ESS2-7.1 to 7.6). Circle any under 4 of 5 correct.'), ('Exit ticket', 'Tomorrow is the CSA. The target I will study tonight is ____.'))
lesson(10, 'CSA', 'Can I show I have met the targets for this unit?', [1, 2, 3, 4, 5, 6],
       'Students show mastery of the six priority targets on the CSA.',
       [('2', 'Directions', 'Before you start'), ('43', 'CSA', 'Unit 3.1 CSA in Canvas (6 matching, 8 multiple choice, 2 written)')],
       ['Clear desks; pencil only.', 'Early finishers read quietly or use the enrichment choice board.', 'After the CSA, students fill in the notebook reflection page.'],
       ['Students rush the written responses.'], 'CSA scores by target.', 'Reassess below-mastery targets after reteach.',
       dict(left=[('What I learned about Earth and life changing together', 'Three things I understand better now.', 2.8, 'lines'), ('The rusty stripes one more time', 'Explain the banded iron formation with Earth and life changing each other.', 3.2, 'lines')], right=[]),
       ('Warm-up', 'Before the CSA, I feel ____ about ____.'), ('Exit ticket', 'The one idea I want to remember from this unit is ____.'))

KEYNB = {
    1: ['Pre-check (ungraded; compare at the end of the unit): Earth is about 4.5 billion years old; examples vary; living things did change air (photosynthesis) and rocks (soil, reefs).',
        'Warm-up: rust needs oxygen, so oxygen reached the water that touched the rock; questions vary.', 'Exit ticket: e.g., Earth changed when oceans formed; life changed when photosynthesis spread.'],
    2: ['Warm-up: ice sheet: plants and animals die or move; lichen: breaks the rock into tiny pieces and makes soil.', 'Find it in the reading: any sentence from pp. 219-225 showing life changing Earth (e.g., cyanobacteria released oxygen).',
        'Exit ticket: Earth changed life: an ice age made animals evolve thick fur. Life changed Earth: lichens made soil.'],
    3: ['Warm-up: there was little or no oxygen when the stripes formed because rust needs oxygen that arrived later.', 'Wrap-up: Because cells began using photosynthesis, the ocean and air changed, which led to the ozone layer and animal life on land.'],
    4: ['Quick write: e.g., Because plants spread on land, soil formed, which let larger plants grow. Because forests buried carbon, carbon dioxide fell, which cooled the climate.', 'Exit ticket: loop sentences vary.'],
    5: ['Warm-up: disagree; life changed Earth by making oxygen.', 'Argument paragraph: see the argument planner key.'],
    6: ['Warm-up: no; more witnesses that agree make a story more trustworthy.', 'Depth challenge: responses vary; look for perspectives, change over time, and honest unanswered questions.'],
    7: ['Warm-up: geosphere (rock), hydrosphere (water), atmosphere (air), biosphere (living things).', 'Wrap-up: biosphere has the most arrows out; atmosphere or biosphere the most in.'],
    8: ['Warm-up: students choose; e.g., the oxygen arrow because it changed everything after it.', 'Argument: see the timeline key.'],
    9: ['Checklist: students mark honestly; answers vary.'], 10: ['Reflection: look for banded iron formations as evidence of life changing Earth and for loops (oxygen, soil, extinction).'],
}
for l in L:
    l['key_nb'] = [('p', t) for t in KEYNB.get(l['n'], [])]

unit = dict(id='3.1', name='Changing Earth, Changing Life', std_short='HS-ESS2-7 Changing Earth, Changing Life',
            std_line='Standard: HS-ESS2-7. Construct an argument based on evidence about the simultaneous coevolution of Earth\'s systems and life on Earth. Targets are labeled ESS2-7.1 to ESS2-7.6.',
            lessons=L, items=sorted(items, key=lambda i: i['lesson']),
            caveats=['Dates and percentages from the geologic record are rounded and are teaching simplifications. Sources are cited on each item. Scientists revise ranges as new evidence arrives.',
                     'The oxygen graph values are a teaching model built from published reconstructions (Lyons et al. 2014; Berner 2009). Estimates of past oxygen vary a lot; the peak near 30% is model-based.',
                     'The "Big Five" extinction percentages are rounded approximations (Barnosky et al. 2011) and different studies give different ranges.',
                     'Evidence cards (E1 to E6, C1 to C8) summarize types of evidence for classroom use; they are not quotations from the cited papers.',
                     'Sorting by E, L or B has more than one defensible answer for several cards; accept reasoned answers.'],
            match=dict(intro='Use this table to check Lesson 5 and Lesson 6 answers: match each piece of evidence to its kind and what it shows.',
                       table=dict(header=['Evidence', 'Kind', 'What it shows'],
                                  rows=[['Banded iron formation', 'Rock', 'Oxygen reached the oceans and rusted iron'], ['Stromatolites', 'Fossil', 'Photosynthetic life existed 3.5 billion years ago'],
                                        ['Ancient rock chemistry (low oxygen before 2.4 billion years ago)', 'Chemical data', 'Oxygen was rare, then rose'], ['Computer model of oxygen rise', 'Model', 'Photosynthetic spread can raise oxygen'],
                                        ['First land plant fossils and ancient soils', 'Fossil and rock', 'Plants changed the land and made soil'], ['Mass extinction record', 'Data', 'Earth events change life'],
                                        ['Reef limestone', 'Rock', 'Living things change coasts'], ['"The air was always the same" story', 'Story', 'No data; weakest evidence']],
                                  cols=[3.2, 1.6, 3.4])))

if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    build_printables(unit, out + '/Unit3.1_Printables.pdf')
    build_notebook(unit, out + '/Unit3.1_Student_Notebook.pdf')
    build_key(unit, out + '/Unit3.1_Printables_Teacher_Key.pdf')
    print('built')
