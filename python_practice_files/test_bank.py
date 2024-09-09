import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

def test_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("Hey") == 20

def test_other():
    assert value("goodbye") == 100
    assert value("Good morning") == 100
    assert value("what's up") == 100
    assert value("Greetings") == 100

def test_error():
    with pytest.raises(TypeError):
        value(1)
    with pytest.raises(TypeError):
        value(None)
    with pytest.raises(TypeError):
        value([])

if __name__ == "__main__":
    pytest.main()