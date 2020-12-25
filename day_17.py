"""
Advent of Code 2020 - Day 17
"""
import numpy as np

input = """
##.#...#
#..##...
....#..#
....####
#.#....#
###.#.#.
.#.#.#..
.#.....#
"""

steps = 6

a = input.strip().split()

b = np.zeros(shape=(
    len(a) + 2 * steps,
    len(a[0]) + 2 * steps,
    1 + 2 * steps,
))

z = steps
for i in range(len(a)):
    for j in range(len(a[0])):
        x = i+steps
        y = j+steps
        b[x,y,z] = 1 if a[i][j]=='#' else 0


def update(b, x, y, z):
    s = sum(
        b[x + i, y + j, z + k]
        for i in (-1, 0, 1)
            for j in (-1, 0, 1)
                for k in (-1, 0, 1)
                    if not (i==0 and j==0 and k==0)
                        and (0 <= x+i < b.shape[0])
                        and (0 <= y+j < b.shape[1])
                        and (0 <= z+k < b.shape[2])
    )
    if b[x, y, z] == 0:
        return 1 if s == 3 else 0
    else:
        return 1 if s == 2 or s == 3 else 0

def step(b):
    xd, yd, zd = b.shape
    bn = np.zeros((xd,yd,zd))
    for x in range(xd):
        for y in range(yd):
            for z in range(zd):
                bn[x,y,z] = update(b, x, y, z)
    return bn

b0 = b
for i in range(steps):
    b = step(b)

# part 1
# In [106]: np.sum(b)
# Out[106]: 315.0


# part 2

test = """
.#.
..#
###
"""

a = input.strip().split()

b0 = np.zeros(shape=(
    len(a) + 2 * steps,
    len(a[0]) + 2 * steps,
    1 + 2 * steps,
    1 + 2 * steps,
))

z = steps
w = steps
for i in range(len(a)):
    for j in range(len(a[0])):
        x = i+steps
        y = j+steps
        b0[x,y,z,w] = 1 if a[i][j]=='#' else 0


def update_4d(b, x, y, z, w):
    s = sum(
        b[x + i, y + j, z + k, w + l]
        for i in (-1, 0, 1)
            for j in (-1, 0, 1)
                for k in (-1, 0, 1)
                    for l in (-1, 0, 1)
                        if not (i==0 and j==0 and k==0 and l==0)
                            and (0 <= x+i < b.shape[0])
                            and (0 <= y+j < b.shape[1])
                            and (0 <= z+k < b.shape[2])
                            and (0 <= w+l < b.shape[3])
    )
    if b[x, y, z, w] == 0:
        return 1 if s == 3 else 0
    else:
        return 1 if s == 2 or s == 3 else 0

def step_4d(b):
    xd, yd, zd, wd = b.shape
    bn = np.zeros((xd,yd,zd,wd))
    for x in range(xd):
        for y in range(yd):
            for z in range(zd):
                for w in range(wd):
                    bn[x,y,z,w] = update_4d(b, x, y, z, w)
    return bn

b = b0
for i in range(steps):
    b = step_4d(b)
