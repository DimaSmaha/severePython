

def pickingNumbers(numbers: list[int]) -> int:
    numbersArr = numbers
    tempNums = []

    firstNumber = numbersArr[0]
    tempNums.append(firstNumber)

    for index, el in enumerate(numbersArr):
        if index == 0:
            continue

        if (abs(firstNumber - el) == 1 or firstNumber - el == 0):
            if (len(tempNums) < 5):
                tempNums.append(el)

    indexToRemove: list[int] = []
    for index in range(len(tempNums) - 1):
        if not (abs(tempNums[index] - tempNums[index + 1]) == 1 or tempNums[index] - tempNums[index + 1] == 0):
            indexToRemove.append(index)

    if (len(indexToRemove) >= 1):
        tempNums.pop(indexToRemove[0])

    print(tempNums)
    return len(tempNums)


print(pickingNumbers([4, 1]))
print(pickingNumbers([1, 2, 3]))
print(pickingNumbers([4, 6, 5, 3, 3, 1]))
print(pickingNumbers([1, 2, 2, 3, 1, 2]))
print(pickingNumbers([1, 2, 2, 3, 1, 2, 2]))
