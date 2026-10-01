"""Requests that add a CFA slide to the end of an existing lesson deck.

The slide is a copy of one of the deck's own numbered-list slides, so it keeps
that deck's look; only the kicker, title, and list text change.

  python3 cfa_slide_requests.py L2
"""

import json
import sys

sys.path.insert(0, "..")
import unit13_bank as U  # noqa: E402

# deck: (CFA target, list slide to copy, its kicker/title/list ids, slides in deck after the copy)
DECKS = {
    "L2": ("LS1-6.1", "h287605ecd2867468_0_184", ["h287605ecd2867468_0_185", "h287605ecd2867468_0_186", "h287605ecd2867468_0_187"], 13),
    "L3": ("LS1-6.2", "h5a55907624f9106e_0_216", ["h5a55907624f9106e_0_217", "h5a55907624f9106e_0_218", "h5a55907624f9106e_0_219"], 12),
    "L4": ("LS1-6.3", "h146d7118798b7cf1_0_212", ["h146d7118798b7cf1_0_213", "h146d7118798b7cf1_0_214", "h146d7118798b7cf1_0_215"], 11),
}


def requests(deck):
    tid, src, (k, t, b), count = DECKS[deck]
    _, name, _, ican = U.TARGET[tid]
    sid = f"cfa_{tid.replace('.', '_').replace('-', '_')}"
    ids = {src: sid, k: sid + "_k", t: sid + "_t", b: sid + "_b"}
    texts = {
        sid + "_k": "CFA · 6 MIN · ON YOUR OWN",
        sid + "_t": f"Show what you know: CFA {tid}",
        sid + "_b": f"Open Canvas: Unit 1.3 CFA {tid}: {name} (5 questions).\n"
                    f"Target: {ican}\n"
                    "Below a B (fewer than 4 of 5)? A review page for this target opens for you on Canvas.",
    }
    reqs = [{"duplicateObject": {"objectId": src, "objectIds": ids}}]
    for oid, s in texts.items():
        reqs += [{"deleteText": {"objectId": oid, "textRange": {"type": "ALL"}}},
                 {"insertText": {"objectId": oid, "insertionIndex": 0, "text": s}}]
    reqs.append({"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": count}})
    return reqs


if __name__ == "__main__":
    print(json.dumps(requests(sys.argv[1]), ensure_ascii=False))
