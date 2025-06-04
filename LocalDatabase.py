import sqlite3
import os
import cv2  # Add this import for image handling
from datetime import datetime


class LocalDatabase:
    def __init__(self):
        self.db_name = "attendance_system.db"
        self.images_dir = "LocalImages"
        self._initialize_database()

    def _initialize_database(self):
        # Create database and tables if they don't exist
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # Students table
        c.execute('''CREATE TABLE IF NOT EXISTS Students
                     (
                         id TEXT PRIMARY KEY,
                         name TEXT,
                         Course TEXT,
                         Dept TEXT,
                         starting_year INTEGER,
                         total_attendance INTEGER,
                         Roll INTEGER,
                         year TEXT,
                         last_attendance_time TEXT)''')

        # Create images directory if it doesn't exist
        if not os.path.exists(self.images_dir):
            os.makedirs(self.images_dir)

        conn.commit()
        conn.close()

    def add_student(self, student_data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute('''INSERT OR REPLACE INTO Students VALUES 
                     (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (student_data['id'],
                   student_data['name'],
                   student_data['Course'],
                   student_data['Dept'],
                   student_data['starting_year'],
                   student_data['total_attendance'],
                   student_data['Roll'],
                   student_data['year'],
                   student_data['last_attendance_time']))

        conn.commit()
        conn.close()

    def get_student(self, student_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute("SELECT * FROM Students WHERE id=?", (student_id,))
        result = c.fetchone()
        conn.close()

        if result:
            return {
                'id': result[0],
                'name': result[1],
                'Course': result[2],
                'Dept': result[3],
                'starting_year': result[4],
                'total_attendance': result[5],
                'Roll': result[6],
                'year': result[7],
                'last_attendance_time': result[8]
            }
        return None

    def update_attendance(self, student_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # Get current values
        student = self.get_student(student_id)
        if not student:
            return False

        # Update attendance
        new_attendance = student['total_attendance'] + 1
        new_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        c.execute('''UPDATE Students
                     SET total_attendance=?,
                         last_attendance_time=?
                     WHERE id = ?''',
                  (new_attendance, new_time, student_id))

        conn.commit()
        conn.close()
        return True

    def save_image(self, student_id, image_data):
        image_path = os.path.join(self.images_dir, f"{student_id}.png")
        cv2.imwrite(image_path, image_data)

    def get_image(self, student_id):
        image_path = os.path.join(self.images_dir, f"{student_id}.png")
        if os.path.exists(image_path):
            return cv2.imread(image_path)
        return None


# This part is only for testing the class directly
# if __name__ == "__main__":
#     print("This is the LocalDatabase class definition.")
#     print("To test it, create a separate test script that imports this module.")