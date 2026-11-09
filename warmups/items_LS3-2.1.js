  var ITEMS = [
    { skill: "Name the three sources", ref: "Day 2 mini-lesson: Three sources of new variation", type: "single",
      text: "Scientists name three ways new genetic variation arises. Which list names all three?",
      key: "The three sources are (1) new combinations of alleles, (2) copying errors when DNA is copied, and (3) mutations from the environment, like UV light and some chemicals.",
      choices: [
        { t: "New combinations of alleles, errors when DNA is copied, and mutations from the environment", ok: true },
        { t: "New combinations of alleles, errors when DNA is copied, and a suntan from the sun", why: "A suntan changes how skin looks, but the change is not in the DNA, so it is not inherited." },
        { t: "Offspring getting information from only one parent, errors when DNA is copied, and UV light", why: "Every offspring gets information from both parents. That is not a source of variation." },
        { t: "The food an animal eats, the temperature, and the amount of sunlight", why: "Food, temperature, and sunlight can change how an animal looks, but not its DNA." }
      ],
      reteach: { sort: { prompt: "Sort each one. Is it a source of new variation in the DNA, or does it only change how a body looks?",
        buckets: ["Source of new variation", "Only changes the body"],
        cards: [
          { t: "Sex cells join at fertilization", b: 0, why: "Yes. This makes a new combination of alleles." },
          { t: "A rare error slips through when DNA is copied", b: 0, why: "Yes. A copying error changes the DNA." },
          { t: "UV light damages the DNA inside a cell", b: 0, why: "Yes. A mutation from the environment changes the DNA." },
          { t: "A suntan from the sun", b: 1, why: "A suntan changes how skin looks. It is not in the DNA, so it is not inherited." },
          { t: "Eating different food", b: 1, why: "Food can change how a body looks, but not the DNA." },
          { t: "Cold weather changes how fur looks", b: 1, why: "Temperature changes how a body looks, but not the DNA." }
        ] } } },

    { skill: "Match a case to a source", ref: "Day 1 puppy puzzle and Day 2 card activity", type: "single",
      text: "Mom and Dad are both Bb. They have puppies that are BB, Bb, and bb. Which source explains why the puppies are different from each other?",
      key: "Every allele in the puppies, B and b, was already in the parents. No allele changed. Fertilization put two alleles together in different combinations, so this is a new combination of alleles.",
      choices: [
        { t: "New combinations of alleles: each parent's sex cell carries one allele, and fertilization puts two together", ok: true },
        { t: "A copying error: a rare error slipped through when DNA was copied", why: "Copying errors are rare and make a new allele. These puppies have only B and b, which both parents already had." },
        { t: "A mutation from the environment: UV light damaged the DNA", why: "A mutation is a change in the DNA. No allele changed here. The puppies got different combinations of B and b." },
        { t: "The food and temperature changed the puppies' DNA", why: "Food and temperature do not change DNA. They cannot explain BB, Bb, and bb." }
      ],
      reteach: {
        viz: { type: "fertilize", p1: ["B", "b"], p2: ["B", "b"], who: "puppy", plural: "puppies", fixed: { 3: ["b", "B"] }, prompt: "Mom and Dad are both Bb. Each sex cell gets one allele. Make 4 puppies and watch which alleles show up." },
        steps: [
          { q: "Which alleles did your puppies have?", o: ["Only B and b, which the parents already had", "A new allele that neither parent has"], right: "Right. Every allele was already in a parent.", hints: { 1: "Look at the list again. Only B and b appear." } },
          { q: "Did any allele change into something different?", o: ["No, the alleles just got combined in different ways", "Yes, a copying error changed one"], right: "Right. Nothing changed. The alleles were combined in different ways.", hints: { 1: "A copying error would make a brand new allele. You only saw B and b." } },
          { q: "So which source explains BB, Bb, and bb?", o: ["New combinations of alleles", "Copying errors", "Mutations from the environment"], right: "New combinations of alleles.", hints: { 1: "A copying error would make a new allele.", 2: "UV light would damage DNA. Nothing was damaged here." } }
        ] } },

    { skill: "Which sources change the DNA", ref: "Day 2 mini-lesson: Three sources of new variation", type: "multi", pick: 2,
      text: "Two of the three sources of new variation change the DNA itself. Select the TWO.",
      key: "Copying errors and mutations from the environment both change the DNA. A change in how a body looks from food, exercise, or temperature is not in the DNA, so it is not inherited.",
      choices: [
        { t: "A rare error slips through when DNA is copied before a cell divides", ok: true },
        { t: "UV light or some chemicals damage DNA", ok: true },
        { t: "Food, exercise, or temperature change how a body looks", why: "That change is in how the body looks, not in the DNA, so it is not inherited." },
        { t: "A suntan from the sun", why: "A suntan changes how skin looks. It is not in the DNA, so it is not inherited." }
      ],
      reteach: { steps: [
        { q: "A suntan changes how skin looks. Is that change in the DNA?", o: ["No, it is only how the body looks", "Yes, the DNA is changed"], right: "Right. Food, exercise, and temperature work the same way.", hints: { 1: "A suntan is on the skin. The DNA is not changed, so it is not inherited." } },
        { q: "Which of these does change the DNA itself?", o: ["UV light damaging DNA", "Eating healthy food", "Exercise"], right: "UV light and some chemicals can damage DNA. That is a mutation.", hints: { 1: "Food changes how a body looks, not its DNA.", 2: "Exercise changes the body, not the DNA." } },
        { q: "A rare error when DNA is copied changes...", o: ["the DNA", "only how the body looks"], right: "The DNA. That is the second source of new variation.", hints: { 1: "A copying error is a mistake in the DNA itself." } }
      ] } }
  ];

