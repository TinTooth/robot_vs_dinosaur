
from battlefield import BattleField

battlefield = BattleField()

print(battlefield.dinosaur.name,"health",battlefield.dinosaur.health,"attack power",battlefield.dinosaur.attack_power)
battlefield.robot.attack(battlefield.dinosaur)
print(battlefield.dinosaur.name,battlefield.dinosaur.health)


print(battlefield.robot.name,'Health',battlefield.robot.health,'attack power',battlefield.robot.active_weapon.attack_power)
battlefield.dinosaur.attack(battlefield.robot)
print(battlefield.robot.name,battlefield.robot.health)