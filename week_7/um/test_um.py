import pytest
from um import count


def test_1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("Um, thanks, um...") == 2


def test_2():
    assert count("Yummy") == 0
    assert count("instrumentation") == 0
    assert count("Uumma") == 0


def test_3():
    assert count("Yummy um , food") == 1
    assert count("instrumentation, um waas good") == 1
    assert count("Uummay thank um ") == 1
