"""CP1404 Programming 2 - prac 09 - Unreliable Car
Estimated: 30 minutes combined
Start: 9:15
Finish: 9:35
Total: 20 minutes
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test how reliable the car is."""

    good_car = UnreliableCar("All most perfect", 100, 95)
    bad_car = UnreliableCar("Might not make it home", 100, 15)

    for i in range(1, 15):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)


main()
