import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


def euler_mascheroni(terms=100000):
    terms = max(1, int(abs(terms)))
    gamma = 0.0
    for k in range(1, terms + 1):
        gamma += (1 / k) - math.log((k + 1) / k)
    return round_if_float(gamma)


def euler_polynomial(n, x):
    n, x = int(str(abs(n))[0]), int(str(abs(x))[0])
    if n > x:
        x = n
        x1 = n
        n = x1
    E = [1] * (n + 1)
    for k in range(1, n + 1):
        E[k] = E[k - 1] * (x - (k - 1))
    return E[-1]


value_1 = 1
value_2 = 4

result = value_1

result = euler_mascheroni(result if int(abs(result)) not in [0, 1] else value_1)
result = euler_polynomial(result if int(abs(result)) not in [0, 1] else value_1, value_2)
print(result)
