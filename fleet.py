from robot import Robot
class Fleet:
    def __init__(self,dictionary):
        self.robot1 = Robot(dictionary['robot1'])
        self.robot2 = Robot(dictionary['robot2'])
        self.robot3 = Robot(dictionary['robot3'])
        self.robots = [self.robot1,self.robot2,self.robot3]
        self.fleetsize = len(self.robots)
