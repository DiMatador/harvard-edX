''' Test module for fuel.py '''
import pytest
from fuel import convert
from fuel import gauge

def test_Fuel():
    output = convert('1/4')
    assert output == 25
    output1 = convert('3/4')
    assert output1 == 75

def test_empty_full():
    empty = gauge(1)
    assert empty == 'E'
    full = gauge(99)
    assert full == 'F'
    percentage = gauge(55)
    assert percentage == '55%'

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('10/0')
        convert('100/0')

def test_str():
    with pytest.raises(ValueError):
        convert('cat/dog')
        convert('juana/cubana')