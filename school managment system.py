class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id, courses):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = courses

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print("Courses:")
        for course in self.courses:
            print(course)


class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")


def create_person():
    person_type = input("Enter person type (student/teacher): ").lower()
    name = input("Enter name: ")
    age = input("Enter age: ")
    address = input("Enter address: ")

    try:
        age = int(age)
    except ValueError:
        print("Age must be a number.")
        return None

    if person_type == "student":
        student_id = input("Enter student ID: ")
        courses = input("Enter courses (comma-separated): ").split(",")
        return Student(name, age, address, student_id, courses)
    elif person_type == "teacher":
        employee_id = input("Enter employee ID: ")
        subject = input("Enter subject: ")
        return Teacher(name, age, address, employee_id, subject)
    else:
        print("Invalid person type.")
        return None



while True:
    print("\nWelcome to the school management system!")
    print("1. Create a new person")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        person = create_person()
        if person:
            print("\nPerson details:")
            person.display_info()
    elif choice == "2":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
