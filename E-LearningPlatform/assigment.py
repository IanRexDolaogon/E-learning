from databaseConnection import DataBaseConnection

class Assignment:
    def __init__(self, assignment_id, assignment_title, assignment_details, assignment_due_date, assignment_difficulty, course_id, instructor_id, connection=None):
        self._assignment_id = assignment_id
        self._assignment_title = assignment_title
        self._assignment_details = assignment_details
        self._assignment_due_date = assignment_due_date
        self._assignment_difficulty = assignment_difficulty
        self._course_id = course_id
        self._instructor_id = instructor_id
        self.connection = connection or DataBaseConnection()

    def get_assignment_id(self):
        return self._assignment_id

    def get_assignment_details(self):
        return self._assignment_details

    def get_assignment_due_date(self):
        return self._assignment_due_date

    def get_assignment_difficulty(self):
        return self._assignment_difficulty

    def get_course_id(self):
        return self._course_id

    def get_instructor_id(self):
        return self._instructor_id

    def get_assignment_info(self):
        return {
            "assignment_id": self._assignment_id,
            "assignment_title": self._assignment_title,
            "assignment_details": self.get_assignment_details(),
            "assignment_due_date": self.get_assignment_due_date(),
            "assignment_difficulty": self.get_assignment_difficulty(),
            "course_id": self.get_course_id(),
            "instructor_id": self.get_instructor_id()
        }

    def submit_assignment(self):
        try:
            student_id = int(input("Enter your student ID: "))
            assignment_id = int(input("Enter the assignment ID you are submitting: "))
            submission_date = input("Enter the submission date (YYYY-MM-DD): ")
        except ValueError:
            print("Invalid input. Please enter valid integers for student and assignment IDs.")
            return
        except Exception as e:
            print(f"Error with submission date input: {e}")
            return
        
        try:        
            cursor = self.connection.cursor()
            cursor.execute(
                """
                INSERT INTO Submission (student_id, assignment_id, submission_date)
                VALUES (?, ?, ?)
                """,
                (student_id, assignment_id, submission_date)
            )
            self.connection.commit()
            print("Assignment submitted successfully.")
        except Exception as e:
            print(f"Error in submission: {e}")
        finally:
            cursor.close()

    def view_submissions(self):
        try:
            assignment_id = int(input("Enter assignment_id to view submissions: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for assignment ID.")
            return 

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                SELECT s.student_id, s.submission_date
                FROM Submission s
                WHERE s.assignment_id = ?
                """, 
                (assignment_id,)
            )
            submissions = cursor.fetchall()

            if not submissions:
                print(f"No submissions found for assignment ID {assignment_id}.")
            else:
                print(f"Submissions for Assignment ID {assignment_id}:")
                for submission in submissions:
                    student_id, submission_date= submission
                    print(f"Student ID: {student_id}, Submission Date: {submission_date}")

        except Exception as e:
            print(f"Error retrieving submissions: {e}")
        finally:
            cursor.close()

    def view_student_assignments(self):
        try:
            student_id = int(input("Enter your student ID to view your assignments: "))
        except ValueError:
            print("Invalid input. Please enter a valid numeric student ID.")
            return

        if not self.connection:
            print("Database connection is not available.")
            return

        try:
            with self.connection.cursor() as cursor:
                # gets the assignments for the given student based on their enrolled courses
                cursor.execute("""
                    SELECT 
                        a.assignment_id, 
                        a.assignment_title, 
                        a.assignment_details, 
                        a.assignment_due_date, 
                        a.assignment_difficulty
                    FROM Assignment a
                    JOIN Courses c ON a.course_id = c.course_id
                    JOIN Enrollment e ON e.course_id = c.course_id
                    WHERE e.student_id = ?
                """, (student_id,))

                assignments = cursor.fetchall()

                if not assignments:
                    print(f"No assignments found for student ID {student_id}.")
                else:
                    print(f"Assignments for Student ID {student_id}:")
                    for assignment in assignments:
                        assignment_id, title, details, due_date, difficulty = assignment
                        print(f"\nAssignment ID: {assignment_id}")
                        print(f"Title: {title}")
                        print(f"Details: {details}")
                        print(f"Due Date: {due_date}")
                        print(f"Difficulty: {difficulty}")

        except Exception as e:
            print(f"Error retrieving student assignments: {e}")


    def create_assignment(self):
        try:
            course_id = int(input("Enter course_id: "))
            title = input("Enter assignment title: ")
            details = input("Enter assignment details: ")
            due_date = input("Enter assignment due date (YYYY-MM-DD): ")
            difficulty = input("Enter assignment difficulty (e.g., Easy, Medium, Hard): ")
        except ValueError:
            print("Invalid input. Please ensure all fields are correctly filled.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Assignment(course_id, assignment_title, assignment_details, assignment_due_date, assignment_difficulty) VALUES(?, ?, ?, ?, ?)",
                (course_id, title, details, due_date, difficulty))
            self.connection.commit()
            print("Assignment created successfully.")
        except Exception as e:
            print(f"Error creating assignment: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def delete_assignment(self):
        try:
            assignment_id = int(input("Enter assignment_id to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid assignment ID.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Assignment WHERE assignment_id = ?", (assignment_id,))
            self.connection.commit()
            print(f"Assignment with ID {assignment_id} has been deleted.")
        except Exception as e:
            print(f"Error in deleting assignment: {e}")
            self.connection.rollback()
        finally:
            cursor.close()
