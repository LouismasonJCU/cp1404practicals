"""
estimated the amount of time for this question : 50 minutes
actual time :

"""

# email_to_name ={}
# email = input("email :")
# while email != " ":
#     name = extract_name_from_email(email)
#     confirmation:

def extract_name_from_email(email):
 """extract potential names from email"""
email = "john.smith@gmail.com"
prefix = email.split('@')[0]
# print(prefix)
parts = prefix.split('.')
print(parts)

