import json
json_string = """
{"location": "moondalup", "name": "Greatest Carpark in Moondalup", 
"total_bays": 200, "occupied": 42, "is_awesome": true}"""



class Config:
    def __init__(self, file_name):
        self.config = {} # ... build dictionary from json file
