# Example file for Programming Foundations: Algorithms by Joe Marini
# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    # divide arrays until they cant be divided
    # recursively call the division
    # when they can not be divided sort them
    # merge and sort them
    # return sorted
    # merge arrays until you come beack to init lengs

    if len(dataset) <= 1:
        return dataset

    dividedLen = len(dataset) // 2  # always returns integer without remainer

    # returns from 0 to X index passed
    leftPart = dataset[:dividedLen]

    # returns from X index passed to END
    rightPart = dataset[dividedLen:]

    leftPart = mergesort(leftPart)
    rightPart = mergesort(rightPart)

    def merge(left, right):
        resultArr = []
        leftId = 0
        rightId = 0

        while leftId < len(left) and rightId < len(right):
            if left[leftId] > right[rightId]:
                resultArr.append(left[leftId])
                leftId += 1
            else:
                resultArr.append(right[rightId])
                rightId += 1

        print(resultArr)
        return resultArr

    dataset = merge(leftPart, rightPart)
    print(dataset)
    return dataset


print(items)
mergesort(items)
print(items)
