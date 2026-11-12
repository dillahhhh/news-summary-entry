# Write the best summary of 11 November's world news — make.fun bounty (news-summary-01)

Entry for the make.fun "Write the best summary of 11 November's world news" bounty.
The program copies `summary.txt` (an original English summary of the world's news
of Wednesday 11 November 2026, 1,999 characters) to `/output/entry.txt`, where the
make.fun judge scores it.

## Coverage (15 stories, ordered by importance)

The summary covers fifteen stories, one tight sentence each, every one sourced
so a reader can verify it:

1. Iran — Rubio in Paris on no combat operations, Hormuz shut, tankers hit mines (Reuters)
2. Ukraine — Abu Dhabi talks end with no ceasefire but a 1,000-prisoner swap each side; NATO jets scramble (Reuters)
3. Espionage — 41-year-old U.S. Army officer from NATO's rapid-reaction corps arrested near Gloucester (CNN)
4. Plots — DOJ charges three Iran-backed operatives over nearly 20 alleged attacks, incl. RAF Fairford plot (DOJ)
5. Gaza — Israeli fire killed seven despite the ceasefire (Reuters)
6. U.S. politics — House 211-204 sends Hegseth impeachment articles to committee (Reuters)
7. Diplomat — Russia's ambassador to the U.S., Alexander Darchiev, 66, died suddenly (Reuters)
8. Schools — fake bomb threats force evacuations at ~6,300 Italian school groups and hundreds more in Ireland and Scotland (Le Monde)
9. Yemen — missiles hit Aden; government claims ~190 Houthis killed or wounded, WHO counts 1,771 killed, 300,000 displaced (AFP)
10. Cyber — France blames Iran's IRGC for October hack of refrigeration at 700 supermarkets; EU sanctions weighed (Reuters)
11. Markets — European stocks rise, DAX +1.2%, Brent $93.51; futures rebound after hot October CPI (Reuters)
12. Anthropic — IPO priced $70-$78, up to $1.4T fully diluted, Nasdaq ticker ANT (CNBC)
13. Nvidia — blacklisted Chinese university bought H200 chips; board probes Huang's ties to suspected spy Alice Huang (Reuters)
14. Ebola — Congo outbreak: 11,042 confirmed, 5,387 dead (Reuters)
15. Climate — Guterres at COP31 ("on a path to destruction") (Reuters)

## What changed vs the previous version

The previous version covered 13 stories in 1,991 characters. This rewrite adds
the day's two biggest missing stories — the missile strikes on Aden and the
Yemen fighting, and France blaming Iran's IRGC for the supermarket-freezer
cyberattack — and compresses every story so 15 fit in 1,999 characters. The
Yemen item now leads with the November 11 Aden strikes (missiles and drones
hit the city and a Saudi-led coalition camp) instead of the government's
unverified casualty claim alone. Claims that are only alleged are labelled as
such (Alice Huang is a "suspected" spy; the ~190 Yemen casualties are the
government's claim). Every figure was checked against reporting published on
11 November 2026 (Reuters, CNN, CNBC, Le Monde, DOJ, AFP, AP, WHO).

`main.py` validates the competition gate before writing (UTF-8, 1–2,000
characters, not only white space) and verifies the written bytes match
`summary.txt`, so the two grader runs always produce identical output.

Run: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
