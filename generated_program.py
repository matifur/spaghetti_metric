import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


def power(base, exponent):
    base, exponent = int(str(abs(base))[0]), int(str(abs(exponent))[0])
    first_number = int(str(base)[0])
    return base ** exponent


def factorial(n):
    n = int(abs(n))
    first_number = int(str(n)[0])
    return math.factorial(first_number)


value_1 = 2
value_2 = 1

result = value_1

result = power(result if int(abs(result)) not in [0, 1] else value_1, value_2)
result = factorial(result if int(abs(result)) not in [0, 1] else value_1)
print(result)
