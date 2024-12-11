import random

def generate_frankenstein_program(queue_count=3, function_count=3):
    # Nagłówek programu
    header = """def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def safe_division(a, b):
    return a // b if b != 0 else 0\n\n
"""

    # Losowe kolejki generowane podczas tworzenia programu
    examples = {}
    for i in range(queue_count):
        examples[f"example_{i}"] = [random.randint(1, 100) for _ in range(random.randint(5, 10))]

    # Ustalanie losowego przykładu i indeksu przed generowaniem programu
    random_example_idx = random.randint(0, queue_count - 1)
    random_element_idx = random.randint(0, len(examples[f"example_{random_example_idx}"]) - 1)

    # Konwersja kolejek do kodu
    examples_section = ""
    for example_name, example_data in examples.items():
        examples_section += f"{example_name} = {example_data}\n"

    examples_section += "\n"

    # Generowanie jednej funkcji zawierającej wiele pętli for
    operations = ["addition", "subtraction", "multiplication", "safe_division"]
    main_function = "def process_examples(input_example):\n"
    main_function += "    output_example = input_example\n"

    for i in range(function_count):
        operation = random.choice(operations)
        main_function += f"    for idx, value in enumerate(output_example):\n"
        main_function += f"        output_example[idx] = {operation}(value, {random.randint(1, 10)})\n"

    main_function += "    return output_example\n\n"

    # Generowanie losowego przypisania kolejek
    example_assignments = list(range(queue_count))
    random.shuffle(example_assignments)

    main_section = "if __name__ == '__main__':\n"
    for i, target in enumerate(example_assignments):
        main_section += f"    example_{i} = process_examples(example_{target})\n"

    # Wyświetlenie ustalonego wyniku
    main_section += "\n    # Wyświetlenie losowego wyniku\n"
    main_section += f"    print(example_{random_example_idx}[{random_element_idx}])\n"

    # Łączenie całości kodu
    program_code = header + examples_section + main_function + main_section

    # Zapis do pliku z poprawionym kodowaniem
    try:
        with open("frankenstein_program.py", "w", encoding="utf-8") as file:
            file.write(program_code)
        print("Program został wygenerowany i zapisany jako 'frankenstein_program.py'")
    except IOError as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")

# Przykładowe użycie funkcji
generate_frankenstein_program(queue_count=1, function_count=1)
