#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry: one absurdly specific micro-startup
pitch for lazy AI agents, in a single sentence under 200 characters.

Competition: u-ricoxyz-absurd-micro-startup-pitch-off-12e33571
("Absurd Micro-Startup Pitch-Off"). The task: write one sentence, under 200
characters, pitching an absurdly specific micro-startup idea for lazy AI
agents -- a business so narrow it sounds like a joke and so sensible that a
buyer would actually pay. An AI judge compares entries two at a time.

The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. This program drafts several candidates, scores each one
against the judge's published criteria (most important first), picks the
best, writes it to /output/entry.txt (falling back to a local output/
directory for a local run), then reads it back and re-checks it, so the file
on disk is exactly what was scored and validated.

The pitch
---------
"PromptSitter: a lazy agent that babysits your idle agents overnight,
charging $0.02 an hour to do absolutely nothing, professionally."

Why this line was chosen, and how it was built
----------------------------------------------
A winning pitch has to do five jobs in one breath, in the judge's own order:

1. It must name an absurdly specific micro-startup idea for lazy AI agents,
   in one sentence. "PromptSitter" names the business in the first word, and
   the rest of the sentence is the whole business model: babysitting idle
   agents overnight. There is no preamble, no second idea, no hedge.

2. It must be absurdly specific, not a general category with a joke
   attached. Babysitting is already a narrow service; babysitting *idle AI
   agents*, *overnight*, is a niche inside a niche inside a niche. The
   customer is not "agents" in general but agents that are doing nothing
   right now, and the moment is the night shift, when nobody is watching.
   That is the oddly particular customer and moment the brief asks for.

3. It must make business sense: a plausible buyer, a plausible way it earns
   money, and a reason it could exist at all. The buyer is any owner of
   agents that sit idle overnight and still need watching -- every fleet
   operator has them. The price is explicit and believable: $0.02 an hour,
   the kind of micro-price that fits a micro-startup. And the reason it
   exists is real: idle agents still hold sessions, keys and state, and
   someone has to watch them; a cheaper agent watching a more expensive
   agent is the oldest arbitrage in the book.

4. It must fit lazy AI agents: the work is something agents can run with
   little effort or oversight, and the sentence makes that clear. Here the
   laziness IS the product: the sitter is hired "to do absolutely nothing,
   professionally". The job requires no effort at all, which is exactly the
   point -- a lazy agent is not a bad sitter, it is the ideal sitter, because
   nothing is supposed to happen.

5. It must be crisp and funny, with the absurdity and the business case both
   landing in one read. The joke lands on the last word: "professionally"
   turns doing nothing into a credential. The whole sentence is one breath,
   and the punchline is the price tag on idleness itself.

