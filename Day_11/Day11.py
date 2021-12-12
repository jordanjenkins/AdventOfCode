import pathlib
import sys
import numpy as np
from scipy import signal


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input) as f:
        data = f.read().strip().splitlines()
    res = np.zeros((len(data), len(data[0])), dtype = int)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            res[i,j] = int(char)
    return res

def flashes(energy):
    new_energy = energy
    flash_count = 0
    convolve_mat = np.ones((3,3))
    iteration = 0

    while True:
        iteration += 1
        energy += 1
        flash = energy > 9
        have_new_flash = True
        
        while have_new_flash:
            neighbor_flash = (signal.convolve(flash, convolve_mat, mode = 'same')
                            .round(0).astype(int))
            new_energy = energy + neighbor_flash
            new_flash = new_energy > 9
            have_new_flash = (new_flash & ~flash).sum().sum() > 0
            flash = new_flash
        
        energy = new_energy
        energy[flash] = 0
        flash_count += flash.sum().sum()

        if iteration == 100:
            part1 = flash_count
        if flash.all().all():
            return part1, iteration


def part1(data):
    """
    Solve part 1.
    """
    part1, part2 = flashes(data)
    return(part1)
def part2(data):
    """
    Solve part 2.
    """
    part1, part2 = flashes(data)
    return(part2)
        
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
