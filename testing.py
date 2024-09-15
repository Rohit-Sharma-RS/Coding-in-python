import pytest
from my_func import func

def test_passing():
    pass


def test_pass():
    assert func.add(1, 2) == 3


def test_fail():
    assert func.add(1, 2) == 4