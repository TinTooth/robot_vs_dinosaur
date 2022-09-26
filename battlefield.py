import data
from robot import Robot
from dinosaur import Dinosaur

class BattleField:
    def __init__(self):
        self.robot = Robot(data.robots['robot1'])
        self.dinosaur = Dinosaur(data.dinosaurs['dinosaur1'])