"""CP1404 Prac 06 - programming language
estimated time : 30 minutes
Started at: 9:00
finished at: 9:25
total time: 25 minutes
"""


class ProgrammingLanguage:
    """Shows information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """initialise instance for programing language nomenclature"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of the programming language."""
        return f"{self.name},Typing {self.typing},Reflection={self.reflection},First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the programming language is dynamically typed."""
        return self.typing == "Dynamic"
