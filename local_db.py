import json

data = []

with open("test.json", "r") as read_file:
    data = json.load(read_file);

print(data)
