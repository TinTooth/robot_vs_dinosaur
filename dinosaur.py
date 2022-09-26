class Dinosaur:
    def __init__(self,dictionary):
        self.name = dictionary['name']
        self.health = dictionary['health']
        self.attack_power = dictionary['attack_power']

    def attack (self, target):
        target.health = target.health - self.attack_power


