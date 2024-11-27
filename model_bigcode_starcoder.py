import requests


def query_space(prompt):
    # Poprawny adres endpointu
    url = "https://matifur-llama-model-runner.hf.space/api/predict"

    # Zapytanie POST do endpointu
    response = requests.post(url, json={"data": [prompt]})

    if response.status_code == 200:
        return response.json()["data"][0]
    else:
        return f"Error: {response.status_code}, {response.text}"


if __name__ == "__main__":
    program_code = """
    print("Hello, World!")
    """
    output = query_space(f"Given the following Python program:\n{program_code}\n\nWhat will it output?")
    print(output)
