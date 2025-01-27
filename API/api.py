import json

def create_schedules(desired_classes, number_of_years):
    schedules = []
        courses = get_courses(desired_classes)
        for _ in range(number_of_years):
            schedule = []
    return schedules

def convert_to_json(schedules):
    return json.dumps(course.to_dict() for course in schedules)