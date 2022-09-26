from dinosaur import Dinosaur


from dinosaur import Dinosaur
from robot import Robot



robot1 = {'name': 'HeavyArms','health':120,
 'weapon': {'name': 'shoulder missles','attack_power':120,'win':'The missles over powered the claw','type':'Rock'}
}

heavyarms = Robot(robot1)
print(heavyarms.name)