"""CP1404 Practical 5 - Wimbledon
estimated time: ~ 30-45 mins
started at: 19:00
finished: 19:45
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    """Create dictionary of champions and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]
        countries.add(country)
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for name, count in sorted(champion_to_count.items()):
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_records(filename):
    """Get records from file in list of lists form."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        return [line.strip().split(",") for line in in_file]


main()
