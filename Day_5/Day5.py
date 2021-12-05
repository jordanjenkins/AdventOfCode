import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse input"""
    f = open(puzzle_input)
    return list(f.readlines())
    
def parse_points(line):
    match = re.search(r'(\d+),(\d+) -> (\d+),(\d+)', line)
    point_1 = (int(match.group(1)), int(match.group(2)))
    point_2 = (int(match.group(3)), int(match.group(4)))
    return [point_1, point_2]

class Matrix:
    def __init__(self):
        self.points = {}
    
    def add_point(self, point):
        count = self.points.get(point, 0)
        count += 1
        self.points[point] = count

    def get_point_count(self):
        return self.points.get(point, 0)
    
    def add_line(self, point_1, point_2):
        dx = None
        if point_2[0] > point_1[0]:
            dx = 1
        elif point_2[0] < point_1[0]:
            dx = -1
        else:
            dx = 0
        dy = None
        if point_2[1] > point_1[1]:
            dy = 1
        elif point_2[1] < point_1[1]:
            dy = -1
        else:
            dy = 0
        
        point = point_1
        self.add_point(point)

        while point != point_2:
            point = (point[0] + dx, point[1] + dy)
            self.add_point(point)
    
    def get_dangerous_counts(self):
        danger = [count for count in self.points.values() if count >= 2]
        return len(danger)



def part1(data):
    lines = [parse_points(line) for line in data]
    straight_lines = [
        line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]
    ]

    matrix = Matrix()
    for line in straight_lines:
        matrix.add_line(line[0], line[1])
    return matrix.get_dangerous_counts()



def part2(data):
    """
    Solve part 2.
    """
    lines = [parse_points(line) for line in data]

    matrix = Matrix()
    for line in lines:
        matrix.add_line(line[0], line[1])
    return matrix.get_dangerous_counts()

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path)
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
