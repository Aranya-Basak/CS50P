import pytest
from numb3rs import validate

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("25.25.25.25") == True
    assert validate("2.2.2.2") == True
    assert validate("0.255.25.0") == True

def test_false():
        assert validate("255.255.255") == False
        assert validate("255.256.255.255") == False
        assert validate("255.255.256.255") == False
        assert validate("255.255.512.255") == False
        assert validate("shinchan") == False

