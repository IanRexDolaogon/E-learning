from abc import ABC, abstractmethod
from databaseConnection import DataBaseConnection

class Person(ABC):
    def __init__(self, name: str, age: str, email: str, connection=None):
        self._name = name
        self._age = age
        self._email = email
        self.connection = connection or DataBaseConnection()

    def get_full_name(self):
        return self._name  

    @abstractmethod
    def get_role(self):
        pass

    def log_in(self):
        print(f"User {self.get_full_name()} has logged in..")

    def log_out(self):
        print(f"User {self.get_full_name()} has logged out..")
class Student(Person):
    def __init__(self, student_id: int, name: str, age: str, email: str, phone: str, address: str, connection=None):
        super().__init__(name, age, email, connection)  
        self._student_id = student_id
        self._phone = phone
        self._address = address
        
    def get_student_id(self):
        return self._student_id
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_email(self):
        return self._email
    
    def get_phone(self):
        return self._phone
    
    def get_address(self):
        return self._address
    
            
    def get_role(self):
        return "Student"

    def get_details(self):
        details = {
            "Student ID": self._student_id,
            "Name": self.get_name(),
            "Age": self.get_age(),
            "Email": self.get_email(),
            "Phone": self.get_phone(),
            "Address": self.get_address(),
            "Role": self.get_role()
        }
        
        for key, value in details.items():
            print(f"{key}: {value}")

class Instructor(Person):
    def __init__(self, instructor_id: int, name: str, age: str, email: str, phone: str, address: str, connection=None):
        super().__init__(name, age, email, connection)  
        self._instructor_id = instructor_id
        self._phone = phone
        self._address = address
        
    def get_instructor_id(self):
        return self._instructor_id
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_email(self):
        return self._email
    
    def get_phone(self):
        return self._phone
    
    def get_address(self):
        return self._address

    def get_role(self):
        return "Instructor"

    
    def get_details(self):
        details = {
            "Student ID": self._instructor_id,
            "Name": self.get_name(),
            "Age": self.get_age(),
            "Email": self.get_email(),
            "Phone": self.get_phone(),
            "Address": self.get_address(),
            "Role": self.get_role()
        }
        
        for key, value in details.items():
            print(f"{key}: {value}")
