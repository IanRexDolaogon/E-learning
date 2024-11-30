from databaseConnection import DataBaseConnection
class Validate:
    def __init__(self, connection=None):
        self.connection = connection or DataBaseConnection()

    def authenticate_email(self, email: str):
        # Check for a student with the provided email
        query_students = "SELECT * FROM Students WHERE student_email = ?"
        cursor = self.connection.cursor()
        cursor.execute(query_students, (email,))
        student = cursor.fetchone()

        if student:
            return "student", student  # Found a student

        # Check for an instructor with the provided email
        query_instructors = "SELECT * FROM Instructors WHERE instructor_email = ?"
        cursor.execute(query_instructors, (email,))
        instructor = cursor.fetchone()

        if instructor:
            return "instructor", instructor  # Found an instructor

        # Check for an admin with the provided email (add this section for admin)
        query_admin = "SELECT * FROM PlatformAdmin WHERE admin_email = ?"
        cursor.execute(query_admin, (email,))
        admin = cursor.fetchone()

        if admin:
            return "admin", admin  # Found an admin

        return None, None  # No match found


    def get_user_details(self, email: str):
        query_students = "SELECT * FROM Students WHERE student_email = ?"
        cursor = self.connection.cursor()
        cursor.execute(query_students, (email,))
        student = cursor.fetchone()

        if student:
            return student  

        query_instructors = "SELECT * FROM Instructors WHERE instructor_email = ?"
        cursor.execute(query_instructors, (email,))
        instructor = cursor.fetchone()

        if instructor:
            return instructor  

        return None  

    def authenticate_password(self, email: str, password: str):
        query = "SELECT * FROM PlatformAdmin WHERE admin_email = ? AND admin_password = ?"
        cursor = self.connection.cursor() 
        cursor.execute(query, (email, password))  
        user = cursor.fetchone()  
        
        if user:
            return True  
        else:
            print("Invalid email or password.")  
            return False  

   