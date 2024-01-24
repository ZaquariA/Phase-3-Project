import ipdb
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

    @classmethod
    def create_customer(cls):
        name = input("Enter the customer name: ")
        address = input("Enter the customer address: ")
        phone = input("Enter the customer phone number: ")

        sql = '''
            INSERT INTO customers (name, address, phone)
            VALUES (?, ?, ?)
        '''
        CURSOR.execute(sql, (name, address, phone))
        CONN.commit()
        print("Customer created successfully.")


    @classmethod
    def update_customer(cls):
        customer_id = input("Enter the customer ID to update: ")
        name = input("Enter the updated name (leave empty to keep current value): ")
        address = input("Enter the updated address (leave empty to keep current value): ")
        phone = input("Enter the updated phone number (leave empty to keep current value): ")

        # Construct the SQL query
        sql = 'UPDATE customers SET'
        values = []

        if name:
            sql += ' name = ?,'
            values.append(name)
        if address:
            sql += ' address = ?,'
            values.append(address)
        if phone:
            sql += ' phone = ?,'
            values.append(phone)

        # Remove the trailing comma from the SQL query
        sql = sql.rstrip(',')
        sql += ' WHERE id = ?'
        values.append(customer_id)

        CURSOR.execute(sql, tuple(values))
        CONN.commit()

        if CURSOR.rowcount > 0:
            print("Customer updated successfully.")
        else:
            print("Customer not found.")

# Customer.create_customer()


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

    @classmethod
    def create_pizza(cls):
        name = input("Enter the pizza name: ")
        size = input("Enter the pizza size: ")
        crust = input("Enter the pizza crust: ")
        toppings = input("Enter the pizza toppings: ")
        price = float(input("Enter the pizza price: "))

        sql = '''
            INSERT INTO pizzas (name, size, crust, toppings, price)
            VALUES (?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (name, size, crust, toppings, price))
        CONN.commit()
        print("Pizza created successfully.")



# Prompt the user to create a pizza before placing an order


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
        if pizza:
            total_price = pizza.price * quantity
            sql = '''
                INSERT INTO orders (customer_id, pizza_id, quantity, total_price)
                VALUES (?, ?, ?, ?)
            '''
            CURSOR.execute(sql, (customer_id, pizza_id, quantity, total_price))
            CONN.commit()
            print("Order placed successfully.")
        else:
            print(f"Pizza with ID {pizza_id} not found.")

    @classmethod
    def view_orders_by_customer(cls, customer_id):
        sql = '''
            SELECT orders.id, pizzas.name, orders.quantity, pizzas.price * orders.quantity AS total_price
            FROM orders
            INNER JOIN pizzas ON orders.pizza_id = pizzas.id
            WHERE orders.customer_id = ?
        '''
        CURSOR.execute(sql, (customer_id,))
        orders = CURSOR.fetchall()
        if orders:
            for order in orders:
                print(f"Order ID: {order[0]}, Pizza: {order[1]}, Quantity: {order[2]}, Total Price: {order[3]}")
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
        print("|\|+++++++++++++++++++++++++++++++++++|/|")
        print("| |                                   | |")
        print("|/|            Pizza Parlor           |\|")
        print("| |                                   | |")
        print("|\|+++++++++++++++++++++++++++++++++++|/|")
        print("| |                                   | |")
        print("|/|       1. View Pizzas              |\|")
        print("| |       2. Add New Customer         | |")
        print("|\|       3. View Customers           |/|")
        print("| |       4. Place Order              | |")
        print("|/|       5. View Orders              |\|")
        print("| |       0. Exit                     | |")
        print("|\|                                   |/|")
        print("| |+++++++++++++++++++++++++++++++++++| |")
        
        choice = input("Enter your choice (1-5, or 0 to exit): ")
        
        if choice in ("0", "1", "2", "3", "4", "5"):
            return choice
        else:
            os.system('cls||clear')
            print("Invalid input! Please select a valid option.")
            input("Press Enter to continue.")

Pizza.create_table_pizza()

def view_pizzas_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             View Pizzas                ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    Pizza.view_all_pizzas()
    choice = input("Do you want to create a pizza (Y/N)? ")
    choice = choice.lower()

    if choice == "y":
        Pizza.create_pizza()    
    input("Press Enter to go back to the main menu.")

Customer.create_table_customer()

def view_customers_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++            View Customers              ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    Customer.view_all_customers()

    # Prompt the user to create or update a customer
    choice = input("Do you want to create a customer (C) or update a customer (U)? ")
    choice = choice.lower()

    if choice == "c":
        Customer.create_customer()
    elif choice == "u":
        Customer.update_customer()
    else:
        print("Invalid choice.")

    input("Press Enter to go back to the main menu.")

Order.create_table_order()

def place_order_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Place Order                ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    customer_id = input("Enter your customer ID: ")
    pizza_id = input("Enter the pizza ID you want to order: ")
    quantity = int(input("Enter the quantity: "))
    Order.place_order(customer_id, pizza_id, quantity)
    input("Press Enter to go back to the main menu.")

def view_orders_menu():
    os.system('cls||clear')
    print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
    print("||                                        ||")
    print("||             View Orders                ||")
    print("||                                        ||")
    print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
    customer_id = input("Enter your customer ID: ")
    Order.view_orders_by_customer(customer_id)
    input("Press Enter to go back to the main menu.")

while True:
    menu_choice = menu()
    if menu_choice == "1":
        view_pizzas_menu()
    elif menu_choice == "2":
        Customer.create_customer()
    elif menu_choice == "3":
        view_customers_menu()
    elif menu_choice == "4":
        place_order_menu()
    elif menu_choice == "5":
        view_orders_menu()
    elif menu_choice == "0":
        break

menu()