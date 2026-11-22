from jcu_member import JcuMember
from datetime import datetime

class Staff(JcuMember):
    def __init__(self, staff_id = str, salary = float, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.staff_id = staff_id
        self.salary = salary

    def calculate_annual_salary(self):
        return f"{self.salary * 12 :.2f}"

    def __str__(self):
        return f"{super().__str__()}{self.staff-id} {self.salary}. annual salary : {self.calculate_annual_salary()}"
    