def display_fruits(**kwargs):
    print(kwargs, type(kwargs))

display_fruits(kiwi=5, mango=9, apple=10)
display_fruits(kiwi=5, mango=9, apple=10, grape=20, passionfruit=35)