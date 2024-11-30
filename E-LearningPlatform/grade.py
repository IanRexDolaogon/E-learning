from databaseConnection import DataBaseConnection  

class Grade:
    def __init__(self, grade_id, student_id, assignment_id, grade, connection=None):
        self._grade_id = grade_id
        self._student_id = student_id
        self._assignment_id = assignment_id
        self._grade = grade
        self.connection = connection or DataBaseConnection() 

    def view_grades(self):
        try:
            student_id = int(input("Enter student ID to view grades: "))
            query = "SELECT grade_id, assignment_id, grade FROM Grade WHERE student_id = ?"
            cursor = self.connection.cursor()  
            cursor.execute(query, (student_id,))  
            grades = cursor.fetchall()  
            
            if grades:
                for grade in grades:
                    print(f"Assignment ID: {grade[1]} | Grade: {grade[2]}")  
            else:
                print("No grades found for this student.") 
        except ValueError:
            print("Invalid student ID.")  
        except Exception as e:
            print(f"Error retrieving grades: {e}")  
        finally:
            cursor.close()  

    def assign_grades(self):
        try:
            student_id = int(input("Enter student_id: "))
            assignment_id = int(input("Enter assignment_id: "))
            grade = float(input("Enter grade for student: "))
        except ValueError:
            print("Invalid input.")  
            return

        try:
            cursor = self.connection.cursor()  

            cursor.execute("INSERT INTO Grade (student_id, assignment_id, grade) VALUES(?, ?, ?)", (student_id, assignment_id, grade))
            self.connection.commit() 
        except Exception as e:
            print(f"Error in assigning grades: {e}")  
            self.connection.rollback()  
        finally:
            cursor.close()  
