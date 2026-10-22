"""Unit 2.2 Mastery Path reviews: REVIEWS[target] opens when a student scores below a B (fewer than 4 of 5) on that CFA.

Each is a short page: read each section, try the checks, then answer the 3 questions at the bottom (text entry).
Laid out like unit13_reviews.py (Unit 1.3).
"""

BOX = ('<div style="background:#eef5fb;border-left:4px solid #2b6cb0;padding:10px 14px;margin:12px 0">'
       '<p><strong>Learning target {tid}:</strong> {ican}</p></div>')
TABLE = '<table border="1" cellpadding="6" style="border-collapse:collapse"><tbody>{}</tbody></table>'

import content as U


def table(header, *rows):
    th = "<tr>" + "".join(f"<th>{h}</th>" for h in header) + "</tr>"
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return TABLE.format(th + trs)


def try_it(q, a):
    return f"<p><strong>Try it:</strong> {q}</p><details><summary>Check your answer</summary><p>{a}</p></details>"


def review(tid, sections, submit):
    ican = U.TARGET[tid][3]
    body = [BOX.format(tid=tid, ican=ican),
            "<p>Your goal on every CFA is at least a B (4 of 5). Your CFA score was below a B, so this review opened for you. "
            f"Read each section, try the checks, then answer the {len(submit)} questions at the bottom and submit.</p>",
            "<p><strong>Use:</strong> your Unit 2.2 notebook and the Day 1 puppy puzzle.</p>"]
    for n, (title, html) in enumerate(sections, 1):
        body.append(f"<h3>{n}. {title}</h3>{html}")
    body.append("<h3>Show what you know (submit these)</h3><ol>" + "".join(f"<li>{s}</li>" for s in submit) + "</ol>")
    return "\n".join(body)


