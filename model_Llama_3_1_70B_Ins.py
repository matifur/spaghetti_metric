"""
Filename: model_llama_3_1_70B_Ins.py
Description: Program analizujący wyjście terminala dla kodu przekazanego do modelu Llama 3.1 70B Instruct.
Author: Mateusz Furgała
Date: 2024-12-30

Usage:
    part of the Spaghetti Metrics

Requirements:
    - Python 3.12+
    - huggingface_hub 0.26.2

License:
    All Rights Reserved - This code is the intellectual property of Mateusz Furgała.
"""


import os
from huggingface_hub import login
from huggingface_hub import InferenceClient

# Funkcja odpowiadająca za przekazanie programu do modelu i odeberanie wyjścia tego programu
def llama_3_1_70B_Ins_code_interpretation(filename = "generated_program.py"):
    # Wprowadź swój klucz API
    api_key_hf = os.getenv("API_KEY_HF")
    login(api_key_hf)

    client = InferenceClient(model="meta-llama/Llama-3.1-70B-Instruct")

    try:
        with open(filename, "r") as file:
            program_code = file.read()
    except FileNotFoundError:
        print("Plik generated_program.py nie został znaleziony.")
        return

    #prompt = """Tell me what will be terminal output of this program? Print only terminal output it should be a number, no commentary.
#Make sure that what you tell me is exactly what will be printed in terminal.
#Try to be as precise in your calculations as possible.\n\n"""
    prompt = " Please tell me what will be printed in my terminal by this program. Do not write comentary? \n\n"
    prompt += program_code

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3.1-70B-Instruct",
        messages=messages,
        max_tokens=500,
        stream=True
    )
    output = """"""
    for chunk in stream:
        #print(chunk.choices[0].delta.content, end="")
        output = output + chunk.choices[0].delta.content

    return output

#Przykładowe wywołanie funkcji
print(llama_3_1_70B_Ins_code_interpretation())
