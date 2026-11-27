class student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def display(self):
        print("Roll Number :",self.roll,"\nName :",self.name)

s1=student(101,"Omkar")
s1.display()