
import pytest
from challenges.s1_find_most_repeated_chars import most_repeated_character

str1 = 'QA Automation Engineer'
str2 = 'Los Santos, San Fiero, Las Venturas'
str3 = 'a'


def test_should_count_most_popular_char():
    assert most_repeated_character(str1) == 'a, 3'


def test_should_count_most_popular_char_2():
    assert most_repeated_character(str2) == 's, 6'


def test_should_count_most_popular_char_3():
    assert most_repeated_character(str3) == 'a, 1'


def test_should_show_error():
    with pytest.raises(TypeError):
        assert most_repeated_character(1)


def test_should_show_error_value():
    with pytest.raises(ValueError):
        assert most_repeated_character('')
