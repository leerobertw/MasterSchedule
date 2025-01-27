class Course:
    def __init__(self, name, instructor, period):
        self.name = name
        self.instructor = instructor
        self.period = period

class Schedule:
    def __init__(self, courses):
        self.courses = courses
