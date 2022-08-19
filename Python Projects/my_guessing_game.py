#The program randomly selects a number between 1 and 100 or any other combination of 
    #numbers.
#It will then ask the player to enter his proposal.
#It will then check if this number is the same as the one generated randomly by the 
    #computer; if so, the player wins.
#If the player’s guess is not the same, then he will check if the number is higher or 
    #lower than the guess and tell the player.

import random
n= random.randrange (3,9)
guess= input("guess a number 3-9: ")
while n!= int(guess):
    if int(guess) < n:
        print ("Oops! low number")
        guess= input("guess another number 3-9: ")
    elif int(guess) > n:
        print ("ouch! high number")
        guess= input("guess another number 3-9: ")
    else:
        break
print ("Yay! You are a genius")