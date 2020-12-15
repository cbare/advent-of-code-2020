"""
Advent of Code 2020 - Day 13
"""

with open('puzzle-13-input.txt') as f:
    arrival = int(f.readline().strip())
    buses = [(None if b=='x' else int(b))  for b in f.readline().strip().split(',')]


def wait_time(arrival, b):
    return 0 if arrival % b == 0 else (b-(arrival % b))

ws = [(b, wait_time(arrival, b)) for b in buses if b]

rs = [(b, 0 if i==0 else b-(i%b)) for i,b in enumerate(buses) if b]

     147463492
s = 1336467960
for a in range(s, prod(d for d,r in rs)):
    n = 547*a+497
    if check_rs(n, rs):
        print('n=', n)

def check_rs(n, rs):
    for d,r in rs:
        if n % d != r:
            return False
    return True

def solve(rs):
    A,B = rs.pop()
    for a in range(1, A*prod(d for d,r in rs)):
        n = A*a+B
        if check_rs(n, rs):
            print('n=', n)
            return n

def solve_pair(A0,B0,A,B):
    for a in range(1, A0*A):
        n = A0*a + B0
        if n % A == B:
            return n
    raise RuntimeError('oops!')

def solve_iteratively(rs):
    rs_iter = iter(rs)
    A0,B0 = next(rs_iter)
    for A,B in rs_iter:
        n = solve_pair(A0,B0,A,B)
        print('n=',n)
        B0 = n
        A0 = A0 * A
    return n

# In [649]: solve_iteratively(rs)
# n= 209
# n= 317965
# n= 3994655
# n= 85249504
# n= 2173977093
# n= 1197695689218
# n= 41306652116537
# n= 327300950120029
# Out[649]: 327300950120029

# In [650]: check_rs(327300950120029, rs)
# Out[650]: True

# In [651]: rs
# Out[651]: 
# [(19, 0),
#  (37, 24),
#  (523, 504),
#  (13, 2),
#  (23, 4),
#  (29, 10),
#  (547, 497),
#  (41, 22),
#  (17, 1)]
