import pyodbc

class DataBaseConnection:
    def __init__(self):
        self.connection = self.connect()
    
    @staticmethod
    def connect():
        try:
            connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=FUZZYDINASAUR\\SQLEXPRESS;'
                'DATABASE=E-LearningDatabase;'
                'Trusted_Connection=yes;'
            )
            print("Database Connected")
            return connection
        except pyodbc.Error as e:
            print(f"Error connecting to the Database: {e}")
            return None

    def cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise Exception("Database connection not established.")
        
    def commit(self):
        if self.connection:
            self.connection.commit()
        else:
            raise Exception("Database connection not established.")
        
    def rollback(self):
        if self.connection:
            self.connection.rollback()
        else:
            raise Exception("Database connection not established.")
        
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None  # Set the connection to None after closing
            print("Database Connection Closed")
        else:
            raise Exception("Database connection not established.")
