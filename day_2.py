"""
Advent of Code 2020 - Day 2
"""

from collections import namedtuple
import re

Rule = namedtuple('Rule', 'min max char')

def make_rule(txt):
    m = re.match(r'(\d+)\-(\d+) (.)', txt)
    if m:
        return Rule(int(m[1]), int(m[2]), m[3])
    else:
        raise RuntimeError(f"Can't read rule \"{txt}\"")

def make_rule_pw_pair(txt):
    a,b = txt.split(': ')
    return make_rule(a), b

def is_valid(rule, pw):
    return rule.min <= sum(c==rule.char for c in pw) <= rule.max

def is_valid_new(rule, pw):
    return (rule.min-1 < len(pw) and pw[rule.min-1]==rule.char) ^ \
           (rule.max-1 < len(pw) and pw[rule.max-1]==rule.char)

with open('puzzle-2-input.txt') as f:
    pws = [make_rule_pw_pair(line) for line in f]

sum(is_valid_new(rule, pw) for rule, pw in pws)
