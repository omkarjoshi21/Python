# Section 1: Object Oriented Programming (2.1, 2.2, 2.3)

# ---------------------------------------------------------
# 2.1 Class, Object, Method Call, and Accessing Class Members
# ---------------------------------------------------------
# Class: A blueprint or form template.
# Object: One real item made from that template.
# Method Call: Calling a function inside a class using a dot (e.g., s1.show_details()).
# Accessing members outside class: Using object.attribute or ClassName.attribute.

class Student:
    college = "My College"  # Shared by all Student objects

    def __init__(self, name, marks):
        self.name = name    # Stored inside this specific object
        self.marks = marks  # Stored inside this specific object

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


print("=== 2.1 Class, Object, Method Call ===")
# Create one object from the Student class
s1 = Student("Riya", 85)

# Access a variable outside the class using a dot
print("Outside access - Name:", s1.name)
print("Outside access - College:", Student.college)

# Call a method on the object
s1.show_details()


# ---------------------------------------------------------
# 2.2 Setter and Getter Methods
# ---------------------------------------------------------
# Getter: Reads and returns a variable's value.
# Setter: Updates a variable's value after checking an if/else condition.

class Person:
    def __init__(self, age):
        self._age = 0       # Start with a safe default
        self.set_age(age)   # Validate using the setter

    def get_age(self):
        return self._age    # Returns the stored age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
            print("Age set to:", self._age)
        else:
            print("Age cannot be negative. Keeping:", self._age)


print("\n=== 2.2 Setter and Getter Methods ===")
p = Person(20)
print("Current age:", p.get_age())

p.set_age(-5)   # Blocked by if/else
p.set_age(21)   # Accepted
print("Final age:", p.get_age())


# ---------------------------------------------------------
# 2.3 Constructor and Destructor
# ---------------------------------------------------------
# Constructor (__init__): Runs automatically when you create an object.
# Destructor (__del__): Runs automatically when an object is deleted with del.

class Book:
    def __init__(self, title):
        self.title = title
        print("Constructor ran: Book created ->", self.title)

    def __del__(self):
        print("Destructor ran: Book removed ->", self.title)


print("\n=== 2.3 Constructor and Destructor ===")
b = Book("Python Basics")
print("Using book:", b.title)

del b  # Deletes the object and triggers __del__
