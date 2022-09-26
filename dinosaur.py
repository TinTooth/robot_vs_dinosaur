import random
from attack import Attack
class Dinosaur:
    def __init__(self,dictionary):
        self.name = dictionary['name']
        self.health = dictionary['health']
        self.attack_power = dictionary['attack_power']
        self.attacks =[Attack(dictionary['attack1'],self.attack_power),Attack(dictionary['attack2'],self.attack_power),Attack(dictionary['attack3'],self.attack_power)]
        self.active_attack = random.choice(self.attacks)

    def attack (self, target):
        target.health = target.health - self.active_attack.attack_power
        print(self.active_attack.win,f'and did {self.active_attack.attack_power} damage!')
   