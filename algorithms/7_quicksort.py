# Will be honest I have copied it, since doesnt see a sense to write it
# At least now or never

items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # Calculate the split point
        pivotIdx = partition(dataset, first, last)
        # Recursively sort left and right sublists
        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)


def partition(datavalues, first, last):
    pivot = datavalues[first]  # Choose the first item as pivot
    low = first + 1
    high = last

    while True:
        # Move low up while items are <= pivot
        while low <= high and datavalues[low] <= pivot:
            low += 1
        # Move high down while items are >= pivot
        while low <= high and datavalues[high] >= pivot:
            high -= 1
        # If indexes cross, break
        if low > high:
            break
        else:
            # Swap out-of-place elements
            datavalues[low], datavalues[high] = datavalues[high], datavalues[low]

    # Swap pivot with datavalues[high] to put pivot in correct position
    datavalues[first], datavalues[high] = datavalues[high], datavalues[first]
    return high  # Return the final pivot position


# Test the quicksort with data
print("Before:", items)
quickSort(items, 0, len(items) - 1)
print("After: ", items)
