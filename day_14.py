"""
Advent of Code 2020 - Day 14
"""
import re

mask_re = r'mask\s+=\s+([10X]{36})'
mem_re = r'mem\[(\d+)\]\s+=\s+(\d+)'

def apply_mask(mask, a):
    b = f'{a:036b}'
    mb = ''.join(
        '0' if mi=='0' else '1' if mi=='1' else bi
        for mi, bi in zip(mask, b)
    )
    return int(mb, 2)

memory = {}
with open('puzzle-14-input.txt') as f:
    mask = None
    for line in f:
        m = re.match(mask_re, line)
        if m:
            mask = m[1]
            continue

        m = re.match(mem_re, line)
        if m:
            a = int(m[1])
            x = int(m[2])
            memory[a] = apply_mask(mask, x)
            continue

        raise RuntimeError(f'Syntax error: {line}')

sum(v for v in memory.values())


def apply_mask_v2(mask, a):
    b = f'{a:036b}'
    mb = ''.join(
        bi if mi=='0' else '1' if mi=='1' else 'X'
        for mi, bi in zip(mask, b)
    )
    count_xs = sum(mi=='X' for mi in mask)

    for i in range(2**count_xs):
        fstr = f'{{i:0{count_xs}b}}'
        xb = fstr.format(i=i)
        xbi = iter(xb)
        addr = int(
            ''.join(
                next(xbi) if mbi=='X' else mbi
                for mbi in mb
            ),
            2
        )
        yield addr



memory = {}
with open('puzzle-14-input.txt') as f:
    mask = None
    for line in f:
        m = re.match(mask_re, line)
        if m:
            mask = m[1]
            continue

        m = re.match(mem_re, line)
        if m:
            a = int(m[1])
            x = int(m[2])
            for ma in apply_mask_v2(mask, a):
                memory[ma] = x
            continue

        raise RuntimeError(f'Syntax error: {line}')
