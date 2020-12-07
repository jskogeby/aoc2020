import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')

from utils import parse
groups = parse.group(parse.split_input("day6/input.txt", "\n"))

def count_unpack(data):
    return len(set(parse.unpack(data)))

def part1():
    print(sum(map(count_unpack, groups)))

def part2():
    accum = 0
    for g in groups:
        size = len(g)
        flat = parse.unpack(g)
        occ = {question: flat.count(question) for question in set(flat)}
        accum += list(occ.values()).count(size)
    print(accum)

if __name__ == "__main__":
    part1()
    part2()