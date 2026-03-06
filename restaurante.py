class Restaurant:
    def __init__(self, name: str, size: str):
        self.name = name
        self.size = size

class MenuItem:
    def __init__(self, name: str, price: float):    
        self.name = name
        self.price = price

class Order:
    def __init__(self, name: str, item):    
        self.name = name
        self.item = item

class Drinks(MenuItem):
    def __init__(self, type_drink: str, size: str):
        self.type = type_drink
        self.size = size

class PrincipalDishes(MenuItem):
    def __init__(self, dish_type: str, dish_size: str):
        self.dish_type = dish_type
        self.dish_size = dish_size

class Desserts(MenuItem):
    def __init__(self, dessert_type: str, portion_size: str):
        self.dessert_type = dessert_type
        self.portion_size = portion_size

class AdditionalDishes(MenuItem):
    def __init__(self, portion_size: str):
        self.portion_size = portion_size

