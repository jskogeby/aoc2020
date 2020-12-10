import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')


from utils import parse
data = parse.split_input("day9/input.txt", form=int)
preamble = 25

def check_sum(l):
    sums = []
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            sums.append(l[i]+l[j])
    return l[-1] in set(sums)

def part1():
    for i, num in enumerate(data[preamble:]):
        if not check_sum(data[i:i+preamble+1]):
            print(num)
            return num
        
if __name__ == "__main__":
    invalid_num = part1()
    for i in range(2, len(data)-preamble):
        for j in range(0,len(data)-i):
            l = data[j:j+i]
            if sum(l) == invalid_num:
                l.sort()
                print(l[0] + l[-1])