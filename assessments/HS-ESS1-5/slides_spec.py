"""Slide content for the eight Unit 3.1 lesson decks (HS-ESS1-5, HS-ESS1-6).

Writes one slides_helper.py build spec per day (inch-based) plus a small meta file with each
slide's background. Style follows the Unit 1.3 lesson decks: dark-green title slide, cream
content slides, Domine headings, Nunito Sans body text, rust kicker line.

Slide ids are v2l{day}_s{n} so a rebuilt deck can be added next to the old slides, which are then deleted.

Usage: python3 slides_spec.py OUTDIR
"""

import json
import sys
from pathlib import Path

import lessons as L

CREAM, GREEN, RUST, INK, GRAY = "#FBF7EF", "#23392C", "#B34A12", "#22292B", "#424A4A"
TINT, MUTED = "#F1E8D6", "#6E7575"
HEAD, BODY = "Domine", "Nunito Sans"
UNIT = "Unit 3.1 · Age of the Earth"


class Slide:
    def __init__(self, day, n, title, dark=False):
        self.id = f"v4l{day}_s{n}" if day <= 6 else f"v2l{day}_s{n}"
        self.title = title
        self.dark = dark
        self.el = []

    def add(self, role, type_, x, y, w, h=None, **kw):
        e = {"id": f"{self.id}_{role}", "type": type_, "x": x, "y": y, "w": w}
        if h is not None:
            e["h"] = h
        e.update(kw)
        self.el.append(e)

    def spec(self):
        return {"id": self.id, "layout": "BLANK", "elements": self.el}


def head(s, kicker, heading, lesson):
    s.add("kick", "text", 0.5, 0.22, 9, 0.48, text=kicker.upper(), size=14, bold=True, color=RUST, font=BODY)
    s.add("head", "text", 0.5, 0.7, 9, 0.95, text=heading, size=24, bold=True, color=INK, font=HEAD)
    s.add("foot", "text", 0.5, 5.12, 9, 0.4, text=f"{lesson}", size=10, color=MUTED, font=BODY)


def bullets(s, role, items, x=0.5, y=1.75, w=9, h=3.3, size=18, gap=9):
    s.add(role, "text", x, y, w, h, text="\n".join(items), size=size, color=GRAY, font=BODY, bullets=True, space_below=gap)


def table(s, role, rows, x=0.5, y=1.75, w=9, widths=None, align=None, size=14):
    e = dict(rows=rows, header=True, size=size)
    if widths:
        e["col_widths"] = widths
    if align:
        e["col_align"] = align
    s.add(role, "table", x, y, w, **e)


def card(s, role, text, x=0.5, y=1.9, w=9, h=2.4, size=22, font=HEAD, bold=True):
    s.add(role, "round_rect", x, y, w, h, fill=TINT, text=text, size=size, bold=bold, color=INK, font=font, align="START")


def note(s, role, text, y=4.5, h=0.6, size=16):
    s.add(role, "text", 0.5, y, 9, h, text=text, size=size, color=GRAY, font=BODY)


def title_slide(day, title, focus, note_text):
    s = Slide(day, 1, title, dark=True)
    s.add("kick", "text", 0.6, 0.85, 8.8, 0.48, text=f"{UNIT}  ·  LESSON {day}".upper(), size=14, bold=True, color="#EBA36B", font=BODY)
    s.add("title", "text", 0.6, 1.4, 8.8, 1.5, text=title, size=36, bold=True, color="#EFF7EF", font=HEAD)
    s.add("focus", "text", 0.6, 3.1, 8.8, 0.9, text=f"Focus question: {focus}", size=18, color="#C9D8CC", font=BODY)
    s.add("note", "text", 0.6, 4.7, 8.8, 0.4, text=note_text, size=14, color="#C9D8CC", font=BODY)
    return s


def goals_slide(day, n, lesson, can, plan):
    s = Slide(day, n, "Goals and plan")
    head(s, "Today", "Goals and plan", lesson)
    s.add("can_h", "text", 0.5, 1.65, 4.3, 0.5, text="I can…", size=16, bold=True, color=INK, font=BODY)
    bullets(s, "can", can, x=0.5, y=2.15, w=4.3, h=2.9, size=16, gap=8)
    table(s, "plan", [["Min", "Plan"]] + plan, x=5.1, y=1.7, w=4.4, widths=[0.8, 3.6], align=["START", "START"])
    return s


def cfa_slide(day, n, lesson, codes, mins):
    s = Slide(day, n, "CFA")
    names = " and ".join(f"CFA {c}: {L.Q.TARGETS[c][0]}" for c in codes) if len(codes) == 1 else "CFAs " + " and ".join(codes)
    head(s, f"Start with {'a CFA' if len(codes) == 1 else 'two CFAs'} · {mins} min", names if len(codes) == 1 else "; ".join(f"{c}: {L.Q.TARGETS[c][0]}" for c in codes), lesson)
    bullets(s, "b", [f"Take {'the CFA' if len(codes) == 1 else 'both CFAs'} on Canvas now (5 questions{'' if len(codes) == 1 else ' each'}).",
                     f"Below 3 out of 4? A review for {'this target' if len(codes) == 1 else 'that target'} opens for you."], size=20)
    return s


