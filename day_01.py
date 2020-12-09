"""
Advent of Code 2020 - Day 1
"""

with open('puzzle-01-input.txt') as f:
    xs = [int(a) for a in f]

for i,x in enumerate(xs):
    for y in xs[(i+1):]:
        if x + y == 2020:
            print(f'{x} + {y} == {x+y}')
            print(f'{x} * {y} == {x*y}')

# 1825 + 195 == 2020
# 1825 * 195 == 355875

for i,x in enumerate(xs):
    for j, y in enumerate(xs[(i+1):]:
        for y in xs[(i+1):]:
        if x + y == 2020:
            print(f'{x} + {y} == {x+y}')
            print(f'{x} * {y} == {x*y}')

for i in range(len(xs)):
    for j in range((i+1), len(xs)):
        for k in range((j+1), len(xs)):
            x, y, z = xs[i], xs[j], xs[k]
            if x + y + z == 2020:
                print(f'{x} + {y} + {z} == {x+y+z}')
                print(f'{x} * {y} * {z} == {x*y*z}')

# 346 + 1380 + 294 == 2020
# 346 * 1380 * 294 == 140379120
