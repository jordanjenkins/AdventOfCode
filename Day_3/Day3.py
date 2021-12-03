import pathlib
import sys
from itertools import count, filterfalse

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n")]
    

def most_common(x):
    return max(x, key = x.count)


def part1(data):
    """
    Solve part 1.
    """
    lst_tup = [tuple(map(int, [char for char in x]))for x in data]

    bin_lst = [most_common(i) for i in zip(*lst_tup)]

    gamma = 0
    for ele in bin_lst:
        gamma = (gamma << 1) | ele
    
    eps = 0
    for ele in bin_lst:
        ele_inv = abs(1 - ele)
        eps = (eps << 1) | ele_inv

    power_consumption = gamma * eps
    return power_consumption

def part2(data):
    """
    Solve part 2.
    """
    inputs = data
    # O2 Generator Rating
    oxygen = 0
    for col in range(len(data)):
        lst_tup = list(zip(*inputs))
        zeros = lst_tup[col].count('0')
        ones = lst_tup[col].count('1')
        common = '0'
        if (ones >= zeros):
            common = '1'
        inputs = [num for num in inputs if num[col] == common]
        if len(inputs) == 1:
            oxygen = int(inputs[0],2)
            break
    # C02 Scrubber
    co2 = 0
    inputs = data
    for col in range(len(data)):
        lst_tup = list(zip(*inputs))
        zeros = lst_tup[col].count('0')
        ones = lst_tup[col].count('1')
        common = '0'
        if (ones < zeros):
            common = '1'
        inputs = [num for num in inputs if num[col] == common]
        if len(inputs) == 1:
            co2 = int(inputs[0],2)
            break
    
    return(oxygen * co2)

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
