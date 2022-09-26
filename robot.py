from weapons import Weapon

class Robot:
    def __init__(self,dictionary):
        self.name = dictionary['name']
        self.health = dictionary['health']
        self.active_weapon = Weapon(dictionary['weapon'])
