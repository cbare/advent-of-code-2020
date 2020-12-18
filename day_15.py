"""
Advent of Code 2020 - Day 15
"""

examples = [
    ([0,3,6], 436),
    ([1,3,2], 1),
    ([2,1,3], 10),
    ([1,2,3], 27),
    ([2,3,1], 78),
    ([3,2,1], 438),
    ([3,1,2], 1836),
]

def game(start, limit=2020):
    hist = {}
    i = 0
    for n in start[:-1]:
        hist[n] = i
        i += 1

    nn = start[-1]
    while i < limit:
        n = nn
        nn = (i-hist[n]) if n in hist else 0
        hist[n] = i
        i += 1
    
    return n

## Part 1

for start, expected_n in examples:
    n = game(start)
    result = '✅' if n==expected_n else '❌'
    print(f'{start.__repr__():25} {n:6} {expected_n:6} {result}')


n = game([2,0,1,9,5,19])

# In [755]: n
# Out[755]: 1009



## Part 2

examples = [
    ([0,3,6], 175594),
    ([1,3,2], 2578),
    ([2,1,3], 3544142),
    ([1,2,3], 261214),
    ([2,3,1], 6895259),
    ([3,2,1], 18),
    ([3,1,2], 362),
]

for start, expected_n in examples:
    n = game(start, limit=30000000)
    result = '✅' if n==expected_n else '❌'
    print(f'{start.__repr__():25} {n:9} {expected_n:9} {result}')

n = game([2,0,1,9,5,19], limit=30000000)

# In [759]: n
# Out[759]: 62714





