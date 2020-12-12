import sys
sys.path.append('/Users/jskogeby/git/aoc2020/src')
import math

from utils import parse
data = parse.split_input("day12/input.txt", form=str)

class Ferry:

    def __init__(self, data, use_waypoint=False):
        self.actions = data
        self.use_waypoint = use_waypoint
        self.direction = 0
        self.x = 0
        self.y = 0
        self.wpx = 10
        self.wpy = 1
        self.operations = {
            "N": lambda units: self.add(units, "y"),
            "S": lambda units: self.add(-units, "y"),
            "E": lambda units: self.add(units, "x"),
            "W": lambda units: self.add(-units, "x"),
            "L": lambda units: self.add(units, "direction"),
            "R": lambda units: self.add(-units, "direction"),
            "F": lambda units: self.forward(
                units,
                round(math.cos(math.radians(self.direction))),
                round(math.sin(math.radians(self.direction)))
            )
        }
        self.wp_operations = {
            "N": lambda units: self.add(units, "wpy"),
            "S": lambda units: self.add(-units, "wpy"),
            "E": lambda units: self.add(units, "wpx"),
            "W": lambda units: self.add(-units, "wpx"),
            "L": lambda units: self.rotate(units),
            "R": lambda units: self.rotate(-units),
            "F": lambda units: self.forward(
                units,
                self.wpx,
                self.wpy
            )
        }

    def add(self, units, attr):
        prev = getattr(self, attr)
        setattr(self, attr, prev + units)

    def forward(self, units, x_factor, y_factor):
        self.x += units * x_factor
        self.y += units * y_factor

    def rotate(self, units):
        units = math.radians(units)
        old_wpx = self.wpx
        self.wpx = round(math.cos(units)) * old_wpx - round(math.sin(units)) * self.wpy
        self.wpy = round(math.sin(units)) * old_wpx + round(math.cos(units)) * self.wpy

    def go(self):
        ops = self.wp_operations if self.use_waypoint else self.operations
        for a in self.actions:
            action = a[0]
            units = int(a[1:])
            ops[action](units)
        return self

    def manhattan(self):
        return abs(self.x) + abs(self.y)

if __name__ == "__main__":
    part1 = Ferry(data).go().manhattan()
    print(part1)
    part2 = Ferry(data, use_waypoint=True).go().manhattan()
    print(part2)
