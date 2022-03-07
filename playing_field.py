import imp
from player import Player
from ai_player import AiPlayer
from human_player import HumanPlayer




class PlayingField:
    def __init__(self) -> None:
        self.player_one = HumanPlayer()
        self.player_two = self.user_chooses_1_or_2_player()

    def display_welcome(self):
        pass

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
        pass
        #choose between rock, paper, scissor, lizard, spock
        #return user input 
        #check user input
        #if input is within range,
        #return input
    
    def player_two_turn(self):
        pass
        #choose between rock, paper, scissor, lizard, spock
        #return user input 
        #check user input
        #if input is within range, 
        #return input
           

    def display_winner(self):
        pass
        


