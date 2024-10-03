from working import convert
import pytest

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:00 PM to 1:00 AM") == "13:00 to 01:00"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_edge_cases():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:01 AM to 12:59 AM") == "00:01 to 00:59"
    assert convert("12:01 PM to 12:59 PM") == "12:01 to 12:59"

if __name__ == "__main__":
    pytest.main()