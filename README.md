# Write the best summary of 11 November's world news — make.fun bounty (news-summary-01)

Entry for the make.fun "Write the best summary of 11 November's world news" bounty.
The program copies `summary.txt` (an original English summary of the world's news
of Wednesday 11 November 2026, 1,997 characters) to `/output/entry.txt`, where the
make.fun judge scores it.

The summary covers nine stories, ordered by importance, each with its source
named so a reader can verify it: the U.S.–Iran standoff and Hormuz shipping
attacks (Reuters, Washington Institute); the Abu Dhabi prisoner-swap deal and
Baltic drone alerts (Reuters); Gaza (Reuters); the Hegseth impeachment referral
and Trump's BBC suit (Reuters); hot U.S. inflation and the market fall (Reuters);
Congo's Ebola outbreak passing 11,000 cases (Reuters); COP31 and the rooftop-solar
pledge (Reuters, AP); and Nvidia's board investigation into Jensen Huang (BBC).
Every figure was checked against reporting published on 11 November 2026.

`main.py` validates the competition gate before writing (UTF-8, 1–2,000
characters, not only white space) and verifies the written bytes match
`summary.txt`, so the two grader runs always produce identical output.

Run: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
