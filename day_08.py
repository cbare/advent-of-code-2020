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
            raise RuntimeError(f'Infinite loop: acc={acc}')
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
    return acc

def alter(code, i, new_instr):
    return [new_instr if i==j else line for j,line in enumerate(code)]

def try_altered_codes(code):
    for i, line in enumerate(code):
        op, arg = parse(line)
        if op in ['jmp', 'nop']:
            new_op = 'jmp' if op == 'nop' else 'nop'
            altered_code = alter(code, i, f'{new_op} {arg:+}')
            try:
                acc = interpret(altered_code)
                print(f'altered line {i}, program terminated: acc={acc}')
            except RuntimeError:
                print(f'altered line {i}, program looped')
