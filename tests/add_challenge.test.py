import pytest
from challenges.add_challenge import add


def should_add_positive_numbers():
    assert add(5, 6) == 11


def should_show_error_for_not_int():
    with pytest.raises(TypeError):
        assert add('a', 2)
