import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    paired = zip(data, data[1:])
    res = sum(y > x for x, y in paired)
    return(res)

def part2(data):
    """
    Solve part 2, not useful for an arbitrary window size.
    
    """
    n = len(data)
    window_sums = [data[i] + data[i+1] + data[i+2] for i in range(n-2)]
    return(part1(window_sums))

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
