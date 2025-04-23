from challenges.add_challenge import add
import pytest


def test_should_add_positive_numbers():
    assert add(5, 6) == 11


def test_should_add_negative_numbers():
    assert add(-5, -5) == -10


def test_should_show_error_for_not_int():
    with pytest.raises(TypeError):
        assert add('1', 1)


def test_should_show_error_for_second_not_int():
    with pytest.raises(TypeError):
        assert add(1, '1')


def test_should_show_error_for_list():
    with pytest.raises(TypeError):
        assert add([1], 1)
