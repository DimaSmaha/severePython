"""A video player plays a game in which the character competes
in a hurdle race. 
Hurdles are of varying heights, and the characters have a maximum
height they can jump. 
There is a magic potion they can take that will increase
their maximum jump height by  unit for each dose. 
How many doses of the potion must the character take to be able
to jump all of the hurdles. 
If the character can already clear all of the hurdles, return .

Example
The character can jump 2 unit high initially and must take 2
doses of potion to be able to jump all of the hurdles. """


def hurdle_race(k: int, height: list[int]):
    max_height = int(max(height))
    min_potions = max_height - k

    if min_potions < 0:
        return 0

    return min_potions


print(hurdle_race(4, [1, 2, 3, 4, 5]))
print(hurdle_race(3, [1, 2, 3, 4, 5]))
print(hurdle_race(4, [1, 5, 3, 2, 3]))
print(hurdle_race(1, [1, 5, 1, 4, 6]))

# Python style solution
# required_dose = max(heights) - k
# return max(0, required_dose)
