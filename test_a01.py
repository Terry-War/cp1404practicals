import csv
import random

# Constants
FILENAME = "places.csv"


# Functions

def load_places(filename):
    places = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            place = [row[0], row[1], int(row[2]), row[3]]
            places.append(place)
    return places


def save_places(filename, places):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(places)


def display_menu():
    print("\nMenu:")
    print("1. List places")
    print("2. Recommend a place")
    print("3. Add a new place")
    print("4. Mark a place as visited")
    print("5. Quit")


def display_welcome_message():
    print("Welcome to the Travel Tracker Program by [Your Name]!")


def list_places(places):
    if not places:
        print("No places stored yet!")
        return

    places.sort(key=lambda x: (x[3], -x[2]))
    max_name_len = max([len(place[0]) for place in places])
    max_country_len = max([len(place[1]) for place in places])

    print(f"{'Name':<{max_name_len}} | {'Country':<{max_country_len}} | Priority | Visited")
    print("-" * (max_name_len + max_country_len + 22))

    unvisited_count = 0
    for place in places:
        visited = '' if place[3] == 'v' else '*'
        unvisited_count += 1 if place[3] == 'n' else 0
        print(f"{place[0]:<{max_name_len}} | {place[1]:<{max_country_len}} | {place[2]:<8} | {visited}")
    print(f"\n{unvisited_count} places left to visit.")


def recommend_place(places):
    unvisited_places = [place for place in places if place[3] == 'n']
    if not unvisited_places:
        print("No places left to visit!")
    else:
        recommendation = random.choice(unvisited_places)
        print(f"Recommended place to visit: {recommendation[0]}, {recommendation[1]} (priority {recommendation[2]})")


def add_place(places):
    name = input("Enter place name: ")
    country = input("Enter country: ")
    while True:
        try:
            priority = int(input("Enter priority: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number for priority.")
    places.append([name, country, priority, 'n'])
    print(f"{name} in {country} (priority {priority}) added to travel list.")


def mark_visited(places):
    list_places(places)
    unvisited_places = [place for place in places if place[3] == 'n']
    if not unvisited_places:
        print("No unvisited places.")
        return

    try:
        choice = int(input("Enter the number of a place to mark as visited: "))
        if 1 <= choice <= len(places):
            if places[choice - 1][3] == 'v':
                print("That place is already visited!")
            else:
                places[choice - 1][3] = 'v'
                print(f"{places[choice - 1][0]} in {places[choice - 1][1]} marked as visited.")
        else:
            print("Invalid place number.")
    except ValueError:
        print("Invalid input; enter a valid number.")


def main():
    places = load_places(FILENAME)
    display_welcome_message()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            list_places(places)
        elif choice == '2':
            recommend_place(places)
        elif choice == '3':
            add_place(places)
        elif choice == '4':
            mark_visited(places)
        elif choice == '5':
            save_places(FILENAME, places)
            print("Travel list saved. Goodbye!")
            break
        else:
            print("Invalid choice; please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
