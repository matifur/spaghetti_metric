import json
from datetime import datetime
import subprocess
from model_GPT_3_5_turbo import gpt_3_5_code_interpretation
from model_Llama_3_1_70B_Ins import llama_3_1_70B_Ins_code_interpretation


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


def compile_and_save_to_json(filename='generated_program.py', output_filename="measurements.json"):
    try:
        # Wczytanie kodu źródłowego
        with open(filename, 'r') as file:
            source_code = file.read()

        # Uruchomienie programu i pobranie wyniku
        result = subprocess.run(['python', filename], capture_output=True, text=True)

        # Przygotowanie danych do zapisu
        data = {
            "Date and Time": datetime.now().isoformat(),  # Data i czas wykonania
            "Program code": source_code,  # Kod programu
            "Local run output": result.stdout.strip() if result.returncode == 0 else result.stderr.strip(),  # Lokalne uruchomienie
            "Chat GPT 3.5-turbo output": gpt_3_5_code_interpretation(),  # Wynik z LLM
            "Llama 3.1-70B Ins output": llama_3_1_70B_Ins_code_interpretation(),  # Wynik z LLM
        }

        # Zapisz dane do pliku JSON
        save_to_json(data, output_filename)
        print(f"Wynik zapisano do pliku {output_filename}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


# Przykładowe wywołanie funkcji
#compile_and_save_to_json()