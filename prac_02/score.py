"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    print(f"user score {score:.2f} is {score_status(score)}")
    if score >= 90 :
        print("you get a prize !")
    random_number = random.randint(1,100)
    print(f"{random_number:.2f} is {score_status(random_number)}")
def score_status(score):
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")


main()
