import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
import math

from utils import parse
data = parse.split_input("day13/input.txt", form=str)
earliest_departure = int(data[0])
busses = data[1].split(",")
deps = []
for offset, frequency in enumerate(busses):
    if frequency != "x":
        deps.append((offset,int(frequency)))

part1 = [[departure, -earliest_departure % departure] for _, departure in deps]
part1 = sorted(part1, key=lambda x: x[1])
part1 = math.prod(part1[0])
print(part1)

increment = deps[0][1]
t = 0
for i in range(len(deps) - 1):
    while bool((t + deps[i+1][0]) % deps[i+1][1]):
        t += increment
    increment = math.prod([deps[b][1] for b in range(i+2)])
print(t)