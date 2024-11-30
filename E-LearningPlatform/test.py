from person import Student, Instructor

def main():
    # Create a Student instance
    student1 = Student(
        student_id=1,
        last_name="Doe",
        middle_name="A.",
        first_name="John",
        age="21",
        email="john.doe@example.com",
        phone="123-456-7890",
        address="123 Main St"
    )

    # Print student details
    print(student1.get_details())

    # View student's courses
    print("Student's Courses:")
    courses = student1.view_courses()
    for course in courses:
        print(course)

    # Enroll in a new course
    student1.enroll_in_course()

    # Add a new student
    student1.add_new_student()

    # Create an Instructor instance
    instructor1 = Instructor(
        instructor_id=1,
        last_name="Smith",
        middle_name="B.",
        first_name="Jane",
        age="40",
        email="jane.smith@example.com",
        phone="098-765-4321",
        address="456 Elm St"
    )

    # Print instructor details
    print(instructor1.get_details())

    # Create a new assignment
    instructor1.create_assignment()

    # View students in a course
    instructor1.students_in_course()

if __name__ == "__main__":
    main()
