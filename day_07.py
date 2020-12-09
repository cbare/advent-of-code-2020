"""
Advent of Code 2020 - Day 7
"""
import re

def read_bag(line):
    """
    example: vibrant salmon bags contain 1 vibrant gold bag, 2 wavy aqua bags, 1 dotted crimson bag.
    """
    m = re.match(r'(\w+ \w+) bags contain (.*)\.$', line)
    if not m:
        raise RuntimeError(f"Can't parse {line}")

    name = m[1]
    contents = {}
    items = re.split(r',\s*', m[2])
    for item in items:
        if item == 'no other bags':
            break
        cm = re.match(r'(\d+) (\w+ \w+) bags?', item)
        if not cm:
            raise RuntimeError(f"Can't parse {line}")
        contents[cm[2]] = int(cm[1])

    return name, contents


with open('puzzle-07-input.txt') as f:
    bags = {}
    for line in f:
        name, contents = read_bag(line)
        if name in bags:
            raise RuntimeError(f'Duplicate key {name}!')
        bags[name] = contents

## Part 1

q = ['shiny gold']
seen = set()
while q:
    name = q.pop(0)
    for container_name, contains in bags.items():
        if name in contains and container_name not in seen:
            q.append(container_name)
            seen.add(container_name)

print('len(seen) =',len(seen))

## Part 2

def count_contained(name):
    contains = bags[name]
    return sum(
            n + n * count_contained(name_contained)
            for name_contained, n in contains.items()
        )

count_contained('shiny gold')
