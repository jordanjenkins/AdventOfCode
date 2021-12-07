import pathlib
import pytest
import Day7 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that example input is properly parsed"""
    assert example1 == [16,1,2,0,4,2,7,1,2,14]

@pytest.mark.skip(reason="data same as example 1")
def test_parse_example2(example2):
    """Test that example input is properly parsed"""
    assert example2 == []

# @pytest.mark.skip(reason="Not yet implemented")
def test_part1_example(example1):
    """Test part one on example data"""
    
    assert aoc.part1(example1) == 37

# @pytest.mark.skip(reason="Not yet implemented")
def test_part2_example(example1):
    """Test part two on example data"""
    assert aoc.part2(example1) == 168