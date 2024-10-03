from um import count
import pytest

def test_basic():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1

def test_sentences():
    assert count("um, hello") == 1
    assert count("Um, hello um") == 2
    assert count("Um, hello um. Um.") == 3
    assert count("Um, um, um.") == 3

def test_edge_cases():
    assert count("um um um") == 3
    assert count("um? um! um.") == 3
    assert count("um... um... um...") == 3
    assert count("um-um-um") == 0
    assert count("um123 um456") == 0

if __name__ == "__main__":
    pytest.main()