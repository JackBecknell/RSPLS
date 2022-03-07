from player import Player
import random



class AiPlayer(Player):
    def __init__(self):
        
        super().__init__()

    def generate_gesture(self):
        for gesture in range(len(self.gesture)):
            return random.choice(self.gesture)
  