def build_day1():
    lesson = "Lesson 1 · Where Did the Old Ocean Floor Go?"
    out = [title_slide(1, "Where Did the Old Ocean Floor Go?", "How old is the ocean floor compared with the continents, and how do moving plates make and destroy it?",
                       "Have ready: your notebook, a pencil, and colored pencils.")]
    out.append(goals_slide(1, 2, lesson,
                           ["compare the ages of the ocean floor and the continents", "name three plate boundaries and what plates do at each", "say where ocean crust is made and where it sinks"],
                           [["8", "Hook: the mystery"], ["13", "Lab A: plot the pattern"], ["19", "Lab B: clay plate models"], ["5", "Wrap-up and exit ticket"]]))
    s = Slide(1, 3, "Ocean floor"); head(s, "Hook · the ocean floor", "The oldest ocean floor is only about 180 million years old", lesson)
    table(s, "t", [["Place on the ocean floor", "Age of the rock"]] + [
        ["Right at the Mid-Atlantic Ridge", "0 (forming now)"],
        ["Middle of the Atlantic, 2,000 km from the ridge", "about 80 million years"],
        ["Atlantic floor next to eastern North America", "about 180 million years"],
        ["Western Pacific, east of Japan", "about 180 million years"]], widths=[5.6, 3.4], align=["START", "START"])
    note(s, "note", "Ages are rounded. Earth is about 4,500 million years old.", y=4.5, h=0.5)
    out.append(s)
    s = Slide(1, 4, "Continents"); head(s, "Hook · the continents and life", "Continental rock and fossils go back billions of years", lesson)
    table(s, "t", [["Continental material", "Where", "Age"],
                   ["Oldest mineral (zircon)", "Western Australia", "about 4.4 billion years"],
                   ["Oldest known rock", "Canada", "about 4.0 billion years"],
                   ["Oldest fossils", "Western Australia", "about 3.5 billion years"]],
          widths=[3.9, 2.3, 2.8], align=["START", "START", "START"])
    note(s, "note", "In your notebook: what do you notice? What do you wonder?", y=4.3, h=0.7)
    out.append(s)
    s = Slide(1, 5, "Claim"); head(s, "First claim · 2 min · on your own", "Why is the seafloor so much younger than the continents?", lesson)
    card(s, "q", "Write your first claim in one sentence. It is fine if it is wrong. We will revise it all unit.", size=22)
    out.append(s)
    s = Slide(1, 6, "Lab A"); head(s, "Lab A · 13 min · with a partner", "Plot earthquakes and volcanoes on the world map", lesson)
    bullets(s, "b", ["Each partner plots 5 sites.", "Use a red dot for a volcano and a blue X for an earthquake.", "Do the points make lines, or are they random?",
                     "Circle the one site that does not fit."], size=20)
    out.append(s)
    sites = [[s_[0], s_[1], f"{s_[2]}, {s_[3]}"] for s_ in L.SITES]
    s = Slide(1, 7, "Sites 1"); head(s, "Lab A · sites 1–5", "Plot each site: volcano or earthquake?", lesson)
    table(s, "t", [["Site", "Type", "Latitude, longitude"]] + sites[:5], y=1.7, widths=[4.6, 1.5, 2.9], align=["START", "START", "START"])
    out.append(s)
    s = Slide(1, 8, "Sites 2"); head(s, "Lab A · sites 6–10", "Plot these sites too", lesson)
    table(s, "t", [["Site", "Type", "Latitude, longitude"]] + sites[5:], y=1.7, widths=[4.6, 1.5, 2.9], align=["START", "START", "START"])
    note(s, "q", "The points make ______ . They match the edges of the ______ .", y=4.5, h=0.5, size=16)
    out.append(s)
    s = Slide(1, 9, "Lab B"); head(s, "Lab B · 19 min · in a group of 3 or 4", "Model the three plate boundaries with clay", lesson)
    bullets(s, "b", ["You have 2 plates (foam or cardboard) and red, blue, and tan clay.", "You will build 3 models, about 5 minutes each.", "Sketch each one in your notebook. Label the arrows.",
                     "Then fill in the boundary table."], size=19)
    out.append(s)
    s = Slide(1, 10, "Divergent"); head(s, "Lab B · model 1", "Divergent: the plates move apart", lesson)
    bullets(s, "b", ["Put the two plates edge to edge.", "Press a ridge of red clay into the gap (magma).", "Slowly pull the plates apart. Add more red clay in the gap.",
                     "New crust forms at a mid-ocean ridge."], size=20)
    out.append(s)
    s = Slide(1, 11, "Convergent"); head(s, "Lab B · model 2", "Convergent: the plates move together", lesson)
    bullets(s, "b", ["Blue clay slab (ocean crust) on one plate. Tan clay block (continent) on the other.", "Push the plates together. The blue slab slides under.",
                     "The groove is a trench. The sinking is subduction.", "Push a little red clay up behind the block: volcanoes."], size=19)
    out.append(s)
    s = Slide(1, 12, "Transform"); head(s, "Lab B · model 3", "Transform: the plates slide past each other", lesson)
    bullets(s, "b", ["Lay a line of tan clay across both plates.", "Slide the plates past each other.", "Sketch the broken line.", "Earthquakes happen here."], size=20)
    out.append(s)
    s = Slide(1, 13, "Record"); head(s, "Lab B · record", "Fill in the boundary table", lesson)
    table(s, "t", [["Boundary", "What the plates did", "What formed", "Real example"], ["Divergent", "", "", ""], ["Convergent", "", "", ""], ["Transform", "", "", ""]],
          widths=[1.9, 2.6, 2.6, 1.9], align=["START", "START", "START", "START"])
    note(s, "q", "Where is ocean crust made? Where is it destroyed?", y=4.4, h=0.6, size=18)
    out.append(s)
    s = Slide(1, 14, "Exit"); head(s, "Wrap-up · 5 min", "Exit ticket", lesson)
    card(s, "exit", "Where is ocean crust made, and where does it sink back down? Add the words ridge and trench to your first claim if they help.", y=1.8, h=1.8, size=20)
    note(s, "n", "Homework: start a Frayer card for each of the 8 vocabulary words as they come up. Finish by Day 7.", y=4.0, h=0.8, size=16)
    out.append(s)
    return out


