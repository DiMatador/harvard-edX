import pytest
from bank import value

def min():
    test_hello()
    

# test hello, Hello, should return $0
def test_hello():
    assert value('hello') == 0
    assert value('hey') == 20
    assert value('what up') == 100
    assert value('HELLO') == 0
