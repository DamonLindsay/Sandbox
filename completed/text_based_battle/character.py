from weapon import *
from health_bar import HealthBar


class Character:

    def __init__(self, name: str, health: int, weapon: str) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon

    def attack(self, target) -> None:
        target.health -= self.weapon.weapon_dps
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.weapon_dps} damage to {target.name} with {self.weapon.name}.")


class Hero(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health, weapon=weapon)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, colour="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health, weapon=weapon)
        self.health_bar = HealthBar(self, colour="red")
