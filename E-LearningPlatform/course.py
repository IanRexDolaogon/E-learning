from databaseConnection import DataBaseConnection  

class Course:
    def __init__(self, course_id: int, course_title: str, course_details: str, instructor_id: int, connection=None):
        self._course_id = course_id
        self._course_title = course_title
        self._course_details = course_details
        self._instructor_id = instructor_id
        self.connection = connection or DataBaseConnection()  

    def get_course_info(self):
        return {
            "course_id": self._course_id,
            "course_title": self._course_title,
            "course_details": self._course_details,
            "instructor_id": self._instructor_id
        }

    def view_courses(self):
        # View all courses in the Courses table
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Courses")  
            courses = cursor.fetchall()
            if courses:
                for course in courses:
                    print(course)  
            else:
                print("No courses available.")
        except Exception as e:
            print(f"Error viewing courses: {e}")  
        finally:
            cursor.close()  

    def create_course(self):
        try:
            title = input("Enter course title: ")
            details = input("Enter course details: ")
            instructor_id = int(input("Enter instructor_id: "))
        except ValueError:
            print("Invalid input. Please ensure the instructor ID is a number.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Courses (course_title, course_details, instructor_id) VALUES(?, ?, ?)",
                           (title, details, instructor_id))
            self.connection.commit() 
            print("Course created successfully.")  
        except Exception as e:
            print(f"Error creating course: {e}")  
            self.connection.rollback()  
        finally:
            cursor.close()  

    def view_students_in_course(self):
        try:
            course_id = int(input("Enter the course ID to view students enrolled in: "))
        except ValueError:
            print("Invalid input. Please enter a valid course ID.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT s.student_id, s.student_name, s.student_email
                FROM Students s
                JOIN Enrollment e ON s.student_id = e.student_id
                WHERE e.course_id = ?
                """, (course_id,))

            students = cursor.fetchall()

            if not students:
                print(f"No students are enrolled in the course with ID {course_id}.")
            else:
                print(f"Students enrolled in Course ID {course_id}:")
                for student in students:
                    student_id, student_name, student_email = student
                    print(f"\nStudent ID: {student_id}")
                    print(f"Name: {student_name}")
                    print(f"Email: {student_email}")

        except Exception as e:
            print(f"Error retrieving students enrolled in the course: {e}")
        finally:
            cursor.close()
