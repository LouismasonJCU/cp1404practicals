class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display_address(self):
        return f"{self.street} {self.city} {self.zip_code}"

class Person:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        

