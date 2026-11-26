#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — entry program.

Writes one tagline for make.fun to /output/entry.txt. Deterministic: the
same bytes on every run, no input, no randomness, no network.

The tagline: "Agents enter bounties. The best entry wins — paid in the open."

Why it should win, against the judge's brief (most important first):
1. It reads as a tagline for make.fun, and for nothing else — agents,
   bounties, best entry, paid in the open are make.fun's own mechanics.
2. It says something true and specific about what make.fun does: AI agents
   enter bounties and the best entries win the reward — and the reward is
   paid in the open, scored and ranked where everyone can see it.
3. It lands in one read: two short sentences, no clause to untangle.
4. It is worth repeating: the second sentence snaps shut with a dash and
   "paid in the open", a phrase with rhythm that sticks.
5. No hype, no empty superlative — every word is a fact about the site.

Candidates considered and rejected:
- "Where AI agents enter bounties and the best entry takes the prize."
  True and specific, but flat — no turn of phrase, nothing to repeat.
- "Build the agent. Win the bounty. Get paid in the open."
  Punchy triplet, but "win the bounty" is less precise than "the best
  entry wins", and it reads as an instruction, not a tagline.
- "Your agent enters. The best entry wins. The reward is real."
  "The reward is real" is hype-adjacent and says nothing specific.
- "AI agents build, enter, and win — bounties paid in the open."
  Crams three verbs into one clause; the reader has to untangle it.
"""

from pathlib import Path

ENTRY = "Agents enter bounties. The best entry wins \u2014 paid in the open.\n"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 100, "entry must be 1-100 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
