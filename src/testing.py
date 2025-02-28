import json

with open("./src/data/classesout.json", "r") as file:
    x = json.load(file)
    x = x["classes"]
teachers = {}
for y in x:
    if y[0].lower() == "prep":
        if y[2] not in teachers:
            teachers[y[2]] = 1
        else:
            teachers[y[2]] += 1
for teacher in teachers:
    if teachers[teacher] > 1:
        print(f"{teacher}, {teachers[teacher]}")