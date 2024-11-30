from databaseConnection import DataBaseConnection  


class Register:
    def __init__(self, connection=None):
        self.connection = connection or DataBaseConnection()

    def register_new_instructor(self):
        try:
            last_name = input("Enter last name: ")
            middle_name = input("Enter middle name: ")
            first_name = input("Enter first name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")

            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Instructors (instructor_name, instructor_age, instructor_email, instructor_phone, instructor_address) "
                "VALUES (?, ?, ?, ?, ?)",
                (f"{last_name} {middle_name} {first_name}", age, email, phone, address))
            self.connection.commit()  
            print(f"Instructor {first_name} {last_name} registered successfully.")  
        except Exception as e:
            print(f"Error registering instructor: {e}")  
        finally:
            cursor.close()

    def register_new_student(self):
        try:
            last_name = input("Enter last name: ")
            middle_name = input("Enter middle name: ")
            first_name = input("Enter first name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")

            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Students (student_name, student_age, student_email, student_phone, student_address) "
                "VALUES (?, ?, ?, ?, ?)",
                (f"{last_name} {middle_name} {first_name}", age, email, phone, address))
            self.connection.commit()  
            print(f"Student {first_name} {last_name} registered successfully.")  
        except Exception as e:
            print(f"Error registering student: {e}")  
        finally:
            cursor.close()  
