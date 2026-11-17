from prac_06.guitar import Guitar

def main():
    guitars = []
    print("my guitars !")
    name = input("name: ")
    while name != "":
        year = int(input("year:"))
        cost = float(input("cost: $"))
        guitars_to_add = Guitar(name, year, cost)
        guitars.append(guitars_to_add)
        print(f"{name} ({year}): {cost:.2f} added")
        name = input("name:")

    if guitars :
        print("these are my guitars: ")
        for i , guitars in enumerate(guitars, 1):
            vintage_string = ""
            if guitars.is_vintage:
                vintage_string = " (vintage)"
            print(f"guitar {i} : {guitars.name:>20} ({guitars.year}), worth $ {guitars.cost:10,.2f} {vintage_string}")

    else:
        print("no guitars , buy one")
main()

