# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [87, 56, 53, 49, 41, 23, 20, 19, 8, 6]
items3 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted(itemlist, sortedType: str):
    # TODO: using the brute force method
    # create a for loop that would compare the elements to one another
    # if they does not fill the condition return false
    # create for asc desc cases

    if sortedType not in ('asc', 'desc'):
        raise ValueError("sortedType must be 'asc' or 'desc'")

    for index in range(len(itemlist)-1):
        if sortedType == 'desc' and itemlist[index] < itemlist[index+1]:
            return False

        if sortedType == 'asc' and itemlist[index] > itemlist[index+1]:
            return False

    return True


print(is_sorted(items1, 'asc'))  # True
print(is_sorted(items1, 'desc'))  # False
print(is_sorted(items2, 'desc'))  # True
print(is_sorted(items2, 'asc'))  # False
print(is_sorted(items3, 'asc'))  # False
