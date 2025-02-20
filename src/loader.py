import csv, os, json

def mergedict(a, b, ignores):
    for k in a.keys() & b.keys():
        if a[k][0]!=b[k][0] or a[k][1]!=b[k][1]:
            raise ValueError(f"Duplicate key found with different values: {k} {a[k]} {b[k]}")
    c = {**a, **b}
    for key in list(c.keys()):
        for ignore in ignores:
            if ignore.lower() in key.lower():
                del c[key]
    return c

def load_schedules():
    classes = {}
    for csv_file in os.listdir("./src/data"):
        if os.path.splitext(csv_file)[1] == ".csv":
            classes = mergedict(classes, load_schedule(csv_file), ["prep"])
    return classes
def load_schedule(csv_file):
    schedule = {}
    with open(f"./src/data/{csv_file}", 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for i in range(len(rows)):
        row = rows[i]
        if len(row) < 2 or row[1] != '1':
            continue
        teacher = row[0].strip()
        classes = [cls.strip() for cls in row[2:] if cls.strip()]
        for cls in classes:
            if cls not in schedule:
                schedule[f"{(cls, teacher)}"] = [teacher, 1, csv_file.split("/")[-1].split(".csv")[0]]
            else:
                schedule[f"{(cls, teacher)}"][1] += 1
    print(schedule)
    return schedule

with open("./src/data/classesin.json", "w") as jsonfile:
    json.dump(load_schedules(), jsonfile)