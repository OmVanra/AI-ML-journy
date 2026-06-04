# Q3. Create a class 
# Student 
# with private attributes _name, _roll_no, and _marks. 
# Provide getter and setter methods with validation (e.g., marks cannot be 
# negative, roll number has to be between 1 & 100 & name cannot be empty).

class Student:
    def __init__(self, name, roll_no, marks):
        self._name = None
        self._roll_no = None
        self._marks = None
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)
    def set_name(self, name):
        if name:
            self._name = name
        else:
            print("Name cannot be empty.")
    def get_name(self):
        return self._name
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")
    def get_roll_no(self):
        return self._roll_no
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative.")
    def get_marks(self):
        return self._marks
    
# Example usage
student = Student("Alice", 25, 85)
print(f"Student Name: {student.get_name()}")
print(f"Roll Number: {student.get_roll_no()}")
print(f"Marks: {student.get_marks()}")
# Attempting to set invalid values
student.set_name("")  # Should print an error message
student.set_roll_no(150)  # Should print an error message
student.set_marks(-10)  # Should print an error message

                