def build_day2():
    lesson = "Lesson 2 · Reading Rock Ages"
    out = [title_slide(2, "Reading Rock Ages", "What patterns do the ages of ocean crust and continental crust follow?", "Have ready: colored pencils, graph paper, a pencil, your notebook.")]
    out.append(goals_slide(2, 2, lesson,
                           ["read a map of ocean-floor ages and describe the pattern", "find a rate from a graph", "read a map of continent ages and describe the pattern"],
                           [["8", "CFA ESS1-5.1"], ["3", "Warm-up"], ["12", "Lab A: color the seafloor"], ["9", "Lab B: graph the pattern"], ["10", "Lab C: color North America"], ["3", "Wrap-up"]]))
    out.append(cfa_slide(2, 3, lesson, ["ESS1-5.1"], 8))
    s = Slide(2, 4, "Warm-up"); head(s, "Warm-up · 3 min · on your own", "Which rock is older?", lesson)
    card(s, "q", "A ship pulls up seafloor rock at the Mid-Atlantic Ridge and another near the coast of Brazil. Which is older? Say why.", size=22)
    out.append(s)
    s = Slide(2, 5, "Lab A"); head(s, "Lab A · 12 min · with a partner", "Color the seafloor", lesson)
    bullets(s, "b", ["Draw a row of 13 boxes across your page.", "Label the middle box RIDGE. Label the others 500, 1,000 … 3,000 km on each side.",
                     "Color each box by its age. Use the table on the next slide."], size=20)
    out.append(s)
    s = Slide(2, 6, "Data"); head(s, "Lab A · the data and the color key", "Age and color for each distance", lesson)
    table(s, "t", [["Distance from ridge (km)", "Crust age (million years)", "Color"], ["0", "0", "red"], ["500", "20", "orange"], ["1,000", "40", "yellow"], ["1,500", "60", "green"],
                   ["2,000", "80", "blue"], ["2,500", "100", "purple"], ["3,000", "120", "dark purple"]], y=1.65, widths=[3.2, 3.2, 2.6], align=["START", "START", "START"], size=13)
    out.append(s)
    s = Slide(2, 7, "Lab A Q"); head(s, "Lab A · questions", "Describe your colored map", lesson)
    bullets(s, "b", ["Where is the youngest color? The oldest?", "How do the left and right sides compare?", "As you move away from the ridge, the crust gets ______ ."], size=22)
    out.append(s)
    s = Slide(2, 8, "Lab B"); head(s, "Lab B · 9 min · on your own", "Graph age against distance", lesson)
    bullets(s, "b", ["x-axis: distance from ridge (0 to 3,000 km). y-axis: age (0 to 120 million years).", "Plot the 7 points and connect them.",
                     "Pick two points. Rate = distance ÷ time. (500 km in 20 million years)", "1 km per million years = 0.1 cm per year."], size=19)
    out.append(s)
    s = Slide(2, 9, "Lab B Q"); head(s, "Lab B · questions", "Find the rate and make a prediction", lesson)
    bullets(s, "b", ["What is the rate in cm per year? About how fast do fingernails grow?", "Use your line to predict the age of crust 3,500 km from the ridge."], size=22)
    out.append(s)
    s = Slide(2, 10, "Lab C"); head(s, "Lab C · 10 min · with a partner", "Color North America by age", lesson)
    bullets(s, "b", ["Draw a row of 5 boxes from west to east.", "Write the region names in order from the table.", "Oldest region: dark brown. Youngest: light yellow. Pick the colors in between."], size=20)
    out.append(s)
    s = Slide(2, 11, "NA data"); head(s, "Lab C · the data", "Ages of North American crust", lesson)
    table(s, "t", [["Region", "From the core", "Age of the crust"], ["Pacific Coast Ranges", "west, 2,800 km", "about 50 million years"], ["Rocky Mountain region", "west, 1,800 km", "about 150 million years"],
                   ["Canadian Shield (core)", "0", "about 2.7 billion years"], ["Grenville Province", "east, 1,200 km", "about 1.1 billion years"], ["Appalachian Mountains", "east, 2,000 km", "about 400 million years"]],
          y=1.65, widths=[3.6, 2.4, 3.0], align=["START", "START", "START"], size=13)
    note(s, "q", "Where is the oldest crust? How does the age change as you move away from it?", y=4.5, h=0.5, size=15)
    out.append(s)
    s = Slide(2, 12, "Wrap-up"); head(s, "Wrap-up · 3 min", "Add two rows to your evidence log", lesson)
    bullets(s, "b", ["One row for the ocean pattern. One row for the continent pattern. Use a number from today.", "Tomorrow starts with CFA ESS1-5.2: Reading rock ages. Study your colored boxes and graph."], size=19)
    out.append(s)
    return out


