from challenges.add_challenge import add
import pytest


def test_should_add_positive_numbers():
    assert add(5, 6) == 11


def test_should_show_error_for_not_int():
    with pytest.raises(TypeError):
        assert add('a', 2)
