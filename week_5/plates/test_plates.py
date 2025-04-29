import pytest
from plates import is_valid

def test_is_valid_7():
    assert is_valid("CSS") == True
    assert is_valid("48") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False

def test_is_valid_1():
    assert is_valid("CS50") == True

def test_is_valid_2():
    assert is_valid("CS05") == False

def test_is_valid_3():
    assert is_valid("CS50P") == False

def test_is_valid_4():
    assert is_valid("PI3.14") == False

def test_is_valid_5():
    assert is_valid("H") == False

def test_is_valid_6():
    assert is_valid("OUTATIME") == False
