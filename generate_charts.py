import json
import matplotlib.pyplot as plt

# Wczytaj dane z pliku measurements.json
file_path = 'measurements.json'  # Upewnij się, że plik jest w tym samym katalogu co ten program

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def process_data(data):
    # Przygotuj dane do analizy
    functions = []
    chatgpt35Turbo_correctness = []
    llama_correctness = []
    chatgpt4o_correctness = []
    chatgpt4o_mini_correctness = []

    for entry in data:
        num_functions = entry["Liczba funkcji "]
        functions.append(num_functions)
        chatgpt35Turbo_correctness.append(1 if entry["Chat GPT 3.5-Turbo correctness"] else 0)
        llama_correctness.append(1 if entry["Llama 3.1-70B Ins correctness"] else 0)
        chatgpt4o_correctness.append(1 if entry["Chat GPT 4o correctness"] else 0)
        chatgpt4o_mini_correctness.append(1 if entry["Chat GPT 4o mini correctness"] else 0)

    # Oblicz procentową poprawność dla każdej liczby funkcji
    unique_functions = sorted(set(functions))
    chatgpt35Turbo_percent = []
    llama_percent = []
    chatgpt4o_percent = []
    chatgpt4o_mini_percent = []

    for func_count in unique_functions:
        indices = [i for i, x in enumerate(functions) if x == func_count]
        chatgpt35Turbo_avg = sum([chatgpt35Turbo_correctness[i] for i in indices]) / len(indices) * 100
        llama_avg = sum([llama_correctness[i] for i in indices]) / len(indices) * 100
        chatgpt4o_avg = sum([chatgpt4o_correctness[i] for i in indices]) / len(indices) * 100
        chatgpt4o_mini_avg = sum([chatgpt4o_mini_correctness[i] for i in indices]) / len(indices) * 100
        chatgpt35Turbo_percent.append(chatgpt35Turbo_avg)
        llama_percent.append(llama_avg)
        chatgpt4o_percent.append(chatgpt4o_avg)
        chatgpt4o_mini_percent.append(chatgpt4o_mini_avg)

    return unique_functions, chatgpt35Turbo_percent, llama_percent, chatgpt4o_percent, chatgpt4o_mini_percent

def plot_data(unique_functions, chatgpt35Turbo_percent, llama_percent, chatgpt4o_percent, chatgpt4o_mini_percent):
    # Wykres
    plt.figure(figsize=(10, 6))

    plt.plot(unique_functions, chatgpt35Turbo_percent, marker='o', label="Chat GPT 3.5-Turbo Correctness (%)")
    plt.plot(unique_functions, llama_percent, marker='s', label="Llama 3.1-70B Ins Correctness (%)")
    plt.plot(unique_functions, chatgpt4o_percent, marker='o', label="Chat GPT 4o Correctness (%)")
    plt.plot(unique_functions, chatgpt4o_mini_percent, marker='o', label="Chat GPT 4o mini Correctness (%)")

    plt.title("Percentage Correctness vs. Number of Functions")
    plt.xlabel("Number of Functions")
    plt.ylabel("Correctness (%)")
    plt.legend()
    plt.grid(True)

    # Wyświetl wykres
    plt.show()

if __name__ == "__main__":
    try:
        # Załaduj dane
        data = load_data(file_path)

        # Przetwórz dane
        unique_functions, chatgpt35Turbo_percent, llama_percent, chat4o_percent, chat4o_mini_percent = process_data(data)

        # Generuj wykres
        plot_data(unique_functions, chatgpt35Turbo_percent, llama_percent, chat4o_percent, chat4o_mini_percent)

    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony. Upewnij się, że plik znajduje się w tym samym katalogu co ten program.")
    except json.JSONDecodeError:
        print("Nie udało się wczytać danych z pliku. Upewnij się, że plik jest w poprawnym formacie JSON.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
