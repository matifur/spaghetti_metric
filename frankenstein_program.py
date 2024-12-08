# Wygenerowany kod

import random

def safe_division(a, b):
    return a // b if b != 0 else 0

example_0 = [88, 13, 31, 48, 12, 38, 77, 98, 7, 8]
example_1 = [65, 42, 74, 12, 43, 4, 48, 35, 39, 63]
example_2 = [85, 90, 3, 85, 78]
example_3 = [58, 63, 15, 2, 65, 12, 31]
example_4 = [3, 50, 73, 27, 94, 81, 82, 33, 77, 52]

def function_0(input_example):
    output_example = []
    for value in input_example:
        result = value - 10
        output_example.append(result)
    return output_example

def function_1(input_example):
    output_example = []
    for value in input_example:
        result = value * 4
        output_example.append(result)
    return output_example

def function_2(input_example):
    output_example = []
    for value in input_example:
        result = value * 3
        output_example.append(result)
    return output_example

def function_3(input_example):
    output_example = []
    for value in input_example:
        result = value - 7
        output_example.append(result)
    return output_example

if __name__ == '__main__':
    example_0 = function_3(example_0)
    example_1 = function_0(example_1)
    example_2 = function_1(example_2)
    example_3 = function_1(example_3)
    example_4 = function_0(example_4)

    # Wyświetlenie wyników
    print('example_0:', example_0)
    print('example_1:', example_1)
    print('example_2:', example_2)
    print('example_3:', example_3)
    print('example_4:', example_4)
