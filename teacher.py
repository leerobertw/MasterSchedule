class Teacher:
    def __init__(self, name, courses, periods):
        self.name = name
        self.courses = courses
        self.periods = periods
    def __str__(self):
        return f"{self.name} | {self.courses} | {self.periods}"