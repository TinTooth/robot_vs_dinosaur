from unicodedata import numeric
import data
from robot import Robot
from herd import Herd
from fleet import Fleet
import random
import time

class BattleField:
    def __init__(self):
        self.fleet = Fleet(data.robots)
        self.robot = 'TBD'
        self.herd = Herd(data.dinosaurs)
        self.dinosaur = random.choice(self.herd.dinosaurs)
        self.herd.dinosaurs.remove(self.dinosaur)


    def choose_robot(self):
        i = 1
        for robot in self.fleet.robots:
            print(f'{i}) {robot.name} ')
            i +=1
        choice = (input('Pick Your Starting Robot by number!  '))
        while True:
            if choice.isnumeric() and int(choice) in range(len(self.fleet.robots)):
                break
            else:
                choice = input('Please enter a correct number:  ')
        self.robot = self.fleet.robots[int(choice) -1]
        self.fleet.robots.remove(self.robot)

    def display_fighters(self,prompt):
        print()
        print(prompt)
        print(f'{self.robot.name} VS {self.dinosaur.name}')

    def display_welcome_start_game(self):
        print()
        print('Welcome to Robots vs Dinosaurs!')
        self.choose_num_of_fighters()
        self.display_fighters("The First Fighters!")
        print()

    def choose_num_of_fighters(self):
        user_input = input('How many Fighters per Team? 1, 2 or 3:  ')
        while True:
            if user_input.isnumeric() and int(user_input) in range(0,4):
                break
            else:
                user_input = input('Please enter a number 1  2 or 3:  ')
        self.choose_robot()
        if user_input == '1':
            self.fleet.fleetsize -= 2
            self.herd.herdsize -= 2
        elif user_input == '2':
            self.fleet.fleetsize -= 1
            self.herd.herdsize -= 1

    def display_weapons(self):
        i = 1
        for weapon in self.robot.weapons:
            print(f'{i}) {weapon.name}   Attack Power:  {weapon.attack_power}  Type:  {weapon.type}')
            i += 1
    def display_health(self):
        print()
        print(f'{self.robot.name} has {self.robot.health} Health')
        print(f'{self.dinosaur.name} has {self.dinosaur.health} Health') 
        print()      

    def select_weapon(self):
        pass
        
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
        time.sleep(1)
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
       

    def display_winner(self):
        print()
        if self.herd.herdsize == 0:
            print(f'The Robots are VICTORIOUS!!')
        else:
            print(f'The Dinosaurs are VICTORIOUS!!')
        print()
            


    def run_game(self):
        self.display_welcome_start_game()
        self.display_health()
        time.sleep(2)
        i = 1
        while self.herd.herdsize > 0 and self.fleet.fleetsize > 0:
            while self.robot.health > 0 and self.dinosaur.health > 0:
                print(f'ROUND {i} ---------------------------------------------')
                self.battle_phase()
                if self.robot.health > 0 and self.dinosaur.health > 0:
                    self.display_health()
                i = i+1
                time.sleep(1)
            if self.robot.health <= 0:
                self.fleet.fleetsize -= 1
            if self.dinosaur.health <= 0:
                self.herd.herdsize -= 1
            if self.robot.health <=0 and self.fleet.fleetsize > 0:
                print(f'{self.robot.name} was Defeated!')
                time.sleep(2)
                self.choose_robot()
                self.display_fighters("The next Fighter!")
                self.display_health()
            if self.dinosaur.health <= 0 and self.herd.herdsize > 0:
                print(f'{self.dinosaur.name} was Defeated!')
                time.sleep(2)
                self.dinosaur = random.choice(self.herd.dinosaurs)
                self.herd.dinosaurs.remove(self.dinosaur)
                self.display_fighters("The next Fighter!")
                self.display_health() 
            time.sleep(1)  
        self.display_winner() 
            
                

    




                