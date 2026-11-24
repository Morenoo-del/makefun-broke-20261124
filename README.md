# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/morenoo-del/makefun-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/morenoo-del/makefun-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
bounty on [make.fun](https://make.fun): one line of software error copy, at most
200 characters, that tells the user the brutal truth about what went wrong and
makes them laugh on the way.

## The line

> Your disk is full, so we saved your file nowhere. Free up some space — or keep typing into the void.

## Why this line

It names a specific, real failure instead of apologising in generalities: the
disk is full, so the save went nowhere. It tells the user exactly what to do
next (free up space), and the twist — keep typing into the void — is the image
a reader repeats out loud to a colleague. It is a single line a real team could
paste into an error dialog without embarrassment.

## How it works

`main.py` (Python 3.13, no dependencies) writes the line to `/output/entry.txt`,
validating first that it is a single non-empty line of at most 200 characters.

```sh
python3 main.py
cat /output/entry.txt
```
