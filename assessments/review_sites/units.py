"""Content for the Unit 1.1 and Unit 1.2 review sites. Edit here, then run build.py."""

RUBRIC = [
    ("4", "Correct and complete. Uses the key science words. Explains every part of the question and connects the ideas."),
    ("3", "Mostly correct. Connects the ideas but leaves out one piece."),
    ("2", "Partly correct. Names the parts but does not explain how they connect, or is vague."),
    ("1", "Has a major mistake or does not answer the question."),
]

# ---------------------------------------------------------------- Unit 1.1
U11 = dict(
    code="HS-LS1-2",
    out="HS-LS1-2/HS-LS1-2_review_site.html",
    page_title="Unit 1.1 Review Site",
    description="Interactive review for the Unit 1.1 reassessment: levels of organization and how body systems work together.",
    accent="#1f5fbf",
    eyebrow="Unit 1.1 · HS-LS1-2",
    title="From Cells to Organisms",
    lede="Review before your reassessment. Work top to bottom, or jump to the part you missed.",
    footer="Living Earth (Biology) · Unit 1.1 review. Your progress saves in this browser.",
    ideas=[
        dict(t="Living things are built in levels.", d="Cells make tissues. Tissues make organs. Organs make organ systems. Organ systems make an organism. Each level is made of the one before it.",
             eq="cell → tissue → organ → organ system → organism"),
        dict(t="Every system has a main job.", d="Digestive breaks down food. Respiratory takes in oxygen and gets rid of carbon dioxide. Circulatory carries blood to every cell. Nervous sends messages. Muscular moves the body. Skeletal holds up the body and protects organs. Excretory removes wastes."),
        dict(t="Systems work together.", d="No system works alone. A body job almost always needs two or more systems.",
             eq="Respiratory + Circulatory → oxygen reaches cells<br>Digestive + Circulatory → nutrients reach cells<br>Nervous + Muscular → sense and respond<br>Skeletal + Muscular → movement"),
        dict(t="A model shows parts and arrows.", d="Read an arrow as “goes to.” If one part stops working, every part after it is affected."),
        dict(t="To explain, name both parts and connect them.", d="Say what each system does. Then use a word like <b>then</b>, <b>so</b>, or <b>because</b> to show how one leads to the other."),
    ],
    vocab=[
        ("cell", "The smallest unit of a living thing. All living things are made of cells."),
        ("tissue", "A group of the same kind of cells working together."),
        ("organ", "A body part made of different tissues that does one main job, like the heart."),
        ("organ system", "A group of organs that work together to do a big job."),
        ("organism", "A whole living thing."),
        ("stimulus", "Something that causes the body to react, like heat or a loud noise."),
        ("response", "How the body reacts to a stimulus."),
        ("model", "A drawing or diagram that shows how parts of something connect and work."),
    ],
    vocabQuiz=[dict(q="Match each word to its meaning. One meaning will not be used.", tag="Vocabulary",
        pairs=[("tissue", "A group of the same kind of cells working together"),
               ("organ", "A body part made of tissues that does one main job"),
               ("organ system", "Organs that work together to do a big job"),
               ("organism", "A whole living thing"),
               ("response", "How the body reacts to something")],
        extra=["The smallest part of an atom"], why="These five words show up on the reassessment.")],
    practice=[
        dict(q="Which list is in order from smallest to largest?", opts=["organ, cell, tissue, organ system", "cell, tissue, organ, organ system", "tissue, cell, organ system, organ", "cell, organ, tissue, organ system"], a=1,
             why="Cells join to make tissues, tissues make organs, and organs make organ systems.", hint="Start with the smallest unit of life."),
        dict(q="Many muscle cells that look the same and work together form a…", opts=["tissue", "organ", "organ system", "organism"], a=0,
             why="Same kind of cells working together is a tissue.", hint="The cells are all the same type."),
        dict(q="The stomach, small intestine, and liver all work together to break down food. Together they are an…", opts=["organism", "tissue", "organ system", "cell"], a=2,
             why="Several organs doing one big job make an organ system. This one is the digestive system.", hint="More than one organ is working together."),
        dict(q="Which system has the main job of holding up the body and protecting organs like the brain and heart?", opts=["Skeletal", "Nervous", "Digestive", "Respiratory"], a=0,
             why="Bones, like the skull and rib cage, hold you up and protect organs.", hint="Think about what the skull and ribs do."),
        dict(q="The kidneys filter wastes out of the blood. The blood carries those wastes to the kidneys. Which TWO systems work together here?", type="multi",
             opts=["Circulatory", "Excretory", "Skeletal", "Muscular", "Nervous"], a=[0, 1],
             why="The circulatory system carries the wastes, and the excretory system removes them.", hint="One carries, one removes."),
        dict(type="match", q="Match each system to its main job. One job will not be used.",
             pairs=[("Respiratory", "Takes in oxygen and gets rid of carbon dioxide"), ("Digestive", "Breaks down food into nutrients"),
                    ("Circulatory", "Carries blood to every cell"), ("Nervous", "Sends messages between the brain and body"), ("Muscular", "Pulls on bones to move the body")],
             extra=["Fights germs that make you sick"], why="Know each system's one main job."),
        dict(type="match", q="Match each level to an example from the human body. One example will not be used.",
             pairs=[("Cell", "One nerve cell"), ("Tissue", "Nervous tissue (many nerve cells together)"), ("Organ", "The brain"),
                    ("Organ system", "The nervous system (brain, spinal cord, nerves)"), ("Organism", "A whole dog")],
             extra=["A pond with fish and plants"], why="Each level is made of the level before it."),
        dict(q="A cyclist rides up a hill. Her breathing and heart rate both go up. Which TWO systems work together to get more oxygen to her leg muscles?", type="multi",
             opts=["Respiratory", "Circulatory", "Digestive", "Skeletal", "Excretory"], a=[0, 1],
             why="The respiratory system takes in the oxygen. The circulatory system carries it to the muscle cells.", hint="One brings oxygen in, one delivers it."),
        dict(q="Which pair of systems must work together for you to pick up a pencil you see on the floor?", opts=["Nervous and muscular", "Digestive and skeletal", "Respiratory and excretory", "Circulatory and digestive"], a=0,
             why="The nervous system takes in what you see and sends the message. The muscular system moves your arm.", hint="One senses and sends the message. One moves."),
    ],
    model=dict(
        title="Read a model", sub="Models use arrows. Read each arrow as “goes to.”",
        caption="Model: how a runner's brain cells get energy.",
        figure="""<ul class="flow"><li>Food</li><li class="arrow">→</li><li>Stomach and intestines<br><small>digestive system</small></li><li class="arrow">→</li><li>Nutrients go into the blood</li><li class="arrow">→</li><li>Heart and blood vessels<br><small>circulatory system</small></li><li class="arrow">→</li><li>Brain cells</li></ul>""",
        qs=[
            dict(q="According to the model, what does the circulatory system do?", opts=["Breaks down food", "Carries nutrients to the brain cells", "Makes nutrients", "Takes in air"], a=1, why="The arrow goes from the blood to the brain cells, so it carries nutrients there.", hint="Follow the arrow that starts at the heart and blood vessels."),
            dict(q="The heart and blood vessels stop working well. Which result is most likely?", opts=["Food would not be swallowed.", "Brain cells would not get enough nutrients.", "Bones would break.", "The lungs would fill with food."], a=1, why="Every part after the circulatory system is affected. Brain cells come after it.", hint="What comes after the circulatory system in the model?"),
            dict(q="The digestive system cannot break down food. What happens next in the model?", opts=["Nutrients never get into the blood.", "The blood carries extra oxygen.", "The brain sends more messages.", "Nothing changes."], a=0, why="The digestive system makes the nutrients. With no breakdown, there are no nutrients to enter the blood.", hint="Look at the step right after the digestive system."),
            dict(q="This model shows two systems working together. Why does the model need both?", opts=["One system breaks down food and the other carries the nutrients to cells.", "Both systems do the exact same job.", "The second system makes food.", "The first system carries oxygen."], a=0, why="Breaking down food and delivering nutrients are two different jobs. The cells need both to get energy.", hint="Compare the job of each system."),
        ]),
    rubric=RUBRIC,
    write=[
        dict(ctx="A girl sees a ball flying toward her face and ducks. ", q="Explain how the nervous system and the muscular system work together so she can duck. Use the words <b>message</b>, <b>brain</b>, and <b>muscles</b>.",
             frames=["First, the nervous system …", "Then, the muscular system …"],
             check=["I named both systems.", "I said what the nervous system does (eyes see the ball, the brain sends a message).", "I said what the muscular system does (muscles move the body).", "I used a connecting word like <i>then</i> or <i>so</i>."],
             sample="First, the nervous system uses her eyes to see the ball, and her brain sends a message to the muscles in her neck and body. Then, the muscular system gets the message and the muscles pull on bones to move her head down, so she ducks."),
        dict(ctx="A soccer player is running hard in a game and her muscle cells need a lot of oxygen.", q="Explain how the respiratory system and the circulatory system work together to help her muscle cells.",
             frames=["The respiratory system …", "Then the circulatory system …", "This helps her muscles because …"],
             check=["I named both systems.", "I said the respiratory system takes in oxygen.", "I said the circulatory system (blood) carries it to the muscle cells.", "I connected the two systems."],
             sample="The respiratory system takes in oxygen from the air through the lungs. Then the circulatory system moves that oxygen into the blood, and the heart pumps the blood to her muscle cells. This helps her muscles because the cells need oxygen to keep working."),
    ],
    ready=["I can put the levels of organization in order and give an example of each.",
           "I can say the main job of each body system.",
           "I can name two systems that work together and say how.",
           "I can read a model and say what happens if one part stops working.",
           "I can write an explanation that names both systems and connects them."],
)

