import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
from copy import deepcopy

from utils.computer import Computer
from utils import parse
data = parse.split_input("day8/input.txt")
data = parse.split_lines(data, " ", (str, int))

def part1():
    cp = Computer(data)
    cp.execute()
    print(cp.acc)
    return cp.read_instructions

def part2():
    lines_read = part1()
    for line in lines_read:
        new_data = deepcopy(data)
        if new_data[line][0] == "acc":
            continue
        elif new_data[line][0] == "jmp":
            new_data[line][0] = "nop"
        elif new_data[line][0] == "nop":
            new_data[line][0] = "jmp"
        cp = Computer(new_data)
        result = cp.execute()
        if result:
            print(result)
            break

if __name__ == "__main__":
    part2()