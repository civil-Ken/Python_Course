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