from dinosaur import Dinosaur


class Herd:
    def __init__(self,dictionary):
        self.dinosaur1 = Dinosaur(dictionary['dinosaur1'])
        self.dinosaur2 = Dinosaur(dictionary['dinosaur2'])
        self.dinosaur3 = Dinosaur(dictionary['dinosaur3'])
        self.dinosaurs = [self.dinosaur1,self.dinosaur2,self.dinosaur3]
        self.herdsize = len(self.dinosaurs)