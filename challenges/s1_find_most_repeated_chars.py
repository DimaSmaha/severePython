somestr = 'I love New York'


def most_repeated_character(str: str) -> str:
    somestr = list(str.replace(' ', '').lower())
    somestr.sort()
    to_set = set(somestr)

    my_dick = {}
    for i in to_set:
        count_char = somestr.count(i)
        my_dick[i] = count_char

    # списав з вас тупл і сортування
    my_tuple = tuple(my_dick.items())
    sorted_tuple = sorted(my_tuple, key=lambda x: x[1], reverse=True)

    max_char = sorted_tuple[0].__str__().replace(
        '(', '').replace(')', '').replace("'", '')

    return max_char
