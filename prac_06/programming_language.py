"""
estimated time to complete task : 1 hour
actual time :
"""

class ProgrammingLanguage:
    def __init__(self, name ="" , typing ="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self, typing):
        return self.typing == "Dynamic"

