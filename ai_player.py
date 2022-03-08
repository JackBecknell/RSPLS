from player import Player
import random
class AiPlayer(Player):
    def __init__(self):
        self.name = 'Bot'
        self.status = 'Machine'
        super().__init__()
            
    def generate_gesture(self):
        return random.choice(list(self.gestures_win_lose_dict.keys()))
