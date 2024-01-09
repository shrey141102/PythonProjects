class FoodOrderingSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "Burger", "price": 5.99},
            2: {"name": "Pizza", "price": 8.99},
            3: {"name": "Pasta", "price": 7.49},
            4: {"name": "Salad", "price": 4.99},
            5: {"name": "Soda", "price": 1.99},
        }
        self.order = []

    def display_menu(self):
        print("Menu:")
        for item_id, details in self.menu.items():
            print(f"{item_id}. {details['name']} - ${details['price']}")

    def take_order(self):
        while True:
            try:
                item_id = int(input("Enter the item ID you want to order (0 to finish): "))
                if item_id == 0:
                    break
                elif item_id in self.menu:
                    quantity = int(input("Enter the quantity: "))
                    self.order.append({"item_id": item_id, "quantity": quantity})
                else:
                    print("Invalid item ID. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def calculate_total(self):
        total = 0
        for order_item in self.order:
            item_id = order_item["item_id"]
            quantity = order_item["quantity"]
            total += self.menu[item_id]["price"] * quantity
        return total

    def print_receipt(self):
        print("\nReceipt:")
        for order_item in self.order:
            item_id = order_item["item_id"]
            quantity = order_item["quantity"]
            item_name = self.menu[item_id]["name"]
            item_price = self.menu[item_id]["price"]
            subtotal = item_price * quantity
            print(f"{item_name} x{quantity}: ${subtotal:.2f}")
        total = self.calculate_total()
        print(f"\nTotal: ${total:.2f}")

    def run(self):
        print("Welcome to the Food Ordering System!")
        self.display_menu()
        self.take_order()
        self.print_receipt()
        print("Thank you for using the Food Ordering System!")


if __name__ == "__main__":
    food_ordering_system = FoodOrderingSystem()
    food_ordering_system.run()
