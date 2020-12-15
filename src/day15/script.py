import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')

from utils import parse
data = [0,6,1,7,2,19,20]

def run(n_iterations):
    ages = {num: {0: 0, 1: age+1} for age, num in enumerate(data)}
    prev = data[-1]
    for i in range(len(data) + 1, n_iterations + 1):
        prev = ages[prev][1] - ages[prev][0] if ages[prev][0] else 0
        if prev in ages:
            ages[prev][0] = ages[prev][1]
            ages[prev][1] = i
        else:
            ages[prev] = [0, i]
    print(prev)

if __name__ == "__main__":
    run(2020)
    run(30000000)
