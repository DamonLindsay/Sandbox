"""
Musician class module
"""

from person import Person


class Musician(Person):
    def __init__(self, style="", **kwargs):
        super().__init__(**kwargs)
        self.style = style

    def __repr__(self):
        return str(vars(self))

    def play(self, duration):
        return f"{self.name} plays a song for {duration} seconds."
