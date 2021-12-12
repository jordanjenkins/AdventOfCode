import pathlib
import pytest
import Day12 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="data same as example 1")
def test_parse_example1(example1):
    """Test that example input is properly parsed"""
    assert example1 == ['fs-end', 'he-DX', 'fs-he', 'start-DX', 'pj-DX', 'end-zg', 'zg-sl', 'zg-pj', 'pj-he', 'RW-he', 'fs-DX', 'pj-RW', 'zg-RW', 'start-pj', 'he-WI', 'zg-he', 'pj-fs', 'start-RW']

@pytest.mark.skip(reason="data same as example 1")
def test_parse_example2(example2):
    """Test that example input is properly parsed"""
    assert example2 == []

# @pytest.mark.skip(reason="Not yet implemented")
def test_part1_example(example1):
    """Test part one on example data"""
    
    assert aoc.part1(example1) == 226

# @pytest.mark.skip(reason="Not yet implemented")
def test_part2_example(example1):
    """Test part two on example data"""
    assert aoc.part2(example1) == 3509