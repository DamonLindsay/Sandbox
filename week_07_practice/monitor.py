"""
Monitor class
"""


class Monitor:
    def __init__(self, model="", width=0, height=0):
        """Initialize the Monitor object."""
        self.model = model
        self.width = width
        self.height = height

    def __str__(self):
        """Return the string version of the Monitor object."""
        return f"{self.model} {self.width} {self.height}"

    def get_resolution(self):
        """Return the resolution."""
        return (self.width, self.height)
