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
        choice = (input('Pick Your Starting Robot!  '))
        choice = self.validate_num_input(choice,len(self.fleet.robots)+1)
        self.robot = self.fleet.robots[int(choice) -1]
        self.fleet.robots.remove(self.robot)

    def display_fighters(self,prompt):
        print()
        print(prompt)
        print(f'{self.robot.name} VS {self.dinosaur.name}')
        time.sleep(2)

    def display_welcome_start_game(self):
        print()
        print('       Welcome to Robots vs Dinosaurs!')
        self.choose_num_of_fighters()
        self.display_fighters("The First Fighters!")
        self.display_health()
      

    def choose_num_of_fighters(self):
        user_input = input('How many Fighters per Team? 1, 2 or 3:  ')
        user_input = self.validate_num_input(user_input,4)
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
        print(f'           {self.robot.name} has {self.robot.health} Health  ', '/',f'  {self.dinosaur.name} has {self.dinosaur.health} Health')
        # print(f'{self.dinosaur.name} has {self.dinosaur.health} Health') 
        

    def battle_phase(self):
        self.select_weapon()
        print()
        print(f'{self.robot.name}\'s {self.robot.active_weapon.name.upper()} is going against the {self.dinosaur.name}\'s {self.dinosaur.active_attack.name.upper()}')
        print()
        time.sleep(1)
        if self.robot.active_weapon.type == self.dinosaur.active_attack.type:
            print('Neither attack hit!')
            time.sleep(1)
            return
        if self.robot.active_weapon.type == 'power':
                if self.dinosaur.active_attack.type == 'precision':
                    self.robot.attack(self.dinosaur)
                elif self.dinosaur.active_attack.type == 'quick':
                    self.dinosaur.attack(self.robot)
                time.sleep(2)
                return    
        if self.robot.active_weapon.type == 'precision':
                if self.dinosaur.active_attack.type == 'quick':
                    self.robot.attack(self.dinosaur)
                elif self.dinosaur.active_attack.type == 'power':
                    self.dinosaur.attack(self.robot)
                time.sleep(2)
                return    
        if self.robot.active_weapon.type == 'quick':
                if self.dinosaur.active_attack.type == 'power':
                    self.robot.attack(self.dinosaur)
                else:
                    self.dinosaur.attack(self.robot)
                time.sleep(2)
       
    def display_winner(self):
        print()
        if self.herd.herdsize == 0:
            print(f'{self.dinosaur.name} was Defeated!')
            print()
            time.sleep(2)
            print(f'The Robots are VICTORIOUS!!')
        else:
            print(f'{self.robot.name} was Defeated!')
            print()
            time.sleep(2)
            print(f'The Dinosaurs are VICTORIOUS!!')
        print()
            
    def validate_num_input(self,choice,end_of_range):
        while True:
            if choice.isnumeric() and int(choice) in range(end_of_range):
                break
            else:
                choice = input('Please enter a correct number:  ')
        return choice

    def select_weapon(self):
        self.display_weapons()
        user_input = input('Select a Weapon! 1, 2 or 3:  ')
        user_input = self.validate_num_input(user_input,4)
        self.robot.active_weapon = self.robot.weapons[int(user_input)-1]
        self.dinosaur.active_attack = random.choice(self.dinosaur.attacks)

    def check_fighters_health(self):
        if self.robot.health > 0 and self.dinosaur.health > 0:
            self.display_health()
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

    def run_game(self):
        self.display_welcome_start_game()
        time.sleep(1)
        i = 1
        while self.herd.herdsize > 0 and self.fleet.fleetsize > 0:
            while self.robot.health > 0 and self.dinosaur.health > 0:
                print(f'ROUND {i} ---------------------------------------------')
                self.battle_phase()
                self.check_fighters_health()
                i = i+1    
            time.sleep(1)  
        self.display_winner() 
            


    




                