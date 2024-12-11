def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def safe_division(a, b):
    return a // b if b != 0 else 0


example_0 = [74, 17, 24, 12, 81, 19]

def process_examples(input_example):
    output_example = input_example
    for idx, value in enumerate(output_example):
        output_example[idx] = subtraction(value, 4)
    return output_example

if __name__ == '__main__':
    example_0 = process_examples(example_0)

    # Wyświetlenie losowego wyniku
    print(example_0[3])
