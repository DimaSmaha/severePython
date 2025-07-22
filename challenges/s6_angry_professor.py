"""A Discrete Mathematics professor has a class of students. 
Frustrated with their lack of discipline, the professor 
decides to cancel class if fewer than some number of students are present when class starts. 
Arrival times go from on time () to arrived late ().
Given the arrival time of each student and a threshhold number of 
attendees, determine if the class is cancelled."""


def angry_professor(thresholdToCancel: int, studentsCome: list[int]):
    def filter_return_in_time_students(number):
        return number <= 0

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
