import random 

#start the game with the player say "Yes" to return "True" boolean value

def start_game():
    print ("Hello, Dear Player!👋🤚")
    start_option= input("YOU Want To Start The Game? type 'Yes', 'No'! ").lower()
    return start_option =="yes"




# if start_game return True the game will proceed 

# the player choice function to return the player choice 

def get_player_choice():
    while True:
        try: # handle the user input 
            player_choice= input("Choose Your Move\nRock ✊, Paper ✋, Scissor ✌ ").lower()
            if player_choice not in ["rock", "paper", "scissor"]:
                # raise a value error 
                raise ValueError ("Please Enter a valid move 'Rock', 'Paper', 'Scissor'")
            return player_choice # get the player choice value
        except ValueError:
            print ("Invalid Input, Please Type 'Rock', 'Paper' ,or 'Scissor' to start the game! ")




# The computer choice 

def get_computer_choice():
    
    computer_choice= random.choice(["rock", "paper", "scissor" ]) # get the computer choice 
    print(f"I chose {computer_choice.capitalize()}")
    return computer_choice


# implement the game logic btween the user choice and the computer choice

# determine the winner 
def game_winning ():
    player_move =  get_player_choice()
    computer_move = get_computer_choice()

    if player_move == computer_move:
        
        return "tie"  
        
    elif (player_move == "rock" and computer_move =="scissor" ):
        return "You Won "
    elif (player_move == "paper" and computer_move =="rock" ):
        return "You Won "
    elif (player_move == "scissor" and computer_move =="paper" ):
        return "You Won "
    else:
        return "You Lose "
    


 

def play_game ():
    # start the game 
    while True:
        if start_game(): # if the start_game return true
            result = game_winning() # call game_winning which calls the get_player_choice and get_player choice 
           
            # printing the result 
            #if the result is tie 
            if result == "tie":
                print("It's a Tie🤔, play again!")
                continue # start the game function again
                #if the result is you win 
            elif result == "You Won ":
                print ("congaratulation, You Win🎉")
            # if result is you lost 
            elif result == "You Lose ":
                print(" You Lose 😥")  

            #implement play again functionality

            play_again = input("You Want to play again! Type; 'Yes', or 'No'! ").lower()
            # if the user will play again the if condition will not excute 
            # the user will continue inside the loop and start the game from the beginning
            
            # if he want to exit the game   
            if play_again != 'yes': 
                print("Ok, See You Next time🤚")
                break # player will not play again



        # player choose No from the beginning   
        else:
            print("OK, Maybe Later 👋")
            break # the game will not start


        

               
    
play_game() # run the game            












