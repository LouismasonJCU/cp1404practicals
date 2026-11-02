def User :
    def __init__(self,name):
        self.name = name
        self.number_of_taco =5
        self.score=0

    def give_taco(self,other_user):
        if self.number_of_taco > 0:
            self.number_of_taco -= 1
            other_user.score +=1
        else:
            print(f"{self.name}has no taco to give , they poor as hell")

    def __str__(self):
        return f"{self.name} ,{self.score} points , {self.number_of_taco} tacos left "

user1=user("ben")
user2=user("jim")
print(user1)
print(user2)
user1.give_taco(user2)
