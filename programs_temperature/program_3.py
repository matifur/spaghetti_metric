def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def safe_division(a, b):
    return a // b if b != 0 else 0

example_0 = [53, 13, 67, 99, 96, 27, 8, 74, 24]
example_1 = [53, 64, 86, 26, 36, 9, 24, 13, 18, 15]

def process_examples(input_example):
    output_example = input_example
    for idx, value in enumerate(output_example):
        output_example[idx] = subtraction(value, 6)
    for idx, value in enumerate(output_example):
        output_example[idx] = subtraction(value, 1)
    return output_example

if __name__ == '__main__':
    example_0 = process_examples(example_0)
    example_1 = process_examples(example_1)

    # Wyświetlenie losowego wyniku
    print(example_1[4])
