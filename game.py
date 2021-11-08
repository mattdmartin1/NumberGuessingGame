from phrase import Phrase
import random

class Game:
    
    
    def __init__(self):
        
        self.missed = 0
        self.phrases = [
            Phrase("Take with a grain of salt"), 
            Phrase("A dog is a mans best friend"), 
            Phrase("Break a leg"), 
            Phrase("To kill two birds with one stone"), 
            Phrase("You cant judge a book by its cover")
        ]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []
        
    def start(self):
        self.welcome()
        while self.missed < 5:
            if not self.active_phrase.check_complete(self.guesses):
                print("\nYou missed {} out of 5 misses.\n".format(self.missed))
                self.active_phrase.display(self.guesses)
                user_guess = self.get_guess()
                self.guesses.append(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    print("\nThat letter is incorrect. {} out of the 5 tries remaining!".format(4-self.missed))
                    self.missed += 1
                if self.game_over():
                    break


    def get_random_phrase(self):
        return random.choice(self.phrases)


    def welcome(self):
        print("\n-------Welcome to the Phrase Hunter Game!!-------")
        print("\nYou have up to 5 letter guess attempts remaining.")
        print("\nLet's begin!")


    def get_guess(self):
        self.guess = input("\n\nEnter a letter: \n").lower()
        return self.guess
    
    
    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print("\nCongratulations! You guessed the correct phrase!! \n")
            return True
        elif self.missed == 5:
            print("Better luck next time! GAME OVER!! \n")
            return True
        else:
            return False