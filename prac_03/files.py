# 1:
out_file = open("data.txt","w")
user_name = input("enter your name :")
print(user_name , file=out_file)
out_file.close()

#2
in_file = open("name.txt","r")
name = in_file.read().strip()
in_file.close()
print(f"hi {name}!")
