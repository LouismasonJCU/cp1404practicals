def main() :
    get_password()


def get_password():
    password = input("enter password :")
    while len(password) < MINIMUM_LENGTH:
        print("password is too short")
        password = input("enter password: ")


main()