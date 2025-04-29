import json

with open("./src/data/classesout.json", "r") as file:
    x = json.load(file)
    x = x["classes"]
teachers = sorted(list(set([y[2] for y in x if y[2] is not None])))
print(sorted(teachers))