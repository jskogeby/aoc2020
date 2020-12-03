import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')

from utils import parse
data = parse.inp("day3/input.txt", str)

def traverse(step_x, step_y, x=0, y=0, accum=0):
    new_x, new_y = x + step_x, y + step_y
    if new_y >= len(data):
        return accum
    dest = data[new_y][(new_x) % len(data[0])]
    new_accum = accum + 1 if dest == "#" else accum
    return traverse(step_x, step_y, x=new_x, y=new_y, accum=new_accum)

def part1():
    print(traverse(3, 1))

def part2():
    product = traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)
    print(product)

if __name__ == "__main__":
    part1()
    part2()