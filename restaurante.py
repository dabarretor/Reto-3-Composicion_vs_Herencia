"""This program allows us to create a restaurant with a menu of 10
(3 drinks, 3 main dishes, 2 desserts, and 2 additional dishes).
We take customer orders and apply discounts depending on the combo they order.
The program demonstrates the use of classes, composition, and inheritance in Python.
"""

class Restaurant:
    def __init__(self, name: str, size: str):
        self.name = name
        self.size = size
        # Composition: the restaurant is created with its own menu
        self.menu: list["MenuItem"] = []
        self.create_menu()  # We call a function to create the 10 items

    def create_menu(self):
        # There are your 10 minimum items
        # 3 Drinks (type_drink, size, name, price)
        self.menu.append(Drinks("Gaseosa", "Mediana", "Coca-Cola", 2.50))
        self.menu.append(Drinks("Juice", "Big", "Natural lemonade", 3.0))
        self.menu.append(Drinks("Beer", "Small", "Corona", 4.0))

        # 3 Main Dishes (dish_type, dish_size, name, price)
        self.menu.append(PrincipalDishes("Fast food", "Double", "Hamburguer", 12.0))
        self.menu.append(PrincipalDishes("Spaghetti", "Personal", "Spaghetti", 10.0))
        self.menu.append(PrincipalDishes("Meat", "Family", "Chopped meat", 25.0))

        # 2 Desserts (dessert_type, portion_size, name, price)
        self.menu.append(Desserts("Cold", "1 scoop", "Ice Cream", 3.50))
        self.menu.append(Desserts("Hot", "1 portion", "Brownie", 4.50))

        # 2 AdditionalDishes (portion_size, name, price)
        self.menu.append(AdditionalDishes("for share", "French fries", 3.50))
        self.menu.append(AdditionalDishes("Personal", "salad", 2.25))

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"

class Order:
    def __init__(self, name: str):
        # allows us to identify the order, for example,
        # if it's for a specific table or a takeout order.
        self.name = name
        self.items: list["MenuItem"] = []

    # The add_item method allows us to add items to the order,
    # which will be stored in the items list.
    def add_item(self, item: MenuItem):
        self.items.append(item)

    # The total_price method calculates the total price of all items in the order.
    def total_price(self):
        total = 0.0
        for item in self.items:
            total += item.price
        return total

    """ 
    In apply_discount allows identify the orders for determine 
    if gets discount of 15% or 10%.
    Receive a 10% discount when you place three orders from the following
    subclasses: drinks, main courses, and side dishes.
    Receive a 15% discount when you place all orders from all subclasses.
    """

    def apply_discount(self):
        # allows us to identify if the order includes items from each of the subclasses
        # (Drinks, PrincipalDishes, Desserts, AdditionalDishes)
        # to determine the applicable discount.
        asked_drink = False
        asked_principal_dishes = False
        asked_desserts = False
        asked_additional_dishes = False
        # We iterate through the items in the order and check their type to set
        # the corresponding flags (asked_drink, asked_principal_dishes, etc.)
        # to True if an item of that type is found.
        for item in self.items:
            if isinstance(item, Drinks):
                asked_drink = True
            if isinstance(item, PrincipalDishes):
                asked_principal_dishes = True
            if isinstance(item, Desserts):
                asked_desserts = True
            if isinstance(item, AdditionalDishes):
                asked_additional_dishes = True

        total_price = self.total_price()

        if (
            asked_drink
            and asked_principal_dishes
            and asked_desserts
            and asked_additional_dishes
        ):
            discount = total_price * 0.15
            return round(total_price - discount, 2)
        elif asked_drink and asked_principal_dishes and asked_additional_dishes:
            discount = total_price * 0.10
            return round(total_price - discount, 2)
        else:
            return round(total_price, 2)

class Drinks(MenuItem):
    def __init__(self, type_drink: str, size: str, name: str, price: float):
        super().__init__(name, price)
        self.type = type_drink
        self.size = size

class PrincipalDishes(MenuItem):
    def __init__(self, dish_type: str, dish_size: str, name: str, price: float):
        super().__init__(name, price)
        self.dish_type = dish_type
        self.dish_size = dish_size

class Desserts(MenuItem):
    def __init__(self, dessert_type: str, portion_size: str, name: str, price: float):
        super().__init__(name, price)
        self.dessert_type = dessert_type
        self.portion_size = portion_size

class AdditionalDishes(MenuItem):
    def __init__(self, portion_size: str, name: str, price: float):
        super().__init__(name, price)
        self.portion_size = portion_size

# test of program functionality
if __name__ == "__main__":
    # The restaurant opens (with all 10 dishes available)
    my_restaurant = Restaurant("The Corral Python", "Big")

    # The client arrives at table 1
    table_1 = Order("Table order 1")

    # The client orders a 10% combo (Drink + Main Course + Additional Dish)
    print("--- Taking the order ---".center(38))
    table_1.add_item(my_restaurant.menu[0])  # Order Coca-Cola
    table_1.add_item(my_restaurant.menu[3])  # Order Hamburguer
    table_1.add_item(my_restaurant.menu[8])  # Order the French fries
    print("-" * 35)
    print(f"Order 1: {my_restaurant.menu[0]}")
    print(f"Order 2: {my_restaurant.menu[3]}")
    print(f"Order 3: {my_restaurant.menu[8]}")

    # The results are printed
    print("Bill".center(35))
    print("-" * 35)
    print(f"total without discount: ${round(table_1.total_price(), 2)}")  # Output: 18.0
    print(
        f"Discount applied: ${round(table_1.total_price() - table_1.apply_discount(), 2)}"
    )  # Output: 1.8
    print(
        f"Total to pay (with discount applied): ${round(table_1.apply_discount(), 2)}"
    )  # Output: 16.2
    print("-" * 35)
    print("¡Thanks for your visit, see you later!")
