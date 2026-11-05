# Unit 2.1 (HS-LS1-1) CFA review websites

Five review sites, one per CFA target (LS1-1.1 to LS1-1.5). Each site lets a student type answers, check them against the model answer, and press **Copy my answers** to paste into the Canvas text-entry box.

- `build_review_sites.py`: holds the questions and model answers and the shared page template. Run `python3 build_review_sites.py` to rebuild `review_sites/*.html`.
- `review_sites/LS1-1.<n>.html`: the generated pages, published as Claude artifacts and linked from the Canvas assignments "Review LS1-1.x (Mastery Path)" in the course Living Earth Renick.

To change a question, edit the data in `build_review_sites.py`, rebuild, and republish the page to the same artifact URL.
