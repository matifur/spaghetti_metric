import json
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_charts(data):
    # Group data by "Numer programu"
    grouped_data = {}
    for record in data:
        program_number = record["Numer programu"]
        if program_number not in grouped_data:
            grouped_data[program_number] = []
        grouped_data[program_number].append(record)

    # Create a chart for each program number
    fig, axes = plt.subplots(len(grouped_data), 1, figsize=(8, 1.5 * len(grouped_data)))
    if len(grouped_data) == 1:
        axes = [axes]  # Ensure axes is iterable when there's only one subplot

    for ax, (program_number, records) in zip(axes, grouped_data.items()):
        temperatures = [record["Temperatura"] for record in records]
        correctness_values = [record["Chat GPT 4o correctness"] for record in records]

        # Convert True/False to 1/0 for bar heights
        bar_heights = [1 if value else 0 for value in correctness_values]

        # Plot the data
        ax.bar(temperatures, bar_heights, color='blue', width=0.1, edgecolor='black')
        ax.set_title(f"Program {program_number} - Correctness by Temperature")
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Correctness (1=True, 0=False)")
        ax.set_xticks(temperatures)
        ax.set_yticks([0, 1])
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "measurements_temperature.json"

    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
    else:
        data = load_data(file_path)
        create_charts(data)
