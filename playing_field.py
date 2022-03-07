import imp
from player import Player
from ai_player import AiPlayer
from human_player import HumanPlayer




class PlayingField:
    def __init__(self) -> None:
        self.player_one = HumanPlayer()
        self.player_two = self.user_chooses_1_or_2_player()
        self.line_break = "*******************************************************************************************************************************************************\n"


    def display_welcome(self):
        user_input = input(f"{self.line_break}***************************************************************WELCOME TO R.P.S.L.S.*******************************************************************\n{self.line_break}Same rules is your traditional rock, paper, scissors but with a twist, the addition of lizard and spock.\nROCK:\nBeats lizard\nBeats scissors\nLooses to paper\nLoses spock\n\nPAPER:\nBeats rock\nBeats spock\nLooses to scissors\nLoses lizard\n\nSCISSORS:\nBeats paper\nBeats lizard\nLooses to spock\nLoses rock\n\nLIZARD:\nBeats spock\nBeats paper\nLooses to rock\nLoses scissors\n\nSPOCK:\nBeats scissors\nBeats rock\nLooses to lizard\nLoses paper\n\nDo you want to start?[Yes/No]: ").lower()
        while True:
            if user_input == "yes":
                self.run_game()
                break
            elif user_input == "no":
                print("Goodbye!")
                break
            else:
                user_input = input("Invalid response! Do you want to play?[Yes/No]: ")

    def run_game(self):
        pass

    def battle_sequence(self):
        pass
        #while true
        #get result from player 1 input
        #get result from player 2 input
        #iterate over player 1 list
            #iterate over player 2 list
                #compare win/loose choices
                #if player one wins
                    #count ++
                        #count is more than 2
                            #display winner
                #else if player two wins
                    #count ++
                        #if count is more than 2
                            #display winner

    def user_chooses_1_or_2_player(self):
        user_choice = input("Type 1 for one player game.\nType 2 for two player game.\n : ")
        while user_choice not in ['1','2']:
            user_choice = input("Invalid Input\nType 1 for one player game.\nType 2 for two player game.\n : ")
        if user_choice == '1':
            return AiPlayer()
        else:
            return HumanPlayer()
        

    def player_one_turn(self):
        self.player_one.user_picks_gesture()
    

    def display_winner(self):
        print("CONGRATULATIONS {XXXXX}! YOU ARE THE WINNER!")
