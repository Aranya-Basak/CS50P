import pytest
from twttr import shorten

def test_shorten_cap():
    assert shorten("ARANYA") == "RNY"

def test_shorten_sml():
    assert shorten("aranya") == "rny"

def test_shorten_all():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_num():
    assert shorten("1") == "1"

def test_shorten_punc():
    assert shorten(", ") == ", "
