"""Build "Plants Need More Than C, H, and O" (Lesson 2, Part 3 video) as an MP4.

Goes with the 5-10 minute "Who needs the soil?" quick sort that replaced the
11-card sort: CO2 and water bring in only C, H, and O, but proteins, DNA/RNA, and
chlorophyll also need N, P, Mg (and S), which a plant takes in from the soil.

  python3 more_than_cho_video.py out.mp4
"""

import sys

import atom_counting_video as V

V.COLORS.update({"P": (230, 125, 20), "Mg": (40, 150, 80), "S": (200, 165, 20)})
V.NAMES.update({"P": "phosphorus", "Mg": "magnesium", "S": "sulfur"})
W, H, INK, MUTED, HILITE = V.W, V.H, V.INK, V.MUTED, V.HILITE
GOOD, BAD = (46, 125, 50), (190, 50, 50)
TAN = (232, 220, 198)
KICKER = "LESSON 2 · PART 3 · WHO NEEDS THE SOIL?"

GLUCOSE = [("C", 6), ("H", 12), ("O", 6)]
OLEIC = [("C", 18), ("H", 34), ("O", 2)]
VALINE = [("C", 5), ("H", 11), ("N", 1), ("O", 2)]
AMP = [("C", 10), ("H", 14), ("N", 5), ("O", 7), ("P", 1)]
CHLOROPHYLL = [("C", 55), ("H", 72), ("Mg", 1), ("N", 4), ("O", 5)]

# (big-molecule type, examples, elements, example name, formula)
TYPES = [
    ("Carbohydrates", "sugar, starch, cellulose", "C H O", "glucose", GLUCOSE),
    ("Lipids", "fats and oils", "C H O", "oleic acid (a fat)", OLEIC),
    ("Proteins", "built from amino acids", "C H O N (+ S)", "valine (an amino acid)", VALINE),
    ("Nucleic acids", "DNA and RNA", "C H O N P", "AMP (a piece of RNA)", AMP),
]


def chip(d, x, y, w, h, text, fill, color=INK, size=30):
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill, outline=(160, 150, 130), width=2)
    d.text((x + w / 2, y + h / 2), text, font=V.font(size, True), fill=color, anchor="mm")


SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def formula(parts):
    return "".join(s + (str(n).translate(SUB) if n > 1 else "") for s, n in parts)


def soil_needed(elements):
    return any(e in elements for e in ("N", "P", "Mg", "S"))


def draw_types(d, upto, judge=False):
    y0 = 180
    for c, (x, label) in enumerate([(90, "Big molecule"), (450, "Examples"), (800, "Elements")]):
        d.text((x, y0), label, font=V.font(26, True), fill=MUTED)
    if judge:
        d.text((1050, y0), "CO₂ + H₂O only?", font=V.font(22, True), fill=MUTED)
    for i, (name, ex, els, _, _) in enumerate(TYPES[:upto]):
        y = y0 + 50 + i * 95
        d.rounded_rectangle([70, y - 8, 1210, y + 72], radius=14, fill=(255, 255, 255), outline=(200, 190, 170), width=2)
        d.text((90, y + 32), name, font=V.font(34, True), fill=INK, anchor="lm")
        d.text((450, y + 32), ex, font=V.font(26), fill=INK, anchor="lm")
        x = 800
        for e in els.split():
            col = V.COLORS.get(e.strip("(+)"), INK) if e.strip("(+)") != "H" else (120, 120, 120)
            d.text((x, y + 32), e, font=V.font(34, True), fill=col, anchor="lm")
            x += d.textlength(e + " ", font=V.font(34, True))
        if judge:
            ok = not soil_needed(els)
            d.text((1130, y + 32), "✓ yes" if ok else "✗ soil", font=V.font(30, True), fill=GOOD if ok else BAD, anchor="mm")


