import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
import re

from utils import parse

data = parse.group(parse.inp("day7/input.txt", str))[0]

def bagify(string):
    spl = string.split(" bags contain ")
    bag = spl[0]
    if "no other bags" in string:
        return (bag, None)
    content = spl[1].split(", ")
    content_dict = { re.sub(r" bags.| bag.| bags| bag", "", c[2:]) : int(c[0]) for c in content}
    return (bag, content_dict)

def contain_gold(bags, bag):
    content = bags[bag]
    if not content:
        return False
    if "shiny gold" in content:
        return True
    for c in content.keys():
        if contain_gold(bags, c):
            return True
    return False

def total_bags(bags, bag):
    content = bags[bag]
    if not content:
        return 1
    num_bags = sum([content[c] * total_bags(bags, c) for c in content.keys()])
    return num_bags + 1

bags = dict(map(bagify, data))

def part1():
    golds = 0
    for k in bags.keys():
        if contain_gold(bags, k):
            golds += 1
    print(golds)

def part2():
    tot = total_bags(bags, "shiny gold") - 1 
    print(tot)

if __name__ == "__main__":
    part1()
    part2()
