class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40


def add_student(students):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))
    students.append(Student(name, age, marks))
    print(f"Student '{name}' added successfully!\n")


def view_students(students):
    if not students:
        print("No students added yet.\n")
        return

    print("\n--- All Students ---")
    for student in students:
        student.display()
        status = "Passed" if student.is_passed() else "Failed"
        print(f"Status: {status}")
        print("-" * 20)
    print()


def search_student(students):
    name = input("Enter name to search: ")
    found = False
    for student in students:
        if student.name.lower() == name.lower():
            student.display()
            status = "Passed" if student.is_passed() else "Failed"
            print(f"Status: {status}\n")
            found = True
            break

    if not found:
        print(f"No student found with name '{name}'.\n")


def main():
    students = []

    while True:
        print("--- Student Management System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
