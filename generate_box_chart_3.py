import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych z pliku JSON
file_path = "measurements_3.json"  # Zmień na swoją ścieżkę do pliku
with open(file_path, "r") as file:
    data = json.load(file)

# Funkcja do przetwarzania danych
def process_data(data):
    # Przechowywanie wyników w formie {Model -> {Numer testu -> [Wyniki]}}
    model_results = {}

    for entry in data:
        test_id = entry["Numer testu"]
        for model, correctness_key in [
            ("Chat GPT 3.5-turbo", "Chat GPT 3.5-Turbo correctness"),
            ("Llama 3.1-70B Ins", "Llama 3.1-70B Ins correctness"),
            ("Llama 3.1-8B", "Llama 3.1-8B correctness"),
            ("Chat GPT 4o", "Chat GPT 4o correctness"),
            ("Chat GPT 4o mini", "Chat GPT 4o mini correctness"),
        ]:
            if model not in model_results:
                model_results[model] = {}
            if test_id not in model_results[model]:
                model_results[model][test_id] = []
            model_results[model][test_id].append(entry[correctness_key])

    # Obliczanie procentowej poprawności dla każdej serii testów
    accuracy_data = []
    for model, tests in model_results.items():
        for test_id, results in tests.items():
            total_tests = len(results)
            correct_tests = sum(results)  # True = 1, False = 0
            accuracy_percentage = (correct_tests / total_tests) * 100 if total_tests > 0 else 0
            accuracy_data.append({"Model": model, "Test ID": test_id, "Accuracy (%)": accuracy_percentage})

    return pd.DataFrame(accuracy_data)

# Przetwarzanie danych
df = process_data(data)

# Wyświetlanie przetworzonych danych
print("Przetworzone dane z procentową poprawnością:")
print(df)

# Tworzenie wykresu pudełkowego
plt.figure(figsize=(12, 6))
sns.boxplot(x="Model", y="Accuracy (%)", data=df)
plt.title("Rozkład procentu poprawnych odpowiedzi dla modeli")
plt.xlabel("Model")
plt.ylabel("Procent poprawnych odpowiedzi (%)")
plt.show()
