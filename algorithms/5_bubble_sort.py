# Bubble sort algorithm


def bubbleSort(dataset):

    # create a nested loop where
    # the condition = compare I and I+1, swap them if they are bigger
    # if not, continue to next elements
    # i = starting point
    # ii = our bubbles (ii ii+1)

    for i in range(len(dataset)):
        for ii in range(i):
            if dataset[ii] > dataset[ii+1]:
                temp = dataset[ii]
                dataset[ii] = dataset[ii+1]
                dataset[ii+1] = temp
            print("Current state: ", dataset)


list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print("Start: ", list1)
bubbleSort(list1)
print("Result: ", list1)
