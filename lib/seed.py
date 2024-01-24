c1 = Customer("Zaquari", " 123 Street", "123-456-7890", 1)

p1 = Pizza("Pepperoni", "Medium", "Regular", ["Pepperoni", "Cheese"], 10.50, 1)

o1 = Order(1, 1, 1, 10.50, 1)

        sql = '''
            INSERT INTO customers (name, address, phone)
            VALUES ("Zaquari", " 123 Street", "123-456-7890")
            '''
    CURSOR.execute(sql, ("Zaquari", " 123 Street", "123-456-7890"))
    CONN.commit()