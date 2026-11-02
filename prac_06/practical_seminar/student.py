class Student : #new*

    def __init__(self, name="", date_of_birth="",gpa=0.0): #new *
        self.name = name
        self.date_of_birth = date_of_birth
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} {self.date_of_birth} {self.gpa}"

p1 = Student("lukas","21/august/2006", 3.9)
print(p1.name)
print(p1.date_of_birth)
print(p1)


