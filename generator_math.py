import random

# konwencja pisania program_functions:
# 1) def ... ():  <- musi być w pierwszej linijce.
# 2) definicję funkcji kończymy zawsze 2 pustymi linijkami.
# 3) istotna jest ilość tabulacji dlatego zawsze zaczynamy od samego początku lewej strony.
program_functions_math = [
"""def square(number):
    return number ** 2\n\n
""",

"""def square_root(number):
    return math.sqrt(number)\n\n
""",

"""def sum_numbers(a, b):
    return a + b\n\n
""",

"""def absolute_value(number):
    return abs(number)\n\n
""",

"""def factorial(n):
    n = int(abs(n))
    first_number = int(str(n)[0])
    return math.factorial(first_number)\n\n
""",

"""def is_prime(number):
    number = int(abs(number))
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True\n\n
""",

"""def circle_area(radius):
    return 3.14 * radius ** 2\n\n
""",

"""def power(base, exponent):
    base, exponent = int(str(abs(base))[0]), int(str(abs(exponent))[0])
    first_number = int(str(base)[0])
    return base ** exponent\n\n
""",

"""def sine(angle):
    return math.sin(math.radians(angle))\n\n
""",

"""def nth_fibonacci(n):
    if n <= 0:
        return "Enter a number greater than 0."
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b\n\n
""",

"""def catalan_number(n):
    n = int(abs(n))
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))\n\n
""",

"""def stirling_second_kind(n, k):
    n, k = int(str(abs(n))[0]), int(str(abs(k))[0])
    if k > n or k == 0:
        k, n = n, k
    if k == n or k == 1:
        return 1
    return k * stirling_second_kind(n - 1, k) + stirling_second_kind(n - 1, k - 1)\n\n
""",

"""def bernoulli_number(n):
    n = int(abs(n))
    if n == 0:
        return 1
    elif n % 2 != 0 and n > 1:
        return 0
    A = [0] * (n + 1)
    for m in range(n + 1):
        A[m] = 1 / (m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return A[0]\n\n
""",

"""def euler_mascheroni(terms=100000):
    terms = max(1, int(abs(terms)))
    gamma = 0.0
    for k in range(1, terms + 1):
        gamma += (1 / k) - math.log((k + 1) / k)
    return gamma\n\n
""",

"""def harmonic_number(n):
    n = max(1, int(abs(n)))
    return sum(1 / k for k in range(1, n + 1))\n\n
""",

"""def fibonacci_binet(n):
    n = int(abs(n))
    if n > 20:
        n = 10 + int(str(n)[0])
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))\n\n
""",

"""def riemann_zeta(n, terms=100000):
    n = abs(n) if n > 1 else 2
    terms = max(1, int(abs(terms)))
    return sum(1 / k**n for k in range(1, terms + 1))\n\n
""",

"""def pi_leibniz(terms=1000000):
    terms = max(1, int(abs(terms)))
    pi_approx = 0.0
    for k in range(terms):
        pi_approx += ((-1)**k) / (2 * k + 1)
    return 4 * pi_approx\n\n
""",

"""def stirling_first_kind(n, k):
    n, k = int(abs(n)), int(abs(k))
    if k > n or k == 0:
        k, n = n, k
    if k == n:
        return 1
    if k == 1:
        return math.factorial(n - 1)
    return (n - 1) * stirling_first_kind(n - 1, k) + stirling_first_kind(n - 1, k - 1)\n\n
""",

"""def euler_number(n):
    n = int(abs(n))
    if n == 0:
        return 1
    A = [0] * (n + 1)
    for m in range(n + 1):
        A[m] = 1 / (m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return A[0] * (1 if n % 2 == 0 else -1)\n\n
""",

"""def ln2_taylor(terms=1000):
    terms = max(1, int(abs(terms)))
    return sum((-1)**(n + 1) / n for n in range(1, terms + 1))\n\n
""",

"""def e_approximation(terms=20):
    terms = max(1, int(abs(terms)))
    return sum(1 / math.factorial(n) for n in range(terms))\n\n
""",

"""def binomial_coefficient(n, k):
    n, k = int(str(abs(n))[0]), int(str(abs(k))[0])
    if k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))\n\n
""",

"""def euler_polynomial(n, x):
    n, x = int(str(abs(n))[0]), int(str(abs(x))[0])
    if n > x:
        x = n
        x1 = n
        n = x1
    E = [1] * (n + 1)
    for k in range(1, n + 1):
        E[k] = E[k - 1] * (x - (k - 1))
    return E[-1]\n\n
""",

"""def pi_nilakantha(terms=100000):
    terms = abs(int(terms))

    first_digit = int(str(terms)[0])

    terms = first_digit

    pi_approx = 3.0  
    for k in range(1, terms + 1):
        term = 4 / (2 * k * (2 * k + 1) * (2 * k + 2))
        pi_approx += term if k % 2 == 1 else -term  # Naprzemienne dodawanie/odejmowanie
    return pi_approx 
""",

"""def partial_harmonic_sum(n):
    n = max(1, int(abs(n)))
    return sum(1 / k for k in range(1, n + 1))\n\n
""",

"""def taylor_expansion_exp(x, n):
    n, x = max(1, int(abs(n))), int(str(abs(x))[0])
    return sum((x**i) / math.factorial(i) for i in range(n + 1))\n\n
""",

"""def euler_totient(n):
    n = 2 + int(str(abs(n))[0])
    count = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            count += 1
    return count\n\n
"""

]


