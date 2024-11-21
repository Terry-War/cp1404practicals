"""CP1404 Programming 2 - prac 09 - Unreliable Car
Estimated: 30 minutes combined
Start: 9:15
Finish: 9:35
Total: 20 minutes
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an object for a unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on how reliable it is."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
