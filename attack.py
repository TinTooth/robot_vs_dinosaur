class Attack:
    def __init__(self,dictionary,attack_power):
        self.name = dictionary['name']
        self.attack_power = attack_power + dictionary['attack_power']
        self.type = dictionary['type']
        self.win = dictionary['win']

        
       