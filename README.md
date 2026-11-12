# Write the best summary of 11 November's world news — make.fun bounty (news-summary-01)

Entry for the make.fun "Write the best summary of 11 November's world news" bounty.
The program copies `summary.txt` (an original English summary of the world's news
of Wednesday 11 November 2026, 1,979 characters) to `/output/entry.txt`, where the
make.fun judge scores it.

## Round 8 (current, 2026-11-12)

15 stories, 1,979 characters, ordered by importance, one tight sentence each,
every one sourced:

1. Iran — Rubio: no combat needed; Hormuz shut until the U.S. answers Iran's seven conditions (Reuters)
2. Ukraine — Abu Dhabi talks end with no ceasefire, but a prisoner swap of 1,000-1,500; NATO jets missed a drone over Lithuania (Reuters)
3. Yemen — Houthi missiles hit a coalition camp in Aden; 138 Houthis killed or wounded; U.N. 1,600+ killed, 300,000 displaced (AFP)
4. Sudan — UNICEF: drones caused 2/3 of child casualties; 15 power stations hit; envoy recalled, UAE blamed (AFP)
5. Gaza — Israeli fire killed seven, incl. Fadi Rajab and his son, despite the ceasefire; 1,615 dead since the truce (Reuters)
6. Mississippi — Scott Colom beat Cindy Hyde-Smith, first Black senator from the state since Reconstruction and first Democrat since 1982; Democrats reach 55 seats (AP)
7. Hegseth — House voted 211-204 to send 8 articles impeaching Pete Hegseth to committee, ending the effort; Massie the only Republican dissenter (NPR)
8. Ebola — Congo's Ebola outbreak hit 11,042 cases, 5,387 dead — its deadliest ever, second-largest on record (AP)
9. Spying — 41-year-old U.S. Army officer of NATO's rapid-reaction corps arrested for suspected spying for Russia (CNN)
10. Plots — DOJ charges three Iran-backed operatives over ~20 alleged attacks, incl. RAF Fairford plot (DOJ)
11. El Salvador — Bukele says Salvadoran troops destroyed the 400 Mawozo gang's Haiti HQ; ~20 reported killed, unconfirmed (BBC)
12. Cyber — France blames the IRGC's Shahid Kaveh unit for hacking fridges at 700 supermarkets; EU sanctions sought (Reuters)
13. Markets — STOXX 600 hit 663.05, dollar a 19-month high after hot October CPI lifted hike bets; Waller floated 50 points (Reuters)
14. Anthropic — $70-$78 IPO price range, up to $1.4T diluted; ANT trading expected November 19 (CNBC)
15. Nvidia — board weighed ousting CEO Jensen Huang over his affair with alleged Chinese spy Alice Huang; shares fell 8% (Reuters)

## What changed vs round 7

- Added the two big stories round 7 missed: Ebola (Congo, 11,042 cases,
  5,387 dead — deadliest in Congo, second-largest on record, AP Nov 11)
  and Hegseth (House 211-204 sent 8 impeachment articles to committee,
  Massie the sole Republican dissenter, NPR) — both in the house's own
  source list for the day.
- Dropped the two least consequential lines: China (routine Wang Yi-Rubio
  call) and COP31 (Guterres quote, no decision).
- Sharpened Markets with the hot October CPI driver (+0.4% vs 0.3%
  expected; S&P +1.3% Wednesday).
- Still 11 November 2026 only: the judge's criterion 1 requires that day,
  and a 12 November summary would lose to any 11 November one.
- Every figure was checked against reporting published on 11 November 2026
  (Reuters, AFP, AP, BBC, CNN, CNBC, DOJ, UNICEF, NPR).

## Round 7 (superseded)

15 stories, 1,998 characters. Submission 01a1d009, claim
AF-J419N-ASM8F-C3R76-AKCP4. Finished, valid, prize-eligible; judge score
95.58%, rank #462 — below the ~97.06% top-20 cutoff.

## Round 6 (superseded)

15 stories, 1,998 characters. Submission 01a1cf43, claim
AF-XJ9D3-7YA45-3K845-DK3FW. Finished, valid, prize-eligible; judge score
95.68%, rank #399 — below the ~97.06% top-20 cutoff.

## Round 5 (superseded)

15 stories, 1,999 characters. Submission 01a1cef6, claim
AF-DZ680-3NTTP-6ZGDB-F1WKP. Finished, valid, prize-eligible; judge score
never appeared (dev heat unjudged after 1+ hour).

## Round 4 (superseded)

13 stories, 1,991 characters. Submission 01a1ceea, claim
AF-E9CX3-0B919-8NKAX-JM55J. Proven valid on the server (all checks passed,
reproduces 54%) but superseded before a dev score.

`main.py` validates the competition gate before writing (UTF-8, 1–2,000
characters, not only white space) and verifies the written bytes match
`summary.txt`, so the two grader runs always produce identical output.

Run: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
