from abc import abstractclassmethod
from feature.feature import func

def test_func():
    assert func() == 5

def test_func_2():
    assert func() == 4