import pathlib
import sys
from collections import Counter

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split(",")]

class Fish:
    def __init__(self, timer):
        self.timer = timer
    
    def reproduce(self):
        self.timer = 6
        return Fish(9)

def beginSim(startingPop, fish_list):
    for fish in startingPop:
        fish_list.append(Fish(fish))

def runDay(fish_list):
    for fish in fish_list:
        if fish.timer != 0:
            fish.timer -= 1 
        else:
           fish_list.append(fish.reproduce())
            

def part1(data):
    """
    Solve part 1. I went Class-based anticipating Part 2 would deal with some
    population limiter. May re-work to use Counter like part 2
    """
    fish_list = []
    beginSim(data, fish_list)

    for i in range(80):
        runDay(fish_list)
        # print(i + 1, [x.timer for x in fish_list])
    
    return(len(fish_list))

def part2(data):
    """
    Solve part 2. Had to abandon Class-based approach
    """

    fish = Counter(data)

    for i in range(256):
        baby_fish = fish[0]
        for day in range(8):
            fish[day] = fish[day + 1]
        fish[8] = baby_fish
        fish[6] += baby_fish
    return sum(fish.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
