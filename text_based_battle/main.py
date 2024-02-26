import os

from character import Hero, Enemy
from weapon import *

hero = Hero(name="Hero", health=100, weapon=big_iron_fishing_pole)
enemy = Enemy(name="Enemy", health=100, weapon=fists)

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

