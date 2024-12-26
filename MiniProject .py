# Class: A blueprint for creating objects. It defines the structure and behavior (attributes and methods) of the objects.
class Student:
    """
    This class represents a Student with attributes such as roll number, name, age, and marks.
    """

    def __init__(self, roll_no, name, age, marks):
        # Constructor to initialize the attributes of the Student object
        self.roll_no = roll_no  # Unique identifier for the student
        self.name = name        # Name of the student
        self.age = age          # Age of the student
        self.marks = marks      # Marks obtained by the student

    def display(self):
        """
        Display the details of the student in a formatted way.
        """
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}")


class StudentManagementSystem:
    """
    This class manages a collection of Student objects. 
    It provides methods to add, view, update, and delete student records.
    """

    def __init__(self):
        # Initializes an empty list to store Student objects
        self.students = []

    def add_student(self):
        """
        Adds a new student by creating a Student object and appending it to the list.
        """
        # Taking input from the user for the student's details
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        # Creating a new Student object
        student = Student(roll_no, name, age, marks)
        
        # Adding the Student object to the students list
        self.students.append(student)
        print("Student added successfully!")

    def view_all_students(self):
        """
        Displays all student records in the system.
        """
        if not self.students:  # Check if the list is empty
            print("No students found!")
        else:
            print("\nStudent Records:")
            # Loop through each Student object in the list and display its details
            for student in self.students:
                student.display()

    def view_student(self):
        """
        Displays the details of a student identified by their roll number.
        """
        roll_no = input("Enter Roll Number to search: ")
        # Searching for the student by roll number
        for student in self.students:
            if student.roll_no == roll_no:
                student.display()  # Display the found student's details
                return
        print("Student not found!")  # If no student matches the roll number

    def update_student(self):
        """
        Updates the details of an existing student identified by their roll number.
        """
        roll_no = input("Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                # Taking new details from the user
                student.name = input("Enter new Name: ")
                student.age = int(input("Enter new Age: "))
                student.marks = float(input("Enter new Marks: "))
                print("Student updated successfully!")
                return
        print("Student not found!")  # If no student matches the roll number

    def delete_student(self):
        """
        Deletes a student record identified by their roll number.
        """
        roll_no = input("Enter Roll Number to delete: ")
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)  # Remove the student from the list
                print("Student deleted successfully!")
                return
        print("Student not found!")  # If no student matches the roll number

    def menu(self):
        """
        Displays a menu to the user and handles user input for various operations.
        """
        while True:
            # Menu options
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View All Students")
            print("3. View Student by Roll Number")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            # Taking user input for menu choice
            choice = int(input("Enter your choice: "))
            
            # Handling each menu option
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.view_all_students()
            elif choice == 3:
                self.view_student()
            elif choice == 4:
                self.update_student()
            elif choice == 5:
                self.delete_student()
            elif choice == 6:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


# Main Program: Entry point of the program
if __name__ == "__main__":
    # Creating an instance of StudentManagementSystem
    sms = StudentManagementSystem()
    # Calling the menu method to start the application
    sms.menu()
