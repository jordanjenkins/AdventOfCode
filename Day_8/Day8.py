import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    f = open(puzzle_input)
    raw = list(f.readlines())

    out = [x.strip().split(" | ") for x in raw]
    return out
class Entry():
    def __init__(self, sig_pattern, out_pattern):
        self.sig_pattern = sig_pattern.split()
        self.out_pattern = out_pattern.split()
        self.decoded_digits = {}
        self.decoded_output = []

def part1(data):
    """
    Solve part 1.
    """
    counter = 0
    for x in data:
        entry = Entry(x[0], x[1])
        #print(entry.out_pattern)
        for x in entry.out_pattern:
            # print(x, len(x))
            if len(x) == 2:
                counter += 1
            if len(x) == 3:
                counter += 1
            if len(x) == 4:
                counter += 1
            if len(x) == 7:
                counter += 1
    return counter
    
def part2(data):
    """
    Solve part 2.
    """
    def containsAll(str, set):
        """ Check whether sequence str contains ALL of the items in set. """
        return 0 not in [c in str for c in set]
    def convert(list):
            res = int("".join(map(str,list)))
            return res
            
    cumsum = 0
    for x in data:
        entry = Entry(x[0], x[1])
        d = entry.decoded_digits
        e = sorted(entry.sig_pattern, key=len)
        for x in e:
            sorted_x = ''.join(sorted(x))
            if len(sorted_x) == 2:
                d[1] = sorted_x
            if len(sorted_x) == 3:
                d[7] = sorted_x  
            if len(sorted_x) == 4:
                d[4] = sorted_x
            if len(sorted_x) == 5:
                if containsAll(sorted_x, d[7]):
                    d[3] = sorted_x
                else:
                    if len(set(sorted_x).intersection(d[4])) == 3:
                        d[5] = sorted_x
                    else:
                        d[2] = sorted_x
            if len(sorted_x) == 6:
                if containsAll(sorted_x, d[4]):
                   d[9] = sorted_x
                else:
                    if containsAll(sorted_x, d[7]):
                        d[0] = sorted_x
                    else:
                        d[6] = sorted_x
            if len(sorted_x) == 7:
                d[8] = sorted_x
            
        o = entry.out_pattern
        

        for x in o:
            entry.decoded_output.append([k for k, v in d.items() if ''.join(sorted(x)) == v][0])
        cumsum += convert(entry.decoded_output)
    return cumsum

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
