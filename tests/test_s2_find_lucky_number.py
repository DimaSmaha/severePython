import pytest
from challenges.s2_find_lucky_number import get_lucky_ticket_numbers

tickets_one = ['111111', '003212', '001001', '014500', '2124215', '5252']
tickets_two = ['015231', '5252']
tickets_three = ['111111', '5252', '2124215']
noTicketsMessage = 'There are no lucky numbers'


def test_should_return_twoTickets():
    assert get_lucky_ticket_numbers(tickets_one) == ['001001', '014500']


def test_should_return_oneTickets():
    assert get_lucky_ticket_numbers(tickets_two) == ['015231']


def test_should_return_noTickets():
    assert get_lucky_ticket_numbers(tickets_three) == noTicketsMessage


def test_should_return_typeError():
    with pytest.raises(TypeError):
        assert get_lucky_ticket_numbers('')
