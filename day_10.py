"""
Advent of Code 2020 - Day 10
"""
from collections import Counter

with open('puzzle-10-input.txt') as f:
    nums = [int(line.strip()) for line in f]

nums.append(0)
nums.append(max(nums) + 3)

nums = sorted(nums)


# Part 1

diffs = Counter(a-b for a,b in zip(nums[1:], nums[0:-1]))
diffs[1] * diffs[3]


# Part 2

# |-|-|        -> |--| or |-|-|
# |-|-|-|      -> |--|-| or |-|--| or |---| or |-|-|-|
# |-|-|-|-|    -> |--|-|-| or |-|--|-| or |-|-|--| or
#                 |---|-| or |-|---| or |--|--| or |-|-|-|-|

# figure how many ways to set i bits with having 3 contiguous zeros
lookup= Counter()
for i in range(1,9):
    for j in range(2**i):
        fmt = f"{{j:0{i}b}}"
        binary_string = fmt.format(j=j)
        if '000' not in binary_string:
            print(binary_string)
            lookup[i] += 1

diffs = [a-b for a,b in zip(nums[1:], nums[0:-1])]

runs = []
rs = -1
for i, d in enumerate(diffs):
    if d==1:
        if rs==-1:
            rs=i
    else:
        if rs>-1 and (i-rs) > 1:
            runs.append( (rs,i) )
        rs = -1


from functools import reduce
from operator import mul
def prod(xs):
    return reduce(mul, xs, 1)

prod([lookup[b-a-1] for a,b in runs])
# 3022415986688
