CREATE TABLE Students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_age VARCHAR(2),  
    student_email VARCHAR(100) UNIQUE NOT NULL,  
    student_phone VARCHAR(15),
    student_address VARCHAR(255)
);

CREATE TABLE Instructors (
    instructor_id INT IDENTITY(1,1) PRIMARY KEY,
    instructor_name VARCHAR(100) NOT NULL,
    instructor_age VARCHAR(2),  
    instructor_email VARCHAR(100) UNIQUE NOT NULL,  
    instructor_phone VARCHAR(15),
    instructor_address VARCHAR(255)
);

CREATE TABLE Courses (
    course_id INT IDENTITY(1,1) PRIMARY KEY,
    course_title VARCHAR(100) NOT NULL,
    course_details VARCHAR(MAX),
    instructor_id INT,  
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Enrollment (
    enrollment_id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Assignment (
    assignment_id INT IDENTITY(1,1) PRIMARY KEY,
    assignment_title VARCHAR(100) NOT NULL,
    assignment_details VARCHAR(MAX),
    assignment_due_date DATE,
    assignment_difficulty VARCHAR(20),  
    course_id INT,
    instructor_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Grade (
    grade_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT,
    assignment_id INT,
    grade DECIMAL(5, 2) NOT NULL,  
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (assignment_id) REFERENCES Assignment(assignment_id)
);

CREATE TABLE Schedule (
    schedule_id INT PRIMARY KEY IDENTITY(1,1),
    course_id INT,
    schedule_day VARCHAR(20),  
    schedule_time TIME,
    schedule_type VARCHAR(100),  
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE PlatformAdmin (
    admin_id INT PRIMARY KEY IDENTITY(1,1),
    admin_name VARCHAR(100) NOT NULL,
    admin_email VARCHAR(100) UNIQUE NOT NULL,  
    admin_password VARCHAR(255) NOT NULL,  
    admin_phone VARCHAR(15),
    admin_address VARCHAR(255)
);

CREATE TABLE Submission(
	submission_id INT IDENTITY(1,1) PRIMARY KEY,
	student_id INT,
	assignment_id INT, 
	submission_date VARCHAR(20),
	);