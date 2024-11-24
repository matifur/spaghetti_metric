import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


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


def stirling_first_kind(n, k):
    n, k = int(abs(n)), int(abs(k))
    if k > n or k == 0:
        k, n = n, k
    if k == n:
        return 1
    if k == 1:
        return math.factorial(n - 1)
    return (n - 1) * stirling_first_kind(n - 1, k) + stirling_first_kind(n - 1, k - 1)


def euler_mascheroni(terms=100000):
    terms = max(1, int(abs(terms)))
    gamma = 0.0
    for k in range(1, terms + 1):
        gamma += (1 / k) - math.log((k + 1) / k)
    return round_if_float(gamma)


def ln2_taylor(terms=1000):
    terms = max(1, int(abs(terms)))
    return round_if_float(sum((-1)**(n + 1) / n for n in range(1, terms + 1)))


value_1 = 2
value_2 = 1

result = value_1

result = euler_polynomial(result if int(abs(result)) not in [0, 1] else value_1, value_2)
result = stirling_first_kind(result if int(abs(result)) not in [0, 1] else value_1, value_2)
result = euler_mascheroni(result if int(abs(result)) not in [0, 1] else value_1)
result = ln2_taylor(result if int(abs(result)) not in [0, 1] else value_1)
print(result)
