import pathlib
import sys
from math import trunc

def parse(puzzle_input):
    """Parse input"""
    lst = [line for line in puzzle_input.split("\n")]
    return lst

open_list = ["[","{","(", "<"]
close_list = ["]","}",")", ">"]
penalty =  {')': 3, ']': 57, '}': 1197, '>': 25137}
first_illegal_char = []
total_error_score = 0

def check(myStr):
    stack = []
    for char in myStr:
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            pos = close_list.index(char)
            if((len(stack) > 0) and 
                (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                # print('ILLEGAL CHAR', char)
                return char
    if len(stack) == 0:
        return None
    else:
        return stack

def part1(data):
    """
    Solve part 1.
    """
    
    for line in data:
        chk = check(line)
        if chk != None:
            if len(chk) == 1:
                first_illegal_char.append(chk)

    return sum([penalty[x] for x in first_illegal_char])

    

def part2(data):
    """
    Solve part 2.
    """
    penalty_2 =  {'(': 1, '[': 2, '{': 3, '<': 4}
    penalty_score = []

    for line in data:
        tmp_score = 0
        chk = check(line)
        if type(chk) == list:
            chk.reverse()
            for char in chk:
                tmp_score *= 5
                tmp_score += penalty_2[char]
            penalty_score.append(tmp_score)
    middle = trunc(len(penalty_score)/2)
    penalty_score.sort()
    return penalty_score[middle]
        
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
