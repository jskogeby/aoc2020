import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')

from utils import parse
data = parse.inp("day5/input.txt", str)

def dac(lower, upper, seat):
    n = upper - lower
    if len(seat) == 0:
        return lower
    elif seat[0] == "F" or seat[0] == "L":
        return dac(lower, lower + int(n/2), seat[1:])
    elif seat[0] == "B" or seat[0] == "R":
        return dac(lower + int(n/2) + 1, upper, seat[1:])
    else:
        print("You probably fucked up")
        return

def my_seat(seat_ids, current):
    if current in seat_ids:
        return my_seat(seat_ids, current + 1)
    else:
        return current

if __name__ == "__main__":
    seats = {}
    for seat in data:
        row = dac(1, 128, seat[:7]) - 1
        col = dac(1, 8, seat[7:]) - 1
        seats[row * 8 + col] = (row, col)
    seat_ids = list(sorted(seats.keys()))
    my_seat = my_seat(seat_ids, seat_ids[0])
    print(seat_ids[-1])
    print(my_seat)
    