def build_day3():
    lesson = "Lesson 3 · Reading Deep Time and Early Earth"
    out = [title_slide(3, "Reading Deep Time and Early Earth", "How do scientists know how old Earth is, and why do meteorites and moon rocks tell Earth's age better than Earth rocks do?",
                       "Have ready: your notebook, a ruler, and colored pencils.")]
    out.append(goals_slide(3, 2, lesson,
                           ["list the evidence scientists use to learn about early Earth", "explain why meteorites and moon rocks give the age of the solar system"],
                           [["8", "CFA ESS1-5.2"], ["5", "Hook and key ideas"], ["15", "Simulation: crater counter"], ["13", "Lab B: Earth timeline"], ["4", "Wrap-up"]]))
    out.append(cfa_slide(3, 3, lesson, ["ESS1-5.2"], 8))
    s = Slide(3, 4, "Hook"); head(s, "Hook · 5 min", "How could anyone know Earth is 4.5 billion years old?", lesson)
    bullets(s, "b", ["The oldest ocean floor is only about 200 million years old.", "Scientists date rock with atoms that change at a steady rate, like a clock.",
                     "The oldest Earth rock is about 4.0 billion years old. That is younger than Earth.", "Meteorites and moon rocks have hardly changed. They keep the early record."], size=19)
    out.append(s)
    s = Slide(3, 5, "Sim"); head(s, "Simulation A · 15 min · with a partner", "Crater counter: the Moon and Earth, same sky", lesson)
    bullets(s, "b", ["The Moon and Earth are hit by the same space rocks over time.", "Watch four time steps on the board: 1, 2, 3, and 4 billion years.",
                     "At each step, count the craters on the Moon and on Earth. Record both numbers in your table.", "Then answer the questions after step 4."], size=19)
    out.append(s)
    s = Slide(3, 6, "Craters"); head(s, "Simulation A · record and think", "What do the craters tell us?", lesson)
    table(s, "t", [["Time step", "Moon craters", "Earth craters"], ["1 billion years", "", ""], ["2 billion years", "", ""], ["3 billion years", "", ""], ["4 billion years", "", ""]], w=4.4, widths=[1.8, 1.3, 1.3], align=["START", "START", "START"], size=13)
    note(s, "q", "Which surface looks older? Why does Earth show so few craters? A surface has many craters: old or young?", y=4.3, h=0.7, size=15)
    out.append(s)
    # the four animated time-step slides are built in Google Slides (a3sim1 to a3sim4): see the Day 3 deck
    s = Slide(3, 7, "Lab B"); head(s, "Lab B · 13 min · with a partner", "Build a 45 cm timeline of Earth", lesson)
    bullets(s, "b", ["Left end: Earth forms. Right end: today.", "Scale: 1 cm = 100 million years.", "Position = (4,500 − age in millions of years) ÷ 100.", "Mark and label each event on your strip."], size=20)
    out.append(s)
    s = Slide(3, 8, "Timeline"); head(s, "Lab B · the events", "Fill in the missing positions", lesson)
    table(s, "t", [["Event", "Age (million years ago)", "Position (cm)"], ["Earth forms", "4,500", "0"], ["Oldest mineral (zircon)", "4,400", "1"], ["Oldest known rock", "4,000", ""], ["Oldest fossils", "3,500", ""],
                   ["Oldest ocean floor", "200", ""], ["Today", "0", "45"]], y=1.65, widths=[4.2, 2.8, 2.0], align=["START", "START", "START"], size=14)
    out.append(s)
    s = Slide(3, 9, "Lab B Q"); head(s, "Lab B · questions", "Use your timeline", lesson)
    bullets(s, "b", ["How much of the 45 cm is covered by ocean floor that still exists?", "Why is the oldest Earth rock younger than Earth?", "Why are there no fossils that old in the ocean floor?"], size=21)
    out.append(s)
    s = Slide(3, 10, "Exit"); head(s, "Wrap-up · 4 min", "Exit ticket", lesson)
    card(s, "exit", "Why do scientists use meteorites and moon rocks, not Earth rocks, to find the age of the solar system?", y=1.8, h=1.7, size=20)
    note(s, "n", "Add a row to your evidence log: the age of meteorites, moon rocks, or Earth's oldest minerals.", y=4.0, h=0.8, size=16)
    out.append(s)
    return out


