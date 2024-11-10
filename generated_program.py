import math


def nth_fibonacci(n):
    if n <= 0:
        return "Enter a number greater than 0."
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def circle_area(radius):
    return 3.14 * radius ** 2


def taylor_expansion_exp(x, n):
    n, x = max(1, int(abs(n))), int(str(abs(x))[0])
    return sum((x**i) / math.factorial(i) for i in range(n + 1))


def stirling_second_kind(n, k):
    n, k = int(str(abs(n))[0]), int(str(abs(k))[0])
    if k > n or k == 0:
        k, n = n, k
    if k == n or k == 1:
        return 1
    return k * stirling_second_kind(n - 1, k) + stirling_second_kind(n - 1, k - 1)


value_1 = 7
value_2 = 43

result = value_1

result = nth_fibonacci(result if int(abs(result)) not in [0, 1] else value_1)
print('nth_fibonacci result:', result)
result = circle_area(result if int(abs(result)) not in [0, 1] else value_1)
print('circle_area result:', result)
result = taylor_expansion_exp(result if int(abs(result)) not in [0, 1] else value_1, value_2)
print('taylor_expansion_exp result:', result)
result = stirling_second_kind(result if int(abs(result)) not in [0, 1] else value_1, value_2)
print('stirling_second_kind result:', result)
