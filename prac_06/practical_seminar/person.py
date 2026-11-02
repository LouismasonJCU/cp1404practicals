class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return str(vars(self))

p1= Person("jane",19)
print(p1)
people = [Person("alexa",21),Person("siri",25)]
for person in people:
    print(person)
print(people)