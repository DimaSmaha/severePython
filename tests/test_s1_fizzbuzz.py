from challenges.s1_fizzbuzz import fizz_buzz
import pytest


def test_should_return_fizz():
    assert fizz_buzz(3) == 'Fizz'


def test_should_return_fizz_2():
    assert fizz_buzz(9) == 'Fizz'


def test_should_return_buzz():
    assert fizz_buzz(5) == 'Buzz'


def test_should_return_buzz_2():
    assert fizz_buzz(20) == 'Buzz'


def test_should_return_fizz_buzz():
    assert fizz_buzz(15) == 'FizzBuzz'


def test_should_return_fizz_buzz_2():
    assert fizz_buzz(30) == 'FizzBuzz'


def test_should_return_number():
    assert fizz_buzz(4) == 4


def test_should_return_number_2():
    assert fizz_buzz(8) == 8


def test_should_show_error_for_not_int():
    with pytest.raises(TypeError):
        assert fizz_buzz('1')


def test_should_show_error_for_not_int_2():
    with pytest.raises(TypeError):
        assert fizz_buzz('')
