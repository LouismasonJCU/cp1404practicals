MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("enter your name :")

print(MENU)
choice =input (">>>").upper()

while choice != "Q":
    if choice == "H":
        print ("hello ", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("invalid option , try again")
    print(MENU)
    Choice = input (">>>").upper()
print("thank you")
