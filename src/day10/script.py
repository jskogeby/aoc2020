import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')

from utils import parse
data = parse.split_input("day10/input.txt", form=int) + [0]
data.sort()

def part1():
    jolt1 = 0
    jolt3 = 1 # Built-in adapter is rated for 3 jolts
    for i in range(1,len(data)):
        diff = data[i] - data[i-1]
        if diff == 1:
            jolt1 += 1
        elif diff == 3:
            jolt3 += 1
    print(jolt1*jolt3)

def paths(idx, dic):
    for i in range(idx+1, len(data)):
        if data[i] - data[idx] <= 3:
            dic[idx] += dic[i]
        else:
            break

def part2():
    dic = {i:0 for i in range(0, len(data))}
    dic[len(data)-1] = 1
    indices = reversed(range(0, len(data)))
    for i in indices:
        paths(i, dic)
    print(dic[0])

if __name__ == "__main__":
    part1()
    part2()
