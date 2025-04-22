import pytest
from ..challenges.add_challenge import add


def should_add_positive_numbers():
    assert add(5, 6) == 11
