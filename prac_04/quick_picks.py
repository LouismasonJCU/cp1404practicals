import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45
def main():
    number_of_quick_picks = int(input("enter quick picks:"))
    while number_of_quick_picks < 0:
        print("invalid amount of number")
        number_of_quick_picks = int(input("enter quick picks:"))

        for I in range(NUMBERS_PER_LINE):
            quick_pick = []
            for j in range(NUMBERS_PER_LINE):
                number = random.randint(MINIMUM, MAXIMUM)
                while number in quick_pick:
                    number = random.randint(MINIMUM, MAXIMUM)
                quick_pick.append(number)
            quick_pick.sort()
            print(" ".join(f"{number:2}" for number in quick_pick))


main()