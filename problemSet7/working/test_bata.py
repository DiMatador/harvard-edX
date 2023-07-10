import pytest
from working import convert

# test 24-hour clock
def test_working_twenty_four_hour_clock():
    clock_tfh = convert('12 AM to 12:45 AM')
    assert clock_tfh == '00:00 to 00:45'
    clock_tfh1 = convert('9 AM to 5 PM')
    assert clock_tfh1 == "09:00 to 17:00"

# test 0 in front
def test_zero_front():
    zero_f = convert('1 AM to 10 AM')
    assert zero_f == '01:00 to 10:00'


# test ValueError
def test_working_ve():
    with pytest.raises(ValueError):
        convert('9 AM - 7 PM')

    with pytest.raises(ValueError):
        convert('cat to dog')

    with pytest.raises(ValueError):
        convert('9AMto4PM')

    with pytest.raises(ValueError):
        convert('9am to 5pm')

    with pytest.raises(ValueError):
        convert('')

    with pytest.raises(ValueError):
        convert('13 AM to 13 PM')

# test for missing 'to'
def test_working_omit_to():
    with pytest.raises(ValueError):
        convert('9 AM 4 PM')