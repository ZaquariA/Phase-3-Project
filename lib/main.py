import os
import sqlite3

CONN = sqlite3.connect('pizza_database.db')
CURSOR = CONN.cursor()

class Customer:
    def __init__(self, name, address, phone, customer_id=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.customer_id = customer_id

    @classmethod
    def create_table_customer(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS customers
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone TEXT
            )
        '''
        CURSOR.execute(sql)

    @classmethod
    def view_all_customers(cls):
        sql = '''
            SELECT * FROM customers
        '''
        CURSOR.execute(sql)
        customers = CURSOR.fetchall()
        if customers:
            for customer in customers:
                print(f"ID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}, Phone: {customer[3]}")
        else:
            print("No customers found.")

class Pizza:
    def __init__(self, name, size, crust, toppings, price, pizza_id=None):
        self.name = name
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.price = price
        self.pizza_id = pizza_id

    @classmethod
    def create_table_pizza(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pizzas
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                size TEXT,
                crust TEXT,
                toppings TEXT,
                price REAL
            )
        '''
        CURSOR.execute(sql)

    @classmethod
    def view_all_pizzas(cls):
        sql = '''
            SELECT * FROM pizzas
        '''
        CURSOR.execute(sql)
        pizzas = CURSOR.fetchall()
        if pizzas:
            for pizza in pizzas:
                print(f"ID: {pizza[0]}, Name: {pizza[1]}, Size: {pizza[2]}, Crust: {pizza[3]}, Toppings: {pizza[4]}, Price: {pizza[5]}")
        else:
            print("No pizzas found.")

class Order:
    def __init__(self, customer_id, pizza_id, quantity, total_price, order_id=None):
        self.customer_id = customer_id
        self.pizza_id = pizza_id
        self.quantity = quantity
        self.total_price = total_price
        self.order_id = order_id

    @classmethod
    def create_table_order(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS orders
            (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                pizza_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                FOREIGN KEY(customer_id) REFERENCES customers(id),
                FOREIGN KEY(pizza_id) REFERENCES pizzas(id)
            )
        '''
        CURSOR.execute(sql)

    @classmethod
    def place_order(cls, customer_id, pizza_id, quantity):
        pizza = cls.get_pizza_by_id(pizza_id)
        total_price = pizza.price * quantity
        sql = '''
            INSERT INTO orders (customer_id, pizza_id, quantity, total_price)
            VALUES (?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (customer_id, pizza_id, quantity, total_price))
        CONN.commit()
        print("Order placed successfully.")

    @classmethod
    def view_orders_by_customer(cls, customer_id):
        sql = '''
            SELECT orders.id, pizzas.name, pizzas.size, pizzas.crust, pizzas.toppings, pizzas.price, orders.quantity, orders.total_price
            FROM orders
            INNER JOIN pizzas ON orders.pizza_id = pizzas.id
            WHERE orders.customer_id = ?
        '''
        CURSOR.execute(sql, (customer_id,))
        orders = CURSOR.fetchall()
        if orders:
            for order in orders:
                print(f"Order ID: {order[0]}, Pizza: {order[1]} ({order[2]}, {order[3]}, {order[4]}), Price: {order[5]}, Quantity: {order[6]}, Total Price: {order[7]}")
        else:
            print("No orders found for this customer.")

    @classmethod
    def get_pizza_by_id(cls, pizza_id):
        sql = '''
            SELECT * FROM pizzas
            WHERE id = ?
        '''
        CURSOR.execute(sql, (pizza_id,))
        pizza = CURSOR.fetchone()
        if pizza:
            return Pizza(*pizza)
        else:
            return None

def menu():
    while True:
        os.system('cls||clear')
        print("+++++++++++++++++++++++++++++++++++++++")
        print("++                                   ++")
        print("++            Pizza Shop              ++")
        print("++                                   ++")
        print("+++++++++++++++++++++++++++++++++++++++")
        print("++                                   ++")
        print("++       1. View Pizzas              ++")
        print("++       2. View Customers           ++")
        print("++       3. Place Order              ++")
        print("++       4. View Orders              ++")
        print("++       0. Exit                     ++")
        print("++                                   ++")
        print("+++++++++++++++++++++++++++++++++++++++")
        
        choice = input("Enter your choice (1-4, or 0 to exit): ")
        
        if choice in ("0", "1", "2", "3", "4"):
            return choice
        else:
            os.system('cls||clear')
            print("Invalid input! Please select a valid option.")
            input("Press Enter to continue.")

def view_pizzas_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             View Pizzas                 ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    Pizza.view_all_pizzas()
    input("Press Enter to go back to the main menu.")

def view_customers_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++            View Customers               ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    Customer.view_all_customers()
    input("Press Enter to go back to the main menu.")

def place_order_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Place Order                 ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    customer_id = input("Enter your customer ID: ")
    pizza_id = input("Enter the pizza ID you want to order: ")
    quantity = input("Enter the quantity: ")
    Order.place_order(customer_id, pizza_id, quantity)
    input("Press Enter to go back to the main menu.")

def view_orders_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             View Orders                 ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    customer_id = input("Enter your customer ID: ")
    Order.view_orders_by_customer(customer_id)
    input("Press Enter to go back to the main menu.")

while True:
    menu_choice = menu()
    if menu_choice == "1":
        
    