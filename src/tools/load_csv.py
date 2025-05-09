import csv
import os

def load_csv(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        department = next(csv_reader)
        year = next(csv_reader)
        next(csv_reader)  # Instructions
        next(csv_reader)  # Header
        return department[0], year[0].split()[0], [row for row in csv_reader]

class Teacher:
    def __init__(self, name, room):
        self.name = name
        self.room = room

class Course:
    def __init__(self, name, teacher, room, department, period, semester):
        self.name = name
        self.teacher = teacher
        self.room = room
        self.department = department
        self.period = period
        self.semester = semester

class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.courses = []

def build_courses(department, teacher, room, semester, row):
    courses = []
    for i, course_name in enumerate(row):
        new_course = Course(course_name, teacher, room, department, ('A' if i+1 < 5 else 'B') + str(i+1),  semester)
        courses.append(new_course)
    return courses

def build_classes_and_teachers(rows, teachers, courses, department):
    for i in range(0, len(rows)-1, 2):
        teacher_name = rows[i][0]
        room = rows[i+1][0]
        if teacher_name not in teachers:
            teacher = Teacher(teacher_name, room)
        else:
            teacher = teachers[teacher_name]
        semester1 = build_courses(department, teacher, room, '1', rows[i][2:])
        semester2 = build_courses(department, teacher, room, '2', rows[i+1][2:])
        courses.extend(semester1)
        courses.extend(semester2)

def resolve_semesters(course_list):
    courses = {}
    for course in course_list.copy():
        course_key = f"{course.teacher.name}-{course.period}"
        if course_key not in courses:
            courses[course_key] = course
        else:
            if not course.name:
                courses[course_key].semester = "full year"
            else:
                courses[course_key].semester = "1, 2"
            course_list.remove(course)

def load_csv_files(directory):
    teachers = {}
    departments = {}
    courses = []
    for csv_file in os.listdir(directory):
        if csv_file.endswith(".csv"):
            department_name, year, rows = load_csv(directory + '/' + csv_file)
            department = Department(department_name)
            departments[department_name] = department
            build_classes_and_teachers(rows, teachers, courses, department)
            resolve_semesters(courses)
    return teachers, departments, courses



