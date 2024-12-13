import math

def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value

def power(base, exponent):
    base, exponent = int(str(abs(base))[0]), int(str(abs(exponent))[0])
    first_number = int(str(base)[0])
    return base ** exponent

def absolute_value(number):
    return abs(number)

def is_prime(number):
    number = int(abs(number))
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

value_1 = 9
value_2 = 6

result = value_1

result = power(result if int(abs(result)) not in [0, 1] else value_1, value_2)
result = absolute_value(result if int(abs(result)) not in [0, 1] else value_1)
result = is_prime(result if int(abs(result)) not in [0, 1] else value_1)
print(result)
