# name = "Gibson L-5 CES"
# year = 1922
# cost = 16035.40
# print(f"My guitar: {name}, first made in {year} , the price is {cost:.2f}")

import datetime

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self,year):
        return datetime.datetime.now().year - self.year

    def is_vintage(self, year):
        return self.get_age(year) > 50


