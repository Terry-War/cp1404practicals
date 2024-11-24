"""CP1404 Programming 2 - prac 09 - Band
Estimated: too long
Start: 11:00
Finish: 12:00
Total: 60 minutes
"""

class Band:
    """Band Class"""

    def __init__(self, name=""):
        """Initialize Band Class"""
        self.name = name
        self.musicians = []  # List to hold musicians in the band

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join([musician.name for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of the Band with musician details."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the band playing, calling each musician's play method."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
