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
                print(f"ID: {customer[0]} || Name: {customer[1]} || Address: {customer[2]} || Phone: {customer[3]}")
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


        sql = sql.rstrip(',')
        sql += ' WHERE id = ?'
        values.append(customer_id)

        CURSOR.execute(sql, tuple(values))
        CONN.commit()

        if CURSOR.rowcount > 0:
            print("Customer updated successfully.")
        else:
            print("Customer not found.")
            
    @classmethod
    def delete_customer(cls, customer_id):
        sql = '''
            DELETE FROM customers
            WHERE id = ?
        '''
        CURSOR.execute(sql, (customer_id,))
        CONN.commit()
        print("Customer deleted successfully.")

    @classmethod
    def get_customer(cls, customer_input):
        sql = '''
            SELECT * FROM customers
            WHERE id = ? OR name = ?
        '''
        CURSOR.execute(sql, (customer_input, customer_input))
        customer = CURSOR.fetchone()
        if customer:
            return cls(*customer)
        else:
            return None

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
                print(f"ID: {pizza[0]} || Name: {pizza[1]} || Size: {pizza[2]} || Crust: {pizza[3]} || Toppings: ({pizza[4]}) || Price: {pizza[5]}")
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

    @classmethod
    def delete_pizza(cls, pizza_id):
        sql = '''
            DELETE FROM pizzas
            WHERE id = ?
        '''
        CURSOR.execute(sql, (pizza_id,))
        CONN.commit()
        print("Pizza deleted successfully.")

    @classmethod
    def update_pizza(cls):
        pizza_id = input("Enter the pizza ID to update: ")
        name = input("Enter the updated name (leave empty to keep current value): ")
        size = input("Enter the updated size (leave empty to keep current value): ")
        crust = input("Enter the updated crust (leave empty to keep current value): ")
        toppings = input("Enter the updated toppings (leave empty to keep current value): ")
        price = input("Enter the updated price (leave empty to keep current value): ")


        sql = 'UPDATE pizzas SET'
        values = []

        if name:
            sql += ' name = ?,'
            values.append(name)
        if size:
            sql += ' size = ?,'
            values.append(size)
        if crust:
            sql += ' crust = ?,'
            values.append(crust)
        if toppings:
            sql += ' toppings = ?,'
            values.append(toppings)
        if price:
            sql += ' price = ?,'
            values.append(price)

        sql = sql.rstrip(',')
        sql += ' WHERE id = ?'
        values.append(pizza_id)

        CURSOR.execute(sql, tuple(values))
        CONN.commit()

        if CURSOR.rowcount > 0:
            print("Pizza updated successfully.")
        else:
            print("Pizza not found.")

    @classmethod
    def get_most_ordered_pizza(cls):
        sql = '''
            SELECT pizzas.name, COUNT(orders.pizza_id) AS order_count
            FROM pizzas            INNER JOIN orders ON pizzas.id = orders.pizza_id
            GROUP BY pizzas.name
            ORDER BY order_count DESC
            LIMIT 1
        '''
        CURSOR.execute(sql)
        most_ordered_pizza = CURSOR.fetchone()
        if most_ordered_pizza:
            pizza_name, order_count = most_ordered_pizza
            print(f"Fan favorite: {pizza_name}, with {order_count} sold!")
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
                print(f"Order ID: {order[0]} || Pizza: {order[1]} || Quantity: {order[2]} || Total Price: {order[3]}")
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
        
    @classmethod
    def delete_order(cls, order_id):
        sql = '''
            DELETE FROM orders
            WHERE id = ?
        '''
        CURSOR.execute(sql, (order_id,))
        CONN.commit()
        print("Order deleted successfully.")
    

