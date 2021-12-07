import pathlib
import sys
from statistics import median, mean

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split(",")]
            


def part1(data):
    """
    Solve part 1.
    """
    h_pos = int(median(data))
    f_cost = sum([abs(x - h_pos) for x in data])
    return f_cost
    
def part2(data):
    """
    Solve part 2.
    """
    h_pos = int(mean(data))
    ind_diff_0 = [abs(x - h_pos) for x in data]
    ind_diff_1 = [abs(x - h_pos + 1) for x in data]
    ind_diff_2 = [abs(x - h_pos - 1) for x in data]

    diff_cands = [ind_diff_0, ind_diff_1, ind_diff_2]
    f_cost = []
    for cand in diff_cands:
        cost = [sum(x for x in range(1, diff + 1)) for diff in cand]
        f_cost.append(sum(cost))

    return min(f_cost)


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
