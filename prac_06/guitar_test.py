"""CP1404 Prac 06 - guitar test
Estimated time: 30 minutes
Start at: 17:00
Finish at: 17:20
Total time: 20 minutes
"""

from prac_06.guitar import Guitar

def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{guitar.name} get_age() - Expected {102}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {11}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()
