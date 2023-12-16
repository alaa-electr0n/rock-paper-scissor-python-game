import random

def start_game():
    print("Hello, Dear Player!👋🤚")
    return input("Do you want to start the game? Type 'Yes' or 'No': ").lower() == "yes"

def get_player_choice():
    while True:
        player_choice = input("Choose Your Move\nRock ✊, Paper ✋, Scissor ✌: ").lower()
        if player_choice in ["rock", "paper", "scissor"]:
            return player_choice
        print("Invalid Input. Please type 'Rock', 'Paper', or 'Scissor' to start the game!")

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissor"])
    print(f"I chose {computer_choice.capitalize()}")
    return computer_choice

def game_winning(player_move, computer_move):
    outcomes = {
        "rock": {"beats": "scissor", "beaten_by": "paper"},
        "paper": {"beats": "rock", "beaten_by": "scissor"},
        "scissor": {"beats": "paper", "beaten_by": "rock"}
    }

    if player_move == computer_move:
        return "It's a Tie🤔, play again!"
    return "You Win🎉" if computer_move == outcomes[player_move]["beaten_by"] else "You Lose😥"

def play_game():
    while True:
        if start_game():
            player_move = get_player_choice()
            computer_move = get_computer_choice()
            print(game_winning(player_move, computer_move))
            if input("You Want to play again! Type 'Yes' or 'No': ").lower() != 'yes':
                print("Ok, See You Next time🤚")
                break
        else:
            print("OK, Maybe Later 👋")
            break

play_game()
