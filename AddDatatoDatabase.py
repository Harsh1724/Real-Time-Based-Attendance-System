from LocalDatabase import LocalDatabase
from datetime import datetime

db = LocalDatabase()

data = {
    "321654": {
        "id": "321654",
        "name": "Emly Blunt",
        "Course": "B.Tech",
        "Dept": "Robotics",
        "starting_year": 2017,
        "total_attendance": 0,
        "Roll": 82,
        "year": "4th",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "852741": {
        "id": "852741",
        "name": "Abhishek",
        "Course": "B.Tech",
        "Dept": "ECE",
        "starting_year": 2021,
        "total_attendance": 0,
        "Roll": 82,
        "year": "1st",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "963852": {
        "id": "963852",
        "name": "Elon Musk",
        "Course": "B.Tech",
        "Dept": "CSE",
        "starting_year": 2022,
        "total_attendance": 0,
        "Roll": 19,
        "year": "2nd",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "863452": {
        "id": "863452",
        "name": "Harsh Kashyap",
        "Course": "B.Tech",
        "Dept": "AIML",
        "starting_year": 2021,
        "total_attendance": 0,
        "Roll": 20,
        "year": "4th",
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

for student_id, student_data in data.items():
    db.add_student(student_data)
    # If you have images to save:
    # db.save_image(student_id, image_data)

print("Data added to local database successfully.")