"""Drive"""


def drive(self, distance):
    """Drive the car a given distance if enough fuel."""
    if distance > self.fuel:
        distance = self.fuel
        self.fuel = 0
    else:
        self.fuel -= distance

    self._odometer += distance
    return distance
