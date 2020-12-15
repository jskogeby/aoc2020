import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
import itertools

from utils import parse
data = parse.split_input("day14/input.txt", form=str)
data = parse.split_lines(data, " = ", (str, str))

def part1():
    mask = ""
    mem = {}
    for d in data:
        if d[0] == "mask":
            mask = d[1]
        else:
            key = int(d[0][4:-1])
            val = int(d[1])
            bin_val = [s for s in bin(val)[2:]]
            bin_val = ["0"]*(36-len(bin_val)) + bin_val
            for pos in range(1, len(bin_val) + 1):
                if mask[-pos] != "X":
                    bin_val[-pos] = mask[-pos]
            bin_val = "".join(bin_val)
            mem[key] = int(bin_val, 2)

    s = sum(mem.values())
    print(s)

def addr_combinations(addr):
    n_x = addr.count("X")
    combinations = itertools.product(["0", "1"], repeat=n_x)
    combinations = map(list, combinations)
    addr_combinations = []
    for c in combinations:
        a = addr.copy()
        for i in range(len(a)):
            if a[i] == "X":
                a[i] = c.pop()
        addr_combinations.append(a)
    bin_addrs = ["".join(addr) for addr in addr_combinations]
    dec_addrs = [int(addr, 2) for addr in bin_addrs]
    return dec_addrs

def apply_mask(mask, val):
    bin_val = bin(int(val))[2:]
    val = ["0"]*(36-len(bin_val)) + list(bin_val)
    for i in range(len(val)):
        if mask[i] != "0":
            val[i] = mask[i]
    return val

def part2():
    mask = ""
    mem = {}
    for d in data:
        if d[0] == "mask":
            mask = d[1]
        else:
            key = d[0][4:-1]
            val = int(d[1])
            addr = apply_mask(mask, key)
            addrs = addr_combinations(addr)
            for a in addrs:
                mem[a] = val

    s = sum(mem.values())
    print(s)

if __name__ == "__main__":
    part1()
    part2()