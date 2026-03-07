class Restaurant:
    def __init__(self, name: str, size: str):
        self.name = name
        self.size = size
        # COMPOSICIÓN: El restaurante nace con su propio menú
        self.menu = []
        self.create_menu() # Llamamos a una función para crear los 10 items

    def create_menu(self):
        # AQUÍ ESTÁN TUS 10 ELEMENTOS MÍNIMOS
        # 3 Bebidas (type_drink, size, name, price)
        self.menu.append(Drinks("Gaseosa", "Mediana", "Coca-Cola", 2.50))
        self.menu.append(Drinks("Juice", "Big", "Natural lemonade", 3.00))
        self.menu.append(Drinks("Beer", "Small", "Corona", 4.00))
        
        # 3 Platos Principales (dish_type, dish_size, name, price)
        self.menu.append(PrincipalDishes("Fast food", "Double", "Hamburguer", 12.00))
        self.menu.append(PrincipalDishes("Spaghetti", "Personal", "Spaghetti", 15.00))
        self.menu.append(PrincipalDishes("Meat", "Family", "Chopped meat", 25.00))
        
        # 2 Postres (dessert_type, portion_size, name, price)
        self.menu.append(Desserts("Cold", "1 scoop", "Ice Cream", 3.50))
        self.menu.append(Desserts("Hot", "1 portion", "Brownie", 4.50))
        
        # 2 Adicionales (portion_size, name, price)
        self.menu.append(AdditionalDishes("for share", "French fries", 5.00))
        self.menu.append(AdditionalDishes("Personal", "salad", 3.00))

class MenuItem:
    def __init__(self, name: str, price: float):    
        self.name = name
        self.price = price

class Order:
    def __init__(self, name: str):    
        self.name = name
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def total_price(self):
        total = 0.0
        for item in self.items:
                total += item.price
        return total
    
    def apply_discount(self):
        asked_drink = False
        asked_principal_dishes = False
        asked_desserts = False
        asked_additional_dishes = False

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
         
        if asked_drink and asked_principal_dishes and asked_desserts and asked_additional_dishes:
            discount = total_price * 0.15
            return total_price - discount
        elif asked_drink and asked_principal_dishes and asked_additional_dishes:
            discount = total_price * 0.10
            return total_price - discount
        else:
            return total_price
            

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


if __name__ == "__main__":
    # 1. Abrimos el restaurante (Se crean los 10 platos automáticamente)
    mi_restaurante = Restaurant("Python Burger", "Grande")
    
    # 2. Llega un cliente a la Mesa 1
    mesa_1 = Order("Orden Mesa 1")
    
    # 3. El cliente pide un Combo 10% (Bebida + Principal + Adicional)
    print("--- Tomando el pedido ---")
    mesa_1.add_item(mi_restaurante.menu[0]) # Pide la Coca-Cola
    mesa_1.add_item(mi_restaurante.menu[3]) # Pide la Hamburguesa
    mesa_1.add_item(mi_restaurante.menu[8]) # Pide las Papas Fritas
    
    # 4. Imprimimos los resultados
    print("\n--- Factura ---")
    print(f"Total sin descuento: ${mesa_1.total_price()}")
    print(f"Total a pagar (con descuento aplicado): ${mesa_1.apply_discount()}")