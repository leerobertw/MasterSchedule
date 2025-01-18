class Course:
    def __init__(self, name, teachers, periods, semester, classification, hclass):
        self.name = name
        self.teachers = teachers
        self.periods = periods
        self.semester = semester
        self.classification = classification
        self.hclass = hclass
    def __str__(self):
        return f"{self.name} | {self.teachers} | {self.periods} | {self.semester} | {self.classification} | {self.hclass}"