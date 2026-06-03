# . Create a dictionary where:
# • 
# Keys = student names
# • 
# Values = marks (integer)
# A
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
# depending on the operation they want to perform on the dictionary:
# 1. - Add a student
# B
# 2. - Update marks
# C
# 3. - Search for a student
# D
# 4. - Display all students and marks

def student_marks_menu():
    student_marks = {}

    while True:
        print("\nMenu:")
        print("A - Add a student")
        print("B - Update marks")
        print("C - Search for a student")
        print("D - Display all students and marks")
        choice = input("Enter your choice:").upper()

        if choice == 'A':
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            student_marks[name] = marks
            print(f"Student {name} added with marks {marks}.")
        elif choice == 'B':
            name = input("Enter student name to update: ")
            if name in student_marks:
                marks = int(input("Enter new marks: "))
                student_marks[name] = marks
                print(f"Marks for {name} updated to {marks}.")
            else:
                print(f"Student {name} not found.")
        elif choice == 'C':
            name = input("Enter student name to search: ")
            if name in student_marks:
                print(f"{name} has marks {student_marks[name]}.")
            else:
                print(f"Student {name} not found.")
        elif choice == 'D':
            if student_marks:
                print("Student and their marks:")
                for name, marks in student_marks.items():
                    print(f"{name}: {marks}")
            else:
                print("No students in the dictionary.")
        else:
            print("Invalid choice. Please try again.")

            
# Example usage
student_marks_menu()


