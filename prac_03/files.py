# 1:
out_file = open("data.txt","w")
user_name = input("enter your name :")
print(user_name , file=out_file)
out_file.close()

#2
in_file = open("name.txt","w")
name = in_file.read().strip()
print(f"hi {name}")
in_file.close()
