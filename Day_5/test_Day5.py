import pathlib
import pytest
import Day5 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt")
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that example input is properly parsed"""
    assert example1 == ['0,9 -> 5,9\n', '8,0 -> 0,8\n', '9,4 -> 3,4\n', '2,2 -> 2,1\n', '7,0 -> 7,4\n', '6,4 -> 2,0\n', '0,9 -> 2,9\n', '3,4 -> 1,4\n', '0,0 -> 8,8\n', '5,5 -> 8,2']
def test_parse_points(example1):
    res = [aoc.parse_points(line) for line in example1]
    assert res == [[(0, 9), (5, 9)], [(8, 0), (0, 8)], [(9, 4), (3, 4)],
                   [(2, 2), (2, 1)], [(7, 0), (7, 4)], [(6, 4), (2, 0)],
                   [(0, 9), (2, 9)], [(3, 4), (1, 4)], [(0, 0), (8, 8)],
                   [(5, 5), (8, 2)]]

@pytest.mark.skip(reason="data same as example 1")
def test_parse_example2(example2):
    """Test that example input is properly parsed"""
    assert example2 == []

# @pytest.mark.skip(reason="Not yet implemented")
def test_part1_example(example1):
    """Test part one on example data"""
    #res = [aoc.parse_points(line) for line in example1]
    assert aoc.part1(example1) == 5

# @pytest.mark.skip(reason="Not yet implemented")
def test_part2_example(example1):
    """Test part two on example data"""
    assert aoc.part2(example1) == 12