class Attendance:
    def __init__(self):
        self.present_students = []

    def mark_present(self, student_name: str):
        
        if student_name not in self.present_students:
            
            self.present_students.append(student_name)
            
            print(f"{student_name} has been marked as present.")
        else:
            print(f"{student_name} is already marked as present.")

    def remove_student(self, student_name: str):
        if student_name in self.present_students:
            
            self.present_students.remove(student_name)
            print(f"{student_name} has been removed from the attendance list.")
        else:
            print(f"{student_name} is not in the attendance list.")

    def is_present(self, student_name: str) -> bool:
        return student_name in self.present_students

    def display_attendance(self):
        if self.present_students:
            print("Students present today:")
            for student in self.present_students:
                print(f"- {student}")
        else:
            print("No students are present today.")

# Example usage
if __name__ == "__main__":
    attendance = Attendance()

    # Mark students as present
    attendance.mark_present("Devangi")
    attendance.mark_present("kush")

    # Check if a student is present
    print("Is Devangi present?", attendance.is_present("Devangi"))
    print("Is sanya present?", attendance.is_present("sanya"))

    # Remove a student
    attendance.remove_student("kush")

    # Display attendance
    attendance.display_attendance()



