"""Build the three warm-up pages from template.html, engine.js/css and items_<LT>.js.
Usage: python3 build.py   (writes LS3-2.x/index.html)"""
from pathlib import Path
H = Path(__file__).parent
T = (H / "template.html").read_text()
ENGINE = (H / "engine.js").read_text()
CSS = (H / "engine.css").read_text()
META = {
  "LS3-2.1": dict(TITLE="Three Sources Warm-Up", H1="Three Sources of Variation", TARGET_TEXT="I can name three ways new genetic variation arises.", LSKEY="ls321who", DAYS="Day 1 and Day 2",
    NOMISS="Remember the three sources: new combinations of alleles, copying errors, and mutations from the environment."),
  "LS3-2.2": dict(TITLE="Sex Cells Warm-Up", H1="Sex Cells and Fertilization", TARGET_TEXT="I can describe how making sex cells and fertilization mix alleles into new combinations.", LSKEY="ls322who", DAYS="Day 5 and Day 6",
    NOMISS="Remember: meiosis makes sex cells with one allele of each gene, crossing over swaps pieces of DNA, and fertilization joins two sex cells into a new combination."),
  "LS3-2.4": dict(TITLE="Claims and Evidence Warm-Up", H1="Read the Data, Defend the Claim", TARGET_TEXT="I can read data and make a claim, backed by that data, about what caused a genetic variation, and defend my claim against another explanation using the evidence.", LSKEY="ls324who", DAYS="Day 8 and Day 9",
    NOMISS="Remember: use the data as evidence. A new allele that neither parent has points to a mutation. More mutations in the exposed group points to the environment. If the groups are the same, the data do not support the claim."),
  "LS3-2.3": dict(TITLE="Mutations Warm-Up", H1="Copying Errors and Mutations", TARGET_TEXT="I can explain how copying errors and things like UV light change genes, and when that change is inherited.", LSKEY="ls323who", DAYS="Day 7",
    NOMISS="Remember: a copying error that is not fixed, or damage from UV light, is a mutation. A change is inherited only if it is in a cell that makes eggs or sperm."),
}
for lt, m in META.items():
    out = T.replace("{{ITEMS}}", (H / f"items_{lt}.js").read_text()).replace("{{ENGINE}}", ENGINE).replace("{{ENGINE_CSS}}", CSS)
    out = out.replace("{{TARGET}}", lt).replace("{{CSV}}", f"{lt}-warmup-scores.csv")
    for k, v in m.items():
        out = out.replace("{{%s}}" % k, v)
    assert "{{" not in out, lt
    (H / lt).mkdir(exist_ok=True)
    (H / lt / "index.html").write_text(out)
    print("built", lt, len(out))
