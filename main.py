class RestaurantMenu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, name, price):
     self.menu_items[name] = price

    def get_price(self, name):
     return self.menu_items.get(name, None)

    def main():
        menu = RestaurantMenu()
        # Add initial menu items
        menu.add_item("Burger", 10.99)
        menu.add_item("Fries", 4.99)

    if __name__ == "_main_":
        main()