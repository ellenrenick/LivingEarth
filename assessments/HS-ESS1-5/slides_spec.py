"""Slide content for the eight Unit 3.1 lesson decks (HS-ESS1-5).

Writes one slides_helper.py build spec per day (inch-based) plus a small meta file with each
slide's background. Style follows the Unit 1.3 lesson decks: dark-green title slide, cream
content slides, Domine headings, Nunito Sans body text, rust kicker line.

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
        self.id = f"lesson{day}_s{n}"
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


def title_slide(day, lesson_no, title, focus, note):
    s = Slide(day, 1, title, dark=True)
    s.add("kick", "text", 0.6, 0.85, 8.8, 0.48, text=f"{UNIT}  ·  LESSON {lesson_no}".upper(), size=14, bold=True, color="#EBA36B", font=BODY)
    s.add("title", "text", 0.6, 1.4, 8.8, 1.5, text=title, size=36, bold=True, color="#EFF7EF", font=HEAD)
    s.add("focus", "text", 0.6, 3.1, 8.8, 0.9, text=f"Focus question: {focus}", size=18, color="#C9D8CC", font=BODY)
    s.add("note", "text", 0.6, 4.7, 8.8, 0.4, text=note, size=14, color="#C9D8CC", font=BODY)
    return s


def goals_slide(day, n, lesson, can, plan):
    s = Slide(day, n, "Goals and plan")
    head(s, "Today", "Goals and plan", lesson)
    s.add("can_h", "text", 0.5, 1.65, 4.3, 0.5, text="I can…", size=16, bold=True, color=INK, font=BODY)
    bullets(s, "can", can, x=0.5, y=2.15, w=4.3, h=2.9, size=16, gap=8)
    table(s, "plan", [["Min", "Plan"]] + plan, x=5.1, y=1.7, w=4.4, widths=[0.8, 3.6], align=["START", "START"])
    return s


def build_day1():
    lesson = "Lesson 1 · Where Did the Old Ocean Floor Go?"
    out = [title_slide(1, 1, "Where Did the Old Ocean Floor Go?", "How old is the ocean floor compared with the continents?",
                       "Have ready: your notebook and a pencil.")]
    out.append(goals_slide(1, 2, lesson,
                           ["compare the ages of the ocean floor and the continents", "start a claim that explains the difference", "preview the unit vocabulary"],
                           [["5", "Warm-up: guess"], ["10", "The phenomenon"], ["10", "45-meter timeline"], ["10", "Mystery and first claim"], ["8", "Vocabulary preview"], ["2", "Exit ticket"]]))
    s = Slide(1, 3, "Warm-up"); head(s, "Warm-up · 5 min · on your own", "Take a guess before we look at data", lesson)
    card(s, "q", "Earth is about 4.5 billion years old. Guess the age of (a) the oldest ocean floor and (b) the oldest rock or mineral on the continents. Give one reason for each.", size=20)
    out.append(s)
    s = Slide(1, 4, "Ocean floor"); head(s, "Phenomenon · the ocean floor", "The oldest ocean floor is only about 180 million years old", lesson)
    table(s, "t", [["Place on the ocean floor", "Age of the rock"]] + [[r[0], r[1]] for r in [
        ["Right at the Mid-Atlantic Ridge", "0 (forming now)"],
        ["Middle of the Atlantic, 2,000 km from the ridge", "about 80 million years"],
        ["Atlantic floor next to eastern North America", "about 180 million years"],
        ["Right at the East Pacific Rise", "0 (forming now)"],
        ["Western Pacific, east of Japan", "about 180 million years"]]], widths=[5.6, 3.4], align=["START", "START"])
    s.add("note", "text", 0.5, 4.5, 9, 0.5, text="Ages are rounded. In your notebook: what do you notice? What do you wonder?", size=16, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(1, 5, "Continents"); head(s, "Phenomenon · the continents and life", "Continental rock and fossils go back billions of years", lesson)
    table(s, "t", [["Continental material", "Where", "Age"]] + [
        ["Oldest mineral (zircon)", "Western Australia", "about 4.4 billion years"],
        ["Oldest known rock (Acasta Gneiss)", "Canada", "about 4.0 billion years"],
        ["Very old rock (Isua belt)", "Greenland", "about 3.8 billion years"],
        ["Oldest widely accepted fossils", "Western Australia", "about 3.5 billion years"]],
          widths=[3.9, 2.3, 2.8], align=["START", "START", "START"])
    s.add("note", "text", 0.5, 4.3, 9, 0.7, text="Compare with the ocean floor. Add what you notice and wonder to your table.", size=16, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(1, 6, "Timeline"); head(s, "Scale it · 10 min · with a partner", "On a 45 m timeline, all surviving ocean floor fits in the last 2 m", lesson)
    s.add("rule", "text", 0.5, 1.6, 9, 0.4, text="1 m = 100 million years.  Position = (4,500 − age in millions of years) ÷ 100", size=14, color=GRAY, font=BODY)
    table(s, "t", [["Event", "Age (million years)", "Position"], ["Earth forms", "4,500", "0 m"], ["Oldest mineral", "4,400", "1 m"],
                   ["Oldest known rock", "4,000", "?"], ["Oldest fossils", "3,500", "?"], ["Oldest ocean floor", "200", "?"], ["Today", "0", "45 m"]],
          y=2.05, widths=[4.2, 2.8, 2.0], align=["START", "END", "END"])
    out.append(s)
    s = Slide(1, 7, "Claim"); head(s, "The mystery · 10 min · on your own", "Why is the seafloor so much younger than the continents?", lesson)
    bullets(s, "b", ["Draw a cross-section: an ocean between two continents. Show where ocean floor might come from and where it might go.",
                     "Write your first claim for the Unit CER.", "It is fine if it is wrong. We will revise it all unit."])
    out.append(s)
    s = Slide(1, 8, "Vocabulary"); head(s, "Vocabulary preview · 8 min · exit ticket · 2 min", "Ten words you will use all unit", lesson)
    bullets(s, "l", ["continental drift", "seafloor spreading", "mid-ocean ridge", "subduction", "trench"], x=0.5, y=1.7, w=4.3, h=2.2, size=18, gap=6)
    bullets(s, "r", ["magnetic reversal", "plate boundary", "radiometric dating", "half-life", "fossil record"], x=5.0, y=1.7, w=4.5, h=2.2, size=18, gap=6)
    card(s, "exit", "Exit ticket: name one thing you could measure or observe that would test your claim.", y=4.0, h=1.0, size=16, font=BODY, bold=True)
    out.append(s)
    return out


def build_day2():
    lesson = "Lesson 2 · The Fossil Puzzle"
    out = [title_slide(2, 2, "The Fossil Puzzle", "What evidence shows that the continents were once joined?", "Have ready: scissors, tape, colored pencils, your notebook.")]
    out.append(goals_slide(2, 2, lesson,
                           ["describe fossil, rock, mountain, and glacier evidence for continental drift", "explain why the continents fit best at the shelf edge"],
                           [["4", "Warm-up"], ["8", "Wegener's idea"], ["23", "Fossil puzzle lab"], ["4", "More evidence"], ["6", "CFA ESS1-5.1"]]))
    s = Slide(2, 3, "Warm-up"); head(s, "Warm-up · 4 min · on your own", "Could a freshwater reptile swim across the Atlantic?", lesson)
    card(s, "q", "Mesosaurus, a small reptile that lived in fresh water, left fossils in both Brazil and South Africa. Could it have swum across the Atlantic? Explain.", size=20)
    out.append(s)
    s = Slide(2, 4, "Wegener"); head(s, "Wegener's idea · 1912", "Alfred Wegener: the continents were once joined as Pangaea", lesson)
    bullets(s, "b", ["Pangaea means “all land.”", "He proposed the continents slowly drifted apart. This is continental drift.", "Today you test his idea with evidence."])
    out.append(s)
    s = Slide(2, 5, "Lab"); head(s, "Fossil puzzle lab · 23 min · with a partner", "Fit the continents, then plot the fossils", lesson)
    bullets(s, "b", ["Cut out the southern continents along the edge of the continental shelf (the dashed line), not the coastline.",
                     "Fit the pieces together along the shelf edges and tape them down.",
                     "Use a different color for each fossil. Shade where it has been found.",
                     "Describe what you see: do the colors form one continuous pattern?"], size=17)
    out.append(s)
    s = Slide(2, 6, "Fossils"); head(s, "Fossil evidence", "The same four fossils turn up on separated continents", lesson)
    table(s, "t", [["Organism", "Found in", "Age"],
                   ["Glossopteris (seed fern)", "S. America, Africa, India, Australia, Antarctica", "250–300 million years"],
                   ["Mesosaurus (freshwater reptile)", "S. America, southern Africa", "280 million years"],
                   ["Lystrosaurus (land animal)", "Africa, India, Antarctica", "250 million years"],
                   ["Cynognathus (land animal)", "S. America, southern Africa", "240 million years"]],
          widths=[3.0, 3.8, 2.2], align=["START", "START", "START"])
    s.add("q", "text", 0.5, 4.4, 9, 0.7, text="Glossopteris had heavy seeds and Mesosaurus lived in fresh water. “They crossed a gap” or “there was no gap”? Use two pieces of evidence.", size=14, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(2, 7, "More evidence"); head(s, "More evidence · complete the last column", "Rocks, mountains, ice, and shelf edges all point to one landmass", lesson)
    table(s, "t", [["Evidence", "What scientists found", "What it suggests"],
                   ["Rock layers", "Same sequence of rock types and fossils on the southern continents", "?"],
                   ["Mountain belts", "Appalachians match mountains in Scotland and Scandinavia", "?"],
                   ["Glacial scratches", "Same ice-age scratches on five southern continents", "?"],
                   ["Shelf fit", "Shelf edges fit better than coastlines", "?"]],
          widths=[1.9, 5.3, 1.8], align=["START", "START", "START"])
    out.append(s)
    s = Slide(2, 8, "CFA"); head(s, "Wegener's weakness · then show what you know", "Why was Wegener's idea rejected for decades?", lesson)
    bullets(s, "b", ["He could not explain what force could move continents.", "What kind of evidence would scientists have needed?",
                     "Now take Unit 3.1 CFA ESS1-5.1: Evidence for continental drift on Canvas (5 questions).",
                     "Below 3 out of 4? A review opens for you."], size=17)
    out.append(s)
    return out


def build_day3():
    lesson = "Lesson 3 · Making New Crust"
    out = [title_slide(3, 3, "Making New Crust", "How is new ocean floor made, and what pattern does it leave behind?", "Have ready: graph paper, two paper strips, red and blue pencils.")]
    out.append(goals_slide(3, 2, lesson,
                           ["find the spreading rate from age and distance data", "model magnetic stripes at a mid-ocean ridge", "connect new crust to vents and sediment"],
                           [["5", "Warm-up: predict"], ["10", "Data, graph, and rate"], ["17", "Magnetic-stripe model"], ["5", "Life on new crust"], ["3", "Sediment"], ["5", "CFA ESS1-5.2"]]))
    s = Slide(3, 3, "Warm-up"); head(s, "Warm-up · 5 min · on your own", "Which rock is older, at the ridge or near Brazil?", lesson)
    card(s, "q", "A ship pulls up seafloor rock right at the Mid-Atlantic Ridge and another sample near the coast of Brazil. Which is older? Explain your prediction.", size=20)
    out.append(s)
    s = Slide(3, 4, "Data"); head(s, "The data · simplified from a rate of about 2.5 cm per year", "Crust gets older with distance from the ridge", lesson)
    table(s, "t", [["Distance from ridge (km)", "Crust age (million years)", "Sediment (m)"]] + [
        ["0", "0", "about 0"], ["500", "20", "about 50"], ["1,000", "40", "about 150"], ["1,500", "60", "about 250"],
        ["2,000", "80", "about 350"], ["2,500", "100", "about 450"], ["3,000", "120", "about 550"]],
          y=1.65, widths=[3.2, 3.2, 2.6], align=["END", "END", "END"])
    out.append(s)
    s = Slide(3, 5, "Rate"); head(s, "Graph it · 10 min · with a partner", "Find how fast the seafloor moves", lesson)
    bullets(s, "b", ["Graph crust age (y) against distance from the ridge (x). Describe the pattern.",
                     "Rate = distance ÷ time. (1 km per million years = 0.1 cm per year.)",
                     "Predict the age of crust 3,500 km from the ridge.",
                     "Graph sediment thickness against distance. Why is older crust covered with more sediment?"], size=17)
    out.append(s)
    s = Slide(3, 6, "Strips"); head(s, "Paper magnetic-stripe model · make the strips", "Two identical 12 cm strips, oldest band first", lesson)
    table(s, "t", [["Band", "Color", "Length", "Age it represents"], ["1 (push in first)", "Reversed (blue)", "3.4 cm", "3.6–5.3 million years"],
                   ["2", "Normal (red)", "2.0 cm", "2.6–3.6 million years"], ["3", "Reversed (blue)", "3.6 cm", "0.8–2.6 million years"],
                   ["4 (last)", "Normal (red)", "1.6 cm", "0–0.8 million years"]],
          widths=[2.2, 2.2, 1.4, 3.2], align=["START", "START", "END", "START"])
    s.add("n", "text", 0.5, 4.4, 9, 0.6, text="Scale: 2 cm = 1 million years.", size=16, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(3, 7, "Model"); head(s, "Run the model · 10 min", "Pull the strips apart and watch the ridge work", lesson)
    bullets(s, "b", ["Cut a slit in a folded sheet. The slit is the mid-ocean ridge.",
                     "Hold the strips back to back. Push them up through the slit from underneath.",
                     "Pull them slowly apart, one to each side. Draw what you see.",
                     "Where is the youngest crust? The oldest? Why are the two sides mirror images?"], size=17)
    out.append(s)
    s = Slide(3, 8, "Vents"); head(s, "Life on new crust · 5 min", "Vent communities live where the crust is new", lesson)
    bullets(s, "b", ["Magma near the ridge heats seawater, which rises through hydrothermal vents.",
                     "Bacteria use chemicals in the vent water for energy: chemosynthesis. Tube worms, clams, and shrimp live with them.",
                     "Individual vents last years to decades. Vent fields depend on heat found near the ridge.",
                     "Why are vent communities at the ridge but not on old seafloor? Use the age pattern."], size=17, gap=8)
    out.append(s)
    s = Slide(3, 9, "CFA"); head(s, "Show what you know", "CFA ESS1-5.2: Seafloor spreading and the age pattern", lesson)
    bullets(s, "b", ["Take the CFA on Canvas (5 questions).", "Below 3 out of 4? A review for this target opens for you.",
                     "Add a row to your Unit CER evidence log with a specific number from today."], size=18)
    out.append(s)
    return out


def build_day4():
    lesson = "Lesson 4 · Where Crust Goes, and Where It Stays"
    out = [title_slide(4, 4, "Where Crust Goes, and Where It Stays", "If new crust is made at ridges, where does old ocean crust go, and why do the continents stay?", "Have ready: world map, colored pencils, SketchNotes paper.")]
    out.append(goals_slide(4, 2, lesson,
                           ["use earthquakes and volcanoes to find plate boundaries", "explain why ocean crust sinks but continents stay", "connect subduction to the carbon cycle"],
                           [["4", "Warm-up"], ["16", "Plot the pattern"], ["10", "Why some crust sinks"], ["4", "Carbon link"], ["10", "SketchNotes"], ["1", "Tomorrow's CFA"]]))
    s = Slide(4, 3, "Warm-up"); head(s, "Warm-up · 4 min · on your own", "Where does the old ocean crust go?", lesson)
    card(s, "q", "Earth is not getting bigger, but new ocean crust is made at ridges all the time. Where could the old crust go?", size=22)
    out.append(s)
    sites_a = [[s_[0], s_[1], f"{s_[2]}, {s_[3]}"] for s_ in L.SITES[:7]]
    sites_b = [[s_[0], s_[1], f"{s_[2]}, {s_[3]}"] for s_ in L.SITES[7:]]
    s = Slide(4, 4, "Sites 1"); head(s, "Plot the pattern · sites 1–7", "Plot each site on your world map: volcano or earthquake?", lesson)
    table(s, "t", [["Site", "Type", "Latitude, longitude"]] + sites_a, y=1.6, widths=[4.6, 1.5, 2.9], align=["START", "START", "START"], size=14)
    out.append(s)
    s = Slide(4, 5, "Sites 2"); head(s, "Plot the pattern · sites 8–13", "Then decide which boundary type is nearest each site", lesson)
    table(s, "t", [["Site", "Type", "Latitude, longitude"]] + sites_b, y=1.6, widths=[4.6, 1.5, 2.9], align=["START", "START", "START"], size=14)
    s.add("q", "text", 0.5, 4.5, 9, 0.6, text="Which site does not fit the pattern? What could explain it?", size=16, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(4, 6, "Boundaries"); head(s, "Three kinds of plate boundaries", "Where plates move apart, together, or past each other", lesson)
    table(s, "t", [["Boundary", "Plates move…", "Landforms"], ["Divergent", "apart", "mid-ocean ridges, rift valleys"],
                   ["Convergent", "toward each other", "trenches, volcanic arcs, mountain ranges"], ["Transform", "past each other", "faults and earthquakes"]],
          widths=[2.2, 2.6, 4.2], align=["START", "START", "START"])
    out.append(s)
    s = Slide(4, 7, "Density"); head(s, "Why some crust sinks · 10 min", "The denser plate sinks beneath the less-dense plate", lesson)
    table(s, "t", [["Material", "Average density"], ["Ocean crust (basalt)", "about 3.0 g/cm³"], ["Continental crust (granite)", "about 2.7 g/cm³"]],
          w=5.0, widths=[3.0, 2.0], align=["START", "END"], y=1.7)
    bullets(s, "b", ["Which plate sinks when an ocean plate meets a continent?", "What happens when two continents collide?", "Use density to explain why ocean floor is under 200 million years old and continents are not."],
            y=3.25, h=1.8, size=15, gap=5)
    out.append(s)
    s = Slide(4, 8, "Carbon"); head(s, "What rides the plate down · 4 min", "Plankton shells carry carbon into the mantle", lesson)
    bullets(s, "b", ["Seafloor sediment includes the shells of dead plankton, which contain carbon.", "Subduction carries some of it down. Some returns to the air as CO₂ when volcanoes erupt.",
                     "Connect to Unit 1.2: is carbon lost? Explain."], size=18)
    out.append(s)
    s = Slide(4, 9, "SketchNotes"); head(s, "SketchNotes · 10 min", "Half a page of notes and a labeled subduction zone", lesson)
    bullets(s, "b", ["Notes: the three boundary types with a landform for each.", "Sensemaking page: a subduction zone with the trench, sinking plate, volcanic arc, and density labels.",
                     "Add an arrow showing where a plankton shell's carbon goes.", "Photograph your SketchNotes and turn them in: Lesson 4: SketchNotes.",
                     "Tomorrow starts with CFA ESS1-5.3. Finish your Frayer cards tonight."], size=16, gap=7)
    out.append(s)
    return out


def build_day5():
    lesson = "Lesson 5 · Reading Deep Time"
    out = [title_slide(5, 5, "Reading Deep Time", "How do scientists find the age of a rock, and why are the oldest Earth rocks younger than Earth?", "Have ready: 50 coins, a cup, graph paper.")]
    out.append(goals_slide(5, 2, lesson,
                           ["explain how half-life is used to date rocks", "choose the right dating method for a sample", "explain why meteorites are older than any Earth rock"],
                           [["8", "CFA ESS1-5.3"], ["4", "Hook and definitions"], ["18", "Half-life lab"], ["7", "Which clock?"], ["8", "Oldest materials"]]))
    s = Slide(5, 3, "CFA"); head(s, "Start with a CFA · 8 min", "CFA ESS1-5.3: Plate boundaries and subduction", lesson)
    bullets(s, "b", ["Take the CFA on Canvas now (5 questions).", "Below 3 out of 4? A review for this target opens for you."], size=20)
    out.append(s)
    s = Slide(5, 4, "Hook"); head(s, "Hook · 4 min", "How can anyone know Earth is 4.5 billion years old?", lesson)
    bullets(s, "b", ["Some atoms are unstable. They change into a different kind of atom at a steady rate: radioactive decay.",
                     "Half-life: the time for half of the parent atoms in a sample to decay into daughter atoms.",
                     "Radiometric dating uses that steady rate as a clock."], size=17)
    out.append(s)
    s = Slide(5, 5, "Lab"); head(s, "Half-life lab · 18 min · with a partner", "Shake, spill, and remove the “decayed” coins", lesson)
    bullets(s, "b", ["Put 50 coins in a cup. Each coin is a parent atom.", "Shake and spill. Remove every coin that landed marked side up. Count what is left.",
                     "Repeat for 6 rounds. Record each round.", "Graph atoms left against round. If one round is 5,730 years (carbon-14), how old is a sample with 1/8 left?"], size=17)
    out.append(s)
    s = Slide(5, 6, "Clocks"); head(s, "Which clock for which sample? · 7 min", "Each method works only for certain samples", lesson)
    table(s, "t", [["Method", "Half-life", "Good for"], ["Carbon-14", "5,730 years", "Once-living things younger than about 50,000 years"],
                   ["Uranium-235", "about 704 million years", "Zircon crystals in igneous rock; meteorites"],
                   ["Uranium-238", "about 4.47 billion years", "Zircon crystals in igneous rock; meteorites"]],
          y=1.7, widths=[1.9, 2.7, 4.4], align=["START", "START", "START"])
    s.add("q", "text", 0.5, 3.8, 9, 1.2, text="Zircon takes in uranium but not lead when it forms, so any lead came from decay.\nBest method for: a 9,000-year-old spear, a 3-billion-year-old zircon, a 20,000-year-old tusk?", size=15, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(5, 7, "Oldest"); head(s, "The oldest materials · 8 min", "Meteorites are older than any rock found on Earth", lesson)
    table(s, "t", [["Material", "Age"], ["Meteorites (Canyon Diablo)", "about 4.56 billion years"], ["Moon rocks (lunar highlands)", "up to about 4.4 billion years"],
                   ["Oldest Earth mineral (zircon)", "about 4.4 billion years"], ["Oldest known Earth rock", "about 4.0 billion years"],
                   ["Oldest widely accepted fossils", "about 3.5 billion years"], ["Oldest ocean floor", "about 180–200 million years"]],
          y=1.65, widths=[5.0, 4.0], align=["START", "START"])
    out.append(s)
    s = Slide(5, 8, "Tomorrow"); head(s, "Think and prepare", "Why does the oldest Earth rock not give Earth's age?", lesson)
    bullets(s, "b", ["Plate tectonics and erosion recycled Earth's earliest rocks. Meteorites formed with the solar system and changed little.",
                     "Why are there no fossils as old as 3.5 billion years in the ocean floor?",
                     "Tomorrow starts with CFA ESS1-6.1: Radiometric dating and Earth's oldest rocks. Study your half-life data and the clock table."], size=16)
    out.append(s)
    return out


def build_day6():
    lesson = "Lesson 6 · Build the Argument"
    out = [title_slide(6, 6, "Build the Argument", "How do I use evidence and reasoning to answer the unit question?", "Have ready: your Unit CER evidence log.")]
    out.append(goals_slide(6, 2, lesson,
                           ["sort my evidence into a claim, evidence, and reasoning", "write a complete argument", "give and use peer feedback"],
                           [["8", "CFA ESS1-6.1"], ["5", "Sort evidence"], ["14", "Write the argument"], ["11", "Peer feedback"], ["7", "CFA ESS1-5.4"]]))
    s = Slide(6, 3, "CFA"); head(s, "Start with a CFA · 8 min", "CFA ESS1-6.1: Radiometric dating and Earth's oldest rocks", lesson)
    bullets(s, "b", ["Take the CFA on Canvas now (5 questions).", "Below 3 out of 4? A review for this target opens for you."], size=20)
    out.append(s)
    s = Slide(6, 4, "Sort"); head(s, "Sort your evidence · 5 min", "Put each row of your evidence log in a bucket", lesson)
    table(s, "t", [["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], ["", "", ""]],
          widths=[3.0, 3.0, 3.0], align=["START", "START", "START"])
    s.add("q", "text", 0.5, 3.4, 9, 1.3, text="Look at your Day 1 claim. What would you change now?", size=18, color=GRAY, font=BODY)
    out.append(s)
    s = Slide(6, 5, "Frames 1"); head(s, "Write your argument · sentence frames 1 of 2", "Claim and evidence", lesson)
    bullets(s, "b", ["Claim: The ocean floor is much younger than the continents because ______.",
                     "Evidence 1 (pattern): The seafloor age data show ______.",
                     "Evidence 2 (numbers): At a rate of about ______, rock ______ km from the ridge is about ______ million years old.",
                     "Evidence 3 (continents): Continental rocks and minerals as old as ______ exist because ______."], size=16, gap=8)
    out.append(s)
    s = Slide(6, 6, "Frames 2"); head(s, "Write your argument · sentence frames 2 of 2", "Reasoning and counterclaim", lesson)
    bullets(s, "b", ["Reasoning: Because ocean plates are ______ than continental crust, they ______ at subduction zones, so ______.",
                     "Counterclaim: Someone might say the ocean floor is young because ______. This does not fit the evidence because ______.",
                     "Submit your argument on Canvas: Unit 3.1 CER."], size=16, gap=8)
    out.append(s)
    s = Slide(6, 7, "Data"); head(s, "Data you may use", "Everything you need is in your evidence log and here", lesson)
    bullets(s, "b", ["Crust age rises from 0 to 120 million years across 3,000 km (about 2.5 cm per year).", "Oldest ocean floor: about 200 million years. Oldest continental mineral: about 4.4 billion years.",
                     "Ocean crust about 3.0 g/cm³; continental crust about 2.7 g/cm³.", "Oldest fossils, about 3.5 billion years, are in continental rock. Meteorites: about 4.56 billion years."], size=16, gap=8)
    out.append(s)
    s = Slide(6, 8, "Peer"); head(s, "Peer feedback · 11 min", "Trade papers: one star and one step", lesson)
    bullets(s, "b", ["The claim answers the question completely and names the cause.", "Each piece of evidence is specific: a number or a named pattern.", "At least two different kinds of evidence.",
                "The reasoning explains why the evidence supports the claim.", "A counterclaim is answered with evidence."], size=16, gap=7)
    out.append(s)
    s = Slide(6, 9, "CFA2"); head(s, "Show what you know · 7 min", "CFA ESS1-5.4: Argue why the seafloor is young and the continents are old", lesson)
    bullets(s, "b", ["Take the CFA on Canvas (5 questions).", "Below 3 out of 4? A review for this target opens for you."], size=20)
    out.append(s)
    return out


def build_day7():
    lesson = "Lesson 7 · Review Day"
    out = [title_slide(7, 7, "Review Day", "Which targets do I still need to work on before the CSA tomorrow?", "Have ready: your notebook, Frayer cards, and Chromebook.")]
    s = Slide(7, 2, "Plan"); head(s, "Today", "Plan", lesson)
    table(s, "t", [["Min", "Plan"], ["5", "Rate yourself on each target"], ["33", "Work time matched to your CFA scores"], ["5", "Vocabulary self-check with a partner"], ["2", "Preview the CSA"]],
          widths=[1.0, 8.0], align=["START", "START"])
    out.append(s)
    s = Slide(7, 3, "Rate"); head(s, "Rate yourself · 5 min", "1 = I need help, 4 = I could teach it", lesson)
    table(s, "t", [["Target", "Rating (1–4)"], ["ESS1-5.1  Evidence for continental drift", ""], ["ESS1-5.2  Seafloor spreading and the age pattern", ""],
                   ["ESS1-5.3  Plate boundaries and subduction", ""], ["ESS1-6.1  Radiometric dating", ""], ["ESS1-5.4  The argument", ""]],
          widths=[7.0, 2.0], align=["START", "START"])
    out.append(s)
    s = Slide(7, 4, "Work"); head(s, "Work time · 33 min", "Do the work that matches your scores", lesson)
    bullets(s, "b", ["Have not taken a CFA yet? Take it now.", "A Mastery Path review opened for you? Do it now. Study your notebook first.",
                     "No reviews open? Your teacher may assign the enrichment choice board.", "Everyone: finish your Frayer cards and your Unit CER evidence log."], size=18)
    out.append(s)
    s = Slide(7, 5, "Vocab"); head(s, "Vocabulary self-check · 5 min", "Cover the definitions. Explain each word aloud.", lesson)
    bullets(s, "l", ["continental drift", "seafloor spreading", "mid-ocean ridge", "subduction", "trench"], x=0.5, y=1.7, w=4.3, h=2.5, size=18, gap=6)
    bullets(s, "r", ["magnetic reversal", "plate boundary", "radiometric dating", "half-life", "fossil record"], x=5.0, y=1.7, w=4.5, h=2.5, size=18, gap=6)
    out.append(s)
    s = Slide(7, 6, "CSA"); head(s, "Tomorrow", "Unit 3.1 CSA", lesson)
    bullets(s, "b", ["Study your notebook, your CFA results, and your reviews tonight.", "Bring a pencil and a charged Chromebook."], size=20)
    out.append(s)
    return out


def build_day8():
    lesson = "Lesson 8 · Unit 3.1 CSA"
    out = [title_slide(8, 8, "Unit 3.1 CSA", "What do you know about the age of Earth's crust?", "Chromebook open to Canvas. Pencil ready.")]
    s = Slide(8, 2, "About"); head(s, "About the CSA", "16 questions on all five targets", lesson)
    bullets(s, "b", ["14 multiple-choice, select-all, and true/false questions.", "2 written responses: a claim-evidence-reasoning argument using data, and a revision of an explanation.",
                     "Open Unit 3.1 CSA: Age of the Earth (HS-ESS1-5) on Canvas when your teacher says to begin."], size=18)
    out.append(s)
    s = Slide(8, 3, "Tips"); head(s, "To do your best", "Read carefully and use the data", lesson)
    bullets(s, "b", ["Read each question and every answer choice before you choose.", "Use the numbers in the question: distances, ages, and densities.",
                     "For written answers: make a claim, support it with two specific pieces of evidence, and explain why they support it."], size=18)
    out.append(s)
    s = Slide(8, 4, "Done"); head(s, "When you finish", "Check your written answers, then work quietly", lesson)
    bullets(s, "b", ["Reread Q14 and Q16.", "Work quietly on any missing Canvas work.", "A target below 3 gets an intervention and a chance to reassess."], size=18)
    out.append(s)
    return out


DECKS = {
    1: ("Unit 3.1 Lesson 1: Where Did the Old Ocean Floor Go?", build_day1),
    2: ("Unit 3.1 Lesson 2: The Fossil Puzzle", build_day2),
    3: ("Unit 3.1 Lesson 3: Making New Crust", build_day3),
    4: ("Unit 3.1 Lesson 4: Where Crust Goes, and Where It Stays", build_day4),
    5: ("Unit 3.1 Lesson 5: Reading Deep Time", build_day5),
    6: ("Unit 3.1 Lesson 6: Build the Argument", build_day6),
    7: ("Unit 3.1 Lesson 7: Review Day", build_day7),
    8: ("Unit 3.1 Lesson 8: CSA", build_day8),
}


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
