# This is a digital coin flip of Heads or Tails

import random, sys  #Importing the random and sys modules that we will use

random_number = random.randint(1, 2)
choice = "" # stores user's input
result = "" # stores random output


def play_game(): # the main function that calls other function
    instructions()
    decision()
    flip_result()
    quit()
    
    
def decision(): # getting player input
    global choice # calling a global variable in a local scope
    choice = input(" Heads or Tails? ")
    if choice == "1":
        choice = "Heads"
    else:
        choice = "Tails"
    
def flip_result(): # getting random output
    global result
    if random_number == 1:
        result = "Heads"
    else:
        result = "Tails"  
        
    if result == choice: # comparing random output and player input
        print(result, ", You win!")
    else:
        print(result, ", You lose!")
        
def instructions():
    print("The system will generate a random number, either '1- for Heads' or '2- for Tails'.\n Choose '1' or '2' for this digital coin flip")

def quit():
    sys.exit("The game has ended! Restart to flip the coin again")


play_game()
    

    
    
    
    
    
    
    
    


        
