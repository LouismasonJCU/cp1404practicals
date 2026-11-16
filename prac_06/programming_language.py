"""
estimated time to complete task : 1 hour
actual time : 1 hour 30 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name ="" , typing ="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} typing, reflection = {self.reflection}, first appeared in {self.year}"

    def is_dynamic(self, typing):
        return self.typing == "Dynamic"