# ---------------------------------------------------------------- Unit 1.2
CYCLE_SVG = """<svg viewBox="0 0 640 380" role="img" aria-label="Carbon cycle model with four spheres and six lettered arrows">
<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker></defs>
<g style="color:var(--fg)" font-family="system-ui,sans-serif" font-size="15">
<rect x="230" y="12" width="180" height="56" rx="10" fill="var(--accent-soft)" stroke="var(--line)"/><text x="320" y="46" text-anchor="middle" font-weight="700" fill="var(--fg)">Atmosphere (CO₂)</text>
<rect x="30" y="160" width="180" height="56" rx="10" fill="var(--good-soft)" stroke="var(--line)"/><text x="120" y="193" text-anchor="middle" font-weight="700" fill="var(--fg)">Biosphere</text>
<rect x="430" y="160" width="180" height="56" rx="10" fill="var(--accent-soft)" stroke="var(--line)"/><text x="520" y="193" text-anchor="middle" font-weight="700" fill="var(--fg)">Hydrosphere</text>
<rect x="230" y="310" width="180" height="56" rx="10" fill="var(--warn-soft)" stroke="var(--line)"/><text x="320" y="335" text-anchor="middle" font-weight="700" fill="var(--fg)">Geosphere</text><text x="320" y="353" text-anchor="middle" font-size="12" fill="var(--muted)">rock, soil, coal, oil</text>
<g stroke="currentColor" stroke-width="2.5" fill="none" marker-end="url(#ah)">
<path d="M250 70 C200 95 160 120 140 158"/>
<path d="M90 158 C100 120 150 80 228 52"/>
<path d="M390 70 C440 95 480 120 500 158"/>
<path d="M428 188 L214 188"/>
<path d="M110 218 C110 290 160 332 228 336"/>
<path d="M320 308 L320 70"/>
</g>
<g font-weight="800" font-size="16" fill="var(--accent-ink)">
<circle cx="188" cy="112" r="14" fill="var(--accent)"/><text x="188" y="118" text-anchor="middle">A</text>
<circle cx="116" cy="106" r="14" fill="var(--accent)"/><text x="116" y="112" text-anchor="middle">B</text>
<circle cx="452" cy="112" r="14" fill="var(--accent)"/><text x="452" y="118" text-anchor="middle">C</text>
<circle cx="370" cy="188" r="14" fill="var(--accent)"/><text x="370" y="194" text-anchor="middle">D</text>
<circle cx="112" cy="290" r="14" fill="var(--accent)"/><text x="112" y="296" text-anchor="middle">E</text>
<circle cx="320" cy="250" r="14" fill="var(--accent)"/><text x="320" y="256" text-anchor="middle">F</text>
</g></g></svg>"""

