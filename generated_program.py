import math


def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value


def euler_totient(n):
    n = 2 + int(str(abs(n))[0])
    count = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            count += 1
    return count


value_1 = 6
result = value_1

result = euler_totient(result if int(abs(result)) not in [0, 1] else value_1)
print('euler_totient result:', result)
