# Using recursion to implement power and factorial functions
# recursion is used in cases when we dont know how much iteration we will have

# 2^4 = 2*2*2*2 = 16
def power(num, pwr):
    # create an exit statement for 0 to return 0
    # decrease powered number
    # call power with decreaed pwr and use multiply

    if pwr == 0:
        return 1

    return num * power(num, pwr-1)


# 5! = 5*4*3*2*1
# Special case: 0! is 1, because... math
def factorial(num):
    # create an exit statement for 0
    # get your number, subtract 1
    # call a factorial function again up to the zeri

    if num == 0:
        return 1

    return num * factorial(num-1)


print(f"10 to the power of 2 is {power(10, 2)}")
print(f"5 to the power of 3 is {power(5, 3)}")
print(f"2 to the power of 4 is {power(2, 4)}")
print(f"4! is {factorial(5)}")
print(f"4! is {factorial(4)}")
print(f"0! is {factorial(0)}")
