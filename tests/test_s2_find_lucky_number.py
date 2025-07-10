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


def test_valid_lucky_ticket():
    assert get_lucky_ticket_numbers(["001001"]) == ["001001"]


def test_valid_unlucky_ticket():
    assert get_lucky_ticket_numbers(["123456"]) == noTicketsMessage


def test_invalid_ticket_too_short():
    assert get_lucky_ticket_numbers(["12345"]) == noTicketsMessage


def test_invalid_ticket_non_numeric():
    assert get_lucky_ticket_numbers(["12a456"]) == noTicketsMessage


def test_ticket_out_of_range_zero():
    assert get_lucky_ticket_numbers(["000000"]) == noTicketsMessage


def test_ticket_out_of_range_high():
    assert get_lucky_ticket_numbers(["100001"]) == noTicketsMessage


def test_mixed_valid_and_invalid():
    tickets = ["001001", "123456", "abc123", "000000", "100000"]
    assert get_lucky_ticket_numbers(tickets) == ["001001"]


def test_less_than_min_symbols():
    tickets = ["12345"]
    assert get_lucky_ticket_numbers(tickets) == noTicketsMessage
