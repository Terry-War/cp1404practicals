"""CP1404 - Practicals 4 - Shop calculator"""

total_price = 0
number_of_items = int(input("Enter the number of items: "))
while number_of_items <= 0:
    print("Invalid number of items.")
    number_of_items = int(input("Enter the number of items: "))
for i in range(number_of_items):
    price = float(input(f"Enter the price of item: "))
    total_price += price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"The total price for {number_of_items} is: ${total_price:.2f}")
