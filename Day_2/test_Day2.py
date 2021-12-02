import pathlib
import pytest
import Day2 as aoc

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
    assert example1 == ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

@pytest.mark.skip(reason="not implemented")
def test_parse_example2(example2):
    """Test that example input is properly parsed"""
    assert example2 == []


def test_part1_example(example1):
    """Test part one on example data"""
    assert aoc.part1(example1) == 150


@pytest.mark.skip(reason="not implemented")
def test_part2_example(example2):
    """Test part two on example data"""
    assert aoc.part2(example2) == []