def cut_function_name(a):
    lines = program_functions_math[a].splitlines()
    first_line = lines[0].replace(" ", "")
    return first_line[3:first_line.find("(")] if first_line.find("(") != -1 else print('ERROR! No "(" in first line!')


def second_variable_needed(a):
    svr_bool_table = []
    for k in range(0, len(a)):
        lines = program_functions_math[a[k]].splitlines()
        first_line = lines[0]
        if first_line.find(",") != -1:
            svr_bool_table.append(True)
        else:
            svr_bool_table.append(False)
    return svr_bool_table


def generate_math_1(variable_value_1, variable_value_2, select_functions):
    svr = second_variable_needed(select_functions)

    # Część kodu która zawsze będzie znajdowała się na początku programu
    always_include = """import math\n\n\n"""

    # Część główna programu: ustawiamy początkowy wynik na wartość zmiennej value_1
    main_content = f"value_1 = {variable_value_1}\n"
    main_content += f"value_2 = {variable_value_2}\n\n" if any(svr) else ""

    # Początkowa wartość do przekazania
    main_content += "result = value_1\n\n"

    # Generowanie wywołań funkcji, gdzie wynik przechodzi przez kolejne funkcje
    for j, func_index in enumerate(select_functions):
        func_name = cut_function_name(func_index)
        print(f"Funkcja o indexie = {func_index}, j = {j}")

        # Jeśli funkcja wymaga dwóch argumentów, wykorzystajmy `value_2`
        if svr[j]:
            main_content += f"result = {func_name}(result if int(abs(result)) not in [0, 1] else value_1, value_2)\n"
        else:
            main_content += f"result = {func_name}(result if int(abs(result)) not in [0, 1] else value_1)\n"

        # Wyświetlanie wyniku po każdym wywołaniu funkcji
        main_content += f"print('{func_name} result:', result)\n"

    # Łączymy program w całość
    program_code = always_include
    for func_index in select_functions:
        program_code += program_functions_math[func_index]
    program_code += main_content

    # Zapisujemy wygenerowany kod do pliku .py
    try:
        with open("generated_program.py", "w") as file:
            file.write(program_code)
        print("Program został wygenerowany i zapisany jako 'generated_program.py'")
    except IOError as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")