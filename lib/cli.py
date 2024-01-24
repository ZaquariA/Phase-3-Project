from models.customers import Customer
from models.orders import Order
from models.pizza import Pizza



# Constants for pricing
PIZZA_BASE_PRICE = 20
TOPPING_PRICE = 0.75

def calculate_order_total(order):
    total_price = PIZZA_BASE_PRICE * len(order.pizzas)

    for pizza in order.pizzas:
        total_price += TOPPING_PRICE * len(pizza.toppings)

    return total_price

def main():
    print("Welcome to the Pizza Parlor System!")
    
    # Gather customer information
    customer_name = input("Enter your name: ")
    customer = Customer(customer_name)

    # Create an order
    order = Order(customer)

    # Allow user to order pizzas
    while True:
        pizza_type = input("Choose pizza type (Margherita, Pepperoni, Hawaiian, Cheese, Sausage, BBQ chicken): ")
        pizza = Pizza(pizza_type)

        # Add toppings
        toppings = input("Add toppings (comma-separated): ")
        pizza.add_toppings(toppings.split(','))

        # Add pizza to the order
        order.add_pizza(pizza)

        # Ask if the customer wants to order another pizza
        another_pizza = input("Do you want to order another pizza? (yes/no): ").lower()
        if another_pizza != 'yes':
            break

    # Display order details
    print("\nOrder Summary:")
    print(order)

    # Calculate and display total price
    total_price = calculate_order_total(order)
    print(f"\nTotal Price: ${total_price:.2f}")


if __name__ == "__main__":
    main()