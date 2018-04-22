from random import *
import time

name = input('What is your name?')
time.sleep(1)
print("Your name is", name,",my name is Marvin.")
time.sleep(1)
print("Nice to meet you",name,".")
time.sleep(1)
lives = input("Where are you from?")
time.sleep(1)
print(name, "you are from",lives,"but I'm from a galaxy far, far away!")
time.sleep(1)
color = input("What's your favorite color?")
time.sleep(1)
print(name, "Your favorite color is",color,",but I don't have a favorite color as I'm a machine....")
time.sleep(1)
game = input("I'm very sad now, would you like to play a game?")
while game == ('yes' or 'Yes'):
    time.sleep(1)
    print("I'm thinking of a number between 1 and 10.")
    number = randint(1, 10)
    time.sleep(1)
    print("Can you guess what the number is I'm thinking of?")
    time.sleep(1)
    answer = input("Enter the number you had in mind.")
    if number == answer:
        time.sleep(1)
        print("You guessed it right the number is was thinking of was",number,".")
        again= input("Would you like to try again?")
        if again == ("yes" or "Yes"):
                continue
        else:
                break
    else:
        time.sleep(1)
        print("No, that wasn't the number I had in mind.")
        time.sleep(1)
        print("The number I was thinking of was",number,".")
        retry = input("Would you like to try again?")
        if retry == ("yes" or "Yes"):
            time.sleep(1)
            print("Let's try this again shall we?")
        else:
            time.sleep(2)
            break
print("Sorry for asking, goodbye!")
