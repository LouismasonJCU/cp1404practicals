from jcu_member import JcuMember
from datetime import datetime

from prac_06.practical_seminar import student


class Student(JcuMember):
    def __init__(self, student_id = str , total_score = float , #arg , **kwargs):
        super().__init__(*arg, **kwargs)
        self.student_id = student_id
        self.total_score = total_score

    def get_average_score(self):
        return f"{self.total_score / 6:.2f}"

    def __str__(self):
        return f"{super().__str__()}. student is {self.student_id}. average score is {self.get_average_score()}"

student = Student("1231421", 435634.6, "Lea", datetime)
print(student)

