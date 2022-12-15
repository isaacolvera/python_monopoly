# Project 2 - "Monopoly Game" (chance_and_communitychest.py)
#
# Author: Isaac Olvera

import random

def community_chest():
    """Function that picks a random event when the player lands on community chest"""
    print("\nThis is community chest! Selecting the top card...")
    top_card = random.randint(1, 10)
    cash = 0
    
    if top_card == 1:
        print("You were fined $125 for littering... how dare you!")
        cash = -125
        
    elif top_card == 2:
        print("You entered a hamburger eating contest and won $50. Nice job!")
        cash = 50
        
    elif top_card == 3:
        print("Your nephew is sick and needs $25 for some medication. I hope he feels better!")
        cash = -25
        
    elif top_card == 4:
        print("You found $200 on the floor! How lucky of you!")
        cash = 200
        
    elif top_card == 5:
        print("You got scammed by an email asking for $30. You should have known better.")
        cash = -30
        
    elif top_card == 6:
        print("Your aunt gave you $75 for your birthday. How sweet of her!")
        cash = 75
        
    elif top_card == 7:
        print("You lost $200 while gambling in Las Vegas. Better luck next time!")
        cash = -200
        
    elif top_card == 8:
        print("You helped your uncle repaint his bedroom so he gave you $100 for your hardwork!")
        cash = 100
        
    elif top_card == 9:
        print("Your pet ate something they shouldn't have. A nice trip to the vet costs you $300! Ouch!")
        cash = -300
        
    elif top_card == 10:
        print("Your tax return came in. You got $65 back.")
        cash = 65
    
    return cash


def chance():
    """Function that picks a random event when the player lands on chance"""
    print("\nThis is chance! Selecting the top card...")
    top_card = random.randint(1, 10)
    cash = 0
    
    if top_card == 1:
        print("You were charged $20 more on your last grocery trip. Better check the receipt next time!")
        cash = -20
        
    elif top_card == 2:
        print("You decided to visit your grandma and she gave you $40 for visiting her. You tried refusing but she wouldn't take no for an answer!")
        cash = 40
        
    elif top_card == 3:
        print("You spent $110 on a used gaming console just for it to break down the next day. That sucks!")
        cash = -110
        
    elif top_card == 4:
        print("Your dad decided to give you $5 randomly. Thanks dad?")
        cash = 5
        
    elif top_card == 5:
        print("Coming back from a trip to New York, you realize you left your wallet at the hotel you were staying at. It had $100 inside of it...")
        cash = -100
        
    elif top_card == 6:
        print("While working lots of overtime as a waiter, you got an extra $250 in tips!")
        cash = 250
        
    elif top_card == 7:
        print("You lost a bet with your best friend and had to give her $90. I hope it was worth it!")
        cash = -90
        
    elif top_card == 8:
        print("After building your daughter a lemonade stand, she gives you $10 and a beautiful smile for helping her. How wonderful!")
        cash = 10
        
    elif top_card == 9:
        print("Being the kind person you are, you decided to give a homeless person $50 to help them out")
        cash = -50
        
    elif top_card == 10:
        print("Your tax return came in. You got $2... that's nice I guess?")
        cash = 2
    
    return cash
