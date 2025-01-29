from course import Course, Period as p, CourseSemester as cs

class MasterSchedule:
    courses = {
        "Sports Medicine": Course("Sports Medicine", "Bryan", [p.A2, p.A3], cs.full_year),
        "Culinary Basics": Course("Culinary Basics", "Cox", [p.A1, p.A3, p.A4], cs.both),
        "Advanced Culinary": Course("Advanced Culinary", "Cox", [p.B6, p.B7], cs.full_year),
        "Advanced Programming": Course("Advanced Programming", "Lee", [p.B7], cs.full_year),
        "Engineering Principles 1": Course("Engineering Principles 1", "Smith", [p.A1, p.A3], cs.both),
        "AP Calculus AB": Course("AP Calculus AB", "Smith", [p.B5, p.B6], cs.full_year),
        "AP Psychology": Course("AP Psychology", "Kim", [p.B8], cs.full_year)
    }

    @classmethod
    def get_courses(cls, desired):
        return [cls.courses[d] for d in desired]