U12 = dict(
    code="HS-LS2-5",
    out="HS-LS2-5/HS-LS2-5_review_site.html",
    page_title="Unit 1.2 Review Site",
    description="Interactive review for the Unit 1.2 reassessment: photosynthesis, cellular respiration, and the carbon cycle.",
    accent="#1f7a4d",
    eyebrow="Unit 1.2 · HS-LS2-5",
    title="Cell Energy & Carbon",
    lede="Review before your reassessment. Work top to bottom, or jump to the part you missed.",
    footer="Living Earth (Biology) · Unit 1.2 review. Your progress saves in this browser.",
    ideas=[
        dict(t="Photosynthesis moves carbon into living things.", d="Plants and algae take in carbon dioxide and water. They use light energy to build sugar (glucose) and release oxygen.",
             eq="CO₂ + H₂O + light energy → glucose + O₂"),
        dict(t="Cellular respiration releases it again.", d="Cells break down glucose with oxygen to get usable energy (ATP). Carbon dioxide and water are given off. Plants, animals, and decomposers all do this.",
             eq="glucose + O₂ → CO₂ + H₂O + usable energy"),
        dict(t="Plants do both processes.", d="Plants do photosynthesis when there is light, and cellular respiration all the time. In sunlight, photosynthesis is usually faster, so a plant takes in more CO₂ than it gives off."),
        dict(t="Carbon moves between four spheres.", d="<b>Atmosphere</b> (air), <b>biosphere</b> (living things), <b>hydrosphere</b> (water), <b>geosphere</b> (rock, soil, fossil fuels). Photosynthesis, respiration, decomposition, burning (combustion), and dissolving in water move it."),
        dict(t="Matter cycles. Energy flows.", d="The same carbon atoms are used again and again. Energy comes in as sunlight, is used or lost as heat, and is not recycled. Atoms are never created or destroyed. They are rearranged."),
        dict(t="In a model, an arrow shows carbon moving.", d="Ask: where does the arrow start, where does it end, and what process moves the carbon?"),
    ],
    vocab=[
        ("atmosphere", "The air around Earth. Carbon is there as carbon dioxide gas."),
        ("biosphere", "All the living things on Earth."),
        ("hydrosphere", "All the water on Earth: oceans, lakes, rivers, ice."),
        ("geosphere", "The solid parts of Earth: rock, soil, and fossil fuels."),
        ("photosynthesis", "Plants use sunlight to turn carbon dioxide and water into sugar and oxygen."),
        ("cellular respiration", "Cells break down sugar with oxygen to get energy, and give off carbon dioxide."),
        ("combustion", "Burning. Burning wood or fossil fuels gives off carbon dioxide."),
        ("decomposer", "Fungi and bacteria that break down dead things and return carbon to air and soil."),
        ("fossil fuel", "Coal, oil, or gas made from living things that died a very long time ago."),
        ("carbon cycle", "The path carbon takes as it moves between air, water, living things, and rock."),
        ("glucose", "The sugar plants make. Cells break it down for energy."),
        ("ATP", "The form of usable energy that cells make and use."),
    ],
    vocabQuiz=[dict(q="Match each word to its meaning. Two meanings will not be used.", tag="Vocabulary",
        pairs=[("Atmosphere", "The air around Earth"), ("Biosphere", "All living things on Earth"), ("Hydrosphere", "All the water on Earth"),
               ("Geosphere", "Rock, soil, and fossil fuels"), ("Photosynthesis", "Plants use sunlight to make sugar from CO₂ and water"),
               ("Cellular respiration", "Cells break down sugar for energy and give off CO₂"), ("Combustion", "Burning something and giving off CO₂"),
               ("Carbon cycle", "The path carbon takes through Earth's spheres")],
        extra=["Liquid water changes into a gas", "The part of a plant that takes in water"], why="All eight of these words matter on the reassessment.")],
    practice=[
        dict(q="A wheat field grows fast in early summer. Which change would a carbon cycle model show?", opts=["More carbon moves from the wheat to the air.", "More carbon moves from the air into the wheat.", "Carbon stops moving.", "More carbon moves from the wheat into rock."], a=1,
             why="Fast growth means more photosynthesis, which pulls carbon from the air into the plants.", hint="Growing plants are building sugar."),
        dict(q="A campfire burns a pile of logs. What happens to the carbon in the wood?", opts=["It is destroyed.", "It turns into energy and leaves Earth.", "It goes into the air as carbon dioxide.", "It stays in the ash only."], a=2,
             why="Burning is combustion. It releases carbon as CO₂. Atoms are not destroyed.", hint="Think about what burning gives off."),
        dict(q="Which statement about plants is correct?", opts=["Plants only do photosynthesis.", "Plants only do cellular respiration at night.", "Plants do both photosynthesis and cellular respiration.", "Plants never give off carbon dioxide."], a=2,
             why="Plant cells need energy too, so they do cellular respiration all the time.", hint="Do plant cells need energy?"),
        dict(q="Carbon dioxide from the air dissolves in the ocean. Which two spheres are connected?", opts=["Atmosphere and hydrosphere", "Geosphere and biosphere", "Biosphere and atmosphere", "Hydrosphere and geosphere"], a=0,
             why="CO₂ gas moves from the air (atmosphere) into water (hydrosphere).", hint="Where was the CO₂ before, and where is it after?"),
        dict(q="Coal was made from plants that died millions of years ago. In which sphere is coal stored?", opts=["Atmosphere", "Biosphere", "Hydrosphere", "Geosphere"], a=3,
             why="Coal is a solid fossil fuel in the ground, so it is part of the geosphere.", hint="It is a solid in the ground."),
        dict(q="Which statement compares carbon and energy correctly?", opts=["Carbon cycles over and over, but energy flows through and is lost as heat.", "Energy cycles and carbon is used up.", "Both carbon and energy are used up.", "Both carbon and energy are recycled in a loop."], a=0,
             why="Matter (carbon atoms) is reused. Energy enters as light and leaves as heat.", hint="One is matter and one is energy."),
        dict(q="A pond fills with leaves in the fall. Bacteria slowly break the leaves down. Where does most of the carbon go?", opts=["It disappears.", "It goes into the air and water as CO₂ and into the bacteria.", "It becomes sunlight.", "It all stays in the leaves."], a=1,
             why="Decomposers do cellular respiration on the leaves. They give off CO₂ and use some carbon to build their own bodies.", hint="Decomposers break down dead matter."),
        dict(q="Which TWO processes ADD carbon dioxide to the atmosphere?", type="multi",
             opts=["Photosynthesis", "Cellular respiration", "Combustion of gasoline", "Carbon dioxide dissolving in the ocean", "Plants growing"], a=[1, 2],
             why="Respiration and burning release CO₂. Photosynthesis and ocean uptake remove it.", hint="Which two give off CO₂?"),
        dict(type="match", q="Match each photosynthesis or respiration idea to its description. Each is different.",
             pairs=[("What photosynthesis takes in", "CO₂, water, and light energy"), ("What photosynthesis makes", "Sugar is built and O₂ is released"),
                    ("What cellular respiration takes in", "Sugar and O₂ are broken down"), ("What cellular respiration gives off", "CO₂, water, and usable energy")],
             extra=["Only light energy"], why="They are close to opposites. The outputs of one are the inputs of the other."),
        dict(type="match", q="Match each sentence to the two spheres the carbon moves between. Two choices will not be used.",
             pairs=[("A rabbit eats clover.", "biosphere to biosphere"), ("A kelp forest takes in CO₂ dissolved in seawater.", "hydrosphere to biosphere"),
                    ("A power plant burns coal.", "geosphere to atmosphere"), ("CO₂ from the air dissolves into a lake.", "atmosphere to hydrosphere")],
             extra=["atmosphere to geosphere", "biosphere to hydrosphere"], why="Say where the carbon starts and where it ends up."),
    ],
    model=dict(
        title="Read the carbon cycle model", sub="Each lettered arrow shows carbon moving. Use the arrow's start and end to decide the process.",
        caption="Carbon cycle model. Arrows show carbon moving between spheres. Read the start and the end of each arrow.",
        figure=CYCLE_SVG,
        qs=[
            dict(type="match", q="Match each arrow to what is happening. Two will not be used.", pairs=[("Arrow A", "Plants take in CO₂ by photosynthesis"), ("Arrow B", "Cells give off CO₂ by cellular respiration"), ("Arrow C", "CO₂ gas dissolves in the ocean"), ("Arrow F", "A power plant burns coal")],
                 extra=["Rain falls on a forest", "Ice melts into a river"], why="Check where each arrow starts and ends. A ends in the biosphere, B starts there, C ends in the hydrosphere, F starts in the geosphere."),
            dict(q="Cars burn much more gasoline. Which arrow gets bigger?", opts=["A", "B", "C", "F"], a=3,
                 why="Gasoline comes from fossil fuels in the geosphere. Burning it sends CO₂ to the atmosphere (arrow F).", hint="Where does gasoline come from, and where does the CO₂ go?"),
            dict(q="A large algae bloom grows in a lake and takes in dissolved CO₂. Which arrow shows this?", opts=["D", "B", "C", "E"], a=0,
                 why="Algae live in water and are living things. Carbon moves from the hydrosphere to the biosphere (arrow D).", hint="Start: water. End: living things."),
            dict(q="Over millions of years, buried dead organisms become coal and oil. Which arrow shows carbon moving into the geosphere?", opts=["E", "A", "F", "C"], a=0,
                 why="Arrow E goes from living things to the geosphere. Arrow F goes the other way.", hint="Look for the arrow that ENDS at the geosphere."),
            dict(q="A student says, “Carbon atoms that leave the air in arrow A are gone forever.” What does the model show instead?", opts=["Arrows B and F return carbon to the air, so carbon cycles.", "Nothing in the model returns carbon to the air.", "The carbon becomes energy.", "The carbon is destroyed by plants."], a=0,
                 why="The cycle is a loop. Carbon goes into living things and comes back out."),
        ]),
    rubric=RUBRIC,
    write=[
        dict(ctx="A grass field is measured each day. At noon in summer the CO₂ in the air just above the field drops. At night it rises.",
             q="Explain what causes the CO₂ to drop at noon and rise at night. Use <b>photosynthesis</b> and <b>cellular respiration</b>.",
             frames=["During the day, the grass …", "At night, the grass …", "The carbon atoms …"],
             check=["I said the grass does photosynthesis in light and takes CO₂ from the air.", "I said the grass also does cellular respiration and gives off CO₂.", "I explained why the amount rises at night (no light, so only respiration).", "I said where the carbon goes or comes from."],
             sample="During the day, the grass uses light energy to do photosynthesis. It takes CO₂ from the air and builds sugar, so the CO₂ drops. The grass also does cellular respiration all the time, but photosynthesis is faster in sunlight. At night there is no light, so photosynthesis stops. Respiration keeps going and gives off CO₂, so the CO₂ rises. The carbon atoms are not destroyed. They move from the air into the grass's sugar and back to the air."),
        dict(ctx="A student says: “Sunlight energy goes around in a cycle just like carbon does.”", q="Is the student correct? Revise the statement so it is correct. Use the words <b>matter</b>, <b>energy</b>, and <b>heat</b>.",
             frames=["The student is …", "Carbon (matter) …", "Energy …"],
             check=["I said the student is not correct.", "I said carbon, which is matter, cycles and is reused.", "I said energy flows through and does not cycle.", "I said energy leaves as heat."],
             sample="The student is not correct. Carbon is matter, so the same atoms cycle between the air, living things, water, and rock. Energy flows instead. It enters as sunlight, plants store some of it in sugar, and cells use it. Most of it leaves as heat, and that heat does not go back into the cycle."),
    ],
    ready=["I can write what goes in and what comes out of photosynthesis and cellular respiration.",
           "I can explain that plants do both processes.",
           "I can name the four spheres and say where carbon moves between them.",
           "I can read an arrow in a carbon cycle model and name the process.",
           "I can explain why matter cycles but energy flows.",
           "I can explain a result using photosynthesis and respiration together."],
)


