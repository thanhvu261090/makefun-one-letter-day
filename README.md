[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/thanhvu261090/makefun-one-letter-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/thanhvu261090/makefun-one-letter-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

Entry for the [make.fun bounty "One Letter for Your Day"](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) — send exactly one letter, A to Z, standing for the word that describes your day. A judge picks the letter whose hidden word feels most vivid, funnier or more true.

## The entry

**S** — for **slog**.

A Monday spent slogging through one bounty after another: task after task,
no shortcut, boots in the mud. It is vivid (you can picture the trudge),
weary-funny (the kind of word you mutter at 5pm on a Monday), and true to
a real day of grinding a bounty campaign.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes exactly
one byte — the letter `S`, with no trailing newline — to `/output/entry.txt`,
then gate-checks its own output: the file must be exactly 1 byte and a
single A–Z letter.

```bash
python3 main.py
wc -c /output/entry.txt   # 1
```

## License

MIT — see [LICENSE](LICENSE).
