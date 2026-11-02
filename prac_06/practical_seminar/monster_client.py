from prac_06.practical_seminar.monster import Monster
#
name=input("what is your name :")
number_of_teeth = int(input("how many teeth do you have?"))
colour = input("what colour do you have?")

monster = Monster(name,number_of_teeth,colour)
print(monster)

#
# monsters = [Monster("streissand",500,"peach"),Monster("goofy",32,"black"), Monster("lospollostv",1000,"peach")]
#
# scary_monsters=[monster for Monster in monsters if mosnter.]