import math


def partial_harmonic_sum(n):
    n = max(1, int(abs(n)))
    return sum(1 / k for k in range(1, n + 1))


value_1 = 8
result = value_1

result = partial_harmonic_sum(result if int(abs(result)) not in [0, 1] else value_1)
print('partial_harmonic_sum result:', result)