# ---------------------------------------------------------------- Unit 0
BAR_SVG = """<svg viewBox="0 0 520 250" role="img" aria-label="Bar graph of bean plant height after 14 days: sunny window 15 cm, closet 4 cm">
<g font-family="system-ui,sans-serif" font-size="14" fill="var(--fg)">
<line x1="70" y1="20" x2="70" y2="200" stroke="var(--muted)"/><line x1="70" y1="200" x2="500" y2="200" stroke="var(--muted)"/>
<g stroke="var(--line)"><line x1="70" y1="20" x2="500" y2="20"/><line x1="70" y1="65" x2="500" y2="65"/><line x1="70" y1="110" x2="500" y2="110"/><line x1="70" y1="155" x2="500" y2="155"/></g>
<g text-anchor="end" fill="var(--muted)"><text x="62" y="205">0</text><text x="62" y="160">5</text><text x="62" y="115">10</text><text x="62" y="70">15</text><text x="62" y="25">20</text></g>
<rect x="130" y="65" width="110" height="135" fill="var(--good)"/><rect x="330" y="164" width="110" height="36" fill="var(--accent)"/>
<text x="185" y="57" text-anchor="middle" font-weight="700">15 cm</text><text x="385" y="156" text-anchor="middle" font-weight="700">4 cm</text>
<text x="185" y="224" text-anchor="middle">Sunny window</text><text x="385" y="224" text-anchor="middle">Dark closet</text>
<text x="18" y="115" transform="rotate(-90 18 115)" text-anchor="middle" fill="var(--muted)">Height after 14 days (cm)</text></g></svg>"""

