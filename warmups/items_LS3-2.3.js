  var ITEMS = [
    { skill: "What a copying error is", ref: "Day 7 mini-lesson: How do mutations happen?", type: "single",
      text: "Before a cell divides, it copies all of its DNA. Cells check the copy, and most copying errors are fixed. What is a rare copying error that stays?",
      key: "A rare copying error that is not fixed becomes a mutation. A mutation is a change in the DNA sequence.",
      choices: [
        { t: "A mutation, which is a change in the DNA sequence", ok: true },
        { t: "A new combination of alleles, made when a sperm and an egg join", why: "That is fertilization. A copying error is a mistake made when DNA is copied, so it changes the DNA itself." },
        { t: "A change that is always fixed later, so it never affects the DNA", why: "Cells fix most copying errors, but a rare one stays. The ones that stay are the mutations." },
        { t: "A change in how the body looks, like a suntan, that is not in the DNA", why: "A suntan is not in the DNA. A copying error that stays is a change in the DNA itself." }
      ],
      reteach: {
        viz: { type: "spot", orig: "ATGCCTAAG", copy: "ATGCCTTAG", prompt: "A cell is copying its DNA. Tap the one letter in the copy that does not match the original.", found: "That is the copying error. Cells check the copy and fix most errors, but a rare one stays." },
        steps: [
          { q: "A rare copying error that stays in the DNA is called a...", o: ["mutation", "new combination", "suntan"], right: "A mutation.", hints: { 1: "A new combination comes from fertilization, not from copying.", 2: "A suntan is not in the DNA." } },
          { q: "A mutation is a change in the...", o: ["DNA sequence", "way the body looks"], right: "The DNA sequence.", hints: { 1: "Changes in how a body looks are not mutations. A mutation is in the DNA." } }
        ] } },

    { skill: "Which change is inherited", ref: "Day 7 sort: Who passes it on? Five cases", type: "single",
      text: "In an animal, which change could the next generation inherit?",
      key: "In animals, a change is inherited only if it is in a cell that makes eggs or sperm. Skin, muscle, and lung cells are body cells.",
      choices: [
        { t: "A copying error in a cell that makes sperm", ok: true },
        { t: "UV light damages DNA in a skin cell", why: "Skin is a body cell. The change is not passed on, because the skin cell does not make eggs or sperm." },
        { t: "A copying error in a muscle cell of the leg", why: "Muscle is a body cell. A change in a body cell is not passed on, even when it is a real mutation." },
        { t: "Smoke damages DNA in a lung cell", why: "Lung is a body cell. Only a change in a cell that makes eggs or sperm can be passed on." }
      ],
      reteach: { sort: { prompt: "A mutation happens in each of these cells. Could the next generation inherit it?",
        buckets: ["Can be passed on", "Not passed on"],
        cards: [
          { t: "A skin cell", b: 1, why: "Skin is a body cell. The change is not passed on." },
          { t: "A muscle cell in the leg", b: 1, why: "Muscle is a body cell. The change is not passed on." },
          { t: "A lung cell", b: 1, why: "Lung is a body cell. The change is not passed on." },
          { t: "A cell that makes sperm", b: 0, why: "It makes sperm, so the change can be passed on." },
          { t: "A cell that makes eggs", b: 0, why: "It makes eggs, so the change can be passed on." }
        ] } } },

    { skill: "Why a one-letter change matters", ref: "Unit 2.1 and the Day 7 warm-up: GAG to GTG", type: "single",
      text: "In Unit 2.1, one DNA letter changed (GAG to GTG) and one amino acid changed (Glu to Val). Why might a one-letter mutation matter?",
      key: "A mutation changes the DNA sequence, and a different amino acid in a protein can make the protein work differently.",
      choices: [
        { t: "A different amino acid can make the protein work differently", ok: true },
        { t: "The protein is no longer made by any cell in the body", why: "In the Glu to Val example, the protein was still made. One amino acid was different." },
        { t: "Every other gene in the cell changes in the same way", why: "A mutation changes the DNA only where it happens. The other genes stay the same." },
        { t: "The mutation is copied into every cell of the body right away", why: "A mutation is in the cell where it happened, and in copies of that cell. It does not spread to every cell." }
      ],
      reteach: {
        viz: { type: "codon", before: "GAG", aa1: "Glu", after: "GTG", aa2: "Val", prompt: "This is the DNA letter code from Unit 2.1. Change one letter and watch the amino acid." },
        steps: [
          { q: "When one letter changed, what changed in the protein?", o: ["One amino acid (Glu became Val)", "Every amino acid", "Nothing changed"], right: "One amino acid changed.", hints: { 1: "Only the one amino acid for that spot changed.", 2: "Look at the amino acid line. It changed from Glu to Val." } },
          { q: "Can a different amino acid change how the protein works?", o: ["Yes, so one letter can matter", "No, a protein always works the same"], right: "Yes. That is why one letter can matter.", hints: { 1: "A different amino acid can change the protein's shape and how it works." } }
        ] } }
  ];

