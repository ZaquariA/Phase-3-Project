class Order:

    def __init__(self, pizza, customer, price):

        self.pizza = pizza
        self.customer = customer
        self.price = price


class Pizza:

    def __init__(self, name):

        self.name = name

class Customer:

    def __init__(self, name):

        self.name = name