def render(title, spec):
    img, d = V.frame(title, kicker=KICKER)
    kind = spec.get("kind")
    if kind == "intro":
        for i, s in enumerate("CHO"):
            V.bead(d, W / 2 - 200 + i * 200, 250, 50, s)
        d.text((W / 2, 400), "CO₂  +  H₂O  →  only C, H, O", font=V.font(54, True), fill=INK, anchor="mm")
        chip(d, 165, 500, 950, 90, "So how does a plant build proteins and DNA?", HILITE, size=34)
    elif kind == "inputs":
        V.draw_formula(d, [("C", 1), ("O", 2)], 170, size=100)
        V.draw_formula(d, [("H", 2), ("O", 1)], 320, size=100)
        chip(d, 240, 520, 800, 80, "Photosynthesis: 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂", HILITE, size=30)
    elif kind == "type":
        name, ex, els, ex_name, parts = TYPES[spec["i"]]
        d.text((W / 2, 200), f"{name}: {ex}", font=V.font(40, True), fill=INK, anchor="mm")
        hi = next((j for j, (s, _) in enumerate(parts) if s in ("N", "P", "Mg")), None)
        V.draw_formula(d, parts, 260, size=110, hi=hi)
        d.text((W / 2, 470), f"Example: {ex_name}", font=V.font(30), fill=MUTED, anchor="mm")
        ok = not soil_needed(els)
        chip(d, 290, 530, 700, 80, "Only C, H, O: CO₂ + water are enough" if ok else "Has " + spec["extra"] + ": needs another source",
             (214, 236, 214) if ok else (246, 218, 214), size=30)
    elif kind == "chlorophyll":
        V.draw_formula(d, CHLOROPHYLL, 200, size=90, hi=2)
        d.text((W / 2, 400), "Chlorophyll a: the green pigment that captures light", font=V.font(32, True), fill=INK, anchor="mm")
        chip(d, 290, 500, 700, 80, "Needs N and Mg (magnesium)", (246, 218, 214), size=32)
    elif kind == "table":
        draw_types(d, 4, judge=spec.get("judge"))
    elif kind == "nochange":
        d.text((W / 2, 260), "C  →  N ?", font=V.font(150, True), fill=INK, anchor="mm")
        d.line([480, 340, 800, 180], fill=BAD, width=14)
        d.text((W / 2, 470), "Atoms are rearranged, never changed into another element.", font=V.font(32, True), fill=INK, anchor="mm")
        d.text((W / 2, 530), "Extra carbon can't become nitrogen. The N has to come in from outside.", font=V.font(26), fill=MUTED, anchor="mm")
    elif kind == "soil":
        d.rectangle([0, 470, W, 640], fill=(222, 205, 180))
        d.line([W / 2, 470, W / 2, 250], fill=GOOD, width=10)
        for dx in (-160, 160):
            d.ellipse([W / 2 + dx - 70, 230, W / 2 + dx + 70, 300], fill=(120, 180, 110))
        for i, dx in enumerate((-120, -50, 30, 110)):
            d.line([W / 2, 470, W / 2 + dx, 600], fill=(150, 120, 80), width=5)
        items = [("nitrate  NO₃⁻", "N"), ("phosphate  PO₄³⁻", "P"), ("magnesium  Mg²⁺", "Mg"), ("sulfate  SO₄²⁻", "S")]
        for i, (t, e) in enumerate(items):
            x = 70 + (i % 2) * 830
            y = 500 + (i // 2) * 65
            d.text((x, y), t, font=V.font(30, True), fill=V.COLORS[e])
        d.text((W / 2, 195), "Roots take in minerals dissolved in soil water", font=V.font(32, True), fill=INK, anchor="mm")
    elif kind == "fertilizer":
        d.rounded_rectangle([170, 180, 520, 600], radius=24, fill=(255, 255, 255), outline=INK, width=4)
        d.text((345, 250), "PLANT FOOD", font=V.font(34, True), fill=INK, anchor="mm")
        d.text((345, 370), "10-10-10", font=V.font(64, True), fill=INK, anchor="mm")
        d.text((345, 450), "N   -   P   -   K", font=V.font(40, True), fill=MUTED, anchor="mm")
        for i, t in enumerate(["N = nitrogen  →  proteins, DNA, chlorophyll",
                               "P = phosphorus  →  DNA, RNA, cell membranes",
                               "K = potassium  →  helps move water and sugar",
                               "It is not food: no sugar, no energy.",
                               "It supplies elements the plant can't get",
                               "from CO₂ and water."]):
            d.text((570, 220 + i * 62), t, font=V.font(24, i < 3), fill=INK if i < 3 else MUTED)
    elif kind == "build":
        d.text((W / 2, 230), "sugar (C, H, O)   +   N from the soil", font=V.font(46, True), fill=INK, anchor="mm")
        d.text((W / 2, 330), "↓", font=V.font(80, True), fill=INK, anchor="mm")
        d.text((W / 2, 430), "amino acids  →  proteins", font=V.font(54, True), fill=GOOD, anchor="mm")
        d.text((W / 2, 540), "You'll model this with beads in Lesson 4.", font=V.font(28), fill=MUTED, anchor="mm")
    elif kind == "yourturn":
        cols = ["Molecule", "Formula", "Type", "CO₂ + H₂O only?", "Extra from soil"]
        xs = [80, 300, 540, 740, 1000]
        for x, c in zip(xs, cols):
            d.text((x, 190), c, font=V.font(24, True), fill=MUTED)
        for i, (_, _, _, nm, parts) in enumerate(TYPES):
            y = 240 + i * 80
            d.rectangle([70, y - 10, 1210, y + 60], outline=(180, 170, 150), width=2)
            label = nm.split(" (")[0]
            d.text((80, y + 25), label if label.isupper() else label.capitalize(), font=V.font(28, True), fill=INK, anchor="lm")
            d.text((300, y + 25), formula(parts), font=V.font(28), fill=INK, anchor="lm")
        d.text((W / 2, 610), "Pause the video and fill in your quick sort.", font=V.font(30, True), fill=INK, anchor="mm")
    elif kind == "summary":
        for i, t in enumerate(["1. CO₂ + water give a plant only C, H, and O.",
                               "2. Carbohydrates and lipids: C, H, O only.",
                               "3. Proteins need N. DNA and RNA need N and P.",
                               "4. Chlorophyll needs N and Mg.",
                               "5. Those extra elements come from the soil."]):
            d.text((110, 200 + i * 82), t, font=V.font(36, True), fill=INK)
    return img


SCENES = [
    ("Plants Need More Than C, H, and O", dict(kind="intro"),
     "A pumpkin plant takes in carbon dioxide from the air and water from the soil. Those two molecules only bring in three elements: "
     "carbon, hydrogen, and oxygen. So how does a plant build proteins and DNA?"),
    ("What comes in from air and water", dict(kind="inputs"),
     "Carbon dioxide has carbon and oxygen. Water has hydrogen and oxygen. In photosynthesis, the plant rearranges those atoms into glucose, "
     "a sugar made of only carbon, hydrogen, and oxygen."),
    ("Carbohydrates", dict(kind="type", i=0),
     "A plant's body is built from four kinds of big molecules. First, carbohydrates: sugar, starch, and cellulose. "
     "They have only carbon, hydrogen, and oxygen, so a plant can build them from carbon dioxide and water."),
    ("Lipids", dict(kind="type", i=1),
     "Second, lipids: fats and oils, like oleic acid. They are also made of only carbon, hydrogen, and oxygen."),
    ("Proteins", dict(kind="type", i=2, extra="N (nitrogen)"),
     "Third, proteins. Proteins are built from amino acids, and every amino acid has nitrogen. Valine has one nitrogen atom. "
     "A couple of amino acids also have sulfur. Carbon dioxide and water have no nitrogen, so the plant needs another source."),
    ("Nucleic acids", dict(kind="type", i=3, extra="N and P"),
     "Fourth, nucleic acids: DNA and RNA. Their building blocks, like AMP, have nitrogen and phosphorus."),
    ("Chlorophyll", dict(kind="chlorophyll"),
     "One more. Chlorophyll is the green molecule that captures light for photosynthesis. It has nitrogen, "
     "and a magnesium atom right in its center. Without magnesium, a plant can't make chlorophyll."),
    ("The four big molecules", dict(kind="table"),
     "Here are the four big molecules side by side. Look at the elements column. Which ones have something besides carbon, hydrogen, and oxygen?"),
    ("Which can a plant build from CO₂ + water?", dict(kind="table", judge=True),
     "Carbohydrates and lipids, yes. Proteins and nucleic acids, no. They need nitrogen, and nucleic acids also need phosphorus."),
    ("Can carbon turn into nitrogen?", dict(kind="nochange"),
     "Could the plant just turn some extra carbon into nitrogen? No. Remember the sealed bag. Atoms are rearranged, "
     "but they are never created, destroyed, or changed into a different element. The nitrogen has to come in from outside the plant."),
    ("Where do the other elements come from?", dict(kind="soil"),
     "So where do they come from? The soil. Roots take in minerals that are dissolved in soil water: nitrate for nitrogen, "
     "phosphate for phosphorus, magnesium, and sulfate for sulfur."),
    ("What's in fertilizer?", dict(kind="fertilizer"),
     "That's why growers add fertilizer. The three numbers on the bag are nitrogen, phosphorus, and potassium. "
     "Fertilizer is not food for the plant. It has no sugar and no energy. It supplies elements the plant can't get from carbon dioxide and water."),
    ("Putting it together", dict(kind="build"),
     "The plant combines atoms from sugar with nitrogen from the soil to build amino acids, and then links amino acids into proteins. "
     "You'll model this with beads in Lesson 4."),
    ("Your turn: quick sort", dict(kind="yourturn"),
     "Your turn. Pause the video. For each of the four molecules, circle the elements it has, decide whether a plant could build it "
     "from only carbon dioxide and water, and write any extra element it needs from the soil."),
    ("Remember", dict(kind="summary"),
     "Remember. Carbon dioxide and water give a plant only carbon, hydrogen, and oxygen. That's enough for carbohydrates and lipids. "
     "Proteins need nitrogen. DNA and RNA need nitrogen and phosphorus. Chlorophyll needs nitrogen and magnesium. "
     "Those extra elements come from the soil."),
]


def main(out):
    V.SCENES[:] = SCENES
    V.render = render
    V.main(out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "more_than_cho_lesson2.mp4")
