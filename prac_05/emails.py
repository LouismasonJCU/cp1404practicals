"""
estimated the amount of time for this question : 50 minutes
actual time :

"""
def main():
    """create dictionary for email_to_name"""
    email_to_name ={}
    email = input("email :")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"is your name {name}? (y/n) :").upper()
        if confirmation.upper() != "y" or confirmation != " ":
            name = input("name : ")
        email_to_name[email] = name
        email = input("email :")

    for email , name in email_to_name.items():
        print (f"{name} ({email})")

def extract_name_from_email(email):
    """extract potential names from email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()