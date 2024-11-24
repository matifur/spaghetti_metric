import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


def power(base, exponent):
    base, exponent = int(str(abs(base))[0]), int(str(abs(exponent))[0])
    first_number = int(str(base)[0])
    return base ** exponent


def sine(angle):
    return round_if_float(math.sin(math.radians(angle)))


def binomial_coefficient(n, k):
    n, k = int(str(abs(n))[0]), int(str(abs(k))[0])
    if k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def factorial(n):
    n = int(abs(n))
    first_number = int(str(n)[0])
    return math.factorial(first_number)


value_1 = 2
value_2 = 9

result = value_1

result = power(result if int(abs(result)) not in [0, 1] else value_1, value_2)
result = sine(result if int(abs(result)) not in [0, 1] else value_1)
result = binomial_coefficient(result if int(abs(result)) not in [0, 1] else value_1, value_2)
result = factorial(result if int(abs(result)) not in [0, 1] else value_1)
print(result)
