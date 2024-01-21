

from pizza import Pizza
from customers import Customer

class Order:

    all = []

    def __init__(self, pizza, customer, price):

        self.pizza = pizza
        self.customer = customer
        self.price = price
        Order.all.append(self)


    @property

    def pizza(self):
        return self._pizza
    
    @pizza.setter

    def pizza(self, pizza):
        if isinstance(pizza, Pizza):
            self._pizza = pizza

    @property

    def customer(self):
        return self._customer
    
    @customer.setter

    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 15 < price < 20 and not hasattr(self, 'price'):
            self._price = price
        else:
            raise Exception('Price must be of type float /Price must be beteen 15 and 20/ Price can not change.')