CER_RUBRIC = [
    ("4 Mastery", "Clear claim, relevant evidence with numbers, and strong reasoning that explains WHY using biology words."),
    ("3 Proficient", "Clear claim and evidence that supports it. Reasoning is weak or missing one piece."),
    ("2 Developing", "Claim and some data, but the data is not used to prove the claim."),
    ("1 Emerging", "Some vocabulary or ideas, but the claim or evidence is missing."),
]

U0 = dict(
    code="BOOTCAMP",
    out="Bootcamp/Bootcamp_review_site.html",
    page_title="Bootcamp Review Site",
    description="Interactive review for the Bootcamp skills assessment: scientific questions, living things, CER, and sketchnotes.",
    accent="#b4501e",
    eyebrow="Unit 0 · Bootcamp",
    title="Science Skills Bootcamp",
    lede="Review before your reassessment. Work top to bottom, or jump to the part you missed.",
    footer="Living Earth (Biology) · Bootcamp review. Your progress saves in this browser.",
    ideas=[
        dict(t="A scientific question can be tested.", d="It asks about something you can measure or observe, and it names what changes and what you measure. “Which is best?” and “Why is it cute?” are opinions.",
             eq="What happens to <u>plant height</u> when <u>sunlight</u> is reduced?"),
        dict(t="All living things share characteristics.", d="They are made of cells, use energy, grow and develop, respond to their environment, reproduce, and keep a stable inside (homeostasis). Nonliving things like rocks and puddles do not do these things."),
        dict(t="CER is how scientists make an argument.", d="<b>Claim</b>: the answer to the question. <b>Evidence</b>: data from the investigation, with numbers. <b>Reasoning</b>: explain WHY the evidence supports the claim, using biology.",
             eq="Claim → Evidence → Reasoning"),
        dict(t="Sketchnotes have four elements.", d="<b>Color, Picture, Text, Template.</b> Follow the <b>50/50 rule</b>: about equal amounts of pictures and text."),
        dict(t="Focused notes show you are thinking.", d="Highlight the important words. Write questions about the notes. Write a summary in your own words. Do not copy without thinking about the meaning."),
    ],
    vocab=[
        ("claim", "A statement that answers the question."),
        ("evidence", "Data or observations from the investigation that support the claim."),
        ("reasoning", "The explanation of WHY the evidence supports the claim, using science ideas."),
        ("variable", "Something that can change in an experiment."),
        ("cell", "The basic unit of all living things."),
        ("organism", "A whole living thing."),
        ("response", "How an organism reacts to a change in its environment."),
        ("sketchnote", "Notes that combine pictures, text, color, and a template."),
    ],
    vocabQuiz=[dict(q="Match each word to its meaning. One meaning will not be used.", tag="Vocabulary",
        pairs=[("Claim", "A statement that answers the question"), ("Evidence", "Data from the investigation that supports the claim"),
               ("Reasoning", "Explains WHY the evidence supports the claim"), ("Organism", "A whole living thing"), ("Sketchnote", "Notes with pictures, text, color, and a template")],
        extra=["A guess with no data"], why="These words appear in the CER and notes questions.")],
    practice=[
        dict(q="Which question is the BEST scientific question?", opts=["Which pet is the cutest?", "How does the amount of water change how fast a bean seed sprouts?", "Why is summer the best season?", "Is chocolate better than vanilla?"], a=1,
             why="It can be tested. You can change the water and measure how fast the seed sprouts.", hint="Which one can you test by measuring?"),
        dict(q="Which characteristic is shared by ALL living things?", opts=["They have legs.", "They live on land.", "They use energy.", "They are green."], a=2,
             why="All living things use energy. Many do not have legs, live in water, or are green.", hint="Think about what a mushroom, a fish, and a person all have in common."),
        dict(q="Which example BEST shows an organism responding to its environment?", opts=["A snowman melting", "A lizard moving into the shade when it gets hot", "A river flowing downhill", "A car rusting"], a=1,
             why="The lizard is a living thing reacting to a change in its surroundings.", hint="Look for a living thing that reacts."),
        dict(q="Which TWO things are alive or show a characteristic of life?", type="multi", opts=["A seed sprouting into a seedling", "A rock rolling down a hill", "A bird building a nest and laying eggs", "A candle flame burning", "A cloud moving"], a=[0, 2],
             why="Growing and reproducing are characteristics of life. Fire and clouds move or change, but they are not made of cells.", hint="Look for growing, reproducing, and being made of cells."),
        dict(q="According to the Sketchnote Bootcamp, what are the FOUR essential elements of sketchnoting?", opts=["Color, Picture, Text, Template", "Reading, Writing, Testing, Memorizing", "Notes, Homework, Labs, Quizzes", "Highlighting, Typing, Coloring, Copying"], a=0,
             why="Color, Picture, Text, Template."),
        dict(q="The 50/50 rule of sketchnoting means your notes should have…", opts=["Half the page blank", "About equal amounts of pictures and text", "50 words and 50 pictures", "Only pictures"], a=1,
             why="Balance pictures and text. Pictures help you remember. Text holds the details."),
        dict(q="Which action is part of focused note-taking?", opts=["Copying every word from the board", "Highlighting key words and writing a question about the notes", "Using one color so it looks neat", "Skipping the confusing parts"], a=1,
             why="Focused notes show you are thinking: highlight, question, and summarize."),
        dict(type="match", q="Match each part of a CER to its job. One job will not be used.",
             pairs=[("Claim", "Answers the question"), ("Evidence", "Uses data and numbers from the investigation"), ("Reasoning", "Explains why the evidence supports the claim")],
             extra=["Gives your opinion"], why="Claim answers, evidence shows, reasoning explains."),
        dict(type="match", q="Match each characteristic of life to an example. One example will not be used.",
             pairs=[("Made of cells", "Skin from a frog under a microscope shows many tiny units"), ("Uses energy", "A fox eats a mouse and runs"), ("Grows and develops", "A tadpole changes into a frog"), ("Reproduces", "A hen lays eggs that hatch into chicks")],
             extra=["A rock is warmed by the sun"], why="Each example matches one characteristic of life."),
    ],
    model=dict(
        title="Read the data", sub="A CER uses numbers from the data as evidence. Use the graph for these questions.",
        caption="Bean plants grown for 14 days. Same type of plant, same soil, same water. Only the light changed.",
        figure=BAR_SVG,
        qs=[
            dict(q="Which sentence is the best CLAIM?", opts=["Bean plants grew taller in the sunny window than in the dark closet.", "The bar is green.", "I like the sunny window.", "Plants are alive."], a=0, why="A claim answers the question: which condition helped growth?"),
            dict(q="Which sentence is the best EVIDENCE?", opts=["Plants like sunlight.", "The plant in the sunny window grew 15 cm and the plant in the closet grew 4 cm.", "The graph looks good.", "Sunlight is important."], a=1, why="Evidence uses specific numbers from the data."),
            dict(q="Which sentence is the best REASONING?", opts=["The plant grew 15 cm.", "Sunlight is yellow.", "Plants use light energy in photosynthesis to make sugar they need to grow, so more light means more growth.", "The closet is dark."], a=2, why="Reasoning explains WHY using science. Here it connects light to photosynthesis and growth."),
            dict(q="Why must the plants have the same soil and the same amount of water?", opts=["So the only thing that changes is the light.", "So the plants look the same.", "So they grow the same height.", "It does not matter."], a=0, why="If other things changed too, you could not tell what caused the difference."),
        ]),
    rubric=CER_RUBRIC,
    write=[
        dict(ctx="Two groups of radish seeds were planted. Group A was watered every day and grew 9 cm in 10 days. Group B was watered once and grew 2 cm.",
             q="Write a CER. <b>Claim:</b> Which condition helped radishes grow better? <b>Evidence:</b> Use the data. <b>Reasoning:</b> Explain WHY, using biology.",
             frames=["My claim is that …", "The evidence is that …", "This supports my claim because …"],
             check=["My claim answers the question.", "My evidence uses numbers (9 cm and 2 cm).", "My reasoning explains WHY (plants need water for photosynthesis and growth).", "I used biology words."],
             sample="Radishes grew better when they were watered every day. In the investigation, the radishes watered daily grew 9 cm, but the radishes watered once grew only 2 cm. This supports the claim because plants need water for photosynthesis, which makes the sugar they use for energy and to grow. With more water, the plants could make more food, so they grew taller."),
        dict(ctx="A class investigated whether plants grow better with sunlight or without. Plant A had sunlight and grew 12 cm. Plant B had no sunlight and grew 3 cm.",
             q="Write a CER response. Your reasoning must explain why the evidence supports your claim.",
             frames=["Claim: …", "Evidence: …", "Reasoning: …"],
             check=["Clear claim.", "Both numbers (12 cm and 3 cm) are in my evidence.", "My reasoning explains WHY using photosynthesis or energy.", "I used accurate vocabulary."],
             sample="Claim: Plants grow better with sunlight. Evidence: Plant A received sunlight and grew 12 cm, while Plant B received no sunlight and grew only 3 cm. Reasoning: Plants use light energy during photosynthesis to make sugar. Plant A could make more sugar, which gave it the energy and matter to grow. Plant B could not make enough food, so it grew much less."),
    ],
    ready=["I can pick a question that can be tested.",
           "I can name characteristics shared by all living things and give an example.",
           "I can write a Claim, Evidence, and Reasoning that use numbers and biology.",
           "I can name the four elements of sketchnotes and the 50/50 rule.",
           "I can say what focused note-taking looks like."],
)

UNITS = [U0, U11, U12]
