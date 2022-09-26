from unicodedata import numeric
import data
from robot import Robot
from dinosaur import Dinosaur
import random

class BattleField:
    def __init__(self):
        self.robot = Robot(data.robots['robot1'])
        self.dinosaur = Dinosaur(data.dinosaurs['dinosaur1'])

    def display_weapons(self):
        i = 1
        for weapon in self.robot.weapons:
            print(f'{i}) {weapon.name}   Attack Power:  {weapon.attack_power}  Type:  {weapon.type}')
            i += 1

    def battlephase(self):
        self.display_weapons()
    
        user_input = input('Select a Weapon! 1, 2 or 3 ')
        while True:
            if user_input.isnumeric() and int(user_input) in range(0,4):
                break
            else:
                user_input = input('Please enter a number 1  2 or 3  ')

        self.robot.active_weapon = self.robot.weapons[int(user_input)-1]
        weapon_attack = self.robot.active_weapon.type
        dinosaur_attack = random.choice(self.dinosaur.attack_types)

        if weapon_attack == dinosaur_attack:
            print('Neither attack hit!')
            print(f'The {self.dinosaur.name} remains at {self.dinosaur.health} Health')
            print(f'{self.robot.name} has {self.robot.health} Health remaining.')
            return
        if weapon_attack == 'power':
                if dinosaur_attack == 'percision':
                    self.robot.attack(self.dinosaur)
                elif dinosaur_attack == 'quick':
                    self.dinosaur.quick_attacked(self.robot)
        if weapon_attack == 'percision':
                if dinosaur_attack == 'quick':
                    self.robot.attack(self.dinosaur)
                elif dinosaur_attack == 'power':
                    self.dinosaur.power_attacked(self.robot)
        if weapon_attack == 'quick':
                if dinosaur_attack == 'power':
                    self.robot.attack(self.dinosaur)
                else:
                    self.dinosaur.percision_attacked(self.robot)




                