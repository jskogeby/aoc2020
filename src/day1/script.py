
def inp():
    with open("1/input.txt", "r") as file:
        return [int(r.strip()) for r in file.readlines()]

def part1():
    data = inp()
    for i in data:
        j = 2020 - i
        if j in data:
            print(f"{i} * {j} = {i*j}")
            return

def part2():
    data = inp()
    for a in data:
        temp = 2020 - a
        for b in data:
            c = temp - b
            if c in data:
                print(f"{a} * {b} * {c} = {a*b*c}")
                return

if __name__ == "__main__":
    part1()
    part2()