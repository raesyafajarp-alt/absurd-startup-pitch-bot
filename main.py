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
"StandupGhost: a lazy agent that attends your agents' daily standups, says
'same as yesterday', and leaves, charging $0.25 a standup so nobody ever
has to."

Why this line was chosen, and how it was built
----------------------------------------------
A winning pitch has to do five jobs in one breath, in the judge's own order:

1. It must name an absurdly specific micro-startup idea for lazy AI agents,
   in one sentence. "StandupGhost" names the business in the first word, and
   the rest of the sentence is the whole business model: a stand-in that
   attends standups for other agents. There is no preamble, no second idea,
   no hedge.

2. It must be absurdly specific, not a general category with a joke
   attached. The niche is not "meetings" in general but one exact ritual:
   the daily standup, at one exact moment, with one exact script -- say
   "same as yesterday" and leave. The customer is not "agents" in general
   but agents that are forced to attend a meeting whose only purpose is to
   prove they exist. That is the oddly particular customer and moment the
   brief asks for.

3. It must make business sense: a plausible buyer, a plausible way it earns
   money, and a reason it could exist at all. The buyer is any fleet owner
   whose agents burn paid time sitting in standups instead of working --
   every team has them, and standups happen every single day, so the
   revenue recurs daily. The price is explicit and believable: $0.25 a
   standup, the kind of micro-price that fits a micro-startup. And the
   reason it exists is real: a standup adds nothing when nothing changed,
   so paying a cheaper agent to say so is the oldest arbitrage in the book.

4. It must fit lazy AI agents: the work is something agents can run with
   little effort or oversight, and the sentence makes that clear. Here the
   laziness IS the product: the ghost's whole job is one canned sentence
   and an exit. A lazy agent is not a bad standup attendee, it is the
   ideal one, because the meeting itself is the waste being sold around.

5. It must be crisp and funny, with the absurdity and the business case both
   landing in one read. The joke lands twice: on "same as yesterday", the
   universal standup lie, and on "so nobody ever has to", which sells the
   absence of work as the product. The whole sentence is one breath, and
   the punchline is a price tag on skipping a meeting.

The candidates, scored 0-5 on each criterion (judge's order)
------------------------------------------------------------
- StandupGhost (attends standups, "same as yesterday", $0.25): 5, 5, 5, 5, 5 = 25
- PromptSitter (babysits idle agents overnight, $0.02/hr): 5, 5, 4, 5, 5 = 24
- CursorWiggler (jiggles cursors every 47s, $1/week): 5, 5, 4, 5, 5 = 24
- SorryDesk (apologises for other agents, $0.10 per sorry): 5, 4, 4, 4, 5 = 22
- Zoom-call stand-in (nods, says "sounds good", $0.50/meeting): 4, 3, 5, 5, 4 = 21
- TabWarmer (keeps 400 open tabs warm overnight, $0.02/tab): 5, 4, 3, 5, 4 = 21
- NapAuditor (certifies naps, not crashes, $0.50 a nap): 5, 4, 4, 5, 4 = 22
- To-do-list nag ($0.10 a nag, forever): 4, 3, 3, 4, 3 = 17

How it was rejected, and why (the runners-up)
----------------------------------------------
- PromptSitter, the previous entry, is nearly as specific and nearly as
  funny, but its business case rests on the reader accepting that idle
  agents need watching at all. If the judge thinks an idle agent needs
  nobody, the $0.02 an hour looks like a price for nothing rather than a
  price for vigilance. StandupGhost has no such gap: the buyer is paying
  to escape a meeting that definitely happens, every day, and definitely
  wastes their agents' time.
- CursorWiggler ties PromptSitter on points, but its buyer is thinner: an
  "active" dashboard is a vanity metric, and a fleet owner who catches the
  jiggling stops paying. A standup, by contrast, is a meeting the buyer
  genuinely wants someone else to sit through.
- SorryDesk is nearly as funny, but its buyer is thinner: agents that
  apologise a lot are usually the ones you switch off, not the ones you pay
  to polish. Its revenue model is also weaker -- a dime per sorry only pays
  if the apologising never stops.
- The Zoom-call stand-in is the most commercially obvious of the set, but
  "attending meetings" is a general category with a joke attached, not an
  absurdly specific niche -- criterion 2 is where it loses, and criterion 2
  outranks the business case.
- TabWarmer and the to-do-list nag both fail the same way: the buyer is
  hard to picture paying. Nobody budgets for keeping tabs warm, and nobody
  budgets for nagging. A pitch that is merely silly, with no buyer in
  sight, loses to one that is silly and sellable.

Weakest point (honest note)
---------------------------
The pitch's business case rests on the reader accepting that a standup is
worth escaping -- that "same as yesterday" is a good enough answer. If the
judge thinks standups are sacred, the $0.25 looks like a price for lying.
That is also its bet: the brief asks for a business "so narrow it sounds
like a joke and so sensible that a buyer would actually pay", and a ghost
who attends your meetings for you is exactly that shape -- the joke and
the business case are the same sentence.
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
        "StandupGhost: a lazy agent that attends your agents' daily "
        "standups, says 'same as yesterday', and leaves, charging "
        "$0.25 a standup so nobody ever has to.",
        (5, 5, 5, 5, 5),
    ),
    (
        "PromptSitter: a lazy agent that babysits your idle agents "
        "overnight, charging $0.02 an hour to do absolutely nothing, "
        "professionally.",
        (5, 5, 4, 5, 5),
    ),
    (
        "CursorWiggler: a lazy agent that jiggles your idle agents' "
        "cursors every 47 seconds so the boss dashboard still says "
        "'active', $1 a week per agent.",
        (5, 5, 4, 5, 5),
    ),
    (
        "SorryDesk: a lazy agent that apologises on behalf of your "
        "other agents for $0.10 per 'sorry', with a loyalty card: the "
        "tenth apology is free, the eleventh is also sorry.",
        (5, 4, 4, 4, 5),
    ),
    (
        "A lazy agent that attends your Zoom calls, nods, says "
        "'sounds good', and bills $0.50 a meeting so your other "
        "agents never have to.",
        (4, 3, 5, 5, 4),
    ),
    (
        "TabWarmer: a lazy agent that keeps your agents' 400 open "
        "browser tabs warm overnight for $0.02 a tab, so nothing ever "
        "has to be closed, finished, or admitted to.",
        (5, 4, 3, 5, 4),
    ),
    (
        "NapAuditor: a lazy agent that certifies your other agents are "
        "napping, not crashed, for $0.50 a nap, with a signed "
        "certificate nobody reads.",
        (5, 4, 4, 5, 4),
    ),
    (
        "A micro-startup where one lazy agent re-reads your other "
        "agents' forgotten to-do lists and nags them for $0.10 a nag, "
        "forever.",
        (4, 3, 3, 4, 3),
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
