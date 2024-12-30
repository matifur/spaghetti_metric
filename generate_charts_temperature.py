"""
Filename: generate_charts_temperature.py
Description: Program analizujący wpływ temperatury na poprawność modelu Chat GPT-4o dla różnych programów. Generuje wykres przedstawiający zależność poprawności od temperatury.
Author: Mateusz Furgała
Date: 2024-12-30

Usage:
    python generate_charts_temperature.py

Requirements:
    - Python 3.12+
    - json
    - matplotlib
    - os
    - collections (defaultdict)

License:
    All Rights Reserved - This code is the intellectual property of Mateusz Furgała.
"""


import json
import matplotlib.pyplot as plt
import os
from collections import defaultdict

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_percentage(data):
    # Group data by "Numer programu" and "Temperatura"
    grouped_data = defaultdict(lambda: defaultdict(list))
    for record in data:
        program_number = record["Numer programu"]
        temperature = record["Temperatura"]
        correctness = record["Chat GPT 4o correctness"]
        grouped_data[program_number][temperature].append(correctness)

    # Calculate percentages
    percentage_data = {}
    for program_number, temperature_data in grouped_data.items():
        percentage_data[program_number] = {}
        for temperature, correctness_list in temperature_data.items():
            correct_count = sum(correctness_list)
            total_count = len(correctness_list)
            percentage = (correct_count / total_count) * 100
            percentage_data[program_number][temperature] = percentage

    return percentage_data

def create_chart(percentage_data):
    # Prepare data for plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    for program_number, temperature_data in percentage_data.items():
        temperatures = sorted(temperature_data.keys())
        percentages = [temperature_data[temp] for temp in temperatures]

        # Plot the data
        ax.plot(temperatures, percentages, marker='o', label=f"Program {program_number}")

    ax.set_title("Poprawność modeli [%] vs. Temperatura")
    ax.set_xlabel("Temperatura")
    ax.set_ylabel("Poprawność modeli [%]")
    ax.set_xticks(sorted({temp for data in percentage_data.values() for temp in data.keys()}))
    ax.set_yticks(range(0, 101, 10))  # Y-axis from 0% to 100%
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend(title="Programy")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "measurements_temperature.json"

    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
    else:
        data = load_data(file_path)
        percentage_data = calculate_percentage(data)
        create_chart(percentage_data)
