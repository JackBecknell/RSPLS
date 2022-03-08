from ai_player import AiPlayer
from human_player import HumanPlayer



#one problem is that currently the user has to choose whether its a 1 or 2 player game before the welcome display. So I set the default to HumanPlayer and then give the user a change to choose during the "run_game" funtion.
class PlayingField:
    def __init__(self) -> None:
        self.player_one = HumanPlayer()
        self.player_two = HumanPlayer()
        self.line_break = "*******************************************************************************************************************************************************\n"

#master funciton that calls all necessary functions from the start of the game to the finish.
    def run_game(self):
        self.user_chooses_1_or_2_player()
        self.name_fix()
        self.battle_sequence()
        self.display_winner()

#First function to be called in "main" file. Given the user input it will either break or call the "run_game" function.
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

#Lets the users/user play as many round as it takes to reach 3 wins.
    def battle_sequence(self):
        while self.player_one.wins != 3 and self.player_two.wins != 3:
            self.player_one.current_gesture = self.player_one.generate_gesture(self.player_one.name)
            if self.player_two.status == 'Machine':
                self.player_two.current_gesture = self.player_two.generate_gesture()
            else:
                self.player_two.current_gesture = self.player_two.generate_gesture(self.player_two.name)
            if self.player_one.current_gesture == self.player_two.current_gesture:
                print("A Tie!")
            elif self.player_one.current_gesture in ((self.player_two.gestures_win_lose_dict)[self.player_two.current_gesture]):
                print('Player 2 Wins the round!')
                self.player_two.wins += 1
            else:
                print('Player 1 Wins the round!')
                self.player_one.wins += 1
        
#Lets the user choose 1 or 2 players.
    def user_chooses_1_or_2_player(self):
        user_choice = input("Type 1 for one player game.\nType 2 for two player game.\n : ")
        while user_choice not in ['1','2']:
            user_choice = input("Invalid Input\nType 1 for one player game.\nType 2 for two player game.\n : ")
        if user_choice == '1':
            self.player_two = AiPlayer()
        else:
            self.player_two = HumanPlayer()

#function adds a 1 to the end of player 1 and a 2 to the end of player 2
    def name_fix(self):
        self.player_one.name = (f"{self.player_one.name}1")
        self.player_two.name = (f"{self.player_two.name}2")

#last function to run as it displays the winner. 
    def display_winner(self):
        if self.player_one.wins > self.player_two.wins:
            print("Player 1 Wins THE GAME!")
        else:
            print("Player 2 Wins THE GAME!")
