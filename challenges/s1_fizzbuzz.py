def fizz_buzz(a: int) -> str or int:

    if not isinstance(a, int):
        raise TypeError('The input should be number')

    if (a % 3 == 0 and a % 5 == 0):
        return 'FizzBuzz'

    if (a % 3 == 0):
        return 'Fizz'

    if (a % 5 == 0):
        return 'Buzz'

    return a
