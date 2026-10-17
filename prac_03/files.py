# 1:
out_file = open("data.txt","w")
user_name = input("enter your name :")
print(user_name , file=out_file)
out_file.close()