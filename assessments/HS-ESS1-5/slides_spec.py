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
        self.id = f"v2l{day}_s{n}"
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
                           [["3", "Warm-up: guess"], ["8", "The phenomenon"], ["6", "Mystery and first claim"], ["15", "Plot the pattern"], ["8", "Boundaries and the conveyor"], ["5", "Vocabulary and exit ticket"]]))
    s = Slide(1, 3, "Warm-up"); head(s, "Warm-up · 3 min · on your own", "Take a guess before we look at data", lesson)
    card(s, "q", "Earth is about 4.5 billion years old. Guess the age of (a) the oldest ocean floor and (b) the oldest rock or mineral on the continents. Give one reason for each.", size=20)
    out.append(s)
    s = Slide(1, 4, "Ocean floor"); head(s, "Phenomenon · the ocean floor", "The oldest ocean floor is only about 180 million years old", lesson)
    table(s, "t", [["Place on the ocean floor", "Age of the rock"]] + [
        ["Right at the Mid-Atlantic Ridge", "0 (forming now)"],
        ["Middle of the Atlantic, 2,000 km from the ridge", "about 80 million years"],
        ["Atlantic floor next to eastern North America", "about 180 million years"],
        ["Right at the East Pacific Rise", "0 (forming now)"],
        ["Western Pacific, east of Japan", "about 180 million years"]], widths=[5.6, 3.4], align=["START", "START"])
    note(s, "note", "Ages are rounded. In your notebook: what do you notice? What do you wonder?", y=4.5, h=0.5)
    out.append(s)
    s = Slide(1, 5, "Continents"); head(s, "Phenomenon · the continents and life", "Continental rock and fossils go back billions of years", lesson)
    table(s, "t", [["Continental material", "Where", "Age"],
                   ["Oldest mineral (zircon)", "Western Australia", "about 4.4 billion years"],
                   ["Oldest known rock (Acasta Gneiss)", "Canada", "about 4.0 billion years"],
                   ["Very old rock (Isua belt)", "Greenland", "about 3.8 billion years"],
                   ["Oldest widely accepted fossils", "Western Australia", "about 3.5 billion years"]],
          widths=[3.9, 2.3, 2.8], align=["START", "START", "START"])
    note(s, "note", "Compare with the ocean floor. Add what you notice and wonder to your table.", y=4.3, h=0.7)
    out.append(s)
    s = Slide(1, 6, "Claim"); head(s, "The mystery · 6 min · on your own", "Why is the seafloor so much younger than the continents?", lesson)
    bullets(s, "b", ["Draw a cross-section: an ocean between two continents. Show where ocean floor might come from and where it might go.",
                     "Write your first claim for the Unit CER.", "It is fine if it is wrong. We will revise it all unit."])
    out.append(s)
    sites = [[s_[0], s_[1], f"{s_[2]}, {s_[3]}"] for s_ in L.SITES]
    s = Slide(1, 7, "Sites 1"); head(s, "Plot the pattern · sites 1–5", "Plot each site on your world map: volcano or earthquake?", lesson)
    table(s, "t", [["Site", "Type", "Latitude, longitude"]] + sites[:5], y=1.7, widths=[4.6, 1.5, 2.9], align=["START", "START", "START"])
    out.append(s)
    s = Slide(1, 8, "Sites 2"); head(s, "Plot the pattern · sites 6–10", "Then decide which boundary type is nearest each site", lesson)
    table(s, "t", [["Site", "Type", "Latitude, longitude"]] + sites[5:], y=1.7, widths=[4.6, 1.5, 2.9], align=["START", "START", "START"])
    note(s, "q", "Do the points form lines? Which site does not fit the pattern, and what could explain it?", y=4.5, h=0.6, size=15)
    out.append(s)
    s = Slide(1, 9, "Boundaries"); head(s, "Three kinds of plate boundaries · 8 min", "Where plates move apart, together, or past each other", lesson)
    table(s, "t", [["Boundary", "Plates move…", "Example", "Landforms"],
                   ["Divergent", "apart", "Mid-Atlantic Ridge", "ridges, rift valleys"],
                   ["Convergent", "toward each other", "Andes; Japan", "trenches, volcanic arcs"],
                   ["Transform", "past each other", "San Andreas Fault", "faults, earthquakes"]],
          widths=[1.9, 2.4, 2.5, 2.2], align=["START", "START", "START", "START"])
    note(s, "q", "Ridge: plates pull apart and new ocean crust forms. Trench: an old ocean plate sinks into the mantle and the crust is destroyed. Add both to your model.", y=3.9, h=1.1, size=16)
    out.append(s)
    s = Slide(1, 10, "Vocabulary"); head(s, "Vocabulary preview · 4 min · exit ticket · 1 min", "Ten words you will use all unit", lesson)
    bullets(s, "l", ["lithosphere (plate)", "plate boundary", "mid-ocean ridge", "subduction", "trench"], x=0.5, y=1.7, w=4.3, h=2.2, size=18, gap=6)
    bullets(s, "r", ["magnetic reversal", "craton", "radiometric dating", "half-life", "impact crater"], x=5.0, y=1.7, w=4.5, h=2.2, size=18, gap=6)
    card(s, "exit", "Exit ticket: name one thing you could measure or observe that would test your claim.", y=4.0, h=1.0, size=16, font=BODY, bold=True)
    out.append(s)
    return out


