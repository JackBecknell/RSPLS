from player import Player

class HumanPlayer(Player):
    def __init__(self):

        super().__init__()

    def user_picks_gesture(self):
        user_choice = input(f"Hello User.\nFor {self.gesture[0]} type 0\nFor {self.gesture[1]} type 1\nFor {self.gesture[2]} type 2\nFor {self.gesture[3]} type 3\nFor {self.gesture[4]} type 4\n : ")
        while user_choice not in ['0','1','2','3','4']:
            user_choice = input(f"Invlaid Input.\nFor {self.gesture[0]} 0\nFor {self.gesture[1]} type 1\nFor {self.gesture[2]} type 2\nFor {self.gesture[3]} type 3\nFor {self.gesture[4]} type 4\n : ")
        return self.gesture[int(user_choice)]

    