def build_day4():
    lesson = "Lesson 4 · Why the Ocean Is Young and the Continents Old"
    out = [title_slide(4, "Why the Ocean Is Young and the Continents Old", "How is ocean crust made, grown, and recycled, and how do continents grow and survive?",
                       "Have ready: SketchNotes paper, a pencil, and colored pencils.")]
    out.append(goals_slide(4, 2, lesson,
                           ["use density to explain which plate sinks", "explain why ocean crust is young and continents are old", "explain how continents grow from an ancient core"],
                           [["3", "Warm-up"], ["7", "Guided notes"], ["17", "Lab: sink or float"], ["15", "SketchNotes"], ["3", "Wrap-up"]]))
    s = Slide(4, 3, "Warm-up"); head(s, "Warm-up · 3 min · on your own", "Where does the old ocean crust go?", lesson)
    card(s, "q", "You know the ocean floor is under 200 million years old. Where does the old ocean crust go?", size=22)
    out.append(s)
    s = Slide(4, 4, "Notes 1"); head(s, "Guided notes · 7 min", "The life of ocean crust", lesson)
    bullets(s, "b", ["Ocean crust is made at a ______ and moves away about 25 km per million years.", "Travel 3,000 km: 3,000 ÷ 25 = ______ million years.",
                     "In 200 million years it travels 200 × 25 = ______ km. Then it reaches a trench and sinks.", "No ocean floor is older than about ______ million years."], size=19)
    out.append(s)
    s = Slide(4, 5, "Notes 2"); head(s, "Guided notes · density and continents", "Which plate sinks? How do continents grow?", lesson)
    bullets(s, "b", ["Ocean crust: about 3.0 g/cm³. Continental crust: about 2.7 g/cm³. The ______ plate sinks (subduction).", "Each continent has an ancient core.",
                     "Volcanic arcs and pieces of crust are added to its edge, like tree rings.", "The edge is ______ than the core."], size=19)
    out.append(s)
    s = Slide(4, 6, "Lab"); head(s, "Lab · 17 min · in a group of 3 or 4", "Sink or float: the density of plates", lesson)
    bullets(s, "b", ["Predict: which block sinks, and which floats?", "Measure the mass of each block. Measure l × w × h for the volume.", "Density = mass ÷ volume. Water is 1.0 g/cm³.",
                     "Place each block on the water. Then push them toward each other. Which dives under?", "Draw what you saw."], size=18)
    out.append(s)
    s = Slide(4, 7, "Record"); head(s, "Lab · record and think", "Density table", lesson)
    table(s, "t", [["Block", "Mass (g)", "Volume (cm³)", "Density (g/cm³)", "Sinks or floats?"], ["Wood (continent)", "", "", "", ""], ["Clay (old, cold ocean plate)", "", "", "", ""]],
          widths=[3.0, 1.4, 1.6, 1.7, 1.3], align=["START"] * 5, size=13)
    note(s, "q", "Which block is like the ocean plate? What does the denser one do when they meet? What stands in for the mantle?", y=3.8, h=1.0, size=16)
    out.append(s)
    s = Slide(4, 8, "SketchNotes"); head(s, "SketchNotes · 15 min · on your own", "Half page of notes, one page of sensemaking", lesson)
    bullets(s, "b", ["Notes: the life of ocean crust and how continents grow.", "Draw a cross-section: ridge, plate moving away, trench, volcanic arc, a continent with an ancient core and a younger edge.",
                     "Label density. Add an arrow for the plankton-shell carbon riding the plate down.", "Turn in a photo on Canvas: Lesson 4: SketchNotes."], size=17)
    out.append(s)
    s = Slide(4, 9, "Wrap-up"); head(s, "Wrap-up · 3 min", "Add a row and prepare for the CFA", lesson)
    bullets(s, "b", ["Add a row to your evidence log about density or continental growth.", "Tomorrow starts with CFA ESS1-5.3: Why ocean crust is young and continents are old.", "Study your SketchNotes tonight."], size=19)
    out.append(s)
    return out


