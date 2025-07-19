# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, itemlist):
    # get the middle index
    # compare it, to searchable
    # if == return index
    # if < find a middle index of first part
    # if > find a middle inxed of second part
    # retry actions
    print('--------------')

    max_index = int(len(itemlist)-1)
    min_index = 0

    for index in enumerate(itemlist):
        middle_index = int((max_index+min_index)/2)

        if item == itemlist[middle_index]:
            return middle_index

        if item < itemlist[middle_index]:
            print(
                f"{itemlist[middle_index]} is lower than {item} recalculating")
            max_index = middle_index
            continue

        if item > itemlist[middle_index]:
            print(
                f"{itemlist[middle_index]} is bigger than {item} recalculating")
            min_index = middle_index+1
            continue
    return -1


print(binarysearch(6, items))
print('--------------')
print(binarysearch(19, items))
print('--------------')
print(binarysearch(23, items))
print('--------------')
print(binarysearch(49, items))
print('--------------')
print(binarysearch(87, items))
print('--------------')
print(binarysearch(21, items))
print('--------------')
