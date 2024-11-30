from databaseConnection import DataBaseConnection

class Schedule:
    def __init__(self, schedule_id=None, course_id=None, schedule_day=None, schedule_time=None, schedule_type=None, connection=None):
        self._schedule_id = schedule_id
        self._course_id = course_id
        self._schedule_day = schedule_day
        self._schedule_time = schedule_time
        self._schedule_type = schedule_type
        self.connection = connection or DataBaseConnection()

    def view_course_schedule(self):
        try:
            course_id = int(input("Enter the course ID to view its schedule: "))  
            cursor = self.connection.cursor()
            query = """
                SELECT schedule_id, schedule_day, schedule_time, schedule_type
                FROM Schedule
                WHERE course_id = ?
            """
            cursor.execute(query, (course_id,))
            schedules = cursor.fetchall()

            if schedules:
                print(f"Schedule for Course ID: {course_id}")
                for schedule in schedules:
                    print(f"Schedule ID: {schedule[0]}")
                    print(f"Day: {schedule[1]}")
                    print(f"Time: {schedule[2]}")
                    print(f"Type: {schedule[3]}")  
                    print("---")
            else:
                print("No schedule found for the specified course.")
        except ValueError:
            print("Invalid input. Please enter a valid course ID.")
        except Exception as e:
            print(f"Error viewing course schedule: {e}")
        finally:
            if cursor:
                cursor.close()

    def update_course_schedule(self):
        try:
            schedule_id = int(input("Enter the schedule ID to update: ")) 
            schedule_day = input("Enter the new day of the schedule: ") 
            schedule_time = input("Enter the new time of the schedule (e.g., 10:00 AM): ") 
            schedule_type = input("Enter the new type of the schedule (e.g., Lecture, Lab): ")  
        except ValueError:
            print("Invalid input. Please enter valid data.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                UPDATE Schedule 
                SET schedule_day = ?, schedule_time = ?, schedule_type = ?
                WHERE schedule_id = ?
            """
            cursor.execute(query, (schedule_day, schedule_time, schedule_type, schedule_id))
            if cursor.rowcount > 0:
                self.connection.commit()
                print(f"Schedule ID {schedule_id} updated to {schedule_day}, {schedule_time}, {schedule_type}")
            else:
                print("No matching schedule found to update.")
        except Exception as e:
            print(f"Error updating course schedule: {e}")
            self.connection.rollback()
        finally:
            if cursor:
                cursor.close()
