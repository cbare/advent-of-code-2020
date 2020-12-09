"""
Advent of Code 2020 - Day 9
"""
with open('puzzle-09-input.txt') as f:
    nums = [int(line.strip()) for line in f]


def find_addends(nums, sum):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == sum:
                return nums[i], nums[j]
    return None


def find_invalid(nums, preamble_len=25):
    for k in range(preamble_len,len(nums)):
        if find_addends(nums[(k-preamble_len):k], nums[k]) is None:
            print(f'invalid: {nums[k]}')

find_invalid(nums)

def find_contiguous_sum(nums, x):
    for i in range(0,len(nums)-1):
        j = i + 1
        while sum(nums[i:j]) < x and j < len(nums):
            j += 1
        if sum(nums[i:j]) == x:
            return nums[i:j]
    return None

# part 2

addends = find_contiguous_sum(nums, 400480901)
min(addends) + max(addends)
# 67587168
