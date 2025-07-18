def angry_professor(thresholdToCancel: int, studentsCome: list[int]):

    def myFunc(x):
        if x >= 0:
            return False
        else:
            return True

    studentsThatCome = len(list(filter(myFunc, studentsCome)))

    if (studentsThatCome >= thresholdToCancel):
        return 'NO'

    return 'YES'


print(angry_professor(4, [-5, -4, -3, 0, 1, 2]))  # NO
print(angry_professor(2, [-5, 2, 5, 6]))  # YES
print(angry_professor(3, [-5, -4, 0, 1, 2]))  # NO
print(angry_professor(5, [-5, -4, -3, -2, 0, 1, 2]))  # YES
