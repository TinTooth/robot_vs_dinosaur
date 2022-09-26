class Dinosaur:
    def __init__(self,dictionary):
        self.name = dictionary['name']
        self.health = dictionary['health']
        self.quick_attack = dictionary['quick_attack']
        self.power_attack = dictionary['power_attack']
        self.percision_attack = dictionary['precision_attack']
        self.attack_types = ['quick','power','percision']

    def quick_attacked (self, target):
        target.health = target.health - self.quick_attack['attack_power']
        print(self.quick_attack['win'])

    def power_attacked (self, target):
        target.health = target.health - self.power_attack['attack_power']
        print(self.power_attack['win'])  

    def percision_attacked (self, target):
        target.health = target.health - self.percision_attack['attack_power']
        print(self.percision_attack['win'])