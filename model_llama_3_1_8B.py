import os
from groq import Groq
def llama_3_1_8B_code_interpretation():

    client = Groq(
        # This is the default and can be omitted
        api_key=os.environ.get("API_KEY_GROQ"),
    )

    try:
        with open("generated_program.py", "r") as file:
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
