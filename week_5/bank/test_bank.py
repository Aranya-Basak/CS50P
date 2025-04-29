import pytest
from bank import value

def test_value_greet():
    assert value("Hello") == 0

def test_value_greetman():
    assert value("Hello, Newman") == 0

def test_value_num():
    assert value("121") == 100

def test_value_punc():
    assert value(", vvv") == 100

def test_value_h():
    assert value("How are you?") == 20

def test_value_gen():
    assert value("What's") == 100


