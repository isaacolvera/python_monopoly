# Project 2 - "Monopoly Game" (bankrupt.py)
#
# Author: Isaac Olvera

from mortgage_and_unmortgage import *
from houses import *
from rent import *

def maybe_bankrupt(board, player):
    """Function that checks if the player has gone bankrupt."""
    # Check the properties
    properties = player.get_properties()
    all_mortgaged = False
    all_houses_sold = False
    
    # Player is in debt, they need to pay it off (as much as they can)
    while player.get_money_amount() < 0:
        print(
            "\nYou are in debt. Please select one of the options to help pay it off: \n"
            "1. Mortgage property\n"
            "2. Sell houses"
        )
        
        choice = int(input())
        
        while choice > 2 or choice < 1:
            choice = int(input("\nPlease enter a valid number: "))
        
        if choice == 1:
            mortgage_property(player)
            
            # Check the unmortgaged properties
            unmortgaged_properties = []
            
            # Get all of the properties that are not mortgaged already
            for property in properties:
                if property[4] == False:
                    unmortgaged_properties.append(property)
            
            # All of the player's properties are mortgaged or there are no properties
            if unmortgaged_properties == []:
                all_mortgaged = True
        
        elif choice == 2:
            sell_houses(board, player)
            
            # Check the properties with houses on them
            properties_with_houses = []
            
            # Get all of the properties that have houses on them
            for property in properties:
                if property[7] == None:
                    continue
                
                if property[7] == 0:
                    continue
                
                if property[4] == False and property[7] >= 1:
                    properties_with_houses.append(property)
            
            # All of the player's properties have no houses to sell
            if properties_with_houses == []:
                all_houses_sold = True
        
        if all_mortgaged == True and all_houses_sold == True and player.get_money_amount() < 0:
            player.bankrupt = True
            break
    
    if player.get_money_amount() >= 0:
        print("\nNice, you paid off your debt!")
        
        
def bankrupt(board, player):
    """Function that removes the bankrupt player from the game and resets their properties"""
    # Get the player's properties
    properties = player.get_properties()
    
    # Reset isAvailable, isMortgaged, and houses values from player's properties
    for property in range(len(properties)):
        if properties[property][7] == None:
            pass
            
        else:
            properties[property][7] = 0
        
        properties[property][4] = False
        properties[property][2] = True
    
    # Remove all properties from the player and reset rent
    player.properties = []
    check_rent(board, player)
    
    # Remove the player from the board
    player.location = None
