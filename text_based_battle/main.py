import os
import random

from character import Hero, Enemy
from weapon import *

hero = Hero(name="Hero", health=100, weapon=random.choice(weapons))
enemy = Enemy(name="Enemy", health=100, weapon=random.choice(weapons))

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
