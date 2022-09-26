from weapons import Weapon
import random

class Robot:
    def __init__(self,dictionary):
        self.name = dictionary['name']
        self.health = dictionary['health']
        self.weapons = [Weapon(dictionary['weapon1']),Weapon(dictionary['weapon2']),Weapon(dictionary['weapon3'])]
        self.active_weapon = random.choice(self.weapons)

    def attack(self,target):
        target.health = target.health - self.active_weapon.attack_power
