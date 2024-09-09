import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("XYZ456") == True
    assert is_valid("AB") == True
    assert is_valid("AB0123") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("") == False

def test_non_alphanumeric():
    assert is_valid("AB@123") == False
    assert is_valid("XYZ 456") == False
    assert is_valid("A!B2C3") == False

def test_invalid_number_placement():
    assert is_valid("A1B2C3D") == False
    assert is_valid("123ABC") == False
    assert is_valid("A1B2C3") == False
    
if __name__ == "__main__":
    pytest.main()