def build_day2():
    lesson = "Lesson 2 · Reading Rock Ages"
    out = [title_slide(2, "Reading Rock Ages", "What patterns do the ages of ocean crust and continental crust follow?", "Have ready: graph paper, a pencil, your notebook.")]
    out.append(goals_slide(2, 2, lesson,
                           ["read a table or map of rock ages", "describe the age pattern of the ocean floor", "describe the age pattern of a continent"],
                           [["8", "CFA ESS1-5.1"], ["4", "Warm-up: predict"], ["13", "Ocean data, graph, and rate"], ["8", "Read the seafloor age map"], ["12", "The pattern on the continents"]]))
    out.append(cfa_slide(2, 3, lesson, ["ESS1-5.1"], 8))
    s = Slide(2, 4, "Warm-up"); head(s, "Warm-up · 4 min · on your own", "Which rock is older, at the ridge or near Brazil?", lesson)
    card(s, "q", "A ship pulls up seafloor rock right at the Mid-Atlantic Ridge and another sample near the coast of Brazil. Which is older? Explain your prediction.", size=20)
    out.append(s)
    s = Slide(2, 5, "Data"); head(s, "The data · simplified from a rate of about 2.5 cm per year", "Crust gets older with distance from the ridge", lesson)
    table(s, "t", [["Distance from ridge (km)", "Crust age (million years)", "Sediment (m)"]] + [
        ["0", "0", "about 0"], ["500", "20", "about 50"], ["1,000", "40", "about 150"], ["1,500", "60", "about 250"],
        ["2,000", "80", "about 350"], ["2,500", "100", "about 450"], ["3,000", "120", "about 550"]],
          y=1.65, widths=[3.2, 3.2, 2.6], align=["END", "END", "END"])
    out.append(s)
    s = Slide(2, 6, "Rate"); head(s, "Graph it · 13 min · with a partner", "Find the pattern and how fast the seafloor moves", lesson)
    bullets(s, "b", ["Graph crust age (y) against distance from the ridge (x). Describe the pattern in one sentence.",
                     "Rate = distance ÷ time. (1 km per million years = 0.1 cm per year.)",
                     "Predict the age of crust 3,500 km from the ridge.",
                     "Graph sediment against distance. Why is older crust covered with more sediment?"], size=17)
    out.append(s)
    s = Slide(2, 7, "Map"); head(s, "Read the seafloor age map · 8 min", "Find the ridge and read the colors", lesson)
    bullets(s, "b", ["Find the band of the youngest color. What is it, and where does it run?",
                     "How do the colors change as you move away from it on each side? How do the two sides compare?",
                     "Find the oldest color. About how old is it, and where is it found?"], size=18)
    out.append(s)
    s = Slide(2, 8, "Continents"); head(s, "The pattern on the continents · 12 min", "Every continent has an ancient core", lesson)
    table(s, "t", [["Region of North America", "From the core (km)", "Age of the crust"],
                   ["Canadian Shield (core)", "0", "about 2.7 billion years"],
                   ["Grenville Province", "east, about 1,200", "about 1.1 billion years"],
                   ["Appalachian Mountains", "east, about 2,000", "about 400 million years"],
                   ["Rocky Mountain region", "west, about 1,800", "about 150 million years"],
                   ["Pacific Coast Ranges", "west, about 2,800", "about 50 million years"]],
          y=1.65, widths=[3.5, 2.6, 2.9], align=["START", "START", "START"])
    note(s, "q", "Simplified from geologic maps. Where is the oldest crust? How does the age change moving outward?", y=4.35, h=0.7, size=15)
    out.append(s)
    s = Slide(2, 9, "Wrap"); head(s, "Wrap up", "Two patterns to put in your evidence log", lesson)
    bullets(s, "b", ["Ocean: crust is youngest at the ridge and older in both directions, about 25 km per million years.",
                     "Continents: crust is oldest at the ancient core and younger toward the edges.",
                     "Add one row for each pattern to your Unit CER evidence log.",
                     "Tomorrow starts with CFA ESS1-5.2: Reading rock ages."], size=17)
    out.append(s)
    return out


