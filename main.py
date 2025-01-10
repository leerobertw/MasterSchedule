from course import Course
from teacher import Teacher
from period import Period
import csv, math, os, pathlib

inputfiles = [os.path.join("./inputs", d) for d in os.listdir("./inputs")]
rows = []
for inputfile in inputfiles:
    with open(inputfile, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
print(rows)