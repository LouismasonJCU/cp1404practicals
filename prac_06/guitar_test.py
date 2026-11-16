from prac_06.guitar import Guitar

guitar = Guitar("synthaxe", 1985, 13000)
other = Guitar("gibson", 1973, 1000)

print(f"{guitar.name} get_age() - Expected 41. Got {guitar.get_age()}")
print(f"{other.name} get_age() - expected 51. got {other.get_age()}")
print(f"{guitar.name} is_vintage() - expected False. got {guitar.is_vintage()}")
print(f"{other.name} is_vintage() - expected True. got {other.is_vintage()}")
# print(guitar.get_age())
# print(guitar.is_vintage())
