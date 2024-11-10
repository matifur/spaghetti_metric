from generator_math import generate_math_1, program_functions_math
from saving_output import save_to_json, compile_and_save_to_json
import random

# Wywołujemy funkcję z wartością zmiennych oraz funkcjami które chcemy zawrzeć
# Main
variable_1_rand = random.randrange(1, 100, 1)
variable_2_rand = random.randrange(1, 100, 1)
select_function_rand = []
for i in range(1, 5):
    select_function_rand.append(random.randrange(1, len(program_functions_math), 1))
print(len(program_functions_math))

# Wykaz podanych wartości
print(f"variable_1_rand = {variable_1_rand}, variable_2_rand = {variable_2_rand}, select_function_rand = {select_function_rand}")
generate_math_1(variable_1_rand, variable_2_rand, select_function_rand)  # functions randomizer, optional variable

print("==============================================================================")
print("Running program and collecting output from LLM-s")
print("==============================================================================")
compile_and_save_to_json()
print("==============================================================================")
print("Process Completed!")
print("==============================================================================")