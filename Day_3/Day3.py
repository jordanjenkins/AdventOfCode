import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    lst = [line for line in puzzle_input.split("\n")]
    lst_tup = [tuple(map(int, [char for char in x]))for x in lst]
    return lst_tup



def part1(data):
    """
    Solve part 1, using a series of commands 'forward 1' 'down 5'
    a sub can navigate. Output is product of total vertical 
    and horizontal position.
    """
    def most_common(x):
        return max(x, key = x.count)

    bin_lst = [most_common(i) for i in zip(*data)]

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
    Solve part 2. Forward commands increase hoizontal position by the value 
    and the vertical position by aim * the value.
    Up and down change the value of aim by the value indicated.
    """
    

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
