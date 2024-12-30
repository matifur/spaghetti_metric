"""
Filename: generate_charts_frankenstein.py
Description: Program analizujący poprawność wyników różnych modeli językowych w zależności od liczby operacji i danych w programach frankensteinowych. Generuje wykresy na podstawie zapisanych danych w plikach JSON.
Author: Mateusz Furgała
Date: 2024-12-30

Usage:
    python generate_charts_frankenstein.py

Requirements:
    - Python 3.12+
    - json
    - pandas
    - matplotlib

License:
    All Rights Reserved - This code is the intellectual property of Mateusz Furgała.
"""


import json
import pandas as pd
import matplotlib.pyplot as plt

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data(data, key_variable):
    """Process data to calculate the percentage of correct answers."""
    df = pd.DataFrame(data)
    models = [
        "Chat GPT 3.5-Turbo",
        "Llama 3.1-70B Ins",
        "Llama 3.1-8B",
        "Chat GPT 4o",
        "Chat GPT 4o mini",
    ]

    # Ensure the key variable is numeric if necessary
    if key_variable in df.columns:
        df[key_variable] = pd.to_numeric(df[key_variable], errors='coerce')

    # Extract correctness for each model and calculate percentage
    for model in models:
        correctness_column = f"{model} correctness"
        if correctness_column in df.columns:
            df[correctness_column] = df[correctness_column].astype(int, errors='ignore')
            df[model] = df[correctness_column]

    # Group by the key variable (e.g., Liczba operacji or Liczba danych)
    grouped = df.groupby(key_variable).mean(numeric_only=True)

    # Calculate percentage of correct answers
    for model in models:
        if model in grouped.columns:
            grouped[model] = grouped[model] * 100  # Convert to percentage

    return grouped, models

def plot_data(grouped_data, models, x_label, title):
    """Plot the data."""
    plt.figure(figsize=(8, 6))  # Create a new figure for each plot
    for model in models:
        if model in grouped_data.columns:
            plt.plot(grouped_data.index, grouped_data[model], label=model, marker='o')

    plt.xlabel(x_label)
    plt.ylabel("Poprawność modeli [%]")
    plt.title(title)
    plt.legend()
    plt.grid(True)

def main():
    # Load data
    operations_file = "measurements_frankenstein_operations.json"
    data_file = "measurements_frankenstein_data.json"

    operations_data = load_json(operations_file)
    data_data = load_json(data_file)

    # Process data
    grouped_operations, models_operations = process_data(operations_data, "Liczba operacji")
    grouped_data, models_data = process_data(data_data, "Liczba danych")

    # Plot data for operations
    plot_data(grouped_operations, models_operations, "Liczba operacji", "Poprawność modeli [%] vs. Liczba operacji")

    # Show first plot
    plt.show()

    # Plot data for data
    plot_data(grouped_data, models_data, "Liczba danych", "Poprawność modeli [%] vs. Liczba danych")

    # Show second plot
    plt.show()

if __name__ == "__main__":
    main()
