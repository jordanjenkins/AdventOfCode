import pathlib
import sys
from itertools import count, filterfalse

def parse(puzzle_input):
    """Parse input"""
    input_file = open(puzzle_input).read()
    numbers = [int(n) for n in input_file.splitlines()[0].split(',')]
    boards = [
        [[int(n) for n in l.split()] for l in b.splitlines()]
        for b in input_file.strip().split('\n\n')[1:]
    ]
    return numbers, boards
    

def part1(data):
    """
    Solve part 1.
    """
    numbers = data[0]
    boards = data[1]

    for number in numbers:
        for board in boards:
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == number:
                        board[i][j] = None
            for row in board:
                if all(x is None for x in row):
                    score = sum(i for r in board for i in r if i is not None)
                    return(score * number)
            for col in zip(*board):
                if all(x is None for x in col):
                    score = sum(i for r in board for i in r if i is not None)
                    return(score * number)

def part2(data):
    """
    Solve part 2.
    """
    numbers = data[0]
    boards = data[1]

    wins = []
    win = None

    for number in numbers:
        if sum(x not in wins for x in boards) == 1:
            win = next(i for i, x in enumerate(boards) if x not in wins)
        for thisboard, board in enumerate(boards):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == number:
                        board[i][j] = None
            for row in board:
                if all(x is None for x in row):
                    if thisboard == win:  
                        score = sum(i for r in board for i in r if i is not None)
                        return(score * number)
                    wins.append(board)
            for col in zip(*board):
                if all(x is None for x in col):
                    if thisboard == win:
                        score = sum(i for r in board for i in r if i is not None)
                        return(score * number)
                    wins.append(board)
                

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
