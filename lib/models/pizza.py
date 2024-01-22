
# objects/pizza.py
class Pizza:
    def __init__(self, pizza_type):
        self.pizza_type = pizza_type
        self.toppings = []

    def add_toppings(self, toppings):
        self.toppings.extend(toppings)

    def __str__(self):
        toppings_str = ', '.join(self.toppings)
        return f"{self.pizza_type} Pizza with toppings: {toppings_str}"
