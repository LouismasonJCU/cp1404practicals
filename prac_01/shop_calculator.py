total_price = 0
number_of_items= int(input("enter the number of items:"))
while number_of_items < 0 :
    print("error , please enter valid number")
    number_of_items = int(input("enter the number of items:"))

for i in range (number_of_items):
    item_price= float(input("price of item : "))
    total_price+= item_price

if total_price > 100 :
    total_price *= 0.9

print(f"total price of {number_of_items} items are ${total_price:.2f} ")



