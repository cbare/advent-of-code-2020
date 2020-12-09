"""
Advent of Code 2020 - Day 8
"""
import re

with open('puzzle-08-input.txt') as f:
    code = [line.strip() for line in f]

def parse(line):
    m = re.match(r'(\w+) ([+-]\d+)', line)
    if not m:
        raise RuntimeError(f"Syntax Error: {line}")
    return m[1], int(m[2])

def interpret(code):
    seen = set()
    acc = 0
    i=0
    while i < len(code):
        op, arg = parse(code[i])
        if i in seen:
            return acc
        seen.add(i)
        if op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        elif op == 'nop':
            i += 1
        else:
            raise RuntimeError(f'Unknown op {op}')
