"""CP1404 Programming 2 - prac 09 - walk through example"""

from prac_09.taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
