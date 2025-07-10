

def hurdle_race(k: int, height: list[int]):

    maxHurdle = max(height)
    getMinPotionNum = maxHurdle - k

    if getMinPotionNum <= 0:
        return 0

    return getMinPotionNum


print(hurdle_race(4, [1, 2, 3, 4, 5]))
print(hurdle_race(3, [1, 2, 3, 4, 5]))
print(hurdle_race(4, [1, 5, 3, 2, 3]))
print(hurdle_race(1, [1, 5, 1, 4, 6]))
