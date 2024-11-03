"""CP1404 Prac 06 - guitar
Estimated time: 30 minutes
Start at: 9:45
Finish at: 10:30
Total time: 45 minutes
had to go back a reread the practicals page a few times.
"""

CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """Class for guitar quality"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise an instance of Guitar details"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar"""
        return f"Guitar Name: {self.name}, Year: {self.year}, Cost: {self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage by its age"""
        return self.get_age() >= VINTAGE_YEAR
