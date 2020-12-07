"""
Advent of Code 2020 - Day 4
"""

with open('puzzle-5-input.txt') as f:
    bps = [l.strip() for l in f]


tr = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1',
}

def to_id(txt):
    return int(''.join(tr[c] for c in txt), 2)

assert to_id('FBFBBFFRLR') == 357
assert to_id('BFFFBBFRRR') == 567
assert to_id('FFFBBBFRRR') == 119
assert to_id('BBFFBBFRLL') == 820

## Part 1
max(to_id(bp) for bp in bps)

## Part 2
for i,sid in enumerate(sids[0:-1]):
    if sids[i+1] == sid+2:
        print(sid+1)
