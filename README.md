# Phase-3-Project

# Contributors:

- Melissa Velasquez

- Zaquari Andl

# One sentence description:

For this project, we'll be working with an Order domain that with take the id's of the Pizza class and Customer class.

# We have three models:

- Order

- Pizza

- Customers

# ERD

- https://dbdiagram.io/d/65ad4da9ac844320ae61aec7

## MVP CRUD

Create - The user will be able to make an order by selecting types of pizzas and seeing a total price.

Read - The user will be able to use CLI to interact and follow a guide to their order.

Update - 

Delete - The user will be able to delete their user if wanted, and will be able to remove pizzas from their order.

# Property Method Plan

Order will take in: self, customer, pizza, and price

Pizza will take in: self and name

Customer will take in: self and name

The Order class will be the main class that gets and sets the Customer and Pizza classes.

The name of the Pizza and Customer classes must be of type str and will raise an exception otherwise.

The price for the Order must be of type float and will raise an exception if otherwise.