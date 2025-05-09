import json
from load_csv import *

def main():
    directory = "../data/2025-26"
    teachers, departments, courses = load_csv_files(directory)
    jcourses = [{'name': course.name, 'teacher': course.teacher.name, 'room': course.room, 'period': course.period,
                'semester': course.semester} for course in courses if course.name and course.name != 'PREP']
    json.dump(jcourses, open(directory + '/' + "courses.json", "w"))


main()
