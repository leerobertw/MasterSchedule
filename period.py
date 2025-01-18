class Period:
    def __init__(self, name, teacher, period, semester, classification, hclass):
        self.name = name
        self.teacher = teacher
        self.period = period
        self.semester = semester
        self.classification = classification
        self.hclass = hclass
    def __str__(self):
        return f"{self.name} | {self.teacher} | {self.period} | {self.semester} | {self.classification} | {self.hclass}"