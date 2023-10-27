"""Plant (Potential exam question)"""


class Plant:
    def __init__(self, name="", height=0.0, growth_rate=1.0):
        self.name = name
        self.height = height
        self.growth_rate = growth_rate

    # def __str__(self):
    #     return f"{self.name} {self.height} {self.growth_rate}"

    def feed(self, amount_of_water):
        self.height += amount_of_water * self.growth_rate
