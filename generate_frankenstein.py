import random

def generate_frankenstein_program(queue_count=3, function_count=3, max_iterations=5, operations=None):
    if operations is None:
        operations = ["+", "-", "*", "//"]

    # Nagłówek programu
    header = """# Wygenerowany kod\n\nimport random\n\n"""

    # Funkcja pomocnicza
    helper_function = """def safe_division(a, b):
    return a // b if b != 0 else 0\n\n"""

    # Losowe kolejki generowane podczas tworzenia programu
    queues = {}
    for i in range(queue_count):
        queues[f"queue_{i}"] = [random.randint(1, 100) for _ in range(random.randint(5, 10))]

    # Konwersja kolejek do kodu
    queues_section = ""
    for queue_name, queue_data in queues.items():
        queues_section += f"{queue_name} = {queue_data}\n"

    queues_section += "\n"

    # Generowanie funkcji z pętlami for
    functions_section = ""
    for i in range(function_count):
        func_name = f"function_{i}"
        queue_in = f"queue_{random.randint(0, queue_count - 1)}"
        queue_out = f"queue_{random.randint(0, queue_count - 1)}"
        operation = random.choice(operations)

        functions_section += f"def {func_name}(input_queue):\n"
        functions_section += f"    output_queue = []\n"
        functions_section += f"    for value in input_queue:\n"

        if operation == "//":
            functions_section += f"        result = safe_division(value, {random.randint(1, 10)})\n"
        else:
            functions_section += f"        result = value {operation} {random.randint(1, 10)}\n"

        functions_section += f"        output_queue.append(result)\n"
        functions_section += f"    return output_queue\n\n"

    # Generowanie głównego kodu
    main_section = "if __name__ == '__main__':\n"
    for i in range(queue_count):
        queue_name = f"queue_{i}"
        function_to_apply = f"function_{random.randint(0, function_count - 1)}"
        main_section += f"    {queue_name} = {function_to_apply}({queue_name})\n"

    main_section += "\n    # Wyświetlenie wyników\n"
    for i in range(queue_count):
        queue_name = f"queue_{i}"
        main_section += f"    print('{queue_name}:', {queue_name})\n"

    # Łączenie całości kodu
    program_code = header + helper_function + queues_section + functions_section + main_section

    # Zapis do pliku z poprawionym kodowaniem
    try:
        with open("frankenstein_program.py", "w", encoding="utf-8") as file:
            file.write(program_code)
        print("Program został wygenerowany i zapisany jako 'frankenstein_program.py'")
    except IOError as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")


# Przykładowe użycie funkcji
generate_frankenstein_program(queue_count=5, function_count=4, max_iterations=7)
