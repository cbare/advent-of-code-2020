"""
Advent of Code 2020 - Day 16
"""
with open('puzzle-16-input.txt') as f:
    rules = {}
    for line in f:
        line = line.strip()
        if line == '':
            break
        field, valid_ranges = line.split(': ')
        rules[field] = valid_ranges

    your_ticket_label = next(f)
    assert your_ticket_label.strip() == 'your ticket:'

    your_ticket = next(f)

    blank = next(f)
    nearby_tickets_label = next(f)
    assert nearby_tickets_label.strip() == 'nearby tickets:'

    values = []
    for line in f:
        line = line.strip()
        values.append([int(val) for val in line.split(',')])


valid_values = set()
for field, rule in rules.items():
    for r in rule.split(' or '):
        s,e = r.split('-')
        s = int(s)
        e = int(e)
        for i in range(s, (e+1)):
            valid_values.add(i)

# part 1
sum(v for ticket in values for v in ticket if v not in valid_values)

# part 2

valid_tickets = [ticket for ticket in values
    if all(v in valid_values for v in ticket)]

rule_ranges = {}
for field, rule in rules.items():
    rule_ranges[field] = []
    for r in rule.split(' or '):
        s,e = r.split('-')
        s = int(s)
        e = int(e)
        rule_ranges[field].append((s,e))

n_fields = len(rules)

compat = {field:[True]*n_fields for field in rules.keys()}
for ticket in valid_tickets:
    for i, value in enumerate(ticket):
        for field, r in rule_ranges.items():
            compat[field][i] = compat[field][i] and any(s <= value <= e for s,e in r)

for k,v in compat.items():
    print(k, sum(v))

keys = sorted(compat.keys(), key=lambda k: sum(compat[k]))

used = [False]*n_fields
cols = {}
for key in keys:
    x = [a and not b for a,b in zip(compat[key], used)]
    assert sum(x) == 1
    i = x.index(True)
    used[i] = True
    cols[key] = i

your_ticket = [int(x) for x in your_ticket.strip().split(',')]

prod(your_ticket[cols[key]] for key in keys if key.startswith('departure'))
# Out[50]: 809376774329

