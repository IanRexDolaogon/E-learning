from databaseConnection import DataBaseConnection  

class PlatformAdmin:
    def __init__(self, admin_id, admin_name, admin_password,  admin_email, admin_phone, admin_address, connection=None):
        self._admin_id = admin_id
        self._admin_name = admin_name
        self._admin_password = admin_password
        self._admin_email = admin_email
        self._admin_phone = admin_phone
        self._admin_address = admin_address
        self.connection = connection or DataBaseConnection()
        
    def get_admin_id(self):
        return self._admin_id
    
    def get_admin_name(self):
        return self._admin_name
    
    def get_admin_password(self):
        return self._admin_password
    
    def get_admin_email(self):
        return self._admin_email
    
    def get_admin_address(self):
        return self._admin_address
    
    def get_admin_phone(self):
        return self._admin_phone    
    
    def delete_course(self):
        # Delete a course by course ID
        try:
            course_id = int(input("Enter course_id to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid course ID.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Courses WHERE course_id = ?", (course_id,))
            self.connection.commit()  
            print(f"Course with ID {course_id} has been deleted.")  
        except Exception as e:
            print(f"Error in deleting course: {e}")  
            self.connection.rollback()  
        finally:
            cursor.close()
            
    def add_course_schedule(self):
        try:
            course_id = int(input("Enter the course ID to add a schedule: "))  
            schedule_day = input("Enter the day of the schedule: ")  
            schedule_time = input("Enter the time of the schedule (e.g., 10:00 AM): ")  
            schedule_type = input("Enter the type of the schedule: ")  
        except ValueError:
            print("Invalid input. Please enter valid data.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Schedule (course_id, schedule_day, schedule_time, schedule_type) 
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (course_id, schedule_day, schedule_time, schedule_type))
            self.connection.commit()
            print(f"Schedule added for Course ID: {course_id} on {schedule_day} at {schedule_time}.")
        except Exception as e:
            print(f"Error adding course schedule: {e}")
            self.connection.rollback()
        finally:
            if cursor:
                cursor.close()
        

    def view_all_students(self):
        # Method to fetch and display all students and their respective courses and grades
        try:
            cursor = self.connection.cursor()  
            query = """
                SELECT s.student_id, s.student_name, c.course_id, c.course_title, g.grade
                FROM Students s
                LEFT JOIN Enrollment e ON s.student_id = e.student_id
                LEFT JOIN Courses c ON e.course_id = c.course_id
                LEFT JOIN Grade g ON s.student_id = g.student_id
            """
            cursor.execute(query)  
            students = cursor.fetchall()  
            if students:
                for student in students:  
                    print(f"Student ID: {student[0]}, Name: {student[1]}, Course ID: {student[2]}, "
                          f"Course Title: {student[3]}, Grade: {student[4]}")
            else:
                print("No students found.")  
        except Exception as e:
            print(f"Error fetching students: {e}") 
        finally:
            cursor.close()

    def view_all_instructors(self):
        # Method to fetch and display all instructors and their respective courses
        try:
            cursor = self.connection.cursor()  
            query = """
                SELECT i.instructor_id, i.instructor_name, c.course_id, c.course_title
                FROM Instructors i
                LEFT JOIN Courses c ON i.instructor_id = c.instructor_id
            """
            cursor.execute(query) 
            instructors = cursor.fetchall()  
            if instructors:
                for instructor in instructors: 
                    print(f"Instructor ID: {instructor[0]}, Name: {instructor[1]}, Course ID: {instructor[2]}, "
                          f"Course Title: {instructor[3]}")
            else:
                print("No instructors found.")  
        except Exception as e:
            print(f"Error fetching instructors: {e}")
        finally:
            cursor.close()  

    def view_all_courses(self):
        try:
            cursor = self.connection.cursor()  
            query = """
                SELECT c.course_id, c.course_title, s.student_id, s.student_name
                FROM Courses c
                LEFT JOIN Enrollment e ON c.course_id = e.course_id
                LEFT JOIN Students s ON e.student_id = s.student_id
            """
            cursor.execute(query) 
            courses = cursor.fetchall()  
            if courses:
                for course in courses:  
                    print(f"Course ID: {course[0]}, Title: {course[1]}, Student ID: {course[2]}, Student Name: {course[3]}")
            else:
                print("No courses found.") 
        except Exception as e:
            print(f"Error fetching courses: {e}")  
        finally:
            cursor.close()  

    def delete_user(self):
        try:
            user_type = input("Enter user type to delete (student/instructor): ").strip().lower()  
            if user_type not in ["student", "instructor"]: 
                print("Invalid user type.")
                return
            
            user_id = int(input(f"Enter {user_type} ID to delete: "))  
            table_name = "Students" if user_type == "student" else "Instructors"
            query = f"DELETE FROM {table_name} WHERE {user_type}_id = ?"
            
            cursor = self.connection.cursor() 
            cursor.execute(query, (user_id,)) 
            self.connection.commit() 
            print(f"{user_type.capitalize()} with ID {user_id} has been deleted.")  
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")  
        except Exception as e:
            print(f"Error deleting user: {e}")  
            self.connection.rollback() 
        finally:
            cursor.close()  
            
    @classmethod
    def authenticate(cls, email, password, connection):
        """Authenticate the admin based on email and password."""
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PlatformAdmin WHERE admin_email = ?", (email,))
        admin_data = cursor.fetchone()

        if admin_data and admin_data["admin_password"] == password:  # Ensure password validation
            # Create an instance of PlatformAdmin with fetched data
            return cls(admin_id=admin_data['admin_id'],
                       admin_name=admin_data['admin_name'],
                       admin_password=admin_data['admin_password'],
                       admin_email=admin_data['admin_email'],
                       admin_phone=admin_data['admin_phone'],
                       admin_address=admin_data['admin_address'],
                       connection=connection)
        return None
