# objects/order.py
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def __str__(self):
        order_details = f"Customer: {self.customer.name}\n"
        order_details += "Pizzas:\n"
        for pizza in self.pizzas:
            order_details += f"  - {pizza}\n"
        return order_details
