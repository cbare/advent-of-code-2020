"""
Advent of Code 2020 - Day 4
"""
import re

def to_dict(txt):
    return {
        k:v for k,v in 
        [pair.split(':') for pair in re.split(r'\s+', txt.strip())]
    }

with open('puzzle-4-input.txt') as f:
    pps = [to_dict(pp) for pp in f.read().split('\n\n')]

fields = {
    'byr': True,
    'iyr': True,
    'eyr': True,
    'hgt': True,
    'hcl': True,
    'ecl': True,
    'pid': True,
    'cid': False,
}

def validate(pp, fields):
    for field, required in fields.items():
        if required and field not in pp:
            return False
    return True

count = sum(validate(pp, fields) for pp in pps)


#--- Part 2 -----


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def validate_byr(txt):
    try:
        return 1920 <= int(txt) <= 2002
    except:
        return False

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def validate_iyr(txt):
    try:
        return 2010 <= int(txt) <= 2020
    except:
        return False

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def validate_eyr(txt):
    try:
        return 2020 <= int(txt) <= 2030
    except:
        return False

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
def validate_hgt(txt):
    m = re.match(r'(\d+)(in|cm)$', txt)
    if m:
        if m[2] == 'cm':
            return 150 <= int(m[1]) <= 193
        elif m[2] == 'in':
            return 59 <= int(m[1]) <= 76
        else:
            raise RuntimeError(f'WTF? "{txt}"')
    return False

#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def validate_hcl(txt):
    m = re.match(r'#[0-9a-f]{6}$', txt)
    return True if m else False


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def validate_ecl(txt):
    m = re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$', txt)
    return True if m else False

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def validate_pid(txt):
    m = re.match(r'\d{9}$', txt)
    return True if m else False

fields = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
    'cid': False,
}

def validate(pp, fields):
    for field, valid in fields.items():
        if valid is False:
            continue
        if field not in pp:
            return False
        if not valid(pp[field]):
            return False
    return True

count = sum(validate(pp, fields) for pp in pps)
