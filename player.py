
#For the self.gestures_win_lose_dict the values stored to the keywords are the values the keyword can beat.
class Player:
    def __init__(self) -> None:
        self.current_gesture = ''
        self.wins = 0
        self.gestures_win_lose_dict = {
    "scissors": ['paper','lizard'],
    "paper" : ['rock','spock'],
    "rock" : ['lizard','scissors'],
    "lizard" : ['spock','paper'],
    "spock" : ['paper','lizard'],
}

#changed the generate gesture to return a random key for the dicitonary in Player.
    def generate_gesture(self):
        pass
