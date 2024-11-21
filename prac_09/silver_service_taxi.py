"""CP1404 Programming 2 - prac 09 - silver service taxi
Estimate: 30 minutes combined with test
Start: 9:35
Finish: 9:55
Total: 20 minutes
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a fancy silver taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise an object for SilverServiceTaxi."""
        super().__init__(name, fuel, price_per_km=0)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()