def build_day3():
    lesson = "Lesson 3 · Reading Deep Time and Early Earth"
    out = [title_slide(3, "Reading Deep Time and Early Earth", "How do scientists find ages in the billions of years, and why do meteorites and moon rocks tell Earth's age better than Earth rocks do?",
                       "Have ready: 50 coins, a cup, graph paper.")]
    out.append(goals_slide(3, 2, lesson,
                           ["use half-life to explain how rocks are dated", "list the evidence for early Earth", "explain why meteorites and moon rocks give the age"],
                           [["7", "CFA ESS1-5.2"], ["3", "Hook and definitions"], ["12", "Half-life lab"], ["4", "Which clock?"], ["8", "Oldest materials and timeline"], ["6", "Impact craters"], ["5", "Why meteorites?"]]))
    out.append(cfa_slide(3, 3, lesson, ["ESS1-5.2"], 7))
    s = Slide(3, 4, "Hook"); head(s, "Hook · 3 min", "How can anyone know Earth is 4.5 billion years old?", lesson)
    bullets(s, "b", ["Some atoms are unstable. They change into a different kind of atom at a steady rate: radioactive decay.",
                     "Half-life: the time for half of the parent atoms in a sample to decay into daughter atoms.",
                     "Radiometric dating uses that steady rate as a clock."], size=17)
    out.append(s)
    s = Slide(3, 5, "Lab"); head(s, "Half-life lab · 12 min · with a partner", "Shake, spill, and remove the “decayed” coins", lesson)
    bullets(s, "b", ["Put 50 coins in a cup. Each coin is a parent atom.", "Shake and spill. Remove every coin that landed marked side up. Count what is left.",
                     "Repeat for 6 rounds. Record each round.", "Graph atoms left against round. If one round is 5,730 years (carbon-14), how old is a sample with 1/8 left?"], size=17)
    out.append(s)
    s = Slide(3, 6, "Clocks"); head(s, "Which clock for which sample? · 4 min", "Each method works only for certain samples", lesson)
    table(s, "t", [["Method", "Half-life", "Good for"], ["Carbon-14", "5,730 years", "Once-living things younger than about 50,000 years"],
                   ["Uranium-235", "about 704 million years", "Zircon crystals in igneous rock; meteorites"],
                   ["Uranium-238", "about 4.47 billion years", "Zircon crystals in igneous rock; meteorites"]],
          y=1.7, widths=[1.9, 2.7, 4.4], align=["START", "START", "START"])
    note(s, "q", "Zircon takes in uranium but not lead when it forms, so any lead came from decay. Best method for a 9,000-year-old spear? A 3-billion-year-old zircon? A 20,000-year-old tusk?", y=3.8, h=1.2, size=15)
    out.append(s)
    s = Slide(3, 7, "Oldest"); head(s, "The oldest materials · 8 min", "Meteorites are older than any rock found on Earth", lesson)
    table(s, "t", [["Material", "Age"], ["Meteorites (Canyon Diablo)", "about 4.56 billion years"], ["Moon rocks (lunar highlands)", "up to about 4.4 billion years"],
                   ["Oldest Earth mineral (zircon)", "about 4.4 billion years"], ["Oldest known Earth rock", "about 4.0 billion years"],
                   ["Oldest widely accepted fossils", "about 3.5 billion years"], ["Oldest ocean floor", "about 180–200 million years"]],
          y=1.65, widths=[5.0, 4.0], align=["START", "START"])
    out.append(s)
    s = Slide(3, 8, "Timeline"); head(s, "45-meter timeline · with a partner", "Where do these events fall on Earth's history?", lesson)
    note(s, "rule", "1 m = 100 million years.  Position = (4,500 − age in millions of years) ÷ 100", y=1.6, h=0.4, size=14)
    table(s, "t", [["Event", "Age (million years)", "Position"], ["Earth forms", "4,500", "0 m"], ["Oldest mineral", "4,400", "1 m"],
                   ["Oldest known rock", "4,000", "?"], ["Oldest fossils", "3,500", "?"], ["Oldest ocean floor", "200", "?"], ["Today", "0", "45 m"]],
          y=2.05, widths=[4.2, 2.8, 2.0], align=["START", "END", "END"])
    out.append(s)
    s = Slide(3, 9, "Craters"); head(s, "The impact-crater record · 6 min", "More craters means an older surface", lesson)
    table(s, "t", [["Surface", "What it looks like", "Age"],
                   ["Moon highlands", "Overlapping craters", "about 4.4 billion years or more"],
                   ["Moon dark plains", "Far fewer craters", "about 3.2 to 3.9 billion years"],
                   ["Mars southern highlands", "Heavily cratered", "about 3.7 billion years or more"],
                   ["Earth", "About 190 known craters; most eroded or buried", "Surface is renewed constantly"]],
          y=1.65, widths=[2.6, 3.4, 3.0], align=["START", "START", "START"])
    note(s, "q", "Earth was hit as often as the Moon. Why does it show so few craters?", y=4.4, h=0.6, size=15)
    out.append(s)
    s = Slide(3, 10, "Why"); head(s, "Why meteorites and moon rocks? · 5 min", "Why does the oldest Earth rock not give Earth's age?", lesson)
    bullets(s, "b", ["Plate tectonics, erosion, and weathering recycled Earth's earliest rocks.",
                     "Meteorites formed with the solar system and changed little. The Moon is geologically quiet, so it kept its early rocks.",
                     "Why are there no fossils as old as 3.5 billion years in the ocean floor?",
                     "Tomorrow starts with CFA ESS1-6.1 and CFA ESS1-6.2. Study your half-life data and the oldest-materials table."], size=16)
    out.append(s)
    return out


def build_day4():
    lesson = "Lesson 4 · Why the Ocean Is Young and the Continents Old"
    out = [title_slide(4, "Why the Ocean Is Young and the Continents Old", "How is ocean crust made, grown, and recycled, and how do continents grow and survive?",
                       "Have ready: SketchNotes paper, colored pencils.")]
    out.append(goals_slide(4, 2, lesson,
                           ["use density to explain why ocean crust sinks and continents stay", "explain why continents are oldest at their cores", "connect subduction to the carbon cycle"],
                           [["10", "CFAs ESS1-6.1 and 6.2"], ["2", "Warm-up"], ["8", "Density and subduction"], ["5", "Life of ocean crust"], ["8", "How continents grow"], ["3", "Carbon link"], ["9", "SketchNotes"]]))
    out.append(cfa_slide(4, 3, lesson, ["ESS1-6.1", "ESS1-6.2"], 10))
    s = Slide(4, 4, "Warm-up"); head(s, "Warm-up · 2 min · on your own", "Where does the old ocean crust go?", lesson)
    card(s, "q", "You know the ocean floor is under 200 million years old. Where does the old ocean crust go, and what must be different about the continents?", size=20)
    out.append(s)
    s = Slide(4, 5, "Density"); head(s, "Why some crust sinks · 8 min", "The denser plate sinks beneath the less-dense plate", lesson)
    table(s, "t", [["Material", "Average density"], ["Ocean crust (basalt)", "about 3.0 g/cm³"], ["Continental crust (granite)", "about 2.7 g/cm³"]],
          w=5.0, widths=[3.0, 2.0], align=["START", "END"], y=1.7)
    bullets(s, "b", ["Which plate sinks when an ocean plate meets a continent?", "What happens when two continents collide?", "Use density to explain why the ocean floor is under 200 million years old and continents are not."],
            y=3.25, h=1.8, size=15, gap=5)
    out.append(s)
    s = Slide(4, 6, "Life"); head(s, "The life of ocean crust · 5 min", "Made at a ridge, moved at about 25 km per million years, sunk at a trench", lesson)
    bullets(s, "b", ["A piece of crust travels 3,000 km from the Mid-Atlantic Ridge. How long does the trip take?",
                     "At the same rate, how far can crust travel in 200 million years?",
                     "Explain why no ocean floor is older than that, even though the ocean basins are much older."], size=18)
    out.append(s)
    s = Slide(4, 7, "Grow"); head(s, "How continents grow · 8 min", "Continents grow outward from an ancient core", lesson)
    bullets(s, "b", ["Each continent has an ancient core. Volcanic arcs and pieces of crust crash into its edge and are added to it, like rings on a tree.",
                     "Why is the crust at the edge younger than the crust at the core?",
                     "Draw a cross-section: an ancient core, a younger belt next to it, and a subduction zone at the edge.",
                     "Compare ocean crust (made, moves, destroyed) with continental crust (core, growth, survival)."], size=16, gap=8)
    out.append(s)
    s = Slide(4, 8, "Carbon"); head(s, "What rides the plate down · 3 min", "Plankton shells carry carbon into the mantle", lesson)
    bullets(s, "b", ["Seafloor sediment includes the shells of dead plankton, which contain carbon.", "Subduction carries some of it down. Some returns to the air as CO₂ when volcanoes erupt.",
                     "Connect to Unit 1.2: is carbon lost? Explain."], size=18)
    out.append(s)
    s = Slide(4, 9, "SketchNotes"); head(s, "SketchNotes · 9 min", "Half a page of notes and a labeled cross-section", lesson)
    bullets(s, "b", ["Notes: the life of ocean crust and how continents grow.", "Sensemaking page: a ridge, a plate moving away, a trench, a volcanic arc, and a continent with an ancient core and a younger edge.",
                     "Label density and add an arrow for where a plankton shell's carbon goes.", "Photograph your SketchNotes and turn them in: Lesson 4: SketchNotes.",
                     "Tomorrow starts with CFA ESS1-5.3. Finish your Frayer cards tonight."], size=16, gap=7)
    out.append(s)
    return out


