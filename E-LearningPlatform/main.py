from person import Person, Student, Instructor
from validate import Validate
from platformAdmin import PlatformAdmin
from enrollement import Enrollment
from grade import Grade
from register import Register
from course import Course
from assigment import Assignment
from schedule import Schedule
from databaseConnection import DataBaseConnection

# Initialize instances
validate = Validate()
register = Register()

def student_menu(student):
    while True:
        print("\nStudent Menu:")
        print("1. View Courses")
        print("2. View Assignments")
        print("3. View Grades")
        print("4. View Other Courses")
        print("5. Enroll in Course")
        print("6. Get Details")
        print("7. View Schedule")
        print("8. Log Out")
        choice = input("Select option (1-8): ")
        
        enrollment_instance = Enrollment(
            enrollment_id=None,
            student_id=student.get_student_id(),
            course_id=None,
            enrollment_date=None
        )
        assignment_instance = Assignment(
            assignment_id=None,
            assignment_title=None,
            assignment_details=None,
            assignment_due_date=None,
            assignment_difficulty=None,
            course_id=None,
            instructor_id=None
        )
        grade_instance = Grade(
            grade_id=None,
            student_id=student.get_student_id(),
            assignment_id=None,
            grade=None
        )
        course_instance = Course(
            course_id=None,
            course_title=None,
            course_details=None,
            instructor_id=None
        )
        schedule_instance = Schedule(
            schedule_id=None,
            course_id=None,
            schedule_day=None,
            schedule_time=None,
            schedule_type=None
        )
        student_instance = Student(
            student_id=student.get_student_id(),
            name=student.get_name(),
            age=student.get_age(),
            email=student.get_email(),
            phone=student.get_phone(),
            address=student.get_address()
        )
        if choice == "1":
             enrollment_instance.view_enrollments()
        elif choice == "2":
            assignment_instance.view_student_assignments()  
        elif choice == "3":
            grade_instance.view_grades()  
        elif choice == "4":
            course_instance.view_courses() 
        elif choice == "5":
            enrollment_instance.enroll_in_course() 
        elif choice == "6":
            details = student_instance.get_details()  
            print(details)
        elif choice == "7":
            schedule_instance.view_course_schedule()  
        elif choice == "8":
            student_instance.log_out()  
            break
        else:
            print("Invalid input. Please try again.")

def instructor_menu(instructor):
    while True:
        print("\nInstructor Menu:")
        print("1. View Students in Course")
        print("2. View Submissions")
        print("3. Grade Assignment")
        print("4. Create Assignment")
        print("5. Delete Assignment")
        print("6. Update Course Schedule")
        print("7. Get Details")
        print("8. Log Out")
        choice = input("Select option (1-8): ")
        
        enrollment_instance = Enrollment(
            enrollment_id=None,
            student_id=None,
            course_id=None,
            enrollment_date=None
        )
        assignment_instance = Assignment(
            assignment_id=None,
            assignment_title=None,
            assignment_details=None,
            assignment_due_date=None,
            assignment_difficulty=None,
            course_id=None,
            instructor_id=None
        )
        grade_instance = Grade(
            grade_id=None,
            student_id=None,
            assignment_id=None,
            grade=None
        )
        course_instance = Course(
            course_id=None,
            course_title=None,
            course_details=None,
            instructor_id=instructor.get_instructor_id()
        )
        schedule_instance = Schedule(
            schedule_id=None,
            course_id=None,
            schedule_day=None,
            schedule_time=None,
            schedule_type=None
        )
       
        instructor_instrance = Instructor(
            instructor_id=instructor.get_instructor_id(),
            name=instructor.get_name(),
            age=instructor.get_age(),
            email=instructor.get_email(),
            phone=instructor.get_phone(),
            address=instructor.get_address()
        )

        if choice == "1":
            course_instance.view_students_in_course()  
        elif choice == "2":
            assignment_instance.view_submissions()  
        elif choice == "3":
            grade_instance.assign_grades()  
        elif choice == "4":
            assignment_instance.create_assignment()  
        elif choice == "5":
            assignment_instance.delete_assignment()  
        elif choice == "6":
            schedule_instance.update_course_schedule()  
        elif choice == "7":
            instructor_instrance.get_details() 
        elif choice == "8":
            instructor_instrance.log_out() 
            break
        else:
            print("Invalid input. Please try again.")

