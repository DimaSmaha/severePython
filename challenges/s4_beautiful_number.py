def beautiful_numbers(startD: int, endD: int, divider: int):
    number_of_b_date = 0

    for day in range(startD, endD):
        swap_number = int(str(day)[::-1])

        if (day - swap_number) % divider == 0:
            number_of_b_date += 1

    return number_of_b_date


print(beautiful_numbers(20, 24, 6))
