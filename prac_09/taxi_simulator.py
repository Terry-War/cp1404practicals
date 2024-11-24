"""CP1404 Programming 2 - prac 09 - Taxi simulator
Estimated: 60 minutes
Start: 12:00
Finish: 12:45
Total: 45 minutes
This was a colossal effort to get working but once I figured out I could use some previous code and made sure to
reread the prac page over and over again I managed to get this working.
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Display the available taxis and allow user to choose one."""
    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_bill = 0

    menu_string = "\nQ)uit, C)hoose taxi, D)rive"
    print(menu_string)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            current_taxi = choose_taxi(taxis)
        elif choice == 'D':
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(menu_string)
        choice = input(">>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def choose_taxi(taxis):
    """Display the available taxis and allow user to choose one."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(current_taxi, total_bill):
    """Allow the user to drive the chosen taxi and display the trip cost."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return total_bill

    try:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        total_bill += fare
        print(f"Bill to date: ${total_bill:.2f}")
        return total_bill
    except ValueError:
        print("Invalid distance")
        return total_bill


main()
