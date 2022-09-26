from unicodedata import numeric
import data
from robot import Robot
from dinosaur import Dinosaur
import random
import time

class BattleField:
    def __init__(self):
        self.robot = Robot(data.robots['robot1'])
        self.dinosaur = Dinosaur(data.dinosaurs['dinosaur1'])

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')
        print('First Round')
        print(f'{self.robot.name} VS {self.dinosaur.name}')
        print()

    def display_weapons(self):
        i = 1
        for weapon in self.robot.weapons:
            print(f'{i}) {weapon.name}   Attack Power:  {weapon.attack_power}  Type:  {weapon.type}')
            i += 1
    def display_health(self):
        print(f'{self.robot.name} has {self.robot.health} Health')
        print(f'{self.dinosaur.name} has {self.dinosaur.health} Health') 
        print()      

    def battle_phase(self):
        self.display_weapons()
        user_input = input('Select a Weapon! 1, 2 or 3:  ')
        while True:
            if user_input.isnumeric() and int(user_input) in range(0,4):
                break
            else:
                user_input = input('Please enter a number 1  2 or 3:  ')

        self.robot.active_weapon = self.robot.weapons[int(user_input)-1]
        weapon_attack = self.robot.active_weapon.type
        self.dinosaur.active_attack = random.choice(self.dinosaur.attacks)
        dinosaur_attack = self.dinosaur.active_attack.type
        print()
        print(f'{self.robot.name}\'s {self.robot.active_weapon.name} is going against the {self.dinosaur.name}\'s {self.dinosaur.active_attack.name}')
        print()
        time.sleep(2)
        if weapon_attack == dinosaur_attack:
            print('Neither attack hit!')
            return
        if weapon_attack == 'power':
                if dinosaur_attack == 'precision':
                    self.robot.attack(self.dinosaur)
                elif dinosaur_attack == 'quick':
                    self.dinosaur.attack(self.robot)
        if weapon_attack == 'precision':
                if dinosaur_attack == 'quick':
                    self.robot.attack(self.dinosaur)
                elif dinosaur_attack == 'power':
                    self.dinosaur.attack(self.robot)
        if weapon_attack == 'quick':
                if dinosaur_attack == 'power':
                    self.robot.attack(self.dinosaur)
                else:
                    self.dinosaur.attack(self.robot)
        time.sleep(2)

    def display_winner(self):
        if self.dinosaur.health < 0:
            print(f'{self.robot.name} is VICTORIOUS!!')
        else:
            print(f'{self.dinosaur.name} is VICTORIOUS!!')
            


    def run_game(self):
        self.display_welcome()
        time.sleep(2)
        self.display_health()
        time.sleep(1)
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase()
            if self.robot.health > 0 and self.dinosaur.health > 0:
                self.display_health()
        self.display_winner
        
            

    




                