"""CP1404 Programming 2 - Prac 10 - wiki
Estimated: 30 minutes
Start: 22:00
Finish: 22:25
Total: 25 minutes
"""

import wikipedia

def main():
    title = input("\nEnter page title (or press Enter to quit): ")
    while title:
        try:
            page = wikipedia.page(title)  # had to remove 'autosuggest'
            print(f"\nTitle: {page.title}")
            print(f"Summary: {page.summary[:500]}...")
            print(f"URL: {page.url}")
        except wikipedia.exceptions.DisambiguationError as error:
            print("\nWe need a more specific title. Try one of the following:")
            print(error.options)
        except wikipedia.exceptions.PageError:
            print(f"\nPage title '{title}' does not match any pages. Try another title!")
        except Exception as error:
            print(f"\nAn unexpected error occurred: {error}")

        title = input("\nEnter page title (or press Enter to quit): ").strip()

    print("Thank you.")

if __name__ == "__main__":
    main()

