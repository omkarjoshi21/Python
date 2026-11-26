# Section 1: Object Oriented Programming (2.1, 2.2, 2.3)
# Study and revision examples with clear comments for beginners.

# ---------------------------------------------------------
# 2.1 Concept of Class, Object, Method Call, and Accessing
#     Class Members Outside the Class
# ---------------------------------------------------------
# - Class: A blueprint for creating objects.
# - Object: An actual instance created from a class.
# - Method: A function written inside a class.
# - Accessing members outside class: Using object.attribute or object.method()

class Student:
    # Class attribute (shared by all Student objects)
    college = "IMCC"

    def set_info(self, name, roll_no, marks):
        # Instance attributes (different for each object)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def show_info(self):
        print("College :", Student.college)
        print("Name    :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks   :", self.marks)

    def check_pass(self):
        if self.marks >= 40:
            print(self.name, "-> Pass")
        else:
            print(self.name, "-> Fail")


print("=== 2.1 Class, Object, Method Call ===")
s1 = Student()  # Creating first object
s2 = Student()  # Creating second object

# Calling methods on objects
s1.set_info("Aarav", 101, 75)
s2.set_info("Diya", 102, 32)

s1.show_info()
s1.check_pass()

print()
s2.show_info()
s2.check_pass()

# Accessing and updating class members from outside the class
print("\nCollege accessed outside class:", Student.college)
print("Student 1 name accessed directly:", s1.name)

s2.marks = 50  # Updating marks from outside the class
print("Updated Diya's marks to:", s2.marks)
s2.check_pass()


# ---------------------------------------------------------
# 2.2 Setter and Getter Methods
# ---------------------------------------------------------
# - Getter: Method used to read a value safely.
# - Setter: Method used to change a value with checks/validation.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = 0  # Underscore means treat as internal/private
        self.set_balance(balance)

    # Getter method
    def get_balance(self):
        return self._balance

    # Setter method with validation
    def set_balance(self, amount):
        if amount < 0:
            print("Invalid amount! Balance cannot be negative.")
        else:
            self._balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self._balance + amount)
            print("Deposited:", amount)
        else:
            print("Deposit must be greater than 0.")


print("\n=== 2.2 Setter and Getter Methods ===")
acc = BankAccount("Rohan", 1000)
print("Owner:", acc.owner)
print("Starting Balance:", acc.get_balance())

acc.deposit(500)
print("Balance after deposit:", acc.get_balance())

# Trying to set a negative balance (setter will block it)
acc.set_balance(-200)
print("Balance after invalid update:", acc.get_balance())


# ---------------------------------------------------------
# 2.3 Constructor and Destructor
# ---------------------------------------------------------
# - Constructor (__init__): Runs automatically when an object is created.
# - Destructor (__del__): Runs automatically when an object is deleted
#   or when the program finishes.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Constructor called -> Created book:", self.title)

    def display(self):
        print("Book:", self.title, "| Author:", self.author)

    def __del__(self):
        print("Destructor called -> Removed book:", self.title)


print("\n=== 2.3 Constructor and Destructor ===")
b1 = Book("Python Basics", "Guido")
b2 = Book("Clean Code", "Robert")

b1.display()
b2.display()

# Deleting b1 manually triggers its destructor immediately
del b1
print("End of OOP script (b2 will be destroyed automatically now).")
