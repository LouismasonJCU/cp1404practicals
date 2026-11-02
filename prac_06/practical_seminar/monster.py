
TEETH_TRESHOLD = 16

class Monster:

    def __init__(self,name="mike",number_of_teeth=0,colour="blue"):
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour= colour

    def is_scary(self):
        return self.number_of_teeth > TEETH_TRESHOLD or self.color =='red'

    def __str__(self):
        return f"{self.name},{self.number_of_teeth},{self.colour},{self.is_scary()}"

# monster = Monster()
# print(monster.is_scary())
#
#
#     def __str__(self):
#         return f"{self.name}({self.colour})"
#
#     def __int__(self):
#         return f"{self.number_of_teeth}"
#
#     def __repr__(self):
#         return str(vars(self))
#
#
# p1 = Monster("mike",0,"blue")
# print(p1)
# monsters = [Monster("streissand",500,"peach"),Monster("goofy",32,"black")]
# for monster in monsters :
#     print(monster)
# print(monsters)