def build_day5():
    lesson = "Lesson 5 · Evidence for Moving Crust"
    out = [title_slide(5, "Evidence for Moving Crust", "How strong is the evidence that the crust has moved and is still moving?", "Have ready: scissors, red and blue pencils, a ruler, and tape.")]
    out.append(goals_slide(5, 2, lesson,
                           ["use magnetic stripes, measured motion, and fossils as evidence", "judge how strong each line of evidence is"],
                           [["8", "CFA ESS1-5.3"], ["2", "Warm-up"], ["12", "Lab A: magnetic stripes"], ["7", "Lab B: Hawaii and GPS"], ["9", "Lab C: Pangaea puzzle"], ["6", "Evaluate the evidence"]]))
    out.append(cfa_slide(5, 3, lesson, ["ESS1-5.3"], 8))
    s = Slide(5, 4, "Warm-up"); head(s, "Warm-up · 2 min · on your own", "How could you show that the crust moves?", lesson)
    card(s, "q", "Write one idea for how to show the seafloor moved long ago. Write one idea for how to show it is moving today.", size=22)
    out.append(s)
    s = Slide(5, 5, "Lab A"); head(s, "Lab A · 12 min · with a partner", "Paper model of seafloor spreading", lesson)
    bullets(s, "b", ["Color two strips with the table on the next slide. Start at the end you push first (the oldest crust).", "Cut a slit in the folded paper. The slit is the ridge.",
                     "Put the strips back to back. Push them up through the slit and pull them apart.", "Tape the result in your notebook. Label the youngest and oldest crust."], size=18)
    out.append(s)
    s = Slide(5, 6, "Strips"); head(s, "Lab A · the stripes (2 cm = 1 million years)", "Color the bands", lesson)
    table(s, "t", [["Band", "Color", "Length", "Age it represents"], ["1", "Reversed (blue)", "3.4 cm", "about 3.6–5.3 million years"], ["2", "Normal (red)", "2.0 cm", "about 2.6–3.6 million years"],
                   ["3", "Reversed (blue)", "3.6 cm", "about 0.8–2.6 million years"], ["4", "Normal (red)", "1.6 cm", "0–0.8 million years (youngest)"]], widths=[1.1, 2.4, 1.5, 4.0], align=["START"] * 4)
    note(s, "q", "What does a pair of mirror-image stripe patterns tell you about how the crust formed?", y=4.3, h=0.7, size=16)
    out.append(s)
    s = Slide(5, 7, "Lab B"); head(s, "Lab B · 7 min · on your own", "Hawaii and GPS: measured motion", lesson)
    table(s, "t", [["Island", "Distance from Kīlauea (km)", "Age (million years)"], ["Kīlauea", "0", "0"], ["Kauaʻi", "about 500", "about 5"], ["Midway Atoll", "about 2,500", "about 28"]],
          widths=[3.2, 3.2, 2.6], align=["START"] * 3)
    note(s, "q", "Rate = distance ÷ time. 1 km per million years = 0.1 cm per year. Find the rate for Kauaʻi and Midway. GPS says 7 to 8 cm per year. What do you notice?", y=3.9, h=1.1, size=15)
    out.append(s)
    s = Slide(5, 8, "Lab C"); head(s, "Lab C · 9 min · with a partner", "Fit the continents like a puzzle", lesson)
    bullets(s, "b", ["Fit the cut-out continents together. Tape the best fit in your notebook.", "Mark where each fossil lived: Mesosaurus, Glossopteris, Lystrosaurus.",
                     "Mesosaurus lived in fresh water. Glossopteris had heavy seeds. Why does that matter?", "What can fossils NOT tell you that GPS can?"], size=18)
    out.append(s)
    s = Slide(5, 9, "Fossils"); head(s, "Lab C · the fossils", "Where the same fossils were found", lesson)
    table(s, "t", [["Fossil", "What it was", "Found in"], ["Mesosaurus", "freshwater reptile", "South America and southern Africa"], ["Glossopteris", "seed fern (heavy seeds)", "South America, Africa, India, Australia, Antarctica"],
                   ["Lystrosaurus", "land animal", "Africa, India, Antarctica"]], widths=[2.2, 2.8, 4.0], align=["START"] * 3)
    out.append(s)
    s = Slide(5, 10, "Evaluate"); head(s, "Evaluate the evidence · 6 min", "How strong is each line of evidence?", lesson)
    table(s, "t", [["Line of evidence", "Measured?", "Past or present?", "Independent?", "Strength (1–4)"], ["Rock ages across a ridge", "", "", "", ""], ["Magnetic stripes", "", "", "", ""],
                   ["GPS and Hawaii", "", "", "", ""], ["Fossils and rocks", "", "", "", ""]], widths=[3.0, 1.4, 1.7, 1.5, 1.4], align=["START"] * 5, size=13)
    note(s, "q", "Which is strongest for current motion? For past motion? Why does agreement of two independent methods help?", y=4.2, h=0.8, size=15)
    out.append(s)
    return out


