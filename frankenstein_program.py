def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def safe_division(a, b):
    return a // b if b != 0 else 0


example_0 = [11, 45, 18, 63, 64, 67]
example_1 = [50, 15, 63, 57, 43]
example_2 = [29, 69, 52, 96, 99, 89, 40]
example_3 = [75, 14, 13, 89, 78, 36, 36, 99, 48, 79]
example_4 = [74, 65, 86, 43, 15, 24, 90]
example_5 = [45, 7, 61, 66, 17, 4, 13, 98, 72]
example_6 = [19, 95, 60, 37, 81, 47]

def process_examples(input_example):
    output_example = input_example
    for idx, value in enumerate(output_example):
        output_example[idx] = safe_division(value, 9)
    for idx, value in enumerate(output_example):
        output_example[idx] = safe_division(value, 10)
    return output_example

if __name__ == '__main__':
    example_0 = process_examples(example_0)
    example_1 = process_examples(example_3)
    example_2 = process_examples(example_6)
    example_3 = process_examples(example_1)
    example_4 = process_examples(example_2)
    example_5 = process_examples(example_4)
    example_6 = process_examples(example_5)

    # Wyświetlenie losowego wyniku
    print(example_4[4])
