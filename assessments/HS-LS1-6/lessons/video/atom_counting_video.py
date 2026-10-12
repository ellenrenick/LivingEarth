"""Build "Counting Atoms in a Formula" (Lesson 2 support video) as an MP4.

Each scene is a still frame plus a narration line (ffmpeg's flite voice). Element
colors match the bead colors used in Lessons 3 and 4: C black, H white, O red, N blue.

  python3 atom_counting_video.py out.mp4
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
BG = (247, 243, 233)
INK = (35, 57, 44)
MUTED = (110, 117, 110)
HILITE = (255, 214, 102)
COLORS = {"C": (30, 30, 30), "H": (250, 250, 250), "O": (205, 45, 45), "N": (45, 95, 200)}
NAMES = {"C": "carbon", "H": "hydrogen", "O": "oxygen", "N": "nitrogen"}
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def frame(title, kicker="LESSON 2 · COUNTING ATOMS"):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 8], fill=INK)
    d.text((60, 36), kicker, font=font(22, True), fill=MUTED)
    d.text((60, 66), title, font=font(46, True), fill=INK)
    d.text((60, H - 44), "HS-LS1-6 · The Giant Pumpkin Mystery", font=font(18), fill=MUTED)
    return img, d


def draw_formula(d, parts, y, hi=None, coef=None, size=130):
    """parts: [(symbol, count)]. Draws centered; hi = index to highlight, or "coef"."""
    big, sub = font(size, True), font(int(size * 0.55), True)
    pieces = []
    if coef:
        pieces.append(("coef", str(coef), None))
    for i, (sym, n) in enumerate(parts):
        pieces.append((i, sym, str(n) if n > 1 else None))
    widths = []
    for key, sym, n in pieces:
        w = d.textlength(sym, font=big) + (d.textlength(n, font=sub) if n else 0) + (30 if key == "coef" else 6)
        widths.append(w)
    x = (W - sum(widths)) / 2
    for (key, sym, n), w in zip(pieces, widths):
        if key == hi:
            d.rounded_rectangle([x - 12, y - 10, x + w - 2, y + size * 1.25], radius=18, fill=HILITE)
        color = INK if key == "coef" else (COLORS[sym] if sym != "H" else (120, 120, 120))
        d.text((x, y), sym, font=big, fill=color)
        if n:
            d.text((x + d.textlength(sym, font=big), y + size * 0.62), n, font=sub, fill=color)
        x += w


def bead(d, cx, cy, r, sym):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=COLORS[sym], outline=(60, 60, 60), width=3)
    d.text((cx, cy), sym, font=font(int(r * 0.9), True), fill=(255, 255, 255) if sym != "H" else (60, 60, 60), anchor="mm")


def draw_beads(d, counts, y, r=26):
    atoms = [s for s, n in counts for _ in range(n)]
    if not atoms:
        return
    per_row = 16
    rows = [atoms[i:i + per_row] for i in range(0, len(atoms), per_row)]
    for j, row in enumerate(rows):
        x0 = (W - len(row) * (2 * r + 10)) / 2 + r
        for i, s in enumerate(row):
            bead(d, x0 + i * (2 * r + 10), y + j * (2 * r + 12), r, s)


def draw_tally(d, counts, y, total=False):
    text = "     ".join(f"{NAMES[s].capitalize()}: {n}" for s, n in counts)
    size = 34
    while d.textlength(text, font=font(size, True)) > W - 120:
        size -= 2
    d.text((W / 2, y), text, font=font(size, True), fill=INK, anchor="mm")
    if total:
        t = f"Total: {sum(n for _, n in counts)} atoms"
        f = font(34, True)
        tw = d.textlength(t, font=f)
        d.rounded_rectangle([W / 2 - tw / 2 - 16, y + 30, W / 2 + tw / 2 + 16, y + 82], radius=14, fill=HILITE)
        d.text((W / 2, y + 56), t, font=f, fill=INK, anchor="mm")


def molecule_scenes(name, parts, coef=None, words=None):
    """Scenes that count one formula element by element."""
    k = coef or 1
    scenes = []
    label = f"{coef} " if coef else ""
    say_formula = words or ", ".join(f"{s} {n}" if n > 1 else s for s, n in parts)
    scenes.append((f"{name}", dict(parts=parts, coef=coef), f"Let's count the atoms in {name}. The formula is {say_formula}."))
    if coef:
        scenes.append((name, dict(parts=parts, coef=coef, hi="coef"),
                       f"The big {coef} in front is a coefficient. It means {coef} whole molecules, so we multiply every count by {coef}."))
    counted = []
    for i, (sym, n) in enumerate(parts):
        counted.append((sym, n * k))
        if n > 1:
            why = f"The small {n} after {sym} means {n} {NAMES[sym]} atoms."
        else:
            why = f"{sym} has no number after it, so that means 1 {NAMES[sym]} atom."
        if coef:
            why += f" Times {coef} is {n * k}."
        scenes.append((name, dict(parts=parts, coef=coef, hi=i, counts=list(counted)), why))
    total = sum(n for _, n in counted)
    scenes.append((name, dict(parts=parts, coef=coef, counts=list(counted), total=True),
                   f"So {label}{name} has " + ", ".join(f"{n} {NAMES[s]}" for s, n in counted) + f". That is {total} atoms in all."))
    return scenes


SCENES = (
    [("Counting Atoms in a Formula", dict(intro=True),
      "Counting atoms in a formula. In Lesson 2 you will count the atoms in molecules to figure out what a plant could build from carbon dioxide and water."),
     ("Rule 1: Capital letters start an element", dict(rule=1),
      "Rule 1. Every element symbol starts with a capital letter. C is carbon. H is hydrogen. O is oxygen. N is nitrogen."),
     ("Rule 2: The small number counts the atom before it", dict(rule=2),
      "Rule 2. The small number written after a symbol, called a subscript, tells how many atoms of that element. If there is no number, it means 1.")]
    + molecule_scenes("carbon dioxide", [("C", 1), ("O", 2)], words="C, O 2")
    + molecule_scenes("water", [("H", 2), ("O", 1)], words="H 2, O")
    + molecule_scenes("glucose", [("C", 6), ("H", 12), ("O", 6)], words="C 6, H 12, O 6")
    + molecule_scenes("glycine, an amino acid", [("C", 2), ("H", 5), ("N", 1), ("O", 2)], words="C 2, H 5, N, O 2")
    + [("Notice the nitrogen", dict(parts=[("C", 2), ("H", 5), ("N", 1), ("O", 2)], hi=2),
        "Notice the N. Glycine has nitrogen, but carbon dioxide and water do not. A plant cannot build glycine from only carbon dioxide and water. It needs nitrogen from somewhere else.")]
    + molecule_scenes("carbon dioxide", [("C", 1), ("O", 2)], coef=6, words="6 C O 2")
    + [("Your turn: histidine", dict(parts=[("C", 6), ("H", 9), ("N", 3), ("O", 2)]),
        "Your turn. Pause the video and count the atoms in histidine. C 6, H 9, N 3, O 2. Write how many of each element, and the total."),
       ("Check your answer", dict(parts=[("C", 6), ("H", 9), ("N", 3), ("O", 2)], counts=[("C", 6), ("H", 9), ("N", 3), ("O", 2)], total=True),
        "Check your answer. Histidine has 6 carbon, 9 hydrogen, 3 nitrogen, and 2 oxygen. That is 20 atoms. Because it has nitrogen, a plant needs a source of nitrogen to build it."),
       ("Remember", dict(summary=True),
        "Remember. Capital letters start an element. The small number counts the atom before it. No number means 1. A big number in front multiplies everything. Now use these rules on your molecule cards.")]
)


def render(title, spec):
    img, d = frame(title)
    if spec.get("intro"):
        d.text((W / 2, 300), "CO₂     H₂O     C₆H₁₂O₆", font=font(80, True), fill=INK, anchor="mm")
        for i, s in enumerate("CHON"):
            bead(d, W / 2 - 240 + i * 160, 470, 40, s)
            d.text((W / 2 - 240 + i * 160, 535), NAMES[s], font=font(24), fill=INK, anchor="mm")
    elif spec.get("rule") == 1:
        for i, s in enumerate("CHON"):
            x = 220 + i * 280
            d.text((x, 280), s, font=font(150, True), fill=COLORS[s] if s != "H" else (120, 120, 120), anchor="mm")
            d.text((x, 410), NAMES[s], font=font(32), fill=INK, anchor="mm")
            bead(d, x, 500, 34, s)
    elif spec.get("rule") == 2:
        draw_formula(d, [("H", 2), ("O", 1)], 200, hi=0)
        d.text((W / 2, 450), "H₂  →  2 hydrogen atoms        O  →  1 oxygen atom (no number = 1)",
               font=font(32, True), fill=INK, anchor="mm")
        draw_beads(d, [("H", 2), ("O", 1)], 560)
    elif spec.get("summary"):
        lines = ["1. A capital letter starts a new element.", "2. The small number counts the atom before it.",
                 "3. No number means 1.", "4. A big number in front multiplies everything."]
        for i, t in enumerate(lines):
            d.text((140, 210 + i * 90), t, font=font(40, True), fill=INK)
        d.text((140, 590), "Next: count the atoms on your molecule cards.", font=font(30), fill=MUTED)
    else:
        draw_formula(d, spec["parts"], 170, hi=spec.get("hi"), coef=spec.get("coef"))
        if spec.get("counts"):
            draw_tally(d, spec["counts"], 390, total=spec.get("total"))
            draw_beads(d, spec["counts"], 530 if spec.get("total") else 490,
                       r=22 if sum(n for _, n in spec["counts"]) > 16 else 28)
    return img


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main(out):
    tmp = Path(tempfile.mkdtemp())
    segs = []
    for i, (title, spec, say) in enumerate(SCENES):
        png, txt, wav, mp4 = (tmp / f"s{i:02d}{ext}" for ext in (".png", ".txt", ".wav", ".mp4"))
        render(title, spec).save(png)
        txt.write_text(say)
        pause = 6 if title.startswith("Your turn") else 0.7  # time to try it before the answer
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"flite=textfile={txt}:voice=slt", "-af", f"apad=pad_dur={pause}", str(wav)])
        run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(wav), "-c:v", "libx264", "-tune", "stillimage",
             "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-ar", "44100", "-ac", "2", "-shortest", str(mp4)])
        segs.append(mp4)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{s}'\n" for s in segs))
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", out])
    print(out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "counting_atoms_lesson2.mp4")
