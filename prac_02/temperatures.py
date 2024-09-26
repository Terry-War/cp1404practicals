""" CP1404 - Practical 2 - temperature conversion refactoring """


def main():
    menu = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_to_celsius()
        elif choice == "F":
            convert_to_fahrenheit()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9.0 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def convert_to_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
