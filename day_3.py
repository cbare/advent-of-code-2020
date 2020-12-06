"""
Advent of Code 2020 - Day 3
"""

with open('puzzle-3-input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

count = 0
j = 0
for line in lines:
    count += (1 if line[j] == '#' else 0)
    j = (j + 3) % len(line)

print(count)

slopes = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2},
]

def count_trees(right, down):
    count = 0
    j = 0
    for i, line in enumerate(lines):
        if i % down == 0:
            count += (1 if line[j] == '#' else 0)
            j = (j + right) % len(line)
    return count

from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

prod(count_trees(**slope) for slope in slopes)
