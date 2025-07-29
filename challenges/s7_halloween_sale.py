"""
You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price,  dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game will cost  dollars, and every subsequent game will cost  dollars less than the previous one. This continues until the cost becomes less than or equal to  dollars, after which every game will cost  dollars. How many games can you buy during the Halloween Sale?

Example



.

The following are the costs of the first , in order:

Start at  units cost, reduce that by  units each iteration until reaching a minimum possible price, . Starting with  units of currency in your Mist wallet, you can buy 5 games: .
"""


def howManyGames(pre_price, discount, min_price, s_your_money):

    games_prices = []
    games_to_buy = 0
    current_balance = s_your_money
    current_game_cost = pre_price

    # while our budget bigger than 0, then we go inside
    # we get pre price

    while (current_balance >= 0):
        if (current_game_cost <= min_price):
            current_game_cost = min_price

        if (current_balance >= current_game_cost):
            games_prices.append(current_game_cost)
            games_to_buy += 1
            current_balance -= current_game_cost
            current_game_cost -= discount

        if (current_balance <= min_price):
            break

    return games_to_buy, games_prices


print(howManyGames(20, 3, 6, 70))
print(howManyGames(20, 3, 6, 80))
