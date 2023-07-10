import pytest
from seasons import CheckDate

def test_seasons_valid_date():
    birth_date = ('2001-01-01')
    person = CheckDate(birth_date)
    assert person.minutes_in_birthday() == 'Eleven million, seven hundred ninety-six thousand, four hundred eighty minutes'

    birth_date1 = ('1999-01-01')
    person1 = CheckDate(birth_date1)
    assert person1.minutes_in_birthday() == 'Twelve million, eight hundred forty-nine thousand, one hundred twenty minutes'


def test_seasons_invalid_date():
    with pytest.raises(ValueError):
        birth_date = 'Aug-05-1973'
        person = CheckDate(birth_date)
        person.minutes_in_birthday()