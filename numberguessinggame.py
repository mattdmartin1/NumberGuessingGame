"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    print("Welcome to the number guessing game!  ")
    num = random.randint(1, 46) 
    attempt_count = 1
    number = int(input("Guess a number between 1 and 45?  "))

    while number != num:
        try:
            number = int(input("Guess a number between 1 and 45?  "))
            attempt_count = attempt_count + 1
            if number not in range(1,45):
                print("That number is outside the range of numbers. Guess between 1 and 45 ")
                continue
        except ValueError:
                print("Please enter a valid number  ")
        else:
            if number > num:
                print("The number is lower!  ")
            elif number < num:
                print("The number is higher!  ")
    else:
        if num == number:
                print("Congratulations, u got it!!  ")
                print("It took you" , attempt_count, "tries")
                print("Game Over!  ")
  
        

# Kick off the program by calling the start_game function.
start_game()