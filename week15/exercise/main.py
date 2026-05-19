import json

# Look at this function -- it takes a file that it assumes is json and parses it
# Experiment with giving it files and see what it returns.
# Remember that you can run files in python 'interactively' with `python -i filename.py`
def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        try:
            return json.loads(file.read())
        except json.JSONDecodeError:
            print("JSONDecode error! Check your formatting")
            return []