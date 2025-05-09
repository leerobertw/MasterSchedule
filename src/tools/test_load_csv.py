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

    def test_build_courses1(self):
        department = Department("Fine arts")
        teacher = "GIBBY"
        room = 308
        data = ",,,,COMMERCIAL PHOTO 2,YEARBOOK*,COMMERCIAL PHOTO 1,COMMERCIAL PHOTO 1".split(',')
        semester = 2
        classes = build_courses(department, teacher, room, 2, data)
        self.assertEqual(len(classes), 8)
        class5 = classes[4]
        self.assertEqual(class5.name, 'COMMERCIAL PHOTO 2')
        self.assertEqual(class5.teacher, teacher)
        self.assertEqual(class5.room, room)
        self.assertEqual(class5.department, department)
        self.assertEqual(class5.period, 'B5')

    def test_build_courses2(self):
        department = Department("World Languages")
        teacher = "TERRY"
        room = 911
        data = "PREP,ASL 3 & ASL 4* - CONCURRENT ENROLLMENT,ASL 2*,ASL 2*,ASL 1*,ASL 1*,ASL 1*,ASL 1*".split(',')
        semester = "Full year"
        classes = build_courses(department, teacher, room, "Full year", data)
        class2 = classes[1]
        self.assertEqual(class2.name, "ASL 3 & ASL 4* - CONCURRENT ENROLLMENT")
        self.assertEqual(class2.teacher, teacher)
        self.assertEqual(class2.room, room)
        self.assertEqual(class2.department, department)
        self.assertEqual(class2.period, "A2")

    def test_build_courses3(self):
        department = Department("CTE")
        teacher = "LEE"
        room = 140
        data = "COMPUTER PROGRAMMING 1&2* - CONCURRENT ENROLLMENT,PREP,COMPUTER PROGRAMMING 1&2* - CONCURRENT ENROLLMENT,AP COMPUTER PROGRAMMING A*,PREP,WEB DEVELOPMENT 2 - CONCURRENT ENROLLMENT,ADVANCED COMPUTER PROGRAMMING - CONCURRENT ENROLLMENT,REMOTE INFO. TECH. CLASSES -- Click here for titles and details".split(',')
        semester = 2
        classes = build_courses(department, teacher, room, 2, data)
        class6 = classes[5]
        self.assertEqual(class6.name, "WEB DEVELOPMENT 2 - CONCURRENT ENROLLMENT")
        self.assertEqual(class6.teacher, teacher)
        self.assertEqual(class6.room, room)
        self.assertEqual(class6.department, department)
        self.assertEqual(class6.period, "B6")

    def test_build_courses4(self):
        department = Department("General Credit & Financial Literacy Classes")
        teacher = "NEW TEACHER (Ingle)^"
        room = 230
        data = "PREP,STUDY HALL,STUDY HALL,COLLEGE/AP ACADEMIC STUDY HALL,INTRO TO BASKETBALL,HEALTH,HEALTH,BOYS BASKETBALL TEAM".split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        class8 = classes[7]
        self.assertEqual(class8.name, "BOYS BASKETBALL TEAM")
        self.assertEqual(class8.teacher, teacher)
        self.assertEqual(class8.room, room)
        self.assertEqual(class8.department, department)
        self.assertEqual(class8.period, "B8")

    def test_build_courses5(self):
        department = Department("Math")
        teacher = "DAY^"
        room = 802
        data = "ACCOUNTING 1,ACCOUNTING 2,PREP,MARKETING,BUSINESS MANAGEMENT - CONCURRENT ENROLLMENT,BUSINESS MANAGEMENT - CONCURRENT ENROLLMENT,ENTREPRENEUERSHIP,ENTREPRENEUERSHIP".split(',')
        semester = 2
        classes = build_courses(department, teacher, room, 2, data)
        class4 = classes[3]
        self.assertEqual(class4.name, "MARKETING")
        self.assertEqual(class4.teacher, teacher)
        self.assertEqual(class4.room, room)
        self.assertEqual(class4.department, department)
        self.assertEqual(class4.period, "A4")

    def test_build_courses6(self):
        department = Department("PE_Health")
        teacher = "MURPHY^"
        room = "Maroon Gym",
        data = "CHEVALIERS-DRILL TEAM*,,,,,,,".split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        class1 = classes[0]
        self.assertEqual(class1.name, "CHEVALIERS-DRILL TEAM*")
        self.assertEqual(class1.teacher, teacher)
        self.assertEqual(class1.room, room)
        self.assertEqual(class1.department, department)
        self.assertEqual(class1.period, "A1")

    def test_build_courses7(self):
        department = Department("Science")
        teacher = "NAIR"
        room = 226
        data = "PHYSICS*,PHYSICS*,PHYSICS*,PHYSICS*,PHYSICS*,PREP,AP PHYSICS C*,PHYSICS*".split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        class7 = classes[6]
        self.assertEqual(class7.name, "AP PHYSICS C*")
        self.assertEqual(class7.teacher, teacher)
        self.assertEqual(class7.room, room)
        self.assertEqual(class7.department, department)
        self.assertEqual(class7.period, "B7")

    def test_build_courses8(self):
        department = Department("Social Studies")
        teacher = "GUNNARSON"
        room = 135
        data = "PREP,ANCIENT WORLD HISTORY,ANCIENT WORLD HISTORY,US HISTORY*,PREP,US HISTORY*,US HISTORY*,US HISTORY*".split(',')
        semester = 1
        classes = build_courses(department, teacher, room, 1, data)
        class4 = classes[3]
        self.assertEqual(class4.name, "US HISTORY*")
        self.assertEqual(class4.teacher, teacher)
        self.assertEqual(class4.room, room)
        self.assertEqual(class4.department, department)
        self.assertEqual(class4.period, "A4")

    def test_build_courses9(self):
        department = Department("Special Education")
        teacher = "IKA^^"
        room = "rm 122/808"
        data = "ENGLISH 12*,ENGLISH 11*,ENGLISH 12*,GIRLS BASKETBALL TEAM,PREP,ENGLISH 11*,ENGLISH 11*,PEOPLE OF THE PACIFIC".split(',')
        semester = 2
        classes = build_courses(department, teacher, room, 2, data)
        class8 = classes[7]
        self.assertEqual(class8.name, "PEOPLE OF THE PACIFIC")
        self.assertEqual(class8.teacher, teacher)
        self.assertEqual(class8.room, room)
        self.assertEqual(class8.department, department)
        self.assertEqual(class8.period, "B8")





