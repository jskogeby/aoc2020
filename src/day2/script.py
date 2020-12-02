import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')

from utils import parse
data = parse.inp("day2/input.txt", format=str)

def unpack(line):
    count_range, letter, pw = (line.split(" "))
    count_range = count_range.split("-")
    lower, upper = int(count_range[0]), int(count_range[1])
    letter = letter[0]
    return lower, upper, letter, pw

def part1():
    valids = 0
    for d in data:
        lower, upper, letter, pw = unpack(d)
        if pw.count(letter) in range(lower, upper+1):
            valids += 1
    print(valids)

def part2():
    valids = 0
    for d in data:
        lower, upper, letter, pw = unpack(d)
        first = pw[lower-1] if len(pw) >= lower else None
        second = pw[upper-1] if len(pw) >= upper else None
        if (first == letter) != (second == letter):
            valids += 1
    print(valids)

if __name__ == "__main__":
    part1()
    part2()