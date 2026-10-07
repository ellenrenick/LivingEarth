"""Build the Canvas outcomes import CSV for Living Earth (HS-LS standards).

Run: python3 build_outcomes.py   ->  LivingEarth_outcomes.csv
Import in Canvas: Outcomes > Import (course or account level).
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RATINGS = [(4, "Advanced"), (3, "Proficient"), (2, "Developing"),
           (1, "Beginning"), (0, "No Evidence")]
CALC_METHOD, CALC_INT = "decaying_average", 65

GROUPS = [
    ("LE-LS1", "HS-LS1 From Molecules to Organisms: Structures and Processes"),
    ("LE-LS2", "HS-LS2 Ecosystems: Interactions, Energy, and Dynamics"),
    ("LE-LS3", "HS-LS3 Heredity: Inheritance and Variation of Traits"),
    ("LE-LS4", "HS-LS4 Biological Evolution: Unity and Diversity"),
]

OUTCOMES = [
    ("LS1", "HS-LS1-1", "Explain how DNA structure determines protein structure and cell function",
     "Construct an explanation based on evidence for how the structure of DNA determines the structure of proteins which carry out the essential functions of life through systems of specialized cells."),
    ("LS1", "HS-LS1-2", "Model how body systems interact",
     "Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms."),
    ("LS1", "HS-LS1-3", "Investigate feedback mechanisms and homeostasis",
     "Plan and conduct an investigation to provide evidence that feedback mechanisms maintain homeostasis."),
    ("LS1", "HS-LS1-4", "Model the role of mitosis in growth",
     "Use a model to illustrate the role of cellular division (mitosis) and differentiation in producing and maintaining complex organisms."),
    ("LS1", "HS-LS1-5", "Model photosynthesis energy conversion",
     "Use a model to illustrate how photosynthesis transforms light energy into stored chemical energy."),
    ("LS1", "HS-LS1-6", "Explain how sugar becomes amino acids and large molecules",
     "Construct and revise an explanation based on evidence for how carbon, hydrogen, and oxygen from sugar molecules may combine with other elements to form amino acids and/or other large carbon-based molecules."),
    ("LS1", "HS-LS1-7", "Model cellular respiration",
     "Use a model to illustrate that cellular respiration is a chemical process whereby the bonds of food molecules and oxygen molecules are broken and the bonds in new compounds are formed, resulting in a net transfer of energy."),
    ("LS2", "HS-LS2-1", "Use math to explain carrying capacity",
     "Use mathematical and/or computational representations to support explanations of factors that affect carrying capacity of ecosystems at different scales."),
    ("LS2", "HS-LS2-2", "Use math to show biodiversity and population change",
     "Use mathematical representations to support and revise explanations based on evidence about factors affecting biodiversity and populations in ecosystems of different scales."),
    ("LS2", "HS-LS2-3", "Explain matter and energy cycling with and without oxygen",
     "Construct and revise an explanation based on evidence for the cycling of matter and flow of energy in aerobic and anaerobic conditions."),
    ("LS2", "HS-LS2-4", "Use math to model energy transfer in ecosystems",
     "Use mathematical representations to support claims for the cycling of matter and flow of energy among organisms in an ecosystem."),
    ("LS2", "HS-LS2-5", "Model photosynthesis and respiration in the carbon cycle",
     "Develop a model to illustrate the role of photosynthesis and cellular respiration in the cycling of carbon among the biosphere, atmosphere, hydrosphere, and geosphere."),
    ("LS2", "HS-LS2-6", "Evaluate ecosystem stability and change",
     "Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem."),
    ("LS2", "HS-LS2-7", "Design solutions to reduce human impact on biodiversity",
     "Design, evaluate, and refine a solution for reducing the impacts of human activities on the environment and biodiversity."),
    ("LS2", "HS-LS2-8", "Evaluate group behavior and survival",
     "Evaluate the evidence for the role of group behavior on individual and species' chances to survive and reproduce."),
    ("LS3", "HS-LS3-1", "Ask questions about DNA and traits",
     "Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring."),
    ("LS3", "HS-LS3-2", "Explain sources of genetic variation",
     "Make and defend a claim based on evidence that inheritable genetic variations may result from (1) new genetic combinations through meiosis, (2) viable errors occurring during replication, and/or (3) mutations caused by environmental factors."),
    ("LS3", "HS-LS3-3", "Use statistics to explain trait variation",
     "Apply concepts of statistics and probability to explain the variation and distribution of expressed traits in a population."),
    ("LS4", "HS-LS4-1", "Communicate evidence for common ancestry",
     "Communicate scientific information that common ancestry and biological evolution are supported by multiple lines of empirical evidence."),
    ("LS4", "HS-LS4-2", "Explain how natural selection happens",
     "Construct an explanation based on evidence that the process of evolution primarily results from four factors: (1) the potential for a species to increase in number, (2) the heritable genetic variation of individuals in a species, (3) competition for limited resources, and (4) the proliferation of those organisms that are better able to survive and reproduce in the environment."),
    ("LS4", "HS-LS4-3", "Use statistics to show adaptation",
     "Apply concepts of statistics and probability to support explanations that organisms with an advantageous heritable trait tend to increase in proportion to organisms lacking this trait."),
    ("LS4", "HS-LS4-4", "Explain adaptation through natural selection",
     "Construct an explanation based on evidence for how natural selection leads to adaptation of populations."),
    ("LS4", "HS-LS4-5", "Evaluate how environmental change affects species",
     "Evaluate the evidence supporting claims that changes in environmental conditions may result in (1) increases in the number of individuals of some species, (2) the emergence of new species over time, and (3) the extinction of other species."),
    ("LS4", "HS-LS4-6", "Design solutions to reduce human impact on biodiversity",
     "Create or revise a simulation to test a solution to mitigate adverse impacts of human activity on biodiversity."),
]

header = ["vendor_guid", "object_type", "title", "description", "display_name",
          "calculation_method", "calculation_int", "workflow_state",
          "parent_guids", "ratings"] + [""] * (len(RATINGS) * 2 - 1)

rows = [header]
pad = lambda r: r + [""] * (len(header) - len(r))
for guid, title in GROUPS:
    rows.append(pad([guid, "group", title, "", "", "", "", "active", "", ""]))
for ls, code, short, desc in OUTCOMES:
    ratings = [x for pts, name in RATINGS for x in (pts, name)]
    rows.append(pad([f"LE-{code}", "outcome", code, desc, short,
                     CALC_METHOD, CALC_INT, "active", f"LE-{ls}"] + [""] * 0)[:9]
                + ratings)

with open(os.path.join(HERE, "LivingEarth_outcomes.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)
