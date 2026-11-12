# Write the best summary of 11 November's world news — make.fun bounty (news-summary-01)

Entry for the make.fun "Write the best summary of 11 November's world news" bounty.
The program copies `summary.txt` (an original English summary of the world's news
of Wednesday 11 November 2026, 1,998 characters) to `/output/entry.txt`, where the
make.fun judge scores it.

## Round 6 (current, 2026-11-12)

15 stories, 1,998 characters, ordered by importance, one tight sentence each,
every one sourced:

1. Iran — Rubio: no new combat needed; Hormuz shut until U.S. conditions met; UKMTO tanker hit off Oman (Reuters)
2. Ukraine — Abu Dhabi talks end with no ceasefire, agreeing a prisoner swap of 1,000-1,500; NATO jets missed a drone over Lithuania (Reuters)
3. Yemen — Houthi missiles hit a coalition camp in Aden; 138 Houthis killed or wounded; U.N. 1,600+ killed, 300,000 displaced (AFP)
4. Sudan — UNICEF: drones caused two-thirds of child casualties; 15 power stations hit; envoy recalled, UAE blamed (AFP)
5. Gaza — Israeli fire killed seven, incl. Fadi Rajab and his son Abubakr, despite the ceasefire; 1,615 dead since the truce (Reuters)
6. Spying — U.S. Army officer of NATO's rapid-reaction corps arrested near Gloucester for suspected spying for Russia (CNN)
7. Plots — DOJ charges three Iran-backed operatives over nearly 20 alleged attacks, incl. RAF Fairford plot (DOJ)
8. U.S. — House 211-204 sends Massie's Hegseth impeachment articles to committee, effectively killing them (Reuters)
9. China — Wang Yi calls the Rubio call "positive and constructive" ahead of APEC; Xi–Trump meeting expected (Reuters)
10. Diplomat — Russia's ambassador Alexander Darchiev, 66, died in Moscow of a chronic illness; envoy since March 2025 (Reuters)
11. Cyber — France blames the IRGC's Shahid Kaveh unit for hacking fridges at 700 supermarkets; envoy summoned, EU sanctions sought (Reuters)
12. Markets — STOXX 600 hit 663.05, dollar a 19-month high after Fed's Waller floated a 50-point December hike (Reuters)
13. Anthropic — $70-$78 IPO price range, up to $1.4T fully diluted; ANT trading expected November 19 (CNBC)
14. Nvidia — blacklisted Chinese university bought H200s; board probes Huang's ties to suspected spy Alice Huang (Reuters)
15. Ebola — Congo outbreak: 11,042 cases, 5,387 deaths, second-largest on record; no vaccine for Bundibugyo (Reuters)

## What changed vs round 5

- Fixed Yemen figures: 138 Houthis killed/wounded per the army (not ~190),
  U.N. 1,600+ killed (not WHO 1,771) — the round 5 numbers matched no source.
- Fixed Anthropic wording: a $70-$78 price *range* (not "priced").
- Added Sudan (UNICEF drone toll on children, power-grid strikes, envoy
  recalled) and the Wang Yi–Rubio call ahead of APEC.
- Named the IRGC's Shahid Kaveh cyber unit; sharpened markets (STOXX record
  663.05, dollar 19-month high, Waller 50bp); added the NATO jets missing
  a drone over Lithuania and the exact prisoner-swap range (1,000-1,500,
  not a flat 1,000).
- Dropped the schools bomb-threat and COP31 quote lines for the two more
  consequential stories.
- Every figure was checked against reporting published on 11 November 2026
  (Reuters, AFP, CNN, CNBC, DOJ, WHO, UNICEF).

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
