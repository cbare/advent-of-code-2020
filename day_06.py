"""
Advent of Code 2020 - Day 6
"""
import re

def group_answers(grp):
    return set(re.sub('\s+', '', grp))

with open('puzzle-6-input.txt') as f:
    grps = [group_answers(grp) for grp in f.read().split('\n\n')]

sum(len(grp) for grp in grps)


def group_answers_intersect(grp):
    indvs = [set(indv) for indv in grp.split('\n')]
    return set.intersection(*indvs)


with open('puzzle-6-input.txt') as f:
    grps = [group_answers(grp) for grp in f.read().split('\n\n')]

sum(len(grp) for grp in grps)
