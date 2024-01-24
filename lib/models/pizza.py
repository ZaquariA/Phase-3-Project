import sqlite3


CONN = sqlite3.connect('models/pizza.db')
CURSOR = CONN.cursor()


# objects/pizza.py
class Pizza:
    def __init__(self, pizza_type, id=None):
        self.id = id 
        self.pizza_type = pizza_type
        self.toppings = []

    @classmethod
    def create_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS pizzas (
            id INT,
            pizza_type TEXT,
            )
            """
        CURSOR.execute(query)
        CONN.commit()

    def add_toppings(self, toppings):
        self.toppings.extend(toppings)

    def __str__(self):
        toppings_str = ', '.join(self.toppings)
        return f"{self.pizza_type} Pizza with toppings: {toppings_str}"
