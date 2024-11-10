"""CP1404 Prac 07 - guitar
Estimated time: 45 minutes
Start at: 18:50
Finish at: 19:50
Total time: 60 minutes
Pinched alot of the code from the walkthrough example to make this work as intended, pretty happy with how it turned out.
Also had to remember how to use open() file method to save data, haven't used it for a while.
"""
import csv

CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """Class for guitar quality."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise an instance of Guitar details."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"Guitar Name: {self.name}, Year: {self.year}, Cost: {self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage by its age."""
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """Define how to compare guitars by year (for sorting purposes)."""
        return self.year < other.year