def build_day5():
    lesson = "Lesson 5 · Evidence for Moving Crust"
    out = [title_slide(5, "Evidence for Moving Crust", "How strong is the evidence that the crust has moved and is still moving?", "Have ready: scissors, red and blue pencils, a ruler.")]
    out.append(goals_slide(5, 2, lesson,
                           ["use rock ages, magnetic stripes, and measured motion as evidence", "decide how strong each line of evidence is", "explain why independent lines that agree are stronger"],
                           [["7", "CFA ESS1-5.3"], ["3", "Warm-up"], ["10", "Magnetic stripes model"], ["8", "Measured motion"], ["5", "Fossils and rocks"], ["11", "Evaluate the evidence"]]))
    out.append(cfa_slide(5, 3, lesson, ["ESS1-5.3"], 7))
    s = Slide(5, 4, "Warm-up"); head(s, "Warm-up · 3 min · on your own", "How could you show that crust moved?", lesson)
    card(s, "q", "How could a scientist show that a continent or the seafloor moved millions of years ago? How could they show it is moving today? List two ideas for each.", size=20)
    out.append(s)
    s = Slide(5, 5, "Strips"); head(s, "Evidence A: magnetic stripes · make the strips", "Two identical 12 cm strips, oldest band first", lesson)
    table(s, "t", [["Band", "Color", "Length", "Age it represents"], ["1 (push in first)", "Reversed (blue)", "3.4 cm", "3.6–5.3 million years"],
                   ["2", "Normal (red)", "2.0 cm", "2.6–3.6 million years"], ["3", "Reversed (blue)", "3.6 cm", "0.8–2.6 million years"],
                   ["4 (last)", "Normal (red)", "1.6 cm", "0–0.8 million years"]],
          widths=[2.2, 2.2, 1.4, 3.2], align=["START", "START", "END", "START"])
    note(s, "n", "Scale: 2 cm = 1 million years.", y=4.4, h=0.6)
    out.append(s)
    s = Slide(5, 6, "Model"); head(s, "Run the model · 10 min", "Pull the strips apart and watch the ridge work", lesson)
    bullets(s, "b", ["Cut a slit in a folded sheet. The slit is the mid-ocean ridge.",
                     "Hold the strips back to back and push them up through the slit. Pull them apart, one to each side. Draw what you see.",
                     "Where is the youngest crust? The oldest?",
                     "What does a mirror-image stripe pattern tell you about how the crust formed?"], size=17)
    out.append(s)
    s = Slide(5, 7, "Hawaii"); head(s, "Evidence B: measured motion · 8 min", "The Pacific plate moves over a fixed hot spot", lesson)
    table(s, "t", [["Volcano or island", "NW of Kīlauea (km)", "Oldest rock (million years)"], ["Kīlauea (active now)", "0", "0"], ["Oʻahu", "about 400", "about 4"],
                   ["Kauaʻi", "about 500", "about 5"], ["Midway Atoll", "about 2,500", "about 28"]],
          y=1.65, widths=[3.8, 2.6, 2.6], align=["START", "END", "END"])
    note(s, "q", "Find the rate from Kauaʻi and from Midway. Compare with GPS: about 7 to 8 cm per year. (1 km per million years = 0.1 cm per year.)", y=4.0, h=1.0, size=15)
    out.append(s)
    s = Slide(5, 8, "Fossils"); head(s, "Evidence C: matching fossils and rocks · 5 min", "The same fossils turn up on separated continents", lesson)
    table(s, "t", [["Organism", "Found in", "Age"],
                   ["Glossopteris (seed fern)", "S. America, Africa, India, Australia, Antarctica", "250–300 million years"],
                   ["Mesosaurus (freshwater reptile)", "S. America, southern Africa", "280 million years"],
                   ["Lystrosaurus (land animal)", "Africa, India, Antarctica", "250 million years"]],
          widths=[3.0, 3.8, 2.2], align=["START", "START", "START"])
    note(s, "q", "Heavy seeds, and a freshwater animal. Why are they good evidence that lands were once joined? What can fossils not tell you that GPS can?", y=3.9, h=1.1, size=15)
    out.append(s)
    s = Slide(5, 9, "Evaluate"); head(s, "Evaluate the evidence · 11 min", "How strong is each line of evidence?", lesson)
    table(s, "t", [["Line of evidence", "Measured?", "Past or present?", "Independent?", "Strength (1–4)"],
                   ["Rock ages across a ridge", "", "", "", ""], ["Magnetic stripes", "", "", "", ""],
                   ["GPS and Hawaiian islands", "", "", "", ""], ["Matching fossils and rocks", "", "", "", ""]],
          y=1.65, widths=[3.0, 1.4, 1.7, 1.5, 1.4], align=["START", "START", "START", "START", "START"])
    out.append(s)
    s = Slide(5, 10, "Wrap"); head(s, "Think and prepare", "Why do independent lines that agree make a stronger case?", lesson)
    bullets(s, "b", ["Which line is strongest for current motion? For past motion?",
                     "GPS says about 2 cm per year at Iceland. Rock ages say about 2.5. Why does the agreement matter?",
                     "Name one finding that would weaken the idea that the seafloor spreads from ridges.",
                     "Tomorrow starts with CFA ESS1-5.4: Evidence for moving crust."], size=17)
    out.append(s)
    return out


