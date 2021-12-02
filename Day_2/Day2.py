import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    lst = [line for line in puzzle_input.split("\n")]
    return lst



def part1(data):
    """
    Solve part 1, using a series of commands 'forward 1' 'down 5'
    a sub can navigate. Output is product of total vertical 
    and horizontal position.
    """

    horizDist = 0
    vertDist = 0

    for line in data:
        direction = line.split()[0]
        val = int(line.split()[1])

        if direction == 'forward':
            horizDist += val
        elif direction == 'up':
            vertDist -= val
        else:
            vertDist += val

    return(horizDist * vertDist)

def part2(data):
    """
    Solve part 2. Forward commands increase hoizontal position by the value 
    and the vertical position by aim * the value.
    Up and down change the value of aim by the value indicated.
    """
    aim = 0
    horizDist = 0
    vertDist = 0

    for line in data:
        direction = line.split()[0]
        val = int(line.split()[1])

        if direction == 'forward':
            horizDist += val
            vertDist += (aim * val)
        elif direction == 'up':
            aim -= val
        else:
            aim += val

    return(horizDist * vertDist)

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
