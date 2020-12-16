import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
import math

from utils import parse
data = parse.split_input("day16/input.txt", form=str)
fields, my_ticket, nearby_tickets = parse.group(data)
fields = parse.split_lines(fields, ": ", (str, str))
# Sorry for this cancerous one-liner
fields = {
    f: set(parse.unpack([
        list(range(int(r.split("-")[0]), int(r.split("-")[1])+1)) for r in ranges.split(" or ")
    ])) for f, ranges in fields}
my_ticket = [int(num) for num in my_ticket[1].split(",")]
nearby_tickets = parse.split_lines(nearby_tickets[1:], ",", (int,)*20)

def all_valid_values():
    return set(parse.unpack(fields.values()))

def discard_invalid_tickets(tickets):
    valid_values = all_valid_values()
    valid_tickets = list(filter(lambda ticket: all([n in valid_values for n in ticket]), tickets))
    return valid_tickets

def valid_fields_for_col(col, tickets):
    valid_fields = []
    ticket_values = [t[col] for t in tickets]
    for f, valid_values in fields.items():
        valids = [n in valid_values for n in ticket_values]
        if all(valids):
            valid_fields.append(f)
    return col, valid_fields

def part1():
    valid_vals = all_valid_values()
    acc = 0
    for tick in nearby_tickets:
        for num in tick:
            if not num in valid_vals:
                acc += num
    print(acc)

def part2():
    ticks = discard_invalid_tickets(nearby_tickets)
    all_valid_fields = []
    for i in range(0, 20):
        all_valid_fields.append(valid_fields_for_col(i, ticks))
    all_valid_fields.sort(key=lambda x: len(x[1]))
    final_fields = []
    for col, valid_fields in all_valid_fields:
        if len(valid_fields) == 1:
            val = valid_fields[0]
            final_fields.append((val, col))
            for vf in all_valid_fields:
                if val in vf[1]:
                    vf[1].remove(val)
    final_fields = filter(lambda x: "departure" in x[0], final_fields)
    product = math.prod([my_ticket[field[1]] for field in final_fields])
    print(product)

if __name__ == "__main__":
    part1()
    part2()