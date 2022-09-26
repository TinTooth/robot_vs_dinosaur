
from battlefield import BattleField

battlefield = BattleField()


print(battlefield.dinosaur.name,battlefield.dinosaur.health)
print(battlefield.robot.name,'Health',battlefield.robot.health,'attack power',battlefield.robot.active_weapon.attack_power)
battlefield.battlephase()
print(battlefield.dinosaur.name,battlefield.dinosaur.health)
print(battlefield.robot.name,battlefield.robot.health)







