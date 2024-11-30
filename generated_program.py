import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


def is_prime(number):
    number = int(abs(number))
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


value_1 = 5
result = value_1

result = is_prime(result if int(abs(result)) not in [0, 1] else value_1)
print(result)
