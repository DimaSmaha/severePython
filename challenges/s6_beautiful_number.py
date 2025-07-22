"""
Lily likes to play games with integers. 
She has created a new game where she determines the difference
between a number and its reverse. 
For instance, given the number , its reverse is . 
Their difference is . The number  reversed is , and their difference is .

She decides to apply her game to decision making. 
She will look at a numbered range of days and will only go 
to a movie on a beautiful day.

Given a range of numbered days,  
and a number , determine the number of days 
in the range that are beautiful. 
Beautiful numbers are defined as numbers where  is evenly divisible by .
If a day's value is a beautiful number, it is a beautiful day. 
Return the number of beautiful days in the range.

Function Description

Complete the beautifulDays function in the editor below.

beautifulDays has the following parameter(s):

int i: the starting day number
int j: the ending day number
int k: the divisor
"""


def beautiful_numbers(startD: int, endD: int, divider: int):
    get_all_days = list(range(startD, endD))
    beautiful_numbers_arr = []

    for el in get_all_days:
        swap_days_number = str(el)[::-1]

        is_beautiful = abs((el - int(swap_days_number)) % divider) == 0

        if is_beautiful:
            beautiful_numbers_arr.append(el)

    return beautiful_numbers_arr


print(beautiful_numbers(20, 24, 6))
print(beautiful_numbers(16, 24, 4))
print(beautiful_numbers(10, 23, 8))
