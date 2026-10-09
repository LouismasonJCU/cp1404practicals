

def main():
    """complete this program 3with the following structures ,
    menu :
    (G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit)"""

    print("menu: ")
    choice = input(">").upper()
    while choice != "Q" :
        if choice == "G" :
            score = get_score()

        elif choice == "P":
            print(f" your score {score} is {determine_status(score)}")
        else:
            print("invalid choice , try again")
        print("menu :")
        choice = input(">").upper()
    print("farewell")


def get_score():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print( "Invalid score")
        score = float(input("Enter score: "))

    return score




def determine_status(score):
    """Determine the status of a given score."""

    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"




main()