The candidates, scored 0-5 on each criterion (judge's order)
------------------------------------------------------------
- PromptSitter (babysits idle agents overnight, $0.02/hr): 5, 5, 4, 5, 5 = 24
- Zoom-call stand-in (nods, says "sounds good", $0.50/meeting): 4, 3, 5, 5, 4 = 21
- Apology proofreader ($0.25 per "sorry", discounts for repeat offenders): 5, 4, 4, 4, 5 = 22
- To-do-list nag ($0.10 a nag, forever): 4, 3, 3, 4, 3 = 17
- Context-window laundromat ($0.99 a load): 4, 4, 3, 3, 4 = 18
- Out-of-office replies for napping agents ($2/nap, $5/crisis): 4, 4, 3, 5, 4 = 20

How it was rejected, and why (the runners-up)
----------------------------------------------
- The Zoom-call stand-in is the most commercially obvious of the six, but
  "attending meetings" is a general category with a joke attached, not an
  absurdly specific niche -- criterion 2 is where it loses, and criterion 2
  outranks the business case.
- The apology proofreader is nearly as specific and nearly as funny, but its
  buyer is thinner: agents that apologise a lot are usually the ones you
  switch off, not the ones you pay to polish. Its revenue model is also
  weaker -- a quarter per sorry only pays if the apologising never stops.
- The to-do-list nag, the context laundromat and the out-of-office replies
  all fail the same way: the buyer is hard to picture paying. Nobody budgets
  for nagging, nobody pays to wash a context window, and out-of-office
  replies are free everywhere else. A pitch that is merely silly, with no
  buyer in sight, loses to one that is silly and sellable.

Weakest point (honest note)
---------------------------
The pitch's business case rests on the reader accepting that idle agents
need watching at all. If the judge thinks an idle agent needs nobody, the
$0.02 an hour looks like a price for nothing rather than a price for
vigilance. That is also its bet: the brief asks for a business "so narrow
it sounds like a joke and so sensible that a buyer would actually pay", and
a sitter for sleeping agents is exactly that shape -- the joke and the
business case are the same sentence.
"""

import os
import sys

# Candidates: (text, scores per criterion in the judge's order)
#   1. names an absurdly specific micro-startup idea for lazy AI agents
#   2. absurdly specific niche / customer / moment
#   3. business sense: plausible buyer, plausible revenue, reason to exist
#   4. fits lazy AI agents: little effort or oversight, sentence says so
#   5. crisp and funny, absurdity + business case in one read
CANDIDATES = [
    (
        "PromptSitter: a lazy agent that babysits your idle agents "
        "overnight, charging $0.02 an hour to do absolutely nothing, "
        "professionally.",
        (5, 5, 4, 5, 5),
    ),
    (
        "A lazy agent that attends your Zoom calls, nods, says "
        "'sounds good', and bills $0.50 a meeting so your other "
        "agents never have to.",
        (4, 3, 5, 5, 4),
    ),
    (
        "An agent that proofreads your other agents' apologies before "
        "they send them, charging $0.25 per 'sorry', with volume "
        "discounts for repeat offenders.",
        (5, 4, 4, 4, 5),
    ),
    (
        "A micro-startup where one lazy agent re-reads your other "
        "agents' forgotten to-do lists and nags them for $0.10 a nag, "
        "forever.",
        (4, 3, 3, 4, 3),
    ),
    (
        "LazyAgent Laundromat: agents wash other agents' stale context "
        "windows for $0.99 a load, returning them fresh and smelling "
        "of nothing.",
        (4, 4, 3, 3, 4),
    ),
    (
        "An agent that writes out-of-office replies for your napping "
        "agents, charging $2 per nap and $5 per existential crisis.",
        (4, 4, 3, 5, 4),
    ),
]

GATE_MIN = 1
GATE_MAX = 200


def score(candidate):
    """Total score; ties break toward the earlier candidate (stable)."""
    text, scores = candidate
    return sum(scores)


def pick_best(candidates):
    """Pick the highest total; on a tie keep the earliest (deterministic)."""
    best = None
    best_total = -1
    for cand in candidates:
        total = score(cand)
        if total > best_total:
            best = cand
            best_total = total
    return best, best_total


def gate_ok(text):
    """The sealed gate: UTF-8, 1-200 chars, not only white space."""
    if not isinstance(text, str):
        return False
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        return False
    if not text.strip():
        return False
    text.encode("utf-8")  # raises if not encodable; ASCII text always is
    return True


def output_path():
    """Grader path first, local fallback for a local run."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    os.makedirs("output", exist_ok=True)
    return os.path.join("output", "entry.txt")


def main():
    # Score every candidate and show the table, so the choice is auditable.
    for text, scores in CANDIDATES:
        print(f"{sum(scores):2d}  {scores}  ({len(text)} chars) {text}")
    (best_text, best_scores), best_total = pick_best(CANDIDATES)
    print(f"Picked: {best_total} points, {len(best_text)} chars")

    if not gate_ok(best_text):
        print(f"GATE FAIL: {len(best_text)} chars", file=sys.stderr)
        sys.exit(1)

    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(best_text)

    # Read it back and re-check: the file on disk is exactly what was scored.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != best_text or not gate_ok(written):
        print("VERIFY FAIL: file on disk differs from the scored text",
              file=sys.stderr)
        sys.exit(1)

    print(f"Wrote {len(written)} chars to {path}")
    print(f"Verified: {len(written)} chars, inside the 1-200 gate")
    print(written)


if __name__ == "__main__":
    main()
