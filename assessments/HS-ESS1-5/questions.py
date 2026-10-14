"""Question bank for the HS-ESS1-5 CSA: Age of the Earth (unit 3.1).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-ESS1-5`.
"""

TITLE = "HS-ESS1-5 Assessment: Age of the Earth"
STANDARD = "HS-ESS1-5"
QUIZ_ID = "hs_ess1_5_age_of_the_earth"
FILE_PREFIX = "HS-ESS1-5"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [1, 0, 2, 3, 1, 2, 0, 3]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-ESS1-5</strong></p>"
    "<p>Evaluate evidence of the past and current movements of continental and oceanic crust and "
    "the theory of plate tectonics to explain the ages of crustal rocks.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Tectonic plate", "A large, rigid piece of Earth's outer layer that slowly moves over the mantle"),
        ("Mid-ocean ridge", "An underwater mountain chain where new ocean crust forms as plates move apart"),
        ("Subduction zone", "A place where one plate sinks beneath another and the sinking crust is recycled into the mantle"),
        ("Divergent boundary", "A plate boundary where two plates move away from each other"),
        ("Convergent boundary", "A plate boundary where two plates move toward each other"),
        ("Transform boundary", "A plate boundary where two plates slide past each other"),
    ],
    "distractors": [
        "The hot, dense layer of Earth between the crust and the core",
        "A rock formed when pieces of older rock are pressed together in layers",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Which boundary is it?",
        "dok": 2,
        "prompt": (
            "<p>Geologists find an underwater mountain chain in the middle of an ocean. Hot, molten rock rises "
            "along its center and hardens to form new crust. Earthquakes there are shallow, and the plates on "
            "either side move apart.</p>"
            "<p>Which type of boundary and process does this describe?</p>"
        ),
        "choices": [
            "A divergent boundary, where new ocean crust forms as plates move apart",
            "A convergent boundary, where ocean crust is destroyed",
            "A transform boundary, where plates slide past each other without making or destroying crust",
            "A hot spot, where continents are created",
        ],
        "answer": 0,
        "feedback": "New crust forming where plates move apart describes a divergent boundary and a mid-ocean ridge.",
    },
    {
        "title": "MC 2 - Where ocean crust goes",
        "dok": 2,
        "prompt": (
            "<p>Along the coast of South America, a dense ocean plate meets a continental plate. The ocean plate bends "
            "and slides down beneath the continent. Deep earthquakes occur along the sinking plate, and volcanoes "
            "form on the continent.</p>"
            "<p>Which statement <strong>best</strong> describes what happens to the ocean crust at this boundary?</p>"
        ),
        "choices": [
            "It sinks into the mantle at a subduction zone and is recycled, so ocean crust is destroyed here.",
            "It is pushed up and becomes the oldest part of the continent.",
            "It is created here as new seafloor.",
            "It stays on the surface and gets thicker forever.",
        ],
        "answer": 0,
        "feedback": "At a subduction zone, dense ocean crust sinks into the mantle. Ocean crust is created at ridges and destroyed at subduction zones.",
    },
    {
        "title": "MC 3 - Reading the seafloor ages",
        "dok": 2,
        "prompt": (
            "<p>Scientists drill into the seafloor at several distances from the Mid-Atlantic Ridge and date the rock:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Distance from the ridge (km)</th><th>0</th><th>250</th><th>500</th><th>1,000</th><th>2,000</th></tr>"
            "<tr><td>Age of seafloor rock (millions of years)</td><td>0</td><td>12</td><td>25</td><td>50</td><td>100</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> describes the pattern and what it shows?</p>"
        ),
        "choices": [
            "Rock gets older farther from the ridge, which shows new crust forms at the ridge and spreads outward.",
            "Rock gets younger farther from the ridge, which shows crust is destroyed at the ridge.",
            "The rock is the same age everywhere, which shows the seafloor does not move.",
            "Rock ages are random, which shows no pattern.",
        ],
        "answer": 0,
        "feedback": "Age rises steadily with distance from the ridge, as expected if new crust forms at the ridge and moves away.",
    },
    {
        "title": "MC 4 - Ages across a continent",
        "dok": 2,
        "prompt": (
            "<p>A map of rock ages across the center of North America gives these values for the continental crust:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Distance from the ancient core (km)</th><th>0</th><th>500</th><th>1,000</th><th>1,500</th><th>2,000</th></tr>"
            "<tr><td>Age of crust (millions of years)</td><td>3,500</td><td>2,700</td><td>1,800</td><td>1,000</td><td>400</td></tr>"
            "</table>"
            "<p>Which explanation <strong>best</strong> fits this pattern?</p>"
        ),
        "choices": [
            "The continent started as an ancient core and grew outward as plate interactions added newer crust around its edges.",
            "The continent formed all at once, so all of it should be the same age.",
            "The ancient core formed last, after the outer parts were already there.",
            "The age pattern is caused by erosion removing the oldest rock at the edges.",
        ],
        "answer": 0,
        "feedback": "The crust is oldest in the core and younger toward the edges, consistent with crust added over time by past plate interactions.",
    },
    {
        "title": "MC 5 - Young ocean, old continents",
        "dok": 3,
        "prompt": (
            "<p>The oldest ocean crust is about 180 million years old. The oldest continental rocks are about "
            "4,000 million years old. Earth is about 4,600 million years old.</p>"
            "<p>Which explanation using plate tectonics <strong>best</strong> accounts for this difference?</p>"
        ),
        "choices": [
            "Dense ocean crust is created at ridges and sinks back into the mantle at subduction zones, so it is always being recycled; less dense continental crust floats and is not recycled as easily, so old pieces can survive.",
            "Ocean crust formed later than the continents and has never been recycled.",
            "Continents are made of the same material as ocean crust, so they are recycled at the same rate.",
            "Ocean crust is destroyed by erosion, which does not affect continents.",
        ],
        "answer": 0,
        "feedback": "Ocean crust is made and destroyed continually. Continental crust is less dense and tends to stay at the surface, so some of it is much older.",
    },
    {
        "title": "MC 6 - Strength of evidence",
        "dok": 3,
        "prompt": (
            "<p>Two students argue that the continents have moved. </p>"
            "<ul>"
            "<li><strong>Student 1:</strong> &ldquo;The east coast of South America and the west coast of Africa have shapes that fit together.&rdquo;</li>"
            "<li><strong>Student 2:</strong> &ldquo;GPS stations measure plates moving a few centimeters a year today; seafloor rock is older farther from ridges; and matching fossils and rocks are found on continents now far apart.&rdquo;</li>"
            "</ul>"
            "<p>Which statement <strong>best</strong> evaluates the evidence?</p>"
        ),
        "choices": [
            "Student 2's argument is stronger because it uses several independent lines of evidence, including present-day measurements and evidence from the past.",
            "Student 1's argument is stronger because shapes fitting together is the only evidence needed.",
            "Both arguments are equally strong because each uses at least one piece of evidence.",
            "Neither argument is useful because evidence cannot show how Earth's crust moved.",
        ],
        "answer": 0,
        "feedback": "Strong arguments use several independent kinds of evidence that all point to the same conclusion. Student 2 uses current plate motion, seafloor ages, and fossils and rocks.",
    },
    {
        "title": "MC 7 - What a fixed crust would predict",
        "dok": 3,
        "prompt": (
            "<p>An older idea said Earth's crust has always been fixed in place. Scientists compare what the idea of "
            "a fixed crust would predict with what plate tectonics predicts.</p>"
            "<p>Which observation is explained <strong>well by plate tectonics but not by a fixed crust</strong>?</p>"
        ),
        "choices": [
            "Seafloor rock gets steadily older in both directions away from a mid-ocean ridge.",
            "Rocks exist on Earth that are billions of years old.",
            "Earth's crust is made of rock.",
            "Some mountains are taller than others.",
        ],
        "answer": 0,
        "feedback": "A symmetrical age pattern on both sides of a ridge is exactly what spreading crust predicts. A fixed crust gives no reason for it.",
    },
    {
        "title": "MC 8 - Predicting an age",
        "dok": 2,
        "prompt": (
            "<p>The seafloor spreads away from a ridge at a steady rate of 2 centimeters per year. "
            "(1 kilometer = 100,000 centimeters.)</p>"
            "<p>About how old should seafloor rock be at a spot 1,000 kilometers from the ridge?</p>"
        ),
        "choices": [
            "About 50 million years",
            "About 5 million years",
            "About 500 million years",
            "About 2,000 years",
        ],
        "answer": 0,
        "feedback": "1,000 km = 100,000,000 cm. At 2 cm per year, that takes 50,000,000 years, or 50 million years.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Is the crust moving?",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A student claims that Earth's crust has not moved and will not move. Use this evidence:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Evidence</th><th>What was found</th></tr>"
            "<tr><td>A. GPS stations</td><td>Stations on different plates are moving a few centimeters per year, in steady directions.</td></tr>"
            "<tr><td>B. Seafloor ages</td><td>Ocean rock is 0 million years old at the Mid-Atlantic Ridge and 100 million years old 2,000 km away, on both sides of the ridge.</td></tr>"
            "<tr><td>C. Fossils</td><td>Fossils of the same land reptile are found in rocks in both South America and Africa, which are now separated by an ocean.</td></tr>"
            "</table>"
            "<p>Write an evaluation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Evaluate the student's claim.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> lines of evidence (A, B, or C) with specific details.</li>"
            "<li><strong>Reasoning:</strong> Explain what each line of evidence shows about <em>past</em> or <em>current</em> movement, and judge how strong the evidence is as a whole. Include one limit of one line of evidence.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Rejects the claim with accurate reasoning. Uses at least two lines of evidence with specific details. "
             "Explains correctly what each shows (GPS shows current motion; seafloor ages show past spreading; fossils show continents were once joined). "
             "Judges the evidence as strong because independent lines agree, and names a reasonable limit (for example, GPS covers only a short time; fossils alone could be explained other ways)."),
            (3, "Proficient",
             "Rejects the claim with two accurate lines of evidence and correct explanations. "
             "Judges strength but gives no limit, or states the limit without a clear judgment."),
            (2, "Developing",
             "Rejects the claim with one line of evidence, or two lines with inaccurate or vague explanations. Judgment of strength is missing."),
            (1, "Beginning",
             "Accepts the claim or gives no clear claim. Little or no evidence. Shows a major misconception."),
        ],
        "grading_notes": [
            "Accept any two of the three lines. Look for specific details (a few centimeters per year; 0 to 100 million years over 2,000 km on both sides; the same reptile on two continents).",
            "A strong judgment says that independent lines of evidence agree. Any reasonable limit counts (short observation time, fossils could also be explained by animals crossing land or a land bridge, or the sample is small).",
            "Common misconception: the continents moved suddenly in one event.",
        ],
        "exemplar": (
            "The student's claim is not supported; the crust has moved in the past and is moving now. "
            "GPS stations on different plates move a few centimeters per year in steady directions, which shows plates are moving today. "
            "Seafloor rock is 0 million years old at the ridge and 100 million years old 2,000 km away on both sides, which shows new crust forms at the ridge and spreads apart over time. "
            "Fossils of the same reptile on two continents now separated by an ocean suggest the continents were once joined. "
            "The evidence is strong because three independent kinds of evidence, present and past, all point to the same conclusion. One limit is that GPS data cover only a few decades, so by themselves they do not show what happened millions of years ago."
        ),
    },
    {
        "title": "FR 2 - How well does the theory explain the ages?",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Geologists collected the ages of the oldest rocks found in different places:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Place</th><th>Oldest rock found (millions of years)</th></tr>"
            "<tr><td>Mid-ocean ridge (center)</td><td>0</td></tr>"
            "<tr><td>Ocean floor, far from any ridge</td><td>about 180</td></tr>"
            "<tr><td>Edge of a continent, near a mountain belt</td><td>about 300</td></tr>"
            "<tr><td>Ancient core of a continent</td><td>about 3,800</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Explain</strong> how the theory of plate tectonics accounts for the ages of the ocean floor.</li>"
            "<li><strong>Explain</strong> how the theory accounts for the continental ages (core versus edge).</li>"
            "<li><strong>Evaluate:</strong> Judge how well the theory explains these ages, and name one question it does not answer by itself.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Explains ocean ages correctly (new crust at ridges, spreading, recycling by subduction, so ocean crust is young). "
             "Explains continental ages correctly (a core of the oldest crust with younger crust added at the edges by past plate interactions, and less dense continental crust is not recycled as easily). "
             "Judges the theory as a strong explanation, citing at least two numbers, and names a reasonable open question (for example, how the first continental crust formed, or why crust is not recycled at all)."),
            (3, "Proficient",
             "Explains both ocean and continent ages correctly with at least one number. Gives a judgment but the open question is vague or missing."),
            (2, "Developing",
             "Explains only one of the two, or explains both with an error (for example, says ocean crust is destroyed at ridges). Judgment is missing or unsupported."),
            (1, "Beginning",
             "Does not use plate tectonics, or shows a major misconception. Little or no evidence."),
        ],
        "grading_notes": [
            "Expected data: 0 at the ridge, about 180 million years for the oldest ocean floor, about 300 and about 3,800 million years for the continent.",
            "Accept any reasonable open question (for example, what the earliest crust was like, how plates started moving, or how old the very first plates were).",
            "Common misconceptions: ocean crust is destroyed at ridges; continents are the same age everywhere.",
        ],
        "exemplar": (
            "Plate tectonics explains the ocean ages because new crust forms at mid-ocean ridges (0 million years old) and moves away, getting older with distance, until it sinks back into the mantle at subduction zones. Since it is always being recycled, the oldest ocean floor is only about 180 million years old. "
            "Continental crust is less dense and is not recycled as easily, so it can be much older. The core of a continent is about 3,800 million years old, and crust at its edge is younger, about 300 million years, because past plate collisions added newer crust around the old core. "
            "The theory is a strong explanation because it accounts for very different ages with one set of processes and matches the data. One question it does not answer by itself is how the first continental crust formed billions of years ago."
        ),
    },
]
