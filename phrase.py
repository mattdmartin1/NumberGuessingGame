class Phrase:
    
    
    def __init__(self, phrase):
        
        self.phrase = phrase.lower()
        
        
    def display(self, guesses):
        
        for letter in self.phrase:
            if letter in guesses:
                print(letter, end=" ")
            elif letter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
                
        
    def check_guess(self, check_guess):
        
        if check_guess in self.phrase:
            return True
        else:
            return False 

        
    def check_complete(self, guesses):
        
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True