import pathlib
import pytest
import Day1 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that example input is properly parsed"""
    assert example1 == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_part1_example(example1):
    """Test part one on example data"""
    assert aoc.part1(example1) == 7

def test_parse_part2(example2):
    """Test that example input is properly parsed"""
    assert example2 == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_part2_example(example2):
    """Test part two on example data"""
    assert aoc.part2(example2) == 5