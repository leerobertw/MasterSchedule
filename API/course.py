from enum import Enum, auto

class CourseSemester(Enum):
    first_semester = auto()
    second_semester = auto()
    both = auto()
    full_year = auto()

class Period(Enum):
    A1 = auto()
    A2 = auto()
    A3 = auto()
    A4 = auto()
    B5 = auto()
    B6 = auto()
    B7 = auto()
    B8 = auto()

class Course:
    def __init__(self, name: str, instructor: str, periods: list[Period], semesters: CourseSemester):
        self.name = name
        self.instructor = instructor
        self.period = periods
        self.semesters = semesters

class Schedule:
    def __init__(self, courses):
        self.courses = courses
