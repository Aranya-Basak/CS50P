from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_2 = Jar(45)
    assert jar_2.capacity == 45

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    jar.deposit(4)
    assert jar.size == 11


def test_withdraw():
    jar = Jar(13)
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0


def test_errors():
    with pytest.raises(ValueError):
        jar = Jar(-2)
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.deposit(12)
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.deposit(9)
        jar.withdraw(13)
