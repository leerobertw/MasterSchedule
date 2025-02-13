import csv

print("CTE information")
with open('CTE_classes.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("English information")
with open('English_classes.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("Financial Literacy & General Credit classes")
with open("Finance_general_classes.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("Fine Arts information")
with open('Fine_Arts.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("Math information")
with open('Math_classes.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("PE/Health information")
with open('PE_health.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("Science information")
with open('Science_classes.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("Social Studies information")
with open('Social_studies.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("Special Education information")
with open('Special_education.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--------------------------------------------------------------------------------------------")
print("World Language information")
with open('World_languages.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)