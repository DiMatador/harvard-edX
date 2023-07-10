import pytest
from twttr import shorten

def main():
    test_string()
    test_number()
    test_uppercase()
    test_puntuation()
    

def test_string():
    assert shorten('Davila') == 'Dvl'
    
def test_uppercase():
    assert shorten('Julio') == 'Jl'
    
def test_number():
    with pytest.raises(TypeError):
        shorten(25) == 25
    
def test_puntuation():
    assert shorten('.Julio-/,_?') == '.Jl-/,_?'