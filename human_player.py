
from player import Player

class HumanPlayer(Player):
    def __init__(self):
        self.name = 'Player'
        self.status = 'Human'
        super().__init__()
        ##deleted the redundant self.wins = 0 instance variable that was here

#replaced the all the old instance vaiable calls to the new dicitonary calls.
#note to self. If we wanted to show off that we know how to overwrite instance methods we could name the method below 'generate_gesture' changing it from the parent.
    def user_picks_gesture(self, pass_name):
        user_choice = input(f"Hello {pass_name}.\nFor {list(self.gestures_win_lose_dict.keys())[0]} type 0\nFor {list(self.gestures_win_lose_dict.keys())[1]} type 1\nFor {list(self.gestures_win_lose_dict.keys())[2]} type 2\nFor {list(self.gestures_win_lose_dict.keys())[3]} type 3\nFor {list(self.gestures_win_lose_dict.keys())[4]} type 4\n : ")
        while user_choice not in ['0','1','2','3','4']:
            user_choice = input(f"Invlaid Input {pass_name}.\nFor {list(self.gestures_win_lose_dict.keys())[0]} 0\nFor {list(self.gestures_win_lose_dict.keys())[1]} type 1\nFor {list(self.gestures_win_lose_dict.keys())[2]} type 2\nFor {list(self.gestures_win_lose_dict.keys())[3]} type 3\nFor {list(self.gestures_win_lose_dict.keys())[4]} type 4\n : ")
        return (list(self.gestures_win_lose_dict.keys()))[int(user_choice)]