class Student:
    def __init__(self):
        self.__name = ""
        self.__rollno = 0
        self.__marks = None

    def set_data(self, name, rollno, marks):
        self.__name = name
        self.__rollno = rollno

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    # Getter Method
    def get_data(self):
        print("Name:", self.__name)
        print("Roll no:", self.__rollno)
        print("Marks:", self.__marks)


# Object creation
s1 = Student()

name = input("Enter Name :")
roll = int(input("Enter Roll No:"))
marks = float(input("Enter Marks:"))

s1.set_data(name, roll, marks)
print("\nStudent Details")
s1.get_data()