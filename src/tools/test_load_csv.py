from unittest import TestCase
from load_csv import *

class Test(TestCase):
    def test_build_courses(self):
        department = Department("English")
        teacher = "CARPENTER"
        room = 614
        data = 'ENGLISH 10*,PREP,ACCELERATED READING,ENGLISH 10*,ENGLISH 10*,PREP,ENGLISH 10*,JOURNALISM*'.split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        self.assertEqual(len(classes), 8)
        class1 = classes[0]
        self.assertEqual(class1.name, 'ENGLISH 10*')
        self.assertEqual(class1.teacher, teacher)
        self.assertEqual(class1.room, room)
        self.assertEqual(class1.department, department)
        self.assertEqual(class1.period, 'A1')