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

    def test_build_courses_one(self):
        department = Department("Social Studies")
        teacher = "ELMER"
        room = 700
        data = 'PREP,SPORTS PSYCHOLOGY,PSYCHOLOGY,PSYCHOLOGY,POSITIVE PSYCHOLOGY,SPORTS PSYCHOLOGY,POSITIVE PSYCHOLOGY,POSITIVE PSYCHOLOGY'.split(',')
        semester = 2
        classes = build_courses(department, teacher, room, 2, data)
        class1 = classes[0]
        self.assertEqual(class1.name, 'PREP')
        self.assertEqual(class1.teacher, teacher)
        self.assertEqual(class1.room, room)
        self.assertEqual(class1.department, department)
        self.assertEqual(class1.period, 'A1')

    def test_build_courses_two(self):
        department = Department("Fine Arts")
        teacher = "POWELL"
        room = 102
        data = "ADVANCED WOMEN'S ENSEMBLE*,ACAPELLA CHOIR*,AP MUSIC THEORY*,MUSICAL THEATER,ADVANCED MEN'S ENSEMBLE*,CHAMBER CHOIR*,PREP,PRODUCTIONS COMPANY*".split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        class3 = classes[2]
        self.assertEqual(class3.name, 'AP MUSIC THEORY*')
        self.assertEqual(class3.teacher, teacher)
        self.assertEqual(class3.room, room)
        self.assertEqual(class3.department, department)
        self.assertEqual(class3.period, 'A3')

    def test_build_courses_three(self):
        department = Department("PE_Health")
        teacher = "ASAY"
        room = "Main Gym/109"
        data = "HIGH FIT/ZUMBA,LIFETIME ACTIVITY,LIFETIME ACTIVITY,,,LIFETIME ACTIVITY,LIFETIME ACTIVITY,".split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        class6 = classes[5]
        self.assertEqual(class6.name, 'LIFETIME ACTIVITY')
        self.assertEqual(class6.teacher, teacher)
        self.assertEqual(class6.room, room)
        self.assertEqual(class6.department, department)
        self.assertEqual(class6.period, 'B6')