import json
from master_schedule import MasterSchedule

def create_schedules(desired_classes, number_of_years):
    schedules = []
    courses = MasterSchedule.get_courses(desired_classes)
    schedule = [courses[desired] for desired in desired_classes]
    schedules.append(schedule)
    return schedules

def convert_to_json(schedules):
    return [json.dumps(course.to_dict()) for course in schedules]