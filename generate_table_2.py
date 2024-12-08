import json
import pandas as pd


def load_json_data(filename):
    """
    Wczytuje dane JSON z podanego pliku.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {filename}.")
        return None
    except json.JSONDecodeError:
        print(f"Błąd: Plik {filename} nie jest poprawnym plikiem JSON.")
        return None


def process_data_to_table(data):
    """
    Przetwarza dane JSON na tabelę zawierającą procent poprawnych wyników.
    """
    results = {}

    # Grupowanie poprawności wyników według funkcji i modelu
    for entry in data:
        function_name = entry["Nazwa funkcji "]
        models = {
            "Chat GPT 3.5-Turbo": entry["Chat GPT 3.5-Turbo correctness"],
            "Llama 3.1-70B Ins": entry["Llama 3.1-70B Ins correctness"],
            "Llama 3.1-8B": entry["Llama 3.1-8B correctness"],
            "Chat GPT 4o": entry["Chat GPT 4o correctness"],
            "Chat GPT 4o mini": entry["Chat GPT 4o mini correctness"]

        }

        if function_name not in results:
            results[function_name] = {model: {"correct": 0, "total": 0} for model in models.keys()}

        for model, correctness in models.items():
            results[function_name][model]["total"] += 1
            if correctness:
                results[function_name][model]["correct"] += 1

    # Tworzenie tabeli
    table_data = {"Nazwa Modelu": []}
    for function_name in results:
        table_data[function_name] = []

    # Obliczanie procentowej poprawności dla każdej funkcji i modelu
    for model in ["Chat GPT 3.5-Turbo", "Llama 3.1-70B Ins", "Llama 3.1-8B", "Chat GPT 4o", "Chat GPT 4o mini"]:
        table_data["Nazwa Modelu"].append(model)
        for function_name, stats in results.items():
            correct = stats[model]["correct"]
            total = stats[model]["total"]
            percentage = (correct / total) * 100 if total > 0 else 0
            table_data[function_name].append(round(percentage, 2))

    # Konwersja do DataFrame
    df = pd.DataFrame(table_data)
    return df


def save_to_csv(df, filename):
    """
    Zapisuje DataFrame do pliku CSV.
    """
    try:
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Zapisano plik CSV: {filename}")
    except Exception as e:
        print(f"Błąd podczas zapisywania pliku CSV: {e}")


def main():
    """
    Główna funkcja programu.
    """
    print("=== Przetwarzanie danych JSON na CSV ===")

    # Poproś użytkownika o nazwę pliku JSON
    json_filename = input("Podaj nazwę pliku JSON (np. measurements.json): ").strip()
    csv_filename = input("Podaj nazwę pliku wynikowego CSV (np. output_table.csv): ").strip()

    # Wczytaj dane JSON
    data = load_json_data(json_filename)
    if data is None:
        return

    # Przetwórz dane do tabeli
    df = process_data_to_table(data)

    # Zapisz tabelę do pliku CSV
    save_to_csv(df, csv_filename)


if __name__ == "__main__":
    main()
