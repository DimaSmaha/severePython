"""A Discrete Mathematics professor has a class of students. 
Frustrated with their lack of discipline, the professor 
decides to cancel class if fewer than some number of students are present when class starts. 
Arrival times go from on time () to arrived late ().
Given the arrival time of each student and a threshhold number of 
attendees, determine if the class is cancelled."""


def angry_professor(thresholdToCancel: int, studentsCome: list[int]):
    def filter_return_in_time_students(number):
        return number <= 0
    # for python style
    # result = len([x for x in student_timing if x <= 0])
    # return "NO" if result >= threshhold else "YES"

    in_time_students = list(
        filter(filter_return_in_time_students, studentsCome))

    if thresholdToCancel <= len(in_time_students):
        return "NO we are not cancelling"

    return "YES we cancell"


print(angry_professor(4, [-5, -4, -3, 0, 1, 2]))  # NO
print(angry_professor(2, [-5, 2, 5, 6]))  # YES
print(angry_professor(3, [-5, -4, 0, 1, 2]))  # NO
print(angry_professor(5, [-5, -4, -3, -2, 0, 1, 2]))  # NO
print(angry_professor(5, [-5, -4, -3, -2, 1, 1, 2]))  # YES


"""
def filter_return_in_time_students(number):
    if (number <= 0):
        return number

        Because filter() uses the truthiness of the functions return value.

In Python:

filter() keeps elements where the function returns a truthy value

0 is falsy, so it's excluded

So even though you returned 0, it gets treated as False.
"""
