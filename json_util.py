# json_util.py
# Utility module to provide abstractions for reading/writing json data

import json

def set_json(path: str, data):
    """Creates or overwrites the .json file path specified."""
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def get_json(path: str):
    """Returns the result of json.load() from the specified .json file."""
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
def set_value(path: str, key: str, value):
    """Sets a value within the specified .json file."""
    new = get_json(path)
    if new == None:
        return
        
    new[key] = value
    set_json(path, new)

def get_value(path: str, keys: [str]):
    """Safely retrieves a value from the specified .json file. Creates the .json if not found."""
    data = get_json(path)
    if data == None:
        set_json(path, {})
        return None

    current = data
    for key in keys:
        try:
            if current[key] != None:
                current = current[key]
            else:
                break
        except KeyError:
            print("key error ahh")
    return current


if __name__ == "__main__":
    print(get_value("bleh.json", ["fortnite"]))