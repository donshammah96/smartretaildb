from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")