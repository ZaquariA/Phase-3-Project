-- Create the customers table
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

-- Create the pizzas table
CREATE TABLE IF NOT EXISTS pizzas (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    toppings TEXT,
    size TEXT,
    price REAL,
    order_id INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id)
);

-- Create the orders table
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total_amount REAL,
    status TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);
