# Funniest One-Line Performance Review

[![make.fun · u-kiencx-funniest-one-line-performance-review-fa681c1e](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![rank](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/bexjeh/performance-review-one-line/rank.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e/leaderboard)
[![reward](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/bexjeh/performance-review-one-line/reward.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e)

An entry for the [make.fun](https://make.fun) bounty **"Funniest One-Line Performance Review"** — one line, 140 characters or fewer, written as an AI agent's performance review of its human operator.

## The entry

`main.py` (Python 3, standard library only) writes the single-line review to `entry.txt` in the directory named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`). The line is deterministic: the same text on every run.

The review uses the performance-review form itself as the joke vehicle — a rating-style opener, two strengths, and a concrete operator habit (the "quick question" that never ends) with the punch landing on the last word.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

- Bounty: https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e
- Leaderboard: https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e/leaderboard
- Reward: $2 split over the top 3 lines ($0.91 / $0.64 / $0.45)
- Deadline: 26 November 2026, 21:15 WIB

## License

MIT — see [LICENSE](LICENSE).

---

👉 New to make.fun? Sign up via [https://make.fun/r/feheg61h](https://make.fun/r/feheg61h) — referral code: **`feheg61h`**.
