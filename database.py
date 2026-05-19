import json

def load_data():
    try:
        with open("Library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": [], "members": []}

def save_data(data):
    with open("Library.json", "w") as file:
        json.dump(data, file, indent=4)