def build_day6():
    lesson = "Lesson 6 · Evaluate the Theory, Tell Earth's Story"
    out = [title_slide(6, "Evaluate the Theory, Tell Earth's Story", "How well does plate tectonics explain the ages of crustal rocks, and what story do ancient materials tell about Earth's formation?",
                       "Have ready: your Unit CER evidence log.")]
    out.append(goals_slide(6, 2, lesson,
                           ["judge how well plate tectonics explains rock ages", "write an argument with evidence from ocean and continents", "build an account of Earth's formation"],
                           [["7", "CFA ESS1-5.4"], ["4", "Sort evidence"], ["13", "Evaluate the theory"], ["7", "Peer feedback"], ["11", "Tell Earth's story"], ["3", "Preview CFAs"]]))
    out.append(cfa_slide(6, 3, lesson, ["ESS1-5.4"], 7))
    s = Slide(6, 4, "Sort"); head(s, "Sort your evidence · 4 min", "Put each row of your evidence log in a bucket", lesson)
    table(s, "t", [["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], ["", "", ""]],
          widths=[3.0, 3.0, 3.0], align=["START", "START", "START"])
    note(s, "q", "Look at your Day 1 claim. What would you change now?", y=3.4, h=1.3, size=18)
    out.append(s)
    s = Slide(6, 5, "Frames 1"); head(s, "Evaluate the theory · sentence frames 1 of 2", "Claim and evidence", lesson)
    bullets(s, "b", ["Claim: Plate tectonics explains the ages of Earth's crustal rocks (very well / partly / poorly) because ______.",
                     "Evidence 1 (ocean): The seafloor age data show ______.",
                     "Evidence 2 (ocean): The oldest ocean floor is only about ______ million years old because ______.",
                     "Evidence 3 (continents): Continental crust as old as ______ exists, and in North America the crust gets ______ toward the edges."], size=15, gap=8)
    out.append(s)
    s = Slide(6, 6, "Frames 2"); head(s, "Evaluate the theory · sentence frames 2 of 2", "Reasoning, limit, and counterclaim", lesson)
    bullets(s, "b", ["Reasoning: Because ocean plates are ______ than continental crust, they ______ at subduction zones, while continents ______.",
                     "Limit or counterclaim: One thing this evidence cannot show is ______. OR: Someone might say the ocean floor is young because ______. This does not fit because ______.",
                     "Submit your argument on Canvas: Unit 3.1 CER, Part A."], size=15, gap=8)
    out.append(s)
    s = Slide(6, 7, "Data"); head(s, "Data you may use", "Everything you need is in your evidence log and here", lesson)
    bullets(s, "b", ["Crust age rises from 0 to 120 million years across 3,000 km (about 2.5 cm per year). Oldest ocean floor: about 200 million years.",
                     "Oldest continental mineral: about 4.4 billion years. North America: about 2.7 billion years at the core, about 400 million in the Appalachians.",
                     "Ocean crust about 3.0 g/cm³; continental crust about 2.7 g/cm³. GPS about 2 cm per year; rock ages about 2.5.",
                     "Oldest fossils, about 3.5 billion years, are in continental rock."], size=15, gap=8)
    out.append(s)
    s = Slide(6, 8, "Peer"); head(s, "Peer feedback · 7 min", "Trade papers: one star and one step", lesson)
    bullets(s, "b", ["The claim says how well the theory explains the ages and gives a cause.", "Each piece of evidence is specific, and both ocean and continental crust are used.",
                     "The reasoning explains why the evidence supports the claim.", "A limit or a counterclaim is addressed with evidence."], size=16, gap=7)
    out.append(s)
    s = Slide(6, 9, "Cards"); head(s, "Tell Earth's story · evidence cards", "What does each piece of evidence show?", lesson)
    table(s, "t", [["Evidence card", "What it shows"],
                   ["Meteorites: about 4.56 billion years", "The solar system formed then"],
                   ["Moon highland rocks: to about 4.4 billion years; heavily cratered", "Early crust and many impacts"],
                   ["Earth's oldest zircons: about 4.4 billion years", "Solid crust existed on Earth"],
                   ["Oldest Earth rock: about 4.0 billion years", "Rock has survived in the continents"],
                   ["Oldest fossils: about 3.5 billion years", "Life existed"],
                   ["Oldest ocean floor: about 200 million years", "Ocean crust is recycled"]],
          y=1.65, widths=[5.6, 3.4], align=["START", "START"])
    out.append(s)
    s = Slide(6, 10, "Story"); head(s, "Tell Earth's story · 11 min", "Build your account with these frames", lesson)
    bullets(s, "b", ["About ______ billion years ago, ______ happened. The evidence is ______. (Write three of these, in order.)",
                     "Earth's earliest record is missing because ______. Scientists fill the gap with evidence from ______.",
                     "Submit on Canvas: Unit 3.1 CER, Part B.",
                     "Next: CFA ESS1-5.5 and CFA ESS1-6.3, on the work day or at the start of Day 7."], size=16, gap=8)
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
    bullets(s, "b", ["Have not taken a CFA yet? Take it now, including CFA ESS1-5.5 and CFA ESS1-6.3.", "A Mastery Path review opened for you? Do it now. Study your notebook first.",
                     "No reviews open? Your teacher may assign the enrichment choice board.", "Everyone: finish your Frayer cards, your evidence log, and your CER."], size=17)
    out.append(s)
    s = Slide(7, 5, "Vocab"); head(s, "Vocabulary self-check · 5 min", "Cover the definitions. Explain each word aloud.", lesson)
    bullets(s, "l", ["lithosphere (plate)", "plate boundary", "mid-ocean ridge", "subduction", "trench"], x=0.5, y=1.7, w=4.3, h=2.5, size=18, gap=6)
    bullets(s, "r", ["magnetic reversal", "craton", "radiometric dating", "half-life", "impact crater"], x=5.0, y=1.7, w=4.5, h=2.5, size=18, gap=6)
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
