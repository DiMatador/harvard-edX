import pytest
from plates import is_valid


def test_two_characters():
    output = is_valid('jc')
    assert output == True
    output1 = is_valid('JC')
    assert output1 == True


def test_six_characters():
    output_six = is_valid('JCDV73')
    # assert output_six == True


def test_too_many_characters():
    output_to_many = is_valid('JCDV9991')
    assert output_to_many == False


def test_first_digit_zero():
    output_zero = is_valid('AA0AA')
    assert output_zero == False
    output_zero1 = is_valid('jcd073')
    assert output_zero1 == False


def test_all_digits():
    output_all_digits = is_valid('779991')
    assert  output_all_digits == False
    output_number_placement = is_valid('AA973A')
    assert output_number_placement == True


def test_none_alphanumeric():
    output_puntuations = is_valid('jcd.,/')
    assert output_puntuations == False
