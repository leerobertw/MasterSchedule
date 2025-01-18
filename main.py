from course import Course
from teacher import Teacher
from period import Period
import csv, math, os, pathlib
inputfiles = [os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs"), d) for d in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs"))]
rows = []
courses = []
teachers = []
periods = []
for inputfile in inputfiles:
    with open(inputfile, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

"""
0: Teacher name
1: Semester number
2-whatever: Course name
If item 2 is the first period then the period for each item is its list position-1
"""

for row in rows:
    tempperiods = []
    tempcourses = []
    for i in range(2, len(row)):
        period = Period(row[i], row[0], i-1, row[1], "classification", "hclass")
        tempperiods.append(period)
        periods.append(period)
    teacher = Teacher(row[0], "courses", tempperiods)
    teachers.append(teacher)