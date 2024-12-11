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

def plot_data(grouped_data, models, x_label, title, ax):
    """Plot the data."""
    for model in models:
        if model in grouped_data.columns:
            ax.plot(grouped_data.index, grouped_data[model], label=model, marker='o')

    ax.set_xlabel(x_label)
    ax.set_ylabel("Percentage of Correct Answers (%)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

def main():
    # Load data
    operations_file = "measurements_frankenstein_operations.json"
    data_file = "measurements_frankenstein_data.json"

    operations_data = load_json(operations_file)
    data_data = load_json(data_file)

    # Process data
    grouped_operations, models_operations = process_data(operations_data, "Liczba operacji")
    grouped_data, models_data = process_data(data_data, "Liczba danych")

    # Create subplots for both plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Plot data
    plot_data(grouped_operations, models_operations, "Liczba operacji", "Model Accuracy vs Liczba operacji", axes[0])
    plot_data(grouped_data, models_data, "Liczba danych", "Model Accuracy vs Liczba danych", axes[1])

    # Show plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
