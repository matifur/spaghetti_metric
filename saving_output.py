import json
from datetime import datetime
import subprocess
from model_GPT_3_5_turbo import gpt_3_5_code_interpretation
from model_Llama_3_1_70B_Ins import llama_3_1_70B_Ins_code_interpretation
from model_GPT_4o import gpt_4o_code_interpretation
from model_GPT_4o_mini import gpt_4o_mini_code_interpretation
from generator_math import program_functions_math

def cut_function_name_test_2(a, output_filename):
    if output_filename == "measurements_2.json":
        lines = program_functions_math[a].splitlines()
        first_line = lines[0].replace(" ", "")
        return first_line[3:first_line.find("(")] if first_line.find("(") != -1 else print('ERROR! No "(" in first line!')
    else:
        return "null"


#Funkcja porównójąca wyniki działania modeli i kompilatora
def compare_values(value1, value2, tolerance=1e-3):
    # Funkcja pomocnicza do usuwania białych znaków i konwersji na odpowiedni typ
    def clean_and_convert(value):
        if isinstance(value, str):
            value = value.strip()  # Usuwa białe znaki z początku i końca
            try:
                return float(value)  # Próbuj zamienić na float
            except ValueError:
                pass  # Jeśli nie da się zamienić, pozostaw jako string
        return value

    # Czyszczenie i konwersja
    value1 = clean_and_convert(value1)
    value2 = clean_and_convert(value2)

    # Porównanie, jeśli obie wartości to bool
    if isinstance(value1, bool) and isinstance(value2, bool):
        return value1 == value2

    # Porównanie, jeśli obie wartości to liczby
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return abs(value1 - value2) <= tolerance

    # Porównanie bezpośrednie dla innych typów (np. string)
    return value1 == value2


def save_to_json(data, filename="measurements.json"):
    # Wczytanie istniejących danych (jeśli plik istnieje)
    try:
        with open(filename, 'r') as f:
            file_data = json.load(f)
    except FileNotFoundError:
        file_data = []

    # Dodanie nowego wpisu do danych
    file_data.append(data)

    # Zapisanie danych do pliku JSON z wcięciami dla lepszej czytelności
    with open(filename, 'w') as f:
        json.dump(file_data, f, indent=4)


def compile_and_save_to_json(functions_numebr_castj, filename='generated_program.py', output_filename="measurements.json", func_index_castj = 1):
    try:
        # Wczytanie kodu źródłowego
        with open(filename, 'r') as file:
            source_code = file.read()

        # Uruchomienie programu i pobranie wyników z kompilatora i LLM
        result = subprocess.run(['python', filename], capture_output=True, text=True)
        result_chat_gpt_3_5_Turbo = gpt_3_5_code_interpretation()
        result_llama_3_1_70B_Ins = llama_3_1_70B_Ins_code_interpretation()
        result_chat_gpt_4o = gpt_4o_code_interpretation()
        result_chat_gpt_4o_mini = gpt_4o_mini_code_interpretation()

        # Przygotowanie danych do zapisu
        data = {
            "Date and Time": datetime.now().isoformat(),  # Data i czas wykonania
            "Program code": source_code,  # Kod programu
            "Local run output": result.stdout.strip() if result.returncode == 0 else result.stderr.strip(),  # Lokalne uruchomienie
            "Chat GPT 3.5-turbo output": result_chat_gpt_3_5_Turbo,  # Wynik z LLM
            "Llama 3.1-70B Ins output": result_llama_3_1_70B_Ins,  # Wynik z LLM
            "Chat GPT 4o output": result_chat_gpt_4o,  # Wynik z LLM
            "Chat GPT 4o mini output": result_chat_gpt_4o_mini,  # Wynik z LLM
            "Liczba funkcji ": functions_numebr_castj,
            "Nazwa funkcji ": cut_function_name_test_2(func_index_castj, output_filename),
            "Chat GPT 3.5-Turbo correctness": compare_values(result.stdout.strip(), result_chat_gpt_3_5_Turbo),
            "Llama 3.1-70B Ins correctness": compare_values(result.stdout.strip(), result_llama_3_1_70B_Ins),
            "Chat GPT 4o correctness": compare_values(result.stdout.strip(), result_chat_gpt_4o),
            "Chat GPT 4o mini correctness": compare_values(result.stdout.strip(), result_chat_gpt_4o_mini)

        }

        # Zapisz dane do pliku JSON
        save_to_json(data, output_filename)
        print(f"Wynik zapisano do pliku {output_filename}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


# Przykładowe wywołanie funkcji
#compile_and_save_to_json()