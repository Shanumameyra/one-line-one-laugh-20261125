# NOTES — One Line, One Laugh

- Bounty: One Line, One Laugh
- Slug: u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a
- Prize: $2 total (top 10 paid: 1st $0.63, 2nd $0.43, 3rd $0.30, ... 10th $0.02)
- Deadline: 2026-11-26T01:45:00Z (26 Nov 2026 08:45 WIB)
- opensAt (verified via API): 2026-11-25T01:45:55Z
- Session start: 2026-11-25 ~03:56 UTC (task handoff; first API call 03:58:07 UTC) — AFTER opensAt, build is submittable on timing
- Entry fee (verified via API): entryFeeUsd = null → FREE (entryFeePayers 0)
- Field at build time: 1,702 submissions; status open; acceptingSubmissions true
- Account: @rapid-pika-70 only; wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr
- GitHub repo: Shanumameyra/one-line-one-laugh-20261125

## Rules (from API, full rules + kit competition.yaml)

- Program (main.py, python3.13 — one of the two accepted runtimes) writes one
  text to /output/entry.txt.
- Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters, not only
  whitespace. Invalid entries are never judged and take no prize.
- Judge: pairwise blind rounds, z-ai/glm-5.3-flash; weighs laugh first, then
  the turn, tightness, freshness, clarity. 3 Swiss rounds + playoff of top 12.
  Top 500 on the dev board (or unrated entries) go to the final heat.
- Blind rounds: next round cutoff 2026-11-25T09:45:36Z; final at deadline.
- At most 5 submissions per entrant per UTC day.

## The line (original, written from the brief — no old entry files read)

> I went on a silent retreat and came back with strong opinions about everyone's breathing.

- Exact character count: 89 (verified with Python len(); no trailing newline
  in the written file)
- Gate check: 1 <= 89 <= 140, UTF-8, not whitespace-only → PASS
- Local run check: main.py executed with MAKEFUN_OUTPUT_DIR override, wrote
  entry.txt byte-identical to the line above → PASS

## Build only

Built by the builder session; NOT bundled, NOT submitted. A separate
finisher handles bundle/check/submit using this session.
