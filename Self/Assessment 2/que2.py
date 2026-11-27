# #Create an Employee class with the following requirements:
# 1. Create a constructor.
# 2. Store Employee ID and Employee Name.
# 3. Create a method called display().
# 4. Create two objects.
# 5. Display details of both employees.

import grade

class employee:
    def __init__(self,eid,ename,marks):
        self.eid=eid
        self.ename=ename
        self.marks=marks

    def display(self):
        print("\nEmployee id :",self.eid)
        print("Employee Name :",self.ename)
        print("Marks :",self.marks)
        result=grade.calculate(self.marks)
        print("Grade :",result)
        

    def get_eid(self):
        return self.eid

    def set_eid(self,eid):
        if 0 < eid <=100:   
            self.eid=eid
        else:
            print("Invalid Id, Enter id between 1 to 100")

e1 = employee(10, "Yogesh", 10)
e2 = employee(20, "Nikhil", 20)

print("Before updating:")
e1.display()
e2.display()

e1.set_eid(67)
e2.set_eid(51)

print("\nAfter updating:")
print(e1.get_eid())
print(e2.get_eid())

