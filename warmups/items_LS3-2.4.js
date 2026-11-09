  var ITEMS = [
    { skill: "Read the alleles and name the source", ref: "Day 9 warm-up and Case 1: the puppy litter", type: "single",
      grid: [["", "Allele 1", "Allele 2"], ["Mom", "F", "f"], ["Dad", "F", "f"], ["Puppy", "f", "f"]],
      text: "A coat-color gene has the alleles F and f. Which claim is best supported by the data?",
      key: "Both parents carry f, so the puppy ff is a new pairing of alleles the parents already had. Every allele was already in a parent, which is the clue for a new combination.",
      choices: [
        { t: "The puppy's alleles came from a new combination, because f was already in both parents", ok: true },
        { t: "The puppy's alleles came from a mutation, because the puppy differs from both parents", why: "Looking different is not evidence of a mutation. A mutation leaves a new allele that neither parent has. Here every allele was already in a parent." },
        { t: "The puppy's alleles came from UV light, because the puppy looks different from its parents", why: "Nothing in the data shows UV light or any other exposure, and looking different is not evidence. The alleles were already in the parents." },
        { t: "The puppy's alleles came from a copying error, because the puppy has two of the same allele", why: "Two of the same allele is not a clue for a copying error. A copying error leaves a new allele that neither parent has." }
      ],
      reteach: {
        viz: null,
        sort: { prompt: "Mom is Ff and Dad is Ff. Sort each of the puppy's alleles: was it already in a parent, or is it new?",
          buckets: ["Already in a parent", "New"],
          cards: [
            { t: "The puppy's first f", b: 0, why: "Mom has an f, so it was already in a parent." },
            { t: "The puppy's second f", b: 0, why: "Dad has an f too, so it was already in a parent." }
          ] },
        steps: [
          { q: "Every allele in the puppy was already in a parent. What does that clue point to?", o: ["A new combination", "A mutation", "An environmental mutation"], right: "A new combination: a new pairing of alleles the parents already had.", hints: { 1: "A mutation leaves an allele that neither parent has. Here none are new.", 2: "An environmental mutation would also leave a new allele, with more mutations in an exposed group. Nothing like that is here." } },
          { q: "Which clue would point to a mutation instead?", o: ["An allele that neither parent has", "An allele that both parents have", "A puppy that looks different from its parents"], right: "A new allele that neither parent has, like the CCT puppy in Case 2.", hints: { 1: "Alleles both parents have are the clue for a new combination.", 2: "Looking different is not evidence. Check the alleles." } }
        ] } },

    { skill: "Make a claim from the data", ref: "Day 9 Case 3: X-rays and mice", type: "single",
      grid: [["Group of mice", "X-ray dose", "New mutations per 1,000 sperm cells"], ["A", "none", "3"], ["B", "low", "12"], ["C", "high", "25"]],
      text: "Scientists exposed mice to X-rays and counted new mutations in sperm cells. Which claim is best supported by the data?",
      key: "The count goes up as the dose goes up. The group with no X-rays shows the baseline from copying errors, so the extra mutations came from the X-rays.",
      choices: [
        { t: "X-rays increased the number of mutations, because the counts rise as the dose rises", ok: true },
        { t: "X-rays had no effect on mutations, because the group with no X-rays also had mutations", why: "The no-X-ray group's 3 mutations are the baseline from copying errors. The high-dose group had 25, so the X-rays caused the extra." },
        { t: "Copying errors caused every mutation, because all three groups had some mutations", why: "Copying errors happen in every group, so they explain about 3. They cannot explain the extra 22 in the high-dose group." },
        { t: "The low dose caused more mutations than the high dose, because the low dose came first", why: "The order does not matter. Read the numbers: the low dose had 12 and the high dose had 25." }
      ],
      reteach: {
        viz: { type: "dose", label: "X-ray dose", prompt: "Move the slider from no X-rays to a high dose. Watch the number of new mutations.", unit: "mutations per 1,000 sperm cells", max: 25, levels: [{ label: "none", value: 3 }, { label: "low", value: 12 }, { label: "high", value: 25 }] },
        steps: [
          { q: "The group with no X-rays still had 3 mutations. Where did they come from?", o: ["Copying errors", "The X-rays", "A new combination"], right: "Copying errors. They happen in every group, so 3 is the baseline.", hints: { 1: "This group had no X-rays.", 2: "A new combination does not change the DNA, so it is not a mutation." } },
          { q: "As the X-ray dose went up, the number of mutations...", o: ["went up", "stayed the same", "went down"], right: "Went up: 3, then 12, then 25.", hints: { 1: "Look at the slider again. The bar grew.", 2: "The bar got longer, not shorter." } },
          { q: "Which claim does that evidence support?", o: ["X-rays increased the number of mutations", "X-rays had no effect on mutations", "Copying errors caused every mutation"], right: "X-rays increased the number of mutations. Copying errors only explain the baseline of 3.", hints: { 1: "The no-X-ray group had a few mutations, but the high-dose group had far more.", 2: "Copying errors happen in both groups, so they cannot explain the extra 22." } }
        ] } },

    { skill: "Evaluate a claim", ref: "Day 8 mini-lesson: How to defend a claim", type: "single",
      grid: [["Group", "Exposed to the chemical?", "New mutations per 1,000 cells"], ["1", "Yes", "5"], ["2", "No", "5"]],
      text: "Scientists compared mutation counts. A student claims the chemical caused mutations. Which statement best evaluates the claim?",
      key: "If the chemical caused mutations, the exposed group would have more than the group that was not exposed. Both groups had 5, so the data do not support the claim.",
      choices: [
        { t: "The data do not support the claim, because both groups had the same number of mutations", ok: true },
        { t: "The data support the claim, because the exposed group had some mutations in its own cells", why: "The group that was not exposed had 5 mutations too, and those come from copying errors. The chemical added none." },
        { t: "The data support the claim, because chemicals always change the DNA of every cell in the body", why: "That is not evidence from this table. The data would need to show more mutations in the exposed group, and it does not." },
        { t: "The data cannot be used, because there are two groups to compare in the table", why: "Two groups is what you want: one exposed and one not. Comparing them is how you test the claim." }
      ],
      reteach: {
        viz: { type: "dose", label: "Group", prompt: "Switch between the two groups and compare the number of mutations.", unit: "new mutations per 1,000 cells", max: 10, levels: [{ label: "Not exposed", value: 5 }, { label: "Exposed to the chemical", value: 5 }] },
        steps: [
          { q: "How do the two groups compare?", o: ["They are the same: 5 and 5", "The exposed group has more", "The group that was not exposed has more"], right: "The same: 5 and 5.", hints: { 1: "Look at the bars. They are the same length.", 2: "Both bars are the same length." } },
          { q: "If the chemical caused mutations, the exposed group would have...", o: ["more mutations than the group that was not exposed", "fewer mutations", "exactly the same number"], right: "More. The extra would be the chemical's effect, like the extra 22 in the X-ray case.", hints: { 1: "A chemical that damages DNA would add mutations, not remove them.", 2: "If the numbers were the same, the chemical would have changed nothing." } },
          { q: "So do the data support the claim that the chemical caused mutations?", o: ["No, both groups had the same number", "Yes, the exposed group had some mutations", "Yes, chemicals always change DNA"], right: "No. Both groups had 5, so the chemical added no extra mutations.", hints: { 1: "The group that was not exposed had 5 as well, so those are not from the chemical.", 2: "The claim has to be backed by the data, not by what is always true." } }
        ] } }
  ];

