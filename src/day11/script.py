import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
from copy import deepcopy

from utils import parse
data = parse.split_input("day11/input.txt", form=str)
data = list(map(lambda row: [d for d in row], data))
# Pad data to avoid index out of bounds
for d in data:
    d.insert(0, ".")
    d.append(".")
data.insert(0, ["."]*len(data[0]))
data.append(["."]*len(data[0]))

def adjacents(x, y, seats):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and seats[x+i][y+j] == "#":
                count += 1
    return count

def in_sights(x, y, seats):
    count = 0
    axes = [[-1,-1], [-1,1], [1,1], [1,-1], [1,0], [-1,0], [0,1], [0,-1]]
    org_axes = deepcopy(axes)
    for axis in range(len(axes)):
        a = axes[axis]
        while x + a[0] in range(len(seats)) and y + a[1] in range(len(seats[0])) and seats[x + a[0]][y + a[1]] == ".":
            a[0] += org_axes[axis][0]
            a[1] += org_axes[axis][1]
        if x + a[0] in range(len(seats)) and y + a[1] in range(len(seats[0])) and seats[x + a[0]][y + a[1]] == "#":
            count += 1
    return count

def iterate(seats, count_fn, threshold):
    new_seats = deepcopy(seats)
    for x in range(1, len(new_seats) - 1):
        for y in range(1, len(new_seats[x]) - 1):
            count = count_fn(x, y, seats)
            if seats[x][y] == "L" and count == 0:
                new_seats[x][y] = "#"
            elif seats[x][y] == "#" and count >= threshold:
                new_seats[x][y] = "L"
    return new_seats

def seats_taken(count_fn, threshold):
    prev_it = deepcopy(data)
    next_it = iterate(prev_it, count_fn, threshold)
    while next_it != prev_it:
        prev_it = next_it
        next_it = iterate(next_it, count_fn, threshold)
    n_occ = parse.unpack(next_it).count("#")
    print(n_occ)

if __name__ == "__main__":
    seats_taken(adjacents, 4)
    seats_taken(in_sights, 5)
