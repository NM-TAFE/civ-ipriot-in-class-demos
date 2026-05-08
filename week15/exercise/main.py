import json

from conference import Conference
from hackathon import Hackathon

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

fixtures = read_file('fixture.json')
print(type(fixtures))

def make_meetings(kind, fixture):
    if kind == 'conference':
        return Conference.load(fixture)
    elif kind == 'hackathon':
        return Hackathon.load(fixture)
    else:
        print("rargh! unknown kind")

meetings = []
for fixture in fixtures:
    kind = fixture.get('kind')
    meetings.append(make_meetings(kind, fixture))

for meeting in meetings:
    print(str(meeting))
