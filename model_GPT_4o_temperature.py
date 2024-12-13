import openai
import os

# Funkcja odpowiadająca za przekazanie programu do modelu i odeberanie wyjścia tego programu
def gpt_4o_code_interpretation_temp(filename = "frankenstein_program.py", temperature = 0.7):
    # Pobierz klucz API z zmiennej środowiskowej
    api_key = os.getenv("API_KEY_GPT")
    openai.api_key = api_key

    # Wczytaj kod z pliku generated_program.py, zachowując formatowanie
    try:
        with open(filename, "r") as file:
            program_code = file.read()
    except FileNotFoundError:
        print("Plik generated_program.py nie został znaleziony.")
        return

    # Tworzenie promptu
    prompt = """Tell me what will be terminal output of this program? Print only terminal output no comentary. Please do not include ``` characters in your output.\n\n"""
    prompt += program_code

    # Utworzenie zapytania do modelu GPT
    chat_log = [
        {"role": "user", "content": prompt}
    ]

    # Wywołanie modelu i pobranie odpowiedzi
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=chat_log,
        temperature=temperature
    )

    # Pobranie odpowiedzi od asystenta
    assistant_response = response.choices[0].message.content

    # Zwrot odpowiedzi, zachowując formatowanie
    return assistant_response.strip("\n").strip()


# Przykładowe wywołanie funkcji i wydrukowanie wyniku
#output = gpt_4o_code_interpretation_temp()
#if output:
#    print(output)
