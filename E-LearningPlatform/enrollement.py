from databaseConnection import DataBaseConnection  

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date, connection=None):
        self._enrollment_id = enrollment_id
        self._student_id = student_id  
        self._course_id = course_id
        self._enrollment_date = enrollment_date
        self.connection = connection or DataBaseConnection()  

    def enroll_in_course(self):
        try:
            course_id = int(input("Enter course_id to enroll: "))
        except ValueError:
            print("Invalid course_id. Please enter a valid integer.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Enrollment (student_id, course_id) VALUES(?, ?)", (self._student_id, course_id))
            self.connection.commit()  
            print(f"Successfully enrolled in course {course_id}")  
        except Exception as e:
            print(f"Error enrolling in course: {e}") 
            self.connection.rollback()  
        finally:
            cursor.close() 

    def view_enrollments(self):
        try:
            student_id = int(input("Enter student_id to view enrollments: "))
        except ValueError:
            print("Invalid student_id. Please enter a valid integer.")
            return

        try:
            cursor = self.connection.cursor()  
            cursor.execute("""
                SELECT c.course_id, c.course_title, c.course_details 
                FROM Courses c
                JOIN Enrollment e ON c.course_id = e.course_id
                WHERE e.student_id = ?
            """, (student_id,))  
            enrollments = cursor.fetchall() 
            
            if enrollments:
                print(f"Enrollments for Student ID: {student_id}")
                for enrollment in enrollments:
                    print(f"Course ID: {enrollment[0]}")  
                    print(f"Course Title: {enrollment[1]}")  
                    print(f"Course Details: {enrollment[2]}")  
                    print("---")
            else:
                print(f"No courses found for Student ID: {student_id}.")  
        except Exception as e:
            print(f"Error fetching enrollments: {e}")  
        finally:
            cursor.close()  
