"""CP1404 Prac 07 - guitar
Estimated time: 30 minutes
Start at: 18:50
Finish at:
Total time:  minutes
Pinched alot of the code from the walkthrough example to make this work as intended, pretty happy with how it turned out.
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


def main():
    """Read CSV file and sort by oldest to newest year."""
    guitars = []
    # Used the example for reading CSV files from the walkthrough language reader
    # Open and read the CSV file
    with open('guitars.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row

        # Read each row and create Guitar objects
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)

    # Sort the list of guitars by year (oldest to newest)
    guitars.sort()

    # Print the sorted list of guitars
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    main()
