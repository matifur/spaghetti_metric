import os
from huggingface_hub import login
from huggingface_hub import InferenceClient

# Funkcja odpowiadająca za przekazanie programu do modelu i odeberanie wyjścia tego programu
def llama_3_1_70B_Ins_code_interpretation():
    # Wprowadź swój klucz API
    api_key_hf = os.getenv("API_KEY_HF")
    login(api_key_hf)

    client = InferenceClient(model="meta-llama/Llama-3.1-70B-Instruct")

    try:
        with open("generated_program.py", "r") as file:
            program_code = file.read()
    except FileNotFoundError:
        print("Plik generated_program.py nie został znaleziony.")
        return

    prompt = """Tell me what will be terminal output of this program? Print only terminal output, no commentary. 
Make sure that what you tell me is exactly what will be printed in terminal including text not only number.
Try to be as precise in your calculations as possible.\n\n"""
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
#print(llama_3_1_70B_Ins_code_interpretation())
