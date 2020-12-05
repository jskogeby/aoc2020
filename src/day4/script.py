import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
import re

from utils import parse
data = parse.inp("day4/input.txt", str)
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = []
pp = {}
for line in data:
    if line == "":
        passports.append(pp)
        pp = {}
    else:
        vals = list(map(lambda x: x.split(":"), line.split(" ")))
        pp.update(dict(vals))
passports.append(pp)

def validate(pp):
    pairs = pp.items()
    for p in pairs:
        k, v = p
        if k == "byr":
            if len(v) != 4:
                return False
            age = int(v)
            if age < 1920 or age > 2002:
                return False
        elif k == "iyr":
            if len(v) != 4:
                return False
            issue_year = int(v)
            if issue_year < 2010 or issue_year > 2020:
                return False
        elif k == "eyr":
            if len(v) != 4:
                return False
            exp_year = int(v)
            if exp_year < 2020 or exp_year > 2030:
                return False
        elif k == "hgt":
            h = int(v[:-2])
            unit = v[-2:]
            if unit == "in":
                if h < 59 or h > 76:
                    return False
            elif unit == "cm":
                if h < 150 or h > 193:
                    return False
            else:
                return False
        elif k == "hcl":
            if v[0] != "#" or not re.match("[a-f0-9]{6}", v[1:]):
                return False
        elif k == "ecl":
            colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if v not in colors:
                return False
        elif k == "pid":
            if not v.isnumeric() or len(v) != 9:
                return False
    return True


if __name__ == "__main__":
    valid_passports = list(filter(lambda x: all((key in x.keys() for key in fields)), passports))
    print(len(valid_passports))

    valid_passports = list(filter(lambda x: validate(x), valid_passports))
    print(len(valid_passports))
