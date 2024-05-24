'''
Author: Thomas Butkiewicz
Date: 11/30/23
Description: This is a game I made, Rock, Paper, Scissors, which will make you play against a robot and keep your score.
Bugs:None
Challenges: Keeps score, User errors, score limit
Sources: Me, Mr Abanto, Mrs Marciano, Evan Myers, w3school.
'''

import time
import sys
import random #brings in the random library in order to use those functions
# I got this type writer affect from Evan Myers, he helped me along with Ms Marciano to integrate it into my code and make it better.
def typewriter_effect(sentence, type_delay):#creates the sentence and the type delay variable so that it can be plugged in and called
    for char in sentence: # for each character in sentence type it in the typewriter effect

        # Write, display and delay
        sys.stdout.write(char)#tells system to write character
        sys.stdout.flush()#takes the data in the buffer and clears it.
        time.sleep(type_delay)#adds delay to the sleep so they are the same

    time.sleep(1) # Pause after printing the entire sentence

def main(): #The main function
    type_delay = 0.0025 # the speed in which the code is typed out.
    user_score = 0 #creates a variable user_score to keep track of the user's score; sets it to zero to start
    bot_score = 0 #creates a variable user_score to keep track of the user's score; sets it to zero to start
    score_cap = 5 #this is the score cap to not go over it
    plays = ["rock", "paper", "scissors"] #this is the list that will show
    typewriter_effect("I am the magical rock, paper, scissors game\n", type_delay) #prints this message if you want to play the game

    while True:
        play = str.lower(input("Would you like to play a game? (Yes/No) ")) # This asks the question of if you want to play the game, you can respond either lower or upper case.

        if play == "yes": #if you choose yes do everything below.
            while user_score < score_cap and bot_score < score_cap: # this says that keep playing the game if the score of both use and bot is below the score cap
                user = str.lower(input("Enter stop to end. Rock, paper, scissors? \n")) #creates a line that gives you the option to keep playing or kill the code
                bot = random.choice(plays) # this randomizes the bots choice if you want to play

                if user == "stop": #if you choose stop if will end the game
                    exit()
                elif user not in plays: # if you choose something that is not rock paper scissors it will say invalid
                    typewriter_effect("Invalid\n", type_delay) #it will print invalid
                else:
                    typewriter_effect(f"User chose {user}, bot chose {bot}\n",type_delay) #this shows that what the user and bot chose
                    
                    if user == bot: # the user and bot both euqla each other
                        typewriter_effect("Tie", type_delay) # This is if they choose the same thing
                    elif user == "rock" and bot == "scissors":
                        typewriter_effect("user wins!", type_delay) #this is if user chooses something that the bot loses to 
                        user_score += 1   
                    elif user == "rock" and bot == "paper":
                        typewriter_effect("bot wins!", type_delay) #this is if bot chooses something that the user loses to
                        bot_score += 1
                    elif user == "scissors" and bot == "rock":
                        typewriter_effect("bot wins!", type_delay) #this is if bot chooses something that the user loses to
                        bot_score += 1
                    elif user == "scissors" and bot == "paper":
                        typewriter_effect("user wins!", type_delay) #this is if user chooses something that the bot loses to
                        user_score += 1
                    elif user == "paper" and bot == "rock":
                        typewriter_effect("user wins!", type_delay) #this is if user chooses something that the bot loses to
                        user_score = user_score +1
                    elif user == "paper" and bot == "scissors":
                        typewriter_effect("bot wins!", type_delay) #this is if user bot something that the user loses to
                        bot_score += 1 # if the both or user wins add 1 "point" to the user or bots score

                    typewriter_effect(f"User score: {user_score} | Bot score: {bot_score}\n", type_delay) # this will print after every game played to show everybody the score.
        elif play == "no": # this is if you choose no not to play the game
            typewriter_effect("Okay, have a good day.", type_delay) # this will print once you say no to play
            break #end the code
        else:
            typewriter_effect("Invalid\n", type_delay) # if you say anything that is not supposed to be say

main() # for the typewriter affect.


