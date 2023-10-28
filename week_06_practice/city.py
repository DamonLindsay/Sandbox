"""City class"""


class City:
    """City class"""

    def __init__(self, name="", population=0, percent=0.0):
        """Initialise a City object."""
        self.name = name
        self.population = population
        self.percent = percent

    def __str__(self):
        """Return string representation of data in a City."""
        return f"{self.name}, {self.population:,}, {self.percent}%"
