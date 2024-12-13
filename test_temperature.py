# CO ZAIMPLEMENTOWAĆ
# Nie bawimy się tutaj w maina ani nic wszystko w tym jednym pliku

# 1) programów nie trzeba bo będziemy konkretny sobie brać
# 2) Programy wrzucamy do modelu 1 chyba gpt 4o
# 3) Zapisujemy wyniki w .json według schematu który jest gotowy
# 4) Rysujemy schemat po wykonaniu testów


# program_1.py -> Łatwy program (2 funkcja)
# program_2.py -> Trudny program (4 funkcje)
# program_3.py -> Średnio zaawansowany program frankenstein

from model_GPT_4o import gpt_4o_code_interpretation
from saving_output import compile_and_save_temperature


def run_generator_temperature(table_programs_gen, table_temperature_gen):
    index = 0
    for program in table_programs_gen:
        index += 1
        for temperature in table_temperature_gen:
            print("===================================================")
            print(f"Uruchamiam {program} z temperaturą {temperature}")
            print("===================================================")
            compile_and_save_temperature(index, temperature, program, "measurements_temperature.json")


# Main
table_temperature = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
table_programs = ["programs_temperature/program_1.py", "programs_temperature/program_2.py", "programs_temperature/program_3.py"]

run_generator_temperature(table_programs, table_temperature)


