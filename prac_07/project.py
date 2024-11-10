"""CP1404 Prac 07 - project
Estimated time: 2 hours combined for both files
Start at: 19:50
Finish at: 20:40
Total time: 50 minutes
"""

import datetime


class Project:
    """Class for project info"""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initializes a Project object with the given attributes."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __repr__(self):
        """Returns a string representation of the Project object."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, " \
               f"completion: {self.percent_complete}%"

    def is_completed(self):
        """Determines if the project is complete (i.e., if the completion percentage is 100)."""
        return self.percent_complete == 100