def menu():
    while True:
        os.system('cls||clear')
        print("_________________________________________")
        print("|\|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|/|")
        print("| |                                   | |")
        print("|/|            Pizza Parlor           |\|")
        print("| |                                   | |")
        print("|\|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|/|")
        print("| |                                   | |")
        print("|/|       1. View Pizzas              |\|")
        print("| |       2. Add New Customer         | |")
        print("|\|       3. View Customers           |/|")
        print("| |       4. Place Order              | |")
        print("|/|       5. View Orders              |\|")
        print("| |       0. Exit                     | |")
        print("|\|                                   |/|")
        print("| |                                   | |")
        
        choice = input("Enter your choice (1-5, or 0 to exit): ")
        
        if choice in ("0", "1", "2", "3", "4", "5"):
            return choice
        else:
            os.system('cls||clear')
            print("Invalid input! Please select a valid option.")
            input("Press Enter to continue.")

Pizza.create_table_pizza()

def view_pizzas_menu():
    while True:
        os.system('cls||clear')
        print("______________________________________________")
        print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
        print("|/|                                        |\|")
        print("| |             Hand Tossed Pizzas         | |")
        print("|\|                                        |/|")
        print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
        Pizza.get_most_ordered_pizza()
        Pizza.view_all_pizzas()
        choice = input("Do you want to create a pizza (Y/N), update a pizza(u), or delete a pizza?(id#) ")
        choice = choice.lower()

        if choice == "y":
            Pizza.create_pizza()
        elif choice == "u":
            Pizza.update_pizza()
        elif choice.isdigit():
            Pizza.delete_pizza(choice)
        elif choice == "n":
            break
        else:
            print("Invalid choice. Please select a valid option.")
        input("Press Enter to continue.")

    if choice == "y":
        Pizza.create_pizza()    
    input("Press Enter to go back to the main menu.")

Customer.create_table_customer()

def view_customers_menu():
    os.system('cls||clear')
    print("______________________________________________")
    print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
    print("|/|                                        |\|")
    print("| |          Our Valued Customers          | |")
    print("|\|                                        |/|")
    print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
    Customer.view_all_customers()

    # Prompt the user to create or update a customer
    choice = input("Do you want to update a customer (U), or delete a customer? (Id#) ")
    choice = choice.lower()

    if choice == "u":
        Customer.update_customer()
    elif choice.isdigit():
        Customer.delete_customer(choice)
    else:
        print("Invalid choice.")

    input("Press Enter to go back to the main menu.")

Order.create_table_order()

def place_order_menu():
    while True:
        os.system('cls||clear')
        print("______________________________________________")
        print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
        print("|/|                                        |\|")
        print("| |           Call in an Order             | |")
        print("|\|                                        |/|")
        print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
        choice = input("Do you want to place an order? (Y/N): ")
        choice = choice.lower()

        if choice == "y":
            os.system('cls||clear')
            print("______________________________________________")
            print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
            print("|/|                                        |\|")
            print("| |                Customers               | |")
            print("|\|                                        |/|")
            print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
            Customer.view_all_customers()
            customer_input = input("Enter the customer name or ID: ")
            customer = Customer.get_customer(customer_input)

            if customer:
                customer_id = customer.customer_id
            else:
                print("Customer not found.")
                continue

            os.system('cls||clear')
            print("______________________________________________")
            print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
            print("|/|                                        |\|")
            print("| |                Pizzas                  | |")
            print("|\|                                        |/|")
            print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
            Pizza.view_all_pizzas()
            pizza_id = input("Enter the pizza ID: ")
            quantity = int(input("Enter the quantity: "))
        elif choice == "n":
            break
        else:
            print("Invalid choice.")
            continue

        Order.place_order(customer_id, pizza_id, quantity)
        input("Press Enter to go back to the main menu.")

            


def view_orders_menu():
    os.system('cls||clear')
    print("______________________________________________")
    print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
    print("|/|                                        |\|")
    print("| |           Checkout Orders              | |")
    print("|\|                                        |/|")
    print("| |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |")
    Customer.view_all_customers()
    customer_input = input("Enter the customer name or ID: ")
    customer = Customer.get_customer(customer_input)

    if customer:
            customer_id = customer.customer_id
    else:
        print("Customer not found.")
    
    Order.view_orders_by_customer(customer_id)
    choice = input("To remove order, enter order ID#:")
    if choice.isdigit():
        Order.delete_order(choice)
    else:
        print("Invalid choice.")
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