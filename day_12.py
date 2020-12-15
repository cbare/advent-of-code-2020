"""
Advent of Code 2020 - Day 12
"""
from collections import namedtuple
from math import sin, cos, pi, atan2, sqrt
import re

Move = namedtuple("Move", "direction distance")

def parse_move(txt):
    m = re.match(r'(\w)(\d+)', txt)
    if m:
        return Move(m[1], int(m[2]))

with open('puzzle-12-input.txt') as f:
    moves = [parse_move(line) for line in f]


TEST = [
    parse_move(a) for a in 
    """F10
    N3
    F7
    R90
    F11""".split()
]

def do_moves(moves):
    x, y = 0, 0
    d = 0

    for move in moves:
        if move.direction == "N":
            y += move.distance
        elif move.direction == "E":
            x += move.distance
        elif move.direction == "S":
            y -= move.distance
        elif move.direction == "W":
            x -= move.distance
        elif move.direction == "F":
            y = int(round( y + move.distance * sin(d/180*pi) ))
            x = int(round( x + move.distance * cos(d/180*pi) ))
        elif move.direction == "R":
            d = (d-move.distance) % 360
        elif move.direction == "L":
            d = (d+move.distance) % 360

    print(x,y,d)

    return x,y,d


def rotate(x, y, degrees):
    radians = (degrees % 360)/180*pi
    angle0 = atan2(y, x)
    angle1 = (angle0 + radians)
    r = sqrt(x**2 + y**2)
    return r*cos(angle1), r*sin(angle1)


def move_waypoint(moves):
    wx, wy = 10, 1
    sx, sy = 0, 0

    for move in moves:
        if move.direction == "N":
            wy += move.distance
        elif move.direction == "E":
            wx += move.distance
        elif move.direction == "S":
            wy -= move.distance
        elif move.direction == "W":
            wx -= move.distance
        elif move.direction == "F":
            sx += wx*move.distance
            sy += wy*move.distance
        elif move.direction == "R":
            wx, wy = rotate(wx, wy, -move.distance)
        elif move.direction == "L":
            wx, wy = rotate(wx, wy, move.distance)

    print(sx,sy)
    return sx,sy


def manhattan_dist(x,y):
    return abs(x) + abs(y)