def build_day6():
    lesson = "Lesson 6 · Evaluate the Theory, Tell Earth's Story"
    out = [title_slide(6, "Evaluate the Theory, Tell Earth's Story", "How well does plate tectonics explain the ages of crustal rocks, and what story do ancient materials tell about Earth's formation?",
                       "Have ready: your evidence log, scissors, glue, and a pencil.")]
    out.append(goals_slide(6, 2, lesson,
                           ["judge how well plate tectonics explains the ages of rocks", "use evidence from rocks, meteorites, and other planets to tell how Earth formed"],
                           [["8", "CFA ESS1-5.4"], ["3", "Sort your evidence"], ["14", "Part A: evaluate the theory"], ["5", "Peer feedback"], ["12", "Part B: Earth's story"], ["3", "Wrap-up"]]))
    out.append(cfa_slide(6, 3, lesson, ["ESS1-5.4"], 8))
    s = Slide(6, 4, "Sort"); head(s, "Sort your evidence · 3 min", "Put each row of your evidence log in a bucket", lesson)
    table(s, "t", [["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], ["", "", ""]], widths=[3.0, 3.0, 3.0], align=["START"] * 3)
    note(s, "q", "Look back at your Day 1 claim. What would you change now?", y=3.8, h=0.7, size=18)
    out.append(s)
    s = Slide(6, 5, "Part A"); head(s, "Part A · 14 min · on your own", "How well does plate tectonics explain the ages of rocks?", lesson)
    bullets(s, "b", ["Claim: Plate tectonics explains the ages (very well / partly / poorly) because ______ .", "Ocean evidence: The seafloor is youngest at the ______ and gets older with ______ ; the oldest ocean floor is about ______ million years old.",
                     "Continent evidence: Continental crust as old as ______ exists. In North America the crust gets ______ toward the edges."], size=16, gap=8)
    out.append(s)
    s = Slide(6, 6, "Part A 2"); head(s, "Part A · frames, continued", "Reasoning, and a limit", lesson)
    bullets(s, "b", ["Reasoning: Because ocean plates are ______ than continental crust, they ______ at subduction zones, while continents ______ .",
                     "Limit: One thing this evidence cannot show is ______ . OR: Someone might say ______ . That does not fit the evidence because ______ .", "Submit on Canvas: Unit 3.1 CER (Part A)."], size=16, gap=8)
    out.append(s)
    s = Slide(6, 7, "Data"); head(s, "Part A · data you may use", "Pick specific numbers", lesson)
    bullets(s, "b", ["Crust age: 0 to 120 million years across 3,000 km (2.5 cm per year). Oldest ocean floor: about 200 million years.", "Oldest continental mineral: about 4.4 billion years. North America: 2.7 billion years at the core, 400 million years in the Appalachians.",
                     "Ocean crust 3.0 g/cm³. Continental crust 2.7 g/cm³.", "GPS 2 cm per year. Rock ages 2.5 cm per year. Oldest fossils 3.5 billion years, in continental rock."], size=15, gap=6)
    out.append(s)
    s = Slide(6, 8, "Peer"); head(s, "Peer feedback · 5 min", "Trade papers. Give a star and a step.", lesson)
    bullets(s, "b", ["Does the claim say how well and give a cause?", "Is the evidence specific, from ocean and continents?", "Does the reasoning say why the evidence supports the claim?", "Is a limit or counterclaim addressed?",
                     "Write one star and one step. Then fix your own."], size=17)
    out.append(s)
    s = Slide(6, 9, "Part B"); head(s, "Part B · 12 min · with a partner", "Order the evidence cards: Earth's story", lesson)
    bullets(s, "b", ["Cut out the six evidence cards on your page.", "Put them in order from oldest to newest on a paper strip. Glue them down.",
                     "Write the story with the frames: About ___ billion years ago, ___ happened. The evidence is ___ .", "Why is Earth's earliest record missing?"], size=18)
    out.append(s)
    s = Slide(6, 10, "Cards"); head(s, "Part B · the evidence cards", "Cut these out", lesson)
    table(s, "t", [["Evidence card", "What it shows"], ["Meteorites: 4.56 billion years", "The solar system formed."], ["Moon highlands: up to 4.4 billion years", "Solid crust existed early."],
                   ["Earth's oldest zircons: 4.4 billion years", "Solid crust on Earth by then."], ["Oldest Earth rock: 4.0 billion years", "Rock survives in the continents."],
                   ["Oldest fossils: 3.5 billion years", "Life existed by then."], ["Oldest ocean floor: 200 million years", "Ocean crust is recycled."]], widths=[4.6, 4.4], align=["START", "START"], size=13)
    out.append(s)
    s = Slide(6, 11, "Wrap-up"); head(s, "Wrap-up · 3 min", "Last CFA", lesson)
    bullets(s, "b", ["CFA ESS1-5.5: How well plate tectonics explains rock ages (5 questions).", "Take it at the start of your next class or on the work day.", "Below 3 out of 4? A review opens for you."], size=20)
    out.append(s)
    return out


def build_day7():
    lesson = "Lesson 7 · Review Day"
    out = [title_slide(7, "Review Day", "Which targets do I still need to work on before the CSA?", "Have ready: your notebook, Frayer cards, and Chromebook.")]
    s = Slide(7, 2, "Plan"); head(s, "Today", "Plan", lesson)
    table(s, "t", [["Min", "Plan"], ["5", "Rate yourself on each target"], ["33", "Work time matched to your CFA scores"], ["5", "Vocabulary self-check with a partner"], ["2", "Preview the CSA"]],
          widths=[1.0, 8.0], align=["START", "START"])
    out.append(s)
    s = Slide(7, 3, "Rate"); head(s, "Rate yourself · 5 min", "1 = I need help, 4 = I could teach it", lesson)
    rows = [["Target", "Rating"]] + [[f"{c}  {n}", ""] for c, (n, _) in L.Q.TARGETS.items()]
    table(s, "t", rows, y=1.65, widths=[7.6, 1.4], align=["START", "START"])
    out.append(s)
    s = Slide(7, 4, "Work"); head(s, "Work time · 33 min", "Do the work that matches your scores", lesson)
    bullets(s, "b", ["Have not taken a CFA yet? Take it now, including CFA ESS1-5.5.", "A Mastery Path review opened for you? Do it now. Study your notebook first.",
                     "No reviews open? Your teacher may assign the enrichment choice board.", "Everyone: finish your Frayer cards, your evidence log, and your CER."], size=17)
    out.append(s)
    s = Slide(7, 5, "Vocab"); head(s, "Vocabulary self-check · 5 min", "Cover the definitions. Explain each word aloud.", lesson)
    bullets(s, "l", ["lithosphere (plate)", "plate boundary", "mid-ocean ridge", "subduction", "trench"], x=0.5, y=1.7, w=4.3, h=2.5, size=18, gap=6)
    bullets(s, "r", ["magnetic reversal", "craton", "impact crater"], x=5.0, y=1.7, w=4.5, h=2.5, size=18, gap=6)
    out.append(s)
    s = Slide(7, 6, "CSA"); head(s, "The CSA", "Unit 3.1 CSA covers ESS1-5.1 to ESS1-5.5", lesson)
    bullets(s, "b", ["The ESS1-6 targets support ESS1-5.3 and ESS1-5.5 but are not on the CSA.", "Study your notebook, your CFA results, and your reviews.", "Bring a pencil and a charged Chromebook."], size=18)
    out.append(s)
    return out


def build_day8():
    lesson = "Lesson 8 · Unit 3.1 CSA"
    out = [title_slide(8, "Unit 3.1 CSA", "What do you know about the ages of Earth's crust?", "Chromebook open to Canvas. Pencil ready.")]
    s = Slide(8, 2, "About"); head(s, "About the CSA", "16 questions on the five priority targets", lesson)
    bullets(s, "b", ["14 multiple-choice, select-all, and true/false questions.", "2 written responses: an evaluation of evidence for seafloor spreading (Q12), and an evaluation of how well plate tectonics explains rock ages using data (Q16).",
                     "Open Unit 3.1 CSA: Age of the Earth (HS-ESS1-5) on Canvas when your teacher says to begin."], size=17)
    out.append(s)
    s = Slide(8, 3, "Tips"); head(s, "To do your best", "Read carefully and use the data", lesson)
    bullets(s, "b", ["Read each question and every answer choice before you choose.", "Use the numbers in the question: distances, ages, and densities.",
                     "For written answers: make a claim, support it with two specific pieces of evidence, explain why they support it, and name a limit."], size=18)
    out.append(s)
    s = Slide(8, 4, "Done"); head(s, "When you finish", "Check your written answers, then work quietly", lesson)
    bullets(s, "b", ["Reread Q12 and Q16.", "Work quietly on any missing Canvas work.", "A target below 3 gets an intervention and a chance to reassess."], size=18)
    out.append(s)
    return out


DECKS = {
    1: ("Unit 3.1 Lesson 1: Where Did the Old Ocean Floor Go?", build_day1),
    2: ("Unit 3.1 Lesson 2: Reading Rock Ages", build_day2),
    3: ("Unit 3.1 Lesson 3: Reading Deep Time and Early Earth", build_day3),
    4: ("Unit 3.1 Lesson 4: Why the Ocean Is Young and the Continents Old", build_day4),
    5: ("Unit 3.1 Lesson 5: Evidence for Moving Crust", build_day5),
    6: ("Unit 3.1 Lesson 6: Evaluate the Theory, Tell Earth's Story", build_day6),
    7: ("Unit 3.1 Lesson 7: Review Day", build_day7),
    8: ("Unit 3.1 Lesson 8: CSA", build_day8),
}

# Old slide ids in the first version of each deck (deleted when a deck is rebuilt)
OLD_SLIDES = {1: 8, 2: 8, 3: 9, 4: 9, 5: 8, 6: 9, 7: 6, 8: 4}


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for day, (title, fn) in DECKS.items():
        slides = fn()
        (out / f"day{day}_spec.json").write_text(json.dumps({"slides": [s.spec() for s in slides]}))
        (out / f"day{day}_meta.json").write_text(json.dumps({"title": title, "slides": [{"id": s.id, "dark": s.dark} for s in slides]}))
        print(day, title, len(slides), "slides")


if __name__ == "__main__":
    main()
