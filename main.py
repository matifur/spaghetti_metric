from generator_math import generate_math_1, program_functions_math
from saving_output import save_to_json, compile_and_save_to_json, compile_and_save_frankenstein
from generate_frankenstein import generate_frankenstein_program
import random


# Wywołujemy funkcję z wartością zmiennych oraz funkcjami które chcemy zawrzeć
def run_generator_1_functions_randomizer(num_of_functions, num_of_generations):
    for j in range(num_of_generations):
        variable_1_rand = random.randrange(1, 10, 1)
        variable_2_rand = random.randrange(1, 10, 1)
        select_function_rand = []
        # Tutaj wybieramy nie wszystkie funkcje bo wpływ skomplikowanych obliczeń matematycznych jest zbyt duży
        for i in range(num_of_functions):
            select_function_rand.append(random.randrange(1, 10, 1))
        print(len(program_functions_math))

        # Wykaz podanych wartości
        print(f"variable_1_rand = {variable_1_rand}, variable_2_rand = {variable_2_rand}, select_function_rand = {select_function_rand}")
        generate_math_1(variable_1_rand, variable_2_rand, select_function_rand)  # functions randomizer, optional variable

        print("==============================================================================")
        print("Running program and collecting output from LLM-s")
        print("==============================================================================")
        compile_and_save_to_json(num_of_functions)
        print("==============================================================================")
        print("Process Completed!")
        print("==============================================================================")


def run_generator_2_every_function_benchmark(num_of_generations):
    num_of_functions = 1
    for j in range(num_of_generations):
        for h in range(len(program_functions_math)):

            variable_1_rand = random.randrange(1, 10, 1)
            variable_2_rand = random.randrange(1, 10, 1)
            select_function_rand = [h]

            # Wykaz podanych wartości
            print(f"variable_1_rand = {variable_1_rand}, variable_2_rand = {variable_2_rand}, select_function_rand = {select_function_rand}")
            generate_math_1(variable_1_rand, variable_2_rand, select_function_rand)  # functions randomizer, optional variable

            print("==============================================================================")
            print("Running program and collecting output from LLM-s")
            print("==============================================================================")
            compile_and_save_to_json(num_of_functions, "generated_program.py", "measurements_2.json", h)
            print("==============================================================================")
            print("Process Completed!")
            print("==============================================================================")


def run_generator_3_every_function_breaktest(num_of_functions, num_of_generations, test_index):

    for j in range(num_of_generations):

        print("==============================================================================")
        print("Running program and collecting output from LLM-s")
        print("==============================================================================")
        compile_and_save_to_json(num_of_functions, 'generated_program.py', "measurements_3.json", 1, test_index)
        print("==============================================================================")
        print("Process Completed!")
        print("==============================================================================")


def generate_program_for_3_test(num_of_functions):
    variable_1_rand = random.randrange(1, 10, 1)
    variable_2_rand = random.randrange(1, 10, 1)
    select_function_rand = []
    # Tutaj wybieramy nie wszystkie funkcje bo wpływ skomplikowanych obliczeń matematycznych jest zbyt duży
    for i in range(num_of_functions):
        select_function_rand.append(random.randrange(1, 10, 1))

    print(len(program_functions_math))

    # Wykaz podanych wartości
    print(
        f"variable_1_rand = {variable_1_rand}, variable_2_rand = {variable_2_rand}, select_function_rand = {select_function_rand}")
    generate_math_1(variable_1_rand, variable_2_rand, select_function_rand)  # functions randomizer, optional variable

def run_generator_4_frankenstein_operations():
    for i in range(1,8):
        for j in range(25):
            generate_frankenstein_program(2, i)
            print("==============================================================================")
            print("Running program and collecting output from LLM-s")
            print("==============================================================================")
            compile_and_save_frankenstein(2, i, "frankenstein_program.py", "measurements_frankenstein_operations.json")
            print("==============================================================================")
            print("Process Completed!")
            print("==============================================================================")

def run_generator_5_frankenstein_data():
    for i in range(1,8):
        for j in range(25):
            generate_frankenstein_program(i, 2)
            print("==============================================================================")
            print("Running program and collecting output from LLM-s")
            print("==============================================================================")
            compile_and_save_frankenstein(i, 2, "frankenstein_program.py", "measurements_frankenstein_data.json")
            print("==============================================================================")
            print("Process Completed!")
            print("==============================================================================")


# Main
# User input
print("1) Test wpływu długości programu na pracę LLM")
print("2) Test zdolności do ewaluacji każdej funkcji")
print("3) Testowanie tego samego programu")
print("4) Generuj program dla 3 testu")
print("5) Wpływ ilości opracji frankenstein")
print("6) Wpływ ilości danych frankenstein")
while True:
    try:
        choose_test = int(input("Podaj numer testu z listy który chciałbyś uruchomić: "))
        break
    except ValueError:
        print("To nie jest numer. Spróbuj ponownie.")


match choose_test:
    case 1:
        while True:
            try:
                liczba_funkcji = int(input("Podaj liczbę funkcji: "))
                liczba_generacji = int(input("Podaj liczbe generacji: "))
                break
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
        run_generator_1_functions_randomizer(liczba_funkcji, liczba_generacji)
    case 2:
        while True:
            try:
                liczba_generacji = int(input("Podaj liczbe generacji: "))
                break
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
        run_generator_2_every_function_benchmark(liczba_generacji)
    case 3:
        while True:
            try:
                liczba_funkcji = int(input("Podaj liczbę funkcji: "))
                liczba_generacji = int(input("Podaj liczbe generacji: "))
                numer_testu = int(input("Podaj numer testu: "))
                break
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
        run_generator_3_every_function_breaktest(liczba_funkcji, liczba_generacji, numer_testu)
    case 4:
        while True:
            try:
                liczba_funkcji = int(input("Podaj liczbę funkcji: "))
                break
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
        generate_program_for_3_test(liczba_funkcji)
    case 5:
        run_generator_4_frankenstein_operations()
    case 6:
        run_generator_5_frankenstein_data()
    case _:
        print("Niepoprawna opcja")