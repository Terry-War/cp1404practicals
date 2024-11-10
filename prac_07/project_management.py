"""CP1404 Prac 07 - project management
Estimated time: 2 hours combined for both files
Start at: 19:50
Finish at: 20:40
Total time: 50 minutes
I give up....
I don't know how to get this to run or what I'm missing
"""
import datetime
from project import Project

MENU_STRING = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
              "- (F)ilter projects by date\n- (A)dd new project\n" \
              "- (U)pdate project\n- (Q)uit"


def main():
    """The main function of the project management program."""
    filename = 'projects.txt'
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    print(MENU_STRING)

    choice = input(">>> ").lower()

    while choice != "q":
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            save_projects(projects, filename)
            print(f"Projects saved to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice, please try again.")

        # Display the menu again and get the next choice
        print(MENU_STRING)
        choice = input(">>> ").lower()

    save_choice = input(f"Would you like to save to {filename}? (y/n): ").lower()
    if save_choice == 'y':
        save_projects(projects, filename)

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Loads projects from a file and converts them into Project objects."""
    projects = []
    with open('projects.txt', 'r', newline='') as in_file:
        reader = projects(in_file)
        next(reader)  # Skip the header row
        for row in in_file:
            name, Start Date, Priority, Cost Estimate, Completion Percentage = row
            projects = Project(Start Date, Priority, Cost Estimate, Completion Percentage)
    return projects


def save_projects(projects, filename):
    """Saves the list of Project objects to a file."""
    with open(filename, 'w') as output_file:
        for project in projects:
            output_file.write(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
                              f"priority: {project.priority}, estimate: ${project.cost_estimate:.2f}, "
                              f"completion: {project.percent_complete}%\n")
    return projects


def display_projects(projects):
    """Displays all projects, sorted by their completion status and priority."""
    incomplete_projects = []
    completed_projects = []

    for project in projects:
        if project.is_completed():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

def sort_by_start_date(project):
    """Function to sort projects by their start date."""
    return project.start_date


def add_new_project(projects):
    """Adds a new project to the list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)
    return new_project

def update_project(projects):
    """Updates the list of projects."""
        return projects

if __name__ == '__main__':
    main()
