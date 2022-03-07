import imp
from player import Player




class PlayingField:
    def __init__(self) -> None:
        self.player_one = Player()
        self.player_two = "second"

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

