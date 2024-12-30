"""
Filename: model_llama_3_1_8B.py
Description: Program analizujący wyjście terminala dla kodu przekazanego do modelu Llama 3.1 8B.
Author: Mateusz Furgała
Date: 2024-12-30

Usage:
    part of the Spaghetti Metrics

Requirements:
    - Python 3.12+
    - groq 0.13.0

License:
    All Rights Reserved - This code is the intellectual property of Mateusz Furgała.
"""


import os
from groq import Groq
def llama_3_1_8B_code_interpretation(filename = "generated_program.py"):

    client = Groq(
        # This is the default and can be omitted
        api_key=os.environ.get("API_KEY_GROQ"),
    )

    try:
        with open(filename, "r") as file:
            program_code = file.read()
    except FileNotFoundError:
        print("Plik generated_program.py nie został znaleziony.")
        return

    prompt = """Tell me what will be terminal output of this program? Print only terminal output, no commentary. 
Make sure that what you tell me is exactly what will be printed in terminal.
Try to be as precise in your calculations as possible.\n\n"""
    prompt += program_code

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content


#Test wywołania funkcji
#print(llama_3_1_8B_code_interpretation())
