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
        self.dinosaur = 'TBD'
       
    def check_fighters_health(self):
        if self.robot.health > 0 and self.dinosaur.health > 0:
            self.display_health()
            time.sleep(1)
            return
        if self.robot.health <= 0:
            self.fleet.fleetsize -= 1
        if self.dinosaur.health <= 0:
            self.herd.herdsize -= 1
        if self.robot.health <=0 and self.fleet.fleetsize > 0:
            print(f'{self.robot.name} was Defeated!')
            time.sleep(2)
            self.choose_robot()
            self.display_fighters("Your next Robot is Ready to GO!")
            self.display_health()
        if self.dinosaur.health <= 0 and self.herd.herdsize > 0:
            print(f'{self.dinosaur.name} was Defeated!')
            time.sleep(2)
            self.choose_active_dinosaur()
            self.display_fighters("The next Dinosaur Steps into the Ring!")
            self.display_health() 
            
    def choose_active_dinosaur(self):
        self.dinosaur = random.choice(self.herd.dinosaurs)
        self.herd.dinosaurs.remove(self.dinosaur)

    def choose_robot(self):
        self.display_fleet('Your Fleet')
        choice = input('Pick your Fighter!  ')
        choice = self.validate_num_input(choice,len(self.fleet.robots)+1)
        self.robot = self.fleet.robots[int(choice) -1]
        self.fleet.robots.remove(self.robot)

    def choose_num_of_fighters(self):
        print()
        user_input = input('How many Fighters per Team? 1, 2 or 3:  ')
        print()
        user_input = self.validate_num_input(user_input,4)
        if user_input == '1':
            self.fleet.fleetsize -= 2
            self.herd.herdsize -= 2
            print('    1 ROBOT VS 1 DINOSAUR!')
        elif user_input == '2':
            self.fleet.fleetsize -= 1
            self.herd.herdsize -= 1
            print('    2 ROBOTS VS 2 DINOSAURS!')
        else:
            print('    3 ROBOTS VS 3 DINOSAURS!')

    def display_dinosaurs(self):
        print('The Herd of Dinosaurs: The TRI FORCE')
        i = 1
        for dinosaur in self.herd.dinosaurs:
            print(f'{i}) {dinosaur.name}')
            i += 1
        
    def display_fleet(self,prompt):
        i = 1
        print()
        print(prompt)
        for robot in self.fleet.robots:
            print(f'{i}) {robot.name} ')
            i +=1

    def display_fighters(self,prompt):
        print()
        print(prompt)
        print(f'{self.robot.name} VS {self.dinosaur.name}')
        time.sleep(2)
    
    def display_health(self):
        print()
        print(f'           {self.robot.name} has {self.robot.health} Health  ', '/',f'  {self.dinosaur.name} has {self.dinosaur.health} Health')

    def display_weapons(self):
        i = 1
        for weapon in self.robot.weapons:
            print(f'{i}) {weapon.name}   Attack Power:  {weapon.attack_power}  Type:  {weapon.type}')
            i += 1
            
    def display_welcome_start_game(self):
        print()
        print('       Welcome to Robots vs Dinosaurs!')
        print()
        self.display_dinosaurs()
        self.choose_active_dinosaur()
        self.choose_robot()
        self.choose_num_of_fighters()
        self.display_fighters('The First Fighters')
        self.display_health()
        
    def display_winner(self):
        print()
        if self.herd.herdsize == 0:
            print(f'{self.dinosaur.name} was Defeated!')
            print()
            print(f'The Robots are VICTORIOUS!!')
            self.print_robot()
        else:
            print(f'{self.robot.name} was Defeated!')
            print()
            time.sleep(2)
            print(f'The Dinosaurs are VICTORIOUS!!')
            self.print_dinosaur()
        print()

    def select_weapon(self):
        self.display_weapons()
        user_input = input('Select a Weapon! 1, 2 or 3:  ')
        user_input = self.validate_num_input(user_input,4)
        self.robot.active_weapon = self.robot.weapons[int(user_input)-1]
        self.dinosaur.active_attack = random.choice(self.dinosaur.attacks)
            
    def print_dinosaur(self):

        print( '                                                  00000000000000                                     ' )    
        print( '                                               00               00000000                       ' )    
        print( '                                              00    (XXxx)               00                        ' )    
        print( '                                              00                         00                      ' )    
        print( '                                              00                 0 0000000                      ' )    
        print( '                                              00          00 0000    V V                         ' )    
        print( '                                              00                 0000,                             ' )    
        print( '                                              00          0 00 0 000,                              ' )    
        print( '                                              00         00                              ' )    
        print( '               00                     00000000         00                                 ' )    
        print( '               00                  000                  00 11111                                 ' )    
        print( '               0000            00000       11             00    11                                   ' )    
        print( '               0000          0000           11            00    11                                ' )    
        print( '               00000000000000                VVV          00   VV                                       ' )    
        print( '               00                                       000                                 ' )    
        print( '                00                                       00                                ' )    
        print( '                  00 000                                 00                                   ' )    
        print( '                        000                000           00                                    ' )    
        print( '                           000           000 000       00                                         ' )    
        print( '                              000 00000 000     000   00                                               ' )    
        print( '                                  0000            000 0                                       ' )    
        print( '                                  000             000                                       ' )    
        print( '                                  00 0            000                                      ' )    
        print( '                                  00  0           00 0                                       ' )    
        print( '                                  0 00 0          000 0                                        ' )    
        print( '  ')           

    def print_robot(self):
        print('                                                                               ')
        print('                            00000                                                ')
        print('                         00       00                                              ')
        print('                          00     00                                            ')
        print('                            00 00                                                 ')
        print('                              0                                                 ')
        print('                              0                                                 ')
        print('               00000000000000000000000000000000                                                      ')
        print('               0                              0                               ')
        print('               0     0 0 0 0      0 0 0 0     0         000 00          00 000               ')
        print('               0      0 0 0        0 0 0      0         0     0        0     0       ')
        print('               0     0 0 0 0      0 0 0 0     0         0      0      0      0         ')
        print('               0                              0          0      000000      0     ')
        print('               0    1111111111111111111111    0           0               0                       ')
        print('               0     1                    1   0            0 000     000 0        ')
        print('               0      1                  1   0                  0    0         ')
        print('               0       11111111      111    0                   0   0                  ')
        print('                0              111111      0                     0 0                ')
        print('                  0                      0                       0 0         ')
        print('                    0 0000000000000000000          0 0 0000      0 0                           ')
        print('                          00000000                0        0    0    0            ')
        print('          00000000000000000000000000000000000000000         0  0     0                                              ')
        print('          0                                       0           V       0      ')
        print('          0                                       0                  0       ')
        print('          0                                       0  00 000 0000  000                     ')

    def validate_num_input(self,choice,end_of_range):
        while True:
            if choice.isnumeric() and int(choice) in range(end_of_range):
                break
            else:
                choice = input('Please enter a correct number:  ')
        return choice

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