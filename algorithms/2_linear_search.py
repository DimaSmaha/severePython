# Linear search
# Used for searching an item in an UNORDERED list
# By iterating through each element of array

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(item, itemlist):
    # create a loop to go thought each element of array
    # enumerate item list
    # create an if statemnet to return index if found
    # create else to return -1 if not found

    for index, el in enumerate(itemlist):
        if (el == item):
            return index

    return -1


print(find_item(87, items))
print(find_item(49, items))
print(find_item(20, items))
print(find_item(250, items))
