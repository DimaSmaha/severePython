"""
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

Example




There are  prisoners,  pieces of candy and distribution starts at chair . The prisoners arrange themselves in seats numbered  to . Prisoners receive candy at positions . The prisoner to be warned sits in chair number ."""

# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#


def saveThePrisoner(n_prisoners, milki_ways, start_seat):
    current_number_of_candies = milki_ways
    current_seat = start_seat

    while (current_number_of_candies > 0):
        current_number_of_candies -= 1

        if (current_number_of_candies == 1):
            return current_seat

        if (current_seat < n_prisoners):
            current_seat += 1
        else:
            current_seat = 1


print(saveThePrisoner(4, 6, 2))
print(saveThePrisoner(4, 6, 4))
print(saveThePrisoner(5, 12, 1))
print(saveThePrisoner(5, 2, 1))
print(saveThePrisoner(5, 2, 2))
print(saveThePrisoner(3, 7, 3))
print(saveThePrisoner(10, 15, 6))
