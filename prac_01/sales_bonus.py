"""
CP1404 - Practical 1 - sales bonus
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode for sales bonus
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 999:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print(f"The bonus for the sales amount ${sales:.2f} is ${bonus:.2f}. Total for this sale = ${sales + bonus:.2f}")
    sales = float(input("Enter sales: $"))
