INSERT INTO Students (student_name, student_age, student_email, student_phone, student_address)
VALUES
    ('John Doe', '20', 'john.doe@email.com', '09-111-111', 'Avenue St'),
    ('Jane Smith', '22', 'jane.smith@email.com', '09-222-222', 'Avenue St'),
    ('Emily Johnson', '19', 'emily.johnson@email.com', '09-333-333', 'Miracle Block 1'),
    ('Michael Brown', '21', 'michael.brown@email.com', '09-444-444', 'Miracle Block 2'),
    ('Sarah Lee', '23', 'sarah.lee@email.com', '09-555-555', 'Miracle Block 3'),
    ('David Williams', '20', 'david.williams@email.com', '09-666-666', 'Bonifacio St'),
    ('Sophia Taylor', '22', 'sophia.taylor@email.com', '09-777-777', 'Avenue St'),
    ('James Wilson', '21', 'james.wilson@email.com', '09-888-888', 'Miracle St'),
    ('Olivia Martinez', '19', 'olivia.martinez@email.com', '09-999-999', 'Abellera St'),
    ('Daniel Garcia', '22', 'daniel.garcia@email.com', '09-101-101', 'Avenue Ave');


INSERT INTO Instructors (instructor_name, instructor_age, instructor_email, instructor_phone, instructor_address)
VALUES
    ('Dr. Richard Green', '45', 'richard.green@email.com', '666-666-666', 'Bonifacio St'),
    ('Prof. Walter White', '39', 'walter.white@email.com', '777-777-777', 'Miracle Block 1'),
    ('Dr. Robert Black', '50', 'robert.black@email.com', '888-888-888', 'Highway'),
    ('Prof. Karen Clark', '42', 'karen.clark@email.com', '555-555-555', ' Osias'),
    ('Dr. William Davis', '38', 'william.davis@email.com', '999-999-999', 'Avenue Ave');

INSERT INTO Courses (course_title, course_details, instructor_id)
VALUES
    ('Introduction to Programming', 'Learn the basics of programming using Python.', 1),
    ('Data Structures and Algorithms', 'Study of data structures and algorithms using C++.', 2),
    ('Web Development', 'Learn how to build websites using HTML, CSS, and JavaScript.', 3),
    ('Machine Learning Basics', 'Introduction to machine learning and data analysis techniques.', 4),
    ('Database Management Systems', 'Understand relational databases and SQL queries.', 5);

INSERT INTO Enrollment (student_id, course_id, enrollment_date)
VALUES
    (1, 1, '2024-11-01'), (2, 2, '2024-11-02'), (3, 3, '2024-11-03'), (4, 4, '2024-11-04'), (5, 5, '2024-11-05'),
    (6, 1, '2024-11-06'), (7, 2, '2024-11-07'), (8, 3, '2024-11-08'), (9, 4, '2024-11-09'), (10, 5, '2024-11-10');

INSERT INTO Assignment (assignment_title, assignment_details, assignment_due_date, assignment_difficulty, course_id, instructor_id)
VALUES
    ('Assignment 1', 'Write a Python program that prints "Hello, World!"', '2024-12-01', 'Easy', 1, 1),
    ('Assignment 2', 'Implement a linked list in C++', '2024-12-05', 'Easy', 2, 2),
    ('Assignment 3', 'Create a personal webpage using HTML and CSS', '2024-12-10', 'Medium', 3, 3),
    ('Assignment 4', 'Train a simple linear regression model using Python', '2024-12-15', 'Medium', 4, 4),
    ('Assignment 5', 'Write SQL queries to manage a library database', '2024-12-20', 'Hard', 5, 5);

INSERT INTO Grade (student_id, assignment_id, grade)
VALUES
    (1, 1, 85.00), (2, 1, 90.00), (3, 1, 88.50), (4, 1, 92.25), (5, 1, 87.75),
    (6, 2, 80.00), (7, 2, 95.00), (8, 2, 89.00), (9, 2, 91.50), (10, 2, 93.20),
    (1, 3, 84.00), (2, 3, 91.25), (3, 3, 85.00), (4, 3, 93.00), (5, 3, 90.00),
    (6, 4, 76.50), (7, 4, 88.75), (8, 4, 84.00), (9, 4, 92.10), (10, 4, 94.30);

INSERT INTO Schedule (course_id, schedule_day, schedule_time, schedule_type)
VALUES
    (1, 'Monday', '09:00', 'Online'),
    (2, 'Tuesday', '10:00', 'Online'),
    (3, 'Wednesday', '11:00', 'Online'),
    (4, 'Thursday', '14:00', 'Online'),
    (5, 'Friday', '15:00', 'Online');



INSERT INTO PlatformAdmin (admin_name, admin_email, admin_password, admin_phone, admin_address)
VALUES
    ('Dolaogon V. Rex Ian', 'rdolaogon@gmail.com', '123', '09382574449', 'Admin Office 1');
    