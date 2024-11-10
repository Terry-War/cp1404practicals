"""CP1404 Prac 07 - My Guitars
Estimated time: 45 minutes
Start at: 18:50
Finish at: 19:50
Total time: 60 minutes
"""

import csv

from prac_07.guitar import Guitar
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

    # Ask the user to input their guitars to the csv list
    print("My New guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    # Write all guitars back to the CSV file
    with open('guitars.csv', 'w') as file:
        # Write header
        file.write("Name,Year,Cost\n")
        # Save each user's guitar data
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

    print("\nAll guitars saved to 'guitars.csv'.")


if __name__ == "__main__":
    main()
