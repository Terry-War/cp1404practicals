"""CP1404/CP5632 Practical - Car class example."""
"""In the used_cars program file, write one new line of code for each of the following:

Create a new Car object called "limo" that is initialised with 100 units of fuel.

Add 20 more units of fuel to this new car object using the add method.

Print the amount of fuel in the car.

Attempt to drive the car 115 km using the drive method.

Now add the __str__ method to the Car class in car.py.
Using f-string formatting. Make it return a string in the following format:
Car, fuel=42, odometer=277
Remember that you can run this method by printing your car object, or passing the car object to the str() function.
Do NOT call the method verbosely like my_car.__str__()

Now add a name field to the Car class (in car.py), and adjust the __init__ and __str__ methods to set and display this respectively. Make the str method return the car's name instead of just "Car".
Now add names (literals) to the constructors where you create Car objects in the used_cars.py program.
Test your work and make sure you can now make and view named cars.

In your used_cars.py program, print your car object/s to make sure that the __str__ method is working as expected."""

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance