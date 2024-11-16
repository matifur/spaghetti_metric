import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


def stirling_first_kind(n, k):
    n, k = int(abs(n)), int(abs(k))
    if k > n or k == 0:
        k, n = n, k
    if k == n:
        return 1
    if k == 1:
        return math.factorial(n - 1)
    return (n - 1) * stirling_first_kind(n - 1, k) + stirling_first_kind(n - 1, k - 1)


value_1 = 8
value_2 = 8

result = value_1

result = stirling_first_kind(result if int(abs(result)) not in [0, 1] else value_1, value_2)
print('stirling_first_kind result:', result)
