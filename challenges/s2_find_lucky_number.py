"""
- Implement a function that accepts a list of strings as ticket numbers.
- The range should be between 000001 and 100000.
- All numbers outside of this range should be ignored.
- It should return a list of only lucky numbers.
   - A lucky number is a number where the sum of the first three symbols is equal to the sum of the second three symbols.
"""
from typing import List


def get_lucky_ticket_numbers(tickets: List[str]) -> List[str]:
    if (tickets == ''):
        raise TypeError('No empty')

    lucky_numbers: List[str] = []

    for ticket in tickets:
        if len(ticket) == 6:
            if (int(ticket) <= 100_000):
                int_list = []
                for char in ticket:
                    int_list.append(char)

                # We can also get len() of int_list, divide by 2 to get first half of the numbers and set it in sum loop
                first_sum = 0
                second_sum = 0

                for index, i in enumerate(int_list):
                    if (index <= 2):  # sum of first 3 elements
                        first_sum += int(i)
                    if (index >= 3):  # sum of next 3 elements
                        second_sum += int(i)

                print(first_sum, second_sum)
                if (first_sum == second_sum):
                    print(ticket)
                    lucky_numbers.append(str(ticket))

    print(lucky_numbers)
    if (lucky_numbers == []):
        return 'There are no lucky numbers'

    return lucky_numbers


# first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# second_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
