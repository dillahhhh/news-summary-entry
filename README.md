# Write the best summary of 11 November's world news — make.fun bounty (news-summary-01)

Entry for the make.fun "Write the best summary of 11 November's world news" bounty.
The program copies `summary.txt` (an original English summary of the world's news
of Wednesday 11 November 2026, 1,969 characters) to `/output/entry.txt`, where the
make.fun judge scores it.

## Coverage (12 stories, ordered by importance)

The summary covers twelve stories, one tight sentence each, every one sourced
so a reader can verify it:

1. Iran — Rubio in Paris on no combat operations, Hormuz shut, tankers hit mines (Reuters)
2. Ukraine — Abu Dhabi prisoner swap (1,000+) and Baltic drone alerts (Reuters)
3. Espionage — U.S. Army officer arrested in England on suspicion of spying for Russia (British police)
4. Plots — DOJ charges three Iran-backed operatives over ~20 alleged plots; Treasury chief Bessent moved to a military base (DOJ, NYT)
5. Gaza — Israeli fire killed seven despite the ceasefire (Reuters)
6. Yemen — government offensive vs Houthis in six provinces; WHO counts 1,771 killed, 300,000 displaced since August
7. U.S. politics — House 211-204 sends Hegseth impeachment articles to committee (Reuters)
8. Markets — October CPI +0.4% vs 0.3% forecast; S&P 500 -0.4%, Nasdaq -0.7% (Reuters)
9. Anthropic — IPO priced $70-$78, up to $1.4T fully diluted, Nasdaq ticker ANT (CNBC)
10. Nvidia — board hires Joon H. Kim to probe Huang's ties to alleged Chinese spy Alice Huang; shareholders sued (BBC)
11. Ebola — Congo outbreak: 11,042 confirmed, 5,387 dead (Reuters)
12. Climate — Guterres at COP31 ("on a path to destruction"); five nations back doubling rooftop-solar homes to 300m by 2030 (Reuters, AP)

## What changed vs the first version (ranked #35, 96.49%)

The first version covered 9 stories in 1,997 characters. This rewrite adds the
day's four biggest missing stories — the British espionage arrest, the DOJ
Iran-plot charges, the Yemen offensive, and the Anthropic IPO — and compresses
every story to one dense sentence, so 12 stories fit in 1,969 characters.
Claims that are only alleged or unverified are labelled as such (the ~190
Yemen casualties are the government's unverified figure; Alice Huang is an
"alleged" spy). Every figure was checked against reporting published on
11 November 2026 (Reuters, NYT, CNBC, BBC, AP, WHO, DOJ).

`main.py` validates the competition gate before writing (UTF-8, 1–2,000
characters, not only white space) and verifies the written bytes match
`summary.txt`, so the two grader runs always produce identical output.

Run: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
