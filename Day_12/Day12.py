import pathlib
import sys
from collections import deque, defaultdict


def parse(puzzle_input):
    """Parse input"""
    lst = [line for line in puzzle_input.split("\n")]
    # print(lst)
    return lst

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        if u != 'start':
            self.graph[v].append(u)
        if v != 'start':
            self.graph[u].append(v)
    
    def n_paths(self, src, dst):
        stack = deque([(src, {src})])
        total = 0

        while stack:
            node, visited = stack.pop()

            if node == dst:
                total += 1
                continue
            
            for n in self.graph[node]:
                if n in visited and n.islower():
                    continue
                
                stack.append((n, visited | {n}))
        return total
    
    def n_paths2(self, src, dst):
        stack = deque([(src, {src}, False)])
        total = 0

        while stack:
            node, visited, double = stack.pop()
            
            if node == dst:
                total += 1
                continue
            
            for n in self.graph[node]:
                if n not in visited or n.isupper():
                    stack.append((n, visited | {n}, double))
                    continue
                
                if double:
                    continue
                stack.append((n, visited, True))

        return total
    
def part1(data):
    """
    Solve part 1.
    """
    G = Graph()
    for line in data:
        split_line = line.split('-')
        G.addEdge(split_line[0], split_line[1])
    
    n = G.n_paths('start', 'end')
    return n

def part2(data):
    """
    Solve part 2.
    """
    G = Graph()
    for line in data:
        split_line = line.split('-')
        G.addEdge(split_line[0], split_line[1])
    
    n = G.n_paths2('start', 'end')
    return n

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
