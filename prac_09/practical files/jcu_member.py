from datetime import datetime

class JcuMember:
    def __init__(self, name = "" , date_of_birth = ""):
        self.name = name
        self.date_of_birth = date_of_birth
    def __str__(self):
        date_string = datetime.strftime(self.date_of_birth,"%d/%m/%Y")
        return f"{self.name} is age ({selfget_age()}). birthday is on {date_string}"

    def get_age(self):
        return int((datetime.now() - self.date_of_birth).days)