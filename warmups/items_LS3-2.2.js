  var ITEMS = [
    { skill: "Sex cells from a Gg parent", ref: "Day 6 warm-up and mini-lesson: Sex cells and fertilization", type: "single",
      text: "A parent has the genotype Gg. Which sex cells can this parent make?",
      key: "A Gg parent makes sex cells with G or g. Each sex cell gets only one allele of each gene, like a coin flip, so some carry G and some carry g.",
      choices: [
        { t: "Some sex cells with G and some sex cells with g", ok: true },
        { t: "Only sex cells that carry both G and g together", why: "Gg is the genotype of her body cells, which carry two alleles. Her sex cells carry only one." },
        { t: "Only sex cells with the dominant allele, G", why: "Dominant only decides which trait shows up. Meiosis works like a coin flip, so g sex cells are made too." },
        { t: "Only sex cells that carry two copies, GG or gg", why: "Sex cells carry one allele, not two." }
      ],
      reteach: {
        viz: { type: "sexcells", alleles: ["G", "g"], prompt: "This parent is Gg. Her body cells carry two alleles. Make 4 sex cells and see what each one gets." },
        steps: [
          { q: "How many alleles did each sex cell you made get?", o: ["One", "Two", "None"], right: "One. Meiosis gives each sex cell one allele of each gene, like a coin flip.", hints: { 1: "Look at your sex cells. Each shows a single letter.", 2: "Every sex cell showed a letter, so it carried an allele." } },
          { q: "Which sex cells can a Gg parent make?", o: ["Some with G and some with g", "Only G, because G is dominant", "Only sex cells with both G and g"], right: "Some with G and some with g.", hints: { 1: "Dominant only decides which trait shows up. Look at your tally: g sex cells were made too.", 2: "No sex cell showed two letters. Each carries just one." } }
        ] } },

    { skill: "What fertilization does", ref: "Day 6 mini-lesson: Sex cells and fertilization", type: "single",
      text: "What happens at fertilization?",
      key: "At fertilization a sperm and an egg join. The offspring gets one allele from each parent, which makes a new combination of alleles.",
      choices: [
        { t: "A sperm and an egg join, so the offspring gets one allele from each parent: a new combination", ok: true },
        { t: "A body cell copies all of its DNA, so the offspring gets two copies of the same allele", why: "Copying DNA before a cell divides is a different step. Fertilization joins two sex cells, one allele from each parent." },
        { t: "An egg splits in two, so the offspring gets both of its alleles from its mother", why: "The offspring gets one allele from each parent, not both from the mother." },
        { t: "A mutation changes the alleles, so the offspring gets alleles that neither parent had", why: "A mutation is a different source of variation. Fertilization only joins alleles the parents already had." }
      ],
      reteach: {
        viz: { type: "fertilize", p1: ["G", "g"], p2: ["G", "g"], who: "baby", plural: "babies", prompt: "Mom and Dad are both Gg. Join one sex cell from each parent to make 4 babies." },
        steps: [
          { q: "How many alleles does a baby get from each parent?", o: ["One", "Two", "None"], right: "One from each parent.", hints: { 1: "Each sex cell carries one allele, so each parent gives one.", 2: "Each baby had a letter from Mom and a letter from Dad." } },
          { q: "Where do a baby's two alleles come from?", o: ["One from each parent", "Both from its mom", "A mutation made them"], right: "One from each parent.", hints: { 1: "Look at your babies. Each had an egg allele and a sperm allele.", 2: "A mutation is a different source. Here the alleles were already in the parents." } },
          { q: "The mix of alleles from two sex cells is a new ___ of alleles.", o: ["combination", "copy", "mutation"], right: "A combination. That is what fertilization makes.", hints: { 1: "A copy would be the same allele twice.", 2: "A mutation is a change in the DNA. Nothing changed here." } }
        ] } },

    { skill: "Crossing over", ref: "Day 6 vocabulary and mini-lesson: crossing over", type: "single",
      text: "Meiosis makes sex cells. What happens during crossing over?",
      key: "Crossing over happens during meiosis. Paired chromosomes swap pieces of DNA, which mixes the alleles before the sex cells are made.",
      choices: [
        { t: "Paired chromosomes swap pieces of DNA, which mixes the alleles", ok: true },
        { t: "A chromosome copies itself, so a sex cell gets two identical sets of DNA", why: "Copying DNA happens before a cell divides. Crossing over swaps pieces between paired chromosomes." },
        { t: "An egg and a sperm join, so the offspring gets one allele from each parent", why: "That is fertilization. Crossing over happens earlier, during meiosis." },
        { t: "A letter in the DNA changes, so a chromosome gets an allele that is new", why: "A change in the DNA is a mutation. Crossing over swaps pieces that are already there." }
      ],
      reteach: {
        viz: { type: "crossover", prompt: "These are a pair of chromosomes. Press the button to see what crossing over does to their pieces." },
        steps: [
          { q: "After crossing over, did any piece appear that was not already there?", o: ["No, the same pieces were swapped", "Yes, new pieces were made"], right: "No. The pieces were only swapped, so the alleles are mixed in a new way.", hints: { 1: "Compare before and after. The letters are all the same, just in new places." } },
          { q: "When does crossing over happen?", o: ["During meiosis, before the sex cells are made", "At fertilization, when sperm and egg join", "When a body cell copies its DNA"], right: "During meiosis, before the sex cells are made.", hints: { 1: "That is when sex cells join, which comes later.", 2: "Copying DNA is a different step. Crossing over happens when sex cells are made." } }
        ] } }
  ];

