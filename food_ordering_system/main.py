import random

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.menu_items = {
            "Burger": FoodItem("Burger", 5.99),
            "Pizza": FoodItem("Pizza", 8.99),
            "Salad": FoodItem("Salad", 4.99),
            # Add more items as needed
        }

    def display_menu(self):
        print("Menu:")
        for item_name, food_item in self.menu_items.items():
            print(f"{item_name}: ${food_item.price}")

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, food_item, quantity=1):
        for _ in range(quantity):
            self.items.append(food_item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

def main():
    menu = Menu()
    order = Order()

    while True:
        menu.display_menu()

        item_name = input("Enter the name of the item you want to order (or 'exit' to finish): ")

        if item_name.lower() == 'exit':
            break

        if item_name in menu.menu_items:
            quantity = int(input("Enter the quantity: "))
            menu_item = menu.menu_items[item_name]
            order.add_item(menu_item, quantity)
            print(f"{quantity} {item_name}(s) added to your order.")
        else:
            print("Invalid item name. Please choose from the menu.")

    print("\nOrder Summary:")
    for item in order.items:
        print(f"{item.name}: ${item.price}")
    print(f"Total: ${order.calculate_total()}")

if __name__ == "__main__":
    main()
