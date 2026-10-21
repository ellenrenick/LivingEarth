"""Unit 2.1 (next year): one CFA per priority target, 5 one-point auto-graded questions each (the Unit 1.3 model),
and the CSA on the Unit 1.3 blueprint: a DOK 1-2 target gets 3 auto-graded questions, a DOK 3 target gets 1
multiple-choice question plus 1 four-point written response. 5 targets -> 13 questions, 19 raw points, graded out of 4.

Item format is unit13_bank's: "choice" (answer = index of the key; the key is moved by KEY_POSITIONS on upload),
"multi", "tf", "essay". CSA items reused from the 2026-27 CSA come from source_2026.json, with the longer wrong
choices from csa21_new_lts.py so the key is never the one long choice.
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CODE_TABLE = ("<table border=\"1\" cellpadding=\"6\"><tbody><tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th>"
              "<th>Amino acid</th></tr><tr><td>ATG</td><td>Met</td><td>GAG</td><td>Glu</td></tr>"
              "<tr><td>GGA</td><td>Gly</td><td>GAA</td><td>Glu</td></tr><tr><td>AGA</td><td>Arg</td><td>GTG</td><td>Val</td></tr>"
              "<tr><td>CTG</td><td>Leu</td><td>TTT</td><td>Phe</td></tr></tbody></table>")


def c(prompt, choices, fb):
    return {"type": "choice", "prompt": prompt, "choices": choices, "answer": 0, "feedback": fb}


def tf(prompt, answer, fb):
    return {"type": "tf", "prompt": prompt, "answer": answer, "feedback": fb}


CFAS = {
    "LS1-1.1": [
        c("<p>What shape is a DNA molecule?</p>",
          ["A double helix: two strands twisted like a ladder", "A single straight chain of bases, with no second strand to pair with",
           "A round ball of bases packed tightly together in the nucleus", "A flat sheet"],
          "DNA is a double helix: two strands twisted around each other, like a twisted ladder."),
        c("<p>What are the three parts of one nucleotide?</p>",
          ["A sugar, a phosphate, and a base", "An amino acid, a sugar, and a protein", "Two bases and a protein",
           "A gene, a base, and a cell"],
          "Every nucleotide has a sugar, a phosphate, and one of four bases (A, T, C, or G)."),
        c("<p>One strand of DNA reads <strong>A T G C</strong>. What does the matching strand read?</p>",
          ["T A C G", "A T G C", "G C A T", "C G T A"],
          "A pairs with T and C pairs with G, so A T G C pairs with T A C G."),
        c("<p>A scientist finds that 20% of the bases in a DNA sample are C. About what percent are G?</p>",
          ["About 20%, because C pairs with G", "About 30%, because G is always the most common base",
           "About 80%, because the rest of the bases must be G", "It is impossible to tell from the C count"],
          "C pairs with G, so in double-stranded DNA there is about as much G as C (Chargaff's data)."),
        c("<p>Which statement is true?</p>",
          ["DNA holds the instructions, and proteins do jobs for the cell.",
           "Proteins hold the instructions, and DNA does jobs for the cell.",
           "DNA and proteins are the same molecule.", "Neither DNA nor proteins are found in cells."],
          "The order of the bases in DNA is the message, the instructions for building proteins. Proteins do the jobs."),
    ],
    "LS1-1.2": [
        c("<p>Which sequence best describes how a cell uses a gene?</p>",
          ["The gene's message is copied, and the copy is read to link amino acids in order.",
           "The DNA leaves the cell, and the cell reads it outside, where amino acids are linked in order.",
           "The amino acids are copied, and the copy is read to build a new DNA molecule in order.", "The protein is copied to make a gene."],
          "The cell copies the gene's message and reads the copy to link amino acids. The DNA stays safe."),
        c("<p>What is built when the copy of a gene's message is read?</p>",
          ["A chain of amino acids", "A new sugar molecule", "A new cell for the body", "A new DNA molecule"],
          "Reading the copy links amino acids in order. The chain folds into a protein."),
        c(f"<p>Use the code table.</p>{CODE_TABLE}<p>The copy of a gene's message reads <strong>ATG GGA CTG</strong>. "
          "Which chain of amino acids is built?</p>",
          ["Met – Gly – Leu", "Met – Arg – Leu", "Leu – Gly – Met", "Met – Glu – Phe"],
          "Read three letters at a time: ATG = Met, GGA = Gly, CTG = Leu."),
        tf("<p>True or false: A cell reads a gene's message three bases at a time.</p>", True,
           "True. Each group of three bases (a triplet) calls for one amino acid."),
        tf("<p>True or false: Each time a cell builds a protein, it uses up the gene's DNA.</p>", False,
           "False. The cell copies the message and reads the copy. The DNA itself stays safe and can be copied again."),
    ],
    "LS1-1.3": [
        c(f"<p>Use the code table.</p>{CODE_TABLE}<p>A gene reads ATG GAG CTG. A one-base change makes it read ATG GTG CTG. "
          "What changes in the amino acid chain?</p>",
          ["Glu becomes Val", "Met becomes Leu", "Leu becomes Phe", "Nothing changes"],
          "Only the middle triplet changed: GAG (Glu) became GTG (Val). One amino acid is different."),
        c(f"<p>Use the code table.</p>{CODE_TABLE}<p>A triplet in a gene changes from GAG to GAA. "
          "What happens to the amino acid chain?</p>",
          ["Nothing changes, because GAG and GAA both code for Glu.",
           "One amino acid changes, so the protein always stops working.",
           "Every amino acid after it changes.", "The protein is not made at all."],
          "Some triplets code for the same amino acid. GAG and GAA are both Glu, so the chain is the same."),
        c("<p>One letter changes in the switch next to a gene, so the gene is never turned on. What is the most likely effect?</p>",
          ["The protein from that gene is not made.", "The protein has one different amino acid.",
           "The protein is made twice as fast.", "Nothing, because switches are not part of DNA."],
          "If the switch never turns the gene on, the cell never makes that gene's protein."),
        c("<p>Why can a single base change make a protein work differently?</p>",
          ["It can change an amino acid in the chain, and a different chain can make a protein that works differently.",
           "It always removes the whole gene from the cell, so the cell has no instructions left for that protein.",
           "It turns the protein into DNA, so the cell ends up with extra DNA instead of a protein that does a job.",
           "It does not matter, because every base is the same."],
          "Base order sets amino acid order. A different amino acid can change how the protein works."),
        c("<p>In Siamese cats, one base change swaps Gly for Arg in a pigment-making protein. The changed protein works only "
          "in skin cooler than about 33 °C. Which body part is most likely dark?</p>",
          ["An ear (28 °C)", "The back (36 °C)", "The belly (36 °C)", "The upper leg (34 °C)"],
          "The ear is the only part listed below 33 °C, so it is the only place the changed protein makes pigment."),
    ],
    "LS1-1.4": [
        c("<p>Two cells in the same person have the same genes but make different proteins. What explains this?</p>",
          ["Each cell uses a different set of its genes.", "Each cell has different DNA from the other cells.",
           "Only one of the two cells has DNA inside its nucleus.",
           "Proteins are not made from genes."],
          "Almost every cell has the same DNA, but each kind of cell uses only some of its genes."),
        c("<p>Cell type A makes Protein 1. Cell type B makes Protein 2. Both cells have genes 1 and 2. "
          "Which statement is best supported?</p>",
          ["Cell A uses gene 1 and Cell B uses gene 2, so they make different proteins and have different jobs.",
           "The two cells must do exactly the same job, because both of them have the same two genes in their DNA.",
           "Cell B has no DNA at all, so it must get Protein 2 from Cell A instead of making that protein itself.",
           "Cell A has only gene 1."],
          "Same genes, different genes used, different proteins, different jobs."),
        c("<p>A skin cell and a muscle cell from the same person both have the gene for keratin. Only the skin cell makes "
          "keratin. Why?</p>",
          ["The skin cell uses the keratin gene; the muscle cell has it but does not use it.",
           "The muscle cell lost the keratin gene when it became a muscle cell, so it cannot make keratin.",
           "Keratin is made from sugar, not from a gene.",
           "The skin cell has more DNA than the muscle cell, so it has room to make extra keratin."],
          "Both cells have the gene. Only the skin cell uses it, so only the skin cell makes keratin."),
        tf("<p>True or false: A Siamese cat's ear cells and back cells have different DNA, and that is why only the ears are dark.</p>",
           False,
           "False. Every cell has the same DNA. The changed protein works only in cool skin, and the ears are cool."),
        c("<p>Which chain best explains how DNA gives a cell its job?</p>",
          ["DNA → the genes the cell uses → the proteins it makes → its job",
           "Its job → the proteins it makes → the genes it uses → its own DNA",
           "Proteins → DNA → the genes the cell uses → its job in the body tissue",
           "DNA → sugar → its job"],
          "The genes a cell uses decide its proteins, and its proteins carry out its job."),
    ],
    "LS1-1.5": [
        c("<table border=\"1\" cellpadding=\"6\"><tbody><tr><th>Person</th><th>Gene</th><th>Protein</th><th>Symptoms</th></tr>"
          "<tr><td>1</td><td>Typical</td><td>Works</td><td>None</td></tr><tr><td>2</td><td>One base changed</td>"
          "<td>Works poorly</td><td>Yes</td></tr></tbody></table><p>Which conclusion is best supported?</p>",
          ["The DNA change led to a protein that works poorly, and that caused the symptoms.",
           "The symptoms caused the DNA to change, and the changed DNA then made the protein work poorly.",
           "The protein has no link to the symptoms, because the symptoms come only from the DNA itself.",
           "DNA changes never matter."],
          "DNA change → protein works poorly → effect on the body."),
        c("<p>Which sequence correctly shows how a DNA change can affect the body?</p>",
          ["DNA change → different amino acid chain → protein works differently → effect on the body",
           "Effect on the body → protein works differently → a different amino acid chain → DNA change",
           "A protein change comes first → then a DNA change → a different amino acid chain → the body",
           "DNA change → no change in any protein → effect on the body"],
          "The change starts in the DNA and travels through the amino acid chain and the protein to the body."),
        c("<p>In sickle cell disease, red blood cells last about 10 to 20 days instead of about 120 days. What is the most "
          "likely effect on the body?</p>",
          ["Fewer red blood cells, so less oxygen reaches the body and the person feels tired.",
           "More red blood cells, so more oxygen reaches the body and the person has extra energy.",
           "No effect on the body, because red blood cells do not carry anything the body needs.",
           "The person's DNA changes back to normal."],
          "Red blood cells carry oxygen. Cells that break down early mean fewer cells and less oxygen."),
        c("<p>In sickle cell disease, which change happens <strong>first</strong>?</p>",
          ["One base in the hemoglobin gene changes (GAG to GTG).", "Red blood cells bend into sickle shapes in small blood vessels.",
           "Hemoglobin sticks together inside the person's red blood cells.", "The person feels tired."],
          "The DNA change comes first. It swaps one amino acid (Glu to Val), so hemoglobin sticks together and cells sickle."),
        c("<p>A student claims sickle cell disease lowers the oxygen a person's blood can carry. Which data best support "
          "the claim?</p>",
          ["Hemoglobin is about 6 to 10 g/dL with sickle cell disease, compared with about 12 to 17 g/dL.",
           "Hemoglobin is a protein, and proteins are built from chains of amino acids linked in a set order.",
           "Red blood cells are found in blood, and blood moves through the body inside the blood vessels.", "The hemoglobin gene has many triplets."],
          "Hemoglobin carries oxygen, and people with sickle cell disease have much less of it in their blood."),
    ],
}

CFA_TITLE = {t: f"Unit 2.1 CFA {t}" for t in CFAS}


def _plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()


# 2026-27 CSA wrong choices lengthened so the key is never the single longest choice (csa21_new_lts.py).
LONGER = {
    "A single straight strand made of amino acids joined together":
        "A single straight strand made of amino acids joined together end to end, with no sugars, phosphates, or bases anywhere in the model",
    "Two strands twisted together, each made only of sugar molecules":
        "Two strands twisted together, each made only of sugar molecules, with no phosphates or bases attached anywhere along either strand",
    "All three amino acids change, because one base change affects the whole chain.":
        "All three amino acids change, because one base change affects the whole chain, so every amino acid in the protein is now different from before.",
    "No protein is built, because every change in DNA stops protein building.":
        "No protein is built, because every change in DNA stops protein building, so the cell can no longer make this protein at all after the change.",
    "The amino acids are copied, and the copies are read to build DNA.":
        "The amino acids are copied, and the copies are read to build DNA, so the recipe book stands for the amino acids and the dish stands for the DNA.",
    "The whole DNA molecule leaves the nucleus and is taken apart to make a protein.":
        "The whole DNA molecule leaves the nucleus and is taken apart to make a protein, so the recipe book itself is used up each time a dish is made.",
    "Type Y lost gene 1 and Type X lost gene 3, so they cannot make the other proteins.":
        "Type Y lost gene 1 and Type X lost gene 3, so they cannot make the other proteins, which is the only reason each type of cell makes its own different set of proteins.",
    "Type X and Type Y must have different DNA, because they make different proteins.":
        "Type X and Type Y must have different DNA, because they make different proteins, and two cells can only ever make different proteins if their genes are different.",
    "Proteins determine the base sequence of DNA, and DNA carries out jobs for the cell.":
        "Proteins determine the base sequence of DNA, and DNA carries out jobs for the cell, so the instructions flow from the proteins into the DNA molecule.",
    "DNA carries out most jobs in a cell, and proteins store the instructions for DNA.":
        "DNA carries out most jobs in a cell, and proteins store the instructions for DNA, so proteins act as the cell's instruction book and DNA does the work.",
    "The protein changed first, and that caused the DNA to change.":
        "The protein changed first, and that caused the DNA to change, so the base change in Group 2 came after the protein stopped working well.",
    "The symptoms are caused by the protein, not by the DNA, because DNA has no effect on proteins.":
        "The symptoms are caused by the protein, not by the DNA, because DNA has no effect on proteins, so the base change in Group 2 has nothing to do with them.",
    "The claim is supported, because all three changes affect the protein.":
        "The claim is supported, because all three changes affect the protein, so every single-base change in a gene must always stop the protein from working.",
    "The claim is supported, because change C stops the protein.":
        "The claim is supported, because change C stops the protein, and one example where the protein stops working is enough to show that the claim is true.",
}

# CSA blueprint: (target, 2026-27 question name or a new item)
CSA_PLAN = [
    ("LS1-1.1", "Part 1: Vocabulary Matching"), ("LS1-1.1", "MC 1 (DOK 2)"), ("LS1-1.1", "MC 6 (DOK 2)"),
    ("LS1-1.2", "MC 2 (DOK 2)"), ("LS1-1.2", "MC 4 (DOK 2)"),
    ("LS1-1.2", tf("<p>True or false: When a cell reads the copy of a gene, each group of three bases calls for one amino "
                   "acid.</p>", True, "")),
    ("LS1-1.3", "MC 3 (DOK 2)"), ("LS1-1.3", "MC 8 (DOK 3)"),
    ("LS1-1.3", {"type": "choice", "prompt": f"<p>Use the code table.</p>{CODE_TABLE}<p>In one gene, the triplet GAG changes "
                 "to GAA. A student says the protein will now work differently. Which statement best evaluates the claim?</p>",
                 "choices": ["The claim is not supported: GAG and GAA both code for Glu, so the amino acid chain and the "
                             "protein stay the same.",
                             "The claim is supported, because any change to a base in a gene always changes the amino acid "
                             "chain and so always changes how the protein works.",
                             "The claim is supported, because GAA codes for Val, which is a different amino acid from Glu.",
                             "The claim cannot be judged, because a code table cannot tell which amino acid a triplet codes for."],
                 "answer": 0, "feedback": ""}),
    ("LS1-1.4", "MC 5 (DOK 3)"), ("LS1-1.4", "Free response 2 (DOK 3)"),
    ("LS1-1.5", "MC 7 (DOK 3)"), ("LS1-1.5", "Free response 1 (DOK 3)"),
]


def csa_items():
    """[(title, classic question or bank item, kind)] in blueprint order; kind is 'classic' or 'bank'."""
    src = {q["question_name"]: q for q in json.loads((HERE / "source_2026.json").read_text())["csa_questions"]
           if q["question_type"] != "text_only_question"}
    out = []
    for n, (tid, it) in enumerate(CSA_PLAN, 1):
        if isinstance(it, str):
            q = json.loads(json.dumps(src[it]))
            for a in q.get("answers", []):
                t = _plain(a.get("html") or a.get("text"))
                if t in LONGER:
                    a["html"], a["text"] = f"<p>{LONGER[t]}</p>", LONGER[t]
            if q["question_type"] == "essay_question":
                q["neutral_comments_html"] = re.sub(r"<p><em>Scale:.*?</em></p>", "", q["neutral_comments_html"])
            essay = q["question_type"] == "essay_question"
            out.append((f"Q{n} · {tid}" + (" (teacher-graded, 4 points)" if essay else ""), q, "classic"))
        else:
            out.append((f"Q{n} · {tid}", it, "bank"))
    return out
