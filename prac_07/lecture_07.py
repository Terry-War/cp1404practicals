"""CP1404 Programming 2 lecture 7"""


class Monitor:
    """Class for monitor"""
    def __init__(self, model="", width=0, height=0):
        """Initialise an instance of monitor details"""
        self.model = model
        self.width = width
        self.height = height

    def __str__(self):
        """Return string version of monitor instance."""
        return f'{self.model}, {self.width}, {self.height}'

    def __gt__(self, other):
        """Return True if monitor is greater than other"""
        return self.get_total_pixels() > other.get_total_pixels()

    def __eq__(self, other):
        """Return True if monitor is equal to other"""
        return self.width == other.width and self.height == other.height

    def get_resolution(self):
        """Determine the resolution of the monitor"""
        return self.width, self.height

    def get_total_pixels(self):
        """Determine the total number of pixels in the monitor"""
        return self.width * self.height

if __name__ == '__main__':
    m = Monitor("Bob", 1280, 900)
    m2 = Monitor("Jess", 1920, 1080)
    print(m)
    print(m2)
    print(m.get_total_pixels())
    print(m2.get_total_pixels())
    print(m > m2)
    print(m == m2)