REVIEWS = {
    "LS3-2.1": review("LS3-2.1", [
        ("Three sources of new variation",
         "<p>Offspring can differ from their parents and from each other for three reasons that change or rearrange DNA.</p>"
         + table(["Source", "What happens", "Example"],
                 ["New combinations of alleles", "Each sex cell carries one allele of each gene. Fertilization joins two sex cells.",
                  "Two Bb parents have a bb puppy."],
                 ["Copying errors", "Before a cell divides it copies its DNA. A rare error that is not fixed becomes a mutation.",
                  "One letter in a copy is wrong."],
                 ["Mutations from the environment", "UV light, X-rays, and some chemicals damage DNA.",
                  "A chemical in water changes a gene."])
         + try_it("Which source makes new alleles that neither parent has: new combinations or mutations?",
                  "Mutations. A new combination only uses alleles the parents already have.")),
        ("What is a mutation?",
         "<p>A mutation is a change in the order of the bases in DNA. It can come from a copying error or from damage caused by "
         "the environment.</p>"
         + try_it("A tan from the sun makes skin darker for a summer. Is that a mutation?",
                  "No. A tan is a change in how skin looks, not a change in the DNA.")),
        ("Which source is it?",
         "<p>Read each clue and name the source.</p>"
         + try_it("(a) A puppy gets B from Mom and b from Dad. (b) A letter is copied wrong in a dividing cell. (c) UV light "
                  "damages a gene.",
                  "(a) new combination of alleles; (b) copying error; (c) mutation from the environment.")),
    ], [
        "Name the three sources of new genetic variation.",
        "Explain the difference between a new combination of alleles and a mutation.",
        "Two Bb parents have a bb puppy. Which source explains it, and why?",
    ]),
    "LS3-2.2": review("LS3-2.2", [
        ("Each sex cell carries one allele",
         "<p>A body cell has two alleles of each gene. When a parent makes sex cells (eggs or sperm), each sex cell gets only one "
         "allele of each gene, chosen at random, like a coin flip.</p>"
         + try_it("A parent has the alleles Gg. What alleles can her sex cells carry?",
                  "Some carry G and some carry g. No sex cell carries both.")),
        ("Fertilization makes a new combination",
         "<p>At fertilization a sperm and an egg join. The offspring gets one allele from each parent.</p>"
         + table(["Sperm carries", "Egg carries", "Offspring genotype"], ["G", "G", "GG"], ["G", "g", "Gg"], ["g", "g", "gg"])
         + try_it("A sperm with g joins an egg with G. What is the offspring's genotype?", "Gg (write the capital letter first).")),
        ("A Punnett square lists every pairing",
         "<p>Put one parent's sex-cell alleles across the top and the other's down the side. Each box is one possible offspring.</p>"
         + table(["", "G", "g"], ["G", "GG", "Gg"], ["g", "Gg", "gg"])
         + try_it("For Gg × Gg, how many of the 4 boxes are gg?", "1 of 4 boxes, or 25%.")),
    ], [
        "How many alleles of one gene does a sex cell carry, and how does an offspring end up with two?",
        "A parent has the alleles Tt. List the two kinds of sex cells this parent can make.",
        "Explain in one or two sentences why two Gg parents can have a gg offspring.",
    ]),
    "LS3-2.3": review("LS3-2.3", [
        ("How copying errors happen",
         "<p>Before a cell divides, it copies all its DNA. A human cell copies about 6 billion letters. Cells proofread the copy, "
         "so most errors are fixed. A rare error that is not fixed is a mutation.</p>"
         + try_it("What is a mutation caused by a copying error?", "A change in the DNA that was made when DNA was copied and not fixed.")),
        ("The environment can damage DNA",
         "<p>UV light, X-rays, and some chemicals can damage DNA, so these factors raise the number of mutations.</p>"
         + table(["Hours of UV light", "Mutations per 1,000 skin cells"], ["0", "2"], ["1", "9"], ["2", "21"], ["4", "40"])
         + try_it("What happens to the number of mutations as UV exposure goes up?", "It goes up: 2, 9, 21, then 40.")),
        ("Which changes are inherited?",
         "<p>In animals, a mutation is passed to offspring only if it is in a cell that makes eggs or sperm.</p>"
         + table(["Where the DNA changed", "Inherited?"], ["A skin cell (sunburn)", "No"], ["A muscle cell", "No"],
                 ["A cell that is becoming a sperm", "Yes, if that sperm helps make a puppy"])
         + try_it("A chemical in smoke changes DNA in a lung cell. Will the person's children inherit it?",
                  "No. A lung cell does not become an egg or sperm.")),
    ], [
        "Explain how a copying error can become a mutation.",
        "Explain how UV light can change a gene.",
        "Explain why a mutation in a skin cell is not passed on, but a mutation in a cell that makes sperm can be.",
    ]),
    "LS3-2.4": review("LS3-2.4", [
        ("Clues for each source",
         "<p>Use the data to find which source explains a variation.</p>"
         + table(["Source", "Clue in the data"],
                 ["New combination of alleles", "Every allele in the offspring was already in a parent."],
                 ["Copying error", "A new allele that neither parent has, with no extra exposure."],
                 ["Environmental mutation", "More mutations in the group that was exposed than in the group that was not."])
         + try_it("Mom is Ff, Dad is Ff, and a puppy is ff. Which source explains it?",
                  "A new combination: f was already in both parents.")),
        ("Read a table",
         "<p>Scientists exposed mice to X-rays and counted new mutations in sperm cells per 1,000 cells.</p>"
         + table(["Group", "X-ray dose", "Mutations"], ["A", "none", "3"], ["B", "low", "12"], ["C", "high", "25"])
         + try_it("Which claim does the table support?",
                  "X-rays increased mutations: 3 with none, 12 with a low dose, 25 with a high dose.")),
        ("Claim, evidence, reasoning",
         "<p><strong>Claim:</strong> the source. <strong>Evidence:</strong> numbers or alleles from the data. "
         "<strong>Reasoning:</strong> why that evidence points to that source.</p>"
         + try_it("Write a claim, evidence, and reasoning for the mouse table.",
                  "Claim: X-rays caused the extra mutations. Evidence: 25 per 1,000 with a high dose vs 3 with none. Reasoning: copying "
                  "errors alone would give similar numbers in every group.")),
    ], [
        "A puppy has a DNA allele (CCT) that neither parent has. Which source of variation is most likely, and why?",
        "Fruit flies: no radiation 4 mutations, low dose 15, high dose 31 per 1,000 egg cells. Write a claim, one piece of evidence, "
        "and your reasoning.",
        "Name one more piece of data that would help show a variation came from the environment and not a copying error.",
    ]),
    "LS3-2.5": review("LS3-2.5", [
        ("A counterclaim is another explanation",
         "<p>A scientist who makes a claim has to answer other explanations. A counterclaim is another explanation for the same data.</p>"
         + try_it("A student says X-rays caused extra mutations. Another says copying errors did. What is the second student's statement?",
                  "A counterclaim.")),
        ("Defend in three steps",
         "<p>1. Restate your claim. 2. Cite the data that supports it. 3. Show why the other explanation does not fit the data.</p>"
         + table(["Kennel", "Puppies checked", "New coat patterns"], ["A (chemical in water)", "1,000", "14"], ["B (clean water)", "1,000", "3"])
         + try_it("Defend: the chemical caused the extra patterns, not copying errors.",
                  "Kennel A had 14 per 1,000 and Kennel B had 3. Copying errors happen in both kennels at about the same rate, so they "
                  "cannot explain the 11 extra patterns in Kennel A.")),
        ("Check your defense",
         "<p>A strong defense (1) cites numbers, (2) answers the counterclaim, and (3) does not just restate the claim.</p>"
         + try_it("A student writes: \"I think it was the chemical because I believe it is.\" What is missing?",
                  "Data, and an answer to the counterclaim.")),
    ], [
        "Use the kennel table to defend the claim that the chemical caused the extra new coat patterns. Include numbers.",
        "A classmate says all the new patterns are copying errors. Explain why that does not fit the data.",
        "Rewrite one weak defense (\"it was the chemical because I think so\") so that it uses evidence.",
    ]),
}
