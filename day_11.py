"""
Advent of Code 2020 - Day 11
"""

ex = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


seats = [
    list(line)
    for line in ex.split()
]

with open('puzzle-11-input.txt') as f:
    seats = [
        list(line.strip())
        for line in f
    ]

n = len(seats)
m = len(seats[0])


def make_adj_lists(n, m):
    return [
        [
            [
                (i+ia, j+ja)
                for ia in [-1, 0, 1]
                    for ja in [-1, 0, 1]
                        if not(ia==0 and ja==0) and i+ia>=0 and i+ia<n and j+ja>=0 and j+ja<m
            ]
            for j in range(m)
        ]
        for i in range(n)
    ]


def adjacent_occupied(seats, adj, i, j):
    return sum(seats[ia][ja]=='#' for ia, ja in adj[i][j])


def apply_rules(seats, adj, n, m):
    nxt_seats = [[' ' for j in range(m)] for i in range(n)]
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            ao = adjacent_occupied(seats, adj, i, j)
            if seat=='L' and ao==0:
                nxt_seats[i][j] = '#'
            elif seat=='#' and ao >= 4:
                nxt_seats[i][j] = 'L'
            else:
                nxt_seats[i][j] = seat
    return nxt_seats


def print_seats(seats):
    for row in seats:
        print(''.join(row))
    print()


# Part 1

adj = make_adj_lists(n, m)

print_seats(seats)
prev_seats = None
while seats != prev_seats:
    nxt_seats = apply_rules(seats, adj, n, m)
    prev_seats = seats
    seats = nxt_seats
    print('.')

def count_occupied(seats):
    count = 0
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat=='#':
                count += 1
    return count

count_occupied(seats)
# 2438

# Part 2

directions = [
    (-1,-1),
    (-1, 0),
    (-1, 1),
    ( 0,-1),
    ( 0, 1),
    ( 1,-1),
    ( 1, 0),
    ( 1, 1),
]

def visible_occupied(seats, i, j, n, m):
    count = 0
    for id,jd in directions:
        ia = i+id
        ja = j+jd
        while ia>=0 and ia<n and ja>=0 and ja<m:
            if seats[ia][ja]=='#':
                count += 1
                break
            if seats[ia][ja]=='L':
                break
            ia += id
            ja += jd
    return count


def apply_new_rules(seats, adj, n, m):
    nxt_seats = [[' ' for j in range(m)] for i in range(n)]
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            vo = visible_occupied(seats, i, j, n, m)
            if seat=='L' and vo==0:
                nxt_seats[i][j] = '#'
            elif seat=='#' and vo >= 5:
                nxt_seats[i][j] = 'L'
            else:
                nxt_seats[i][j] = seat
    return nxt_seats



with open('puzzle-11-input.txt') as f:
    seats = [
        list(line.strip())
        for line in f
    ]

n = len(seats)
m = len(seats[0])

print_seats(seats)
prev_seats = None
while seats != prev_seats:
    nxt_seats = apply_new_rules(seats, adj, n, m)
    prev_seats = seats
    seats = nxt_seats
    print('.')

count_occupied(seats)
# 2174