def admin_menu(admin):
    while True:
        # Display the Admin Menu
        print("\nAdmin Menu:")
        print("1. View All Students")
        print("2. View All Instructors")
        print("3. View Courses")
        print("4. Delete User")
        print("5. Delete Course")
        print("6. Add New Schedule")
        print("7. Log Out")
        
        choice = input("Select option (1-7): ")
        if choice == "1":
            admin.view_all_students()  
        elif choice == "2":
            admin.view_all_instructors()
        elif choice == "3":
            admin.view_all_courses()  
        elif choice == "4":
            admin.delete_user()  
        elif choice == "5":
            admin.delete_course()  
        elif choice == "6":
            admin.add_course_schedule()  
        elif choice == "7":
            print("Logging out...")
            break  
        else:
            print("Invalid input. Please try again.")  


def main_menu():
    while True:
        print("\nWelcome to the E-Learning Platform")
        print("1. Log in")
        print("2. Register")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            email = input("Enter email: ").strip()

            role, user = validate.authenticate_email(email)
            if user:
                user_type = input("Are you a student, instructor, or admin? (s/i/a): ").lower()

                if user_type == "s" and role == "student":
                    student_details = validate.get_user_details(email)
                    if student_details:
                        print(f"Student details fetched: {student_details}")
                        student = Student(
                            student_id=student_details[0],
                            name=student_details[1],
                            age=student_details[2],
                            email=student_details[3],
                            phone=student_details[4],
                            address=student_details[5]
                        )

                        print(f"Student login successful! Welcome {student.get_full_name()}")
                        student.log_in()
                        student_menu(student)  
                    else:
                        print("Student not found.")
                elif user_type == "i" and role == "instructor":
                    instructor_details = validate.get_user_details(email)
                    if instructor_details:
                        print(f"Instructor details fetched: {instructor_details}")
                        instructor = Instructor(
                            instructor_id=instructor_details[0],
                            name=instructor_details[1],
                            age=instructor_details[2],
                            email=instructor_details[3],
                            phone=instructor_details[4],
                            address=instructor_details[5]
                        )
                        print(f"Instructor login successful! Welcome {instructor.get_full_name()}")
                        instructor.log_in()
                        instructor_menu(instructor)  
                    else:
                        print("Instructor not found.")
                if user_type == "a":
                    email = input("Enter email: ")
                    password = input("Enter password: ")

                    admin_type, admin_details = validate.authenticate_email(email)

                    if admin_type == "admin" and admin_details:
                        if validate.authenticate_password(email, password):  
                            print("Admin login successful!")
                            
                            admin_id, admin_name, admin_password, admin_email, admin_phone, admin_address = admin_details

                            admin_instance = PlatformAdmin(
                                admin_id=admin_id,
                                admin_name=admin_name,
                                admin_password=admin_password,
                                admin_email=admin_email,
                                admin_phone=admin_phone,
                                admin_address=admin_address
                            )

                            admin_menu(admin_instance)

                        else:
                            print("Invalid password for admin.")
                    else:
                        print("Email not found in our system. Please check the email address.")


        if choice == "2":
            register_choice = input("Register as (1) Student or (2) Instructor: ").strip()
            register_instance = Register()
            
            if register_choice == "1":
                register_instance.register_new_student()
            elif register_choice == "2":
                register_instance.register_new_instructor()
            else:
                print("Invalid choice. Returning to main menu.")

        elif choice == "3":
            print("Exiting the platform. Goodbye!")
            break  

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main_menu()
