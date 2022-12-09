# Project 2 - "Monopoly Game" (monopoly.py)
#
# Author: Isaac Olvera

import random
from players import *
from chance_and_communitychest import *
from rent import *
from houses import *
from mortgage_and_unmortgage import *
from bankrupt import *


# Board = [Name, Price, isAvailable, Rent, isMortgaged, Mortgage Price, Unmortgage Price, Houses]
board = [
    ["Go", None, None, 200, None, None, None, None],
    ["Orange", 60, True, 2, False, 30, 33, 0],       
    ["Community Chest", "CC", None, None, None, None, None, None],
    ["Fullerton", 60, True, 4, False, 30, 33, 0],
    ["Income Tax", "IT", None, 200, None, None, None, None],
    ["Central California Traction", 200, True, 25, False, 100, 110, None],
    ["Pomona", 100, True, 6, False, 50, 55, 0],
    ["Chance", "CH", None, None, None, None, None, None],
    ["Rialto", 100, True, 6, False, 50, 55, 0],
    ["Corona", 120, True, 8, False, 60, 66, 0],
    ["Jail/Just Visiting", None, None, 50, None, None, None, None],
    ["Palmdale", 140, True, 10, False, 70, 77, 0],
    ["Southern California Edison", 150, True, 50, False, 75, 83, None],
    ["Inglewood", 140, True, 10, False, 70, 77, 0],
    ["Lancaster", 160, True, 12, False, 80, 88, 0],
    ["Quincy Railroad", 200, True, 25, False, 100, 110, None],
    ["Rancho Cucamonga", 180, True, 14, False, 90, 99, 0],
    ["Community Chest", "CC", None, None, None, None, None, None],
    ["West Covina", 180, True, 14, False, 90, 99, 0],
    ["Ontario", 200, True, 16, False, 100, 110, 0],
    ["Free Parking", "FP", None, 0, None, None, None, None],
    ["Huntington Beach", 220, True, 18, False, 110, 121, 0],
    ["Chance", "CH", None, None, None, None, None, None],
    ["Jurapa Valley", 220, True, 18, False, 110, 121, 0],
    ["Fontana", 240, True, 20, False, 120, 132, 0],
    ["Sacramento Valley Railroad", 200, True, 25, False, 100, 110, None],
    ["San Bernardino", 260, True, 22, False, 130, 143, 0],
    ["Costa Mesa", 260, True, 22, False, 130, 143, 0],
    ["California Water Service", 150, True, 50, False, 75, 83, None],
    ["Anaheim", 280, True, 24, False, 140, 154, 0],
    ["Go To Jail", "GTJ", None, None, None, None, None, None],
    ["Fresno", 300, True, 26, False, 150, 165, 0],
    ["Long Beach", 300, True, 26, False, 150, 165, 0],
    ["Community Chest", "CC", None, None, None, None, None, None],
    ["San Francisco", 320, True, 28, False, 160, 176, 0],
    ["Pacific Harbor Line", 200, True, 25, False, 100, 110, None],
    ["Chance", "CH", None, None, None, None, None, None],
    ["San Diego", 350, True, 35, False, 175, 193, 0],
    ["Luxury Tax", "LT", None, 100, None, None, None, None],
    ["Los Angeles", 400, True, 50, False, 200, 220, 0]
]


def player_in_jail(player, turns_in_jail, location):
    """Function that allows the player to determine certain actions while in jail"""
    print(
        "\nYou are in jail. You have two options:\n"
        "1. Pay $50 fine and go next turn\n"
        "2. Roll doubles for a chance to leave without paying and go next turn (3 turns max)"
    )
    
    # Catch invalid inputs
    while True:
        try:
            jail_ans = int(input())
            
            while jail_ans > 2 or jail_ans < 1:
                jail_ans = int(input("\nPlease enter a valid number: "))
            
            break
        
        except ValueError:
            print("\nPlease enter a valid number: ", end="")
        
    
    # Player pays the $50 fine and will go the next turn
    if jail_ans == 1:
        total_cash = player.get_money_amount()
        total_cash -= board[location][3]
        player.set_money_amount(total_cash)
        
        if player.get_money_amount() < 0:
            maybe_bankrupt(board, player)
        
        elif player.bankrupt == False:
            print("\nYou successfully paid your fine. You will now go next turn.")
            print("This is your new total amount: $" + str(player.get_money_amount()))
            player.inJail = False
            turns_in_jail = 3
    
    # Player takes a chance rolling doubles (only have 3 turns, must pay fine if turns = 0)
    elif jail_ans == 2:
        input("\nPress [Enter] to roll the dice.")
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("You rolled [" + str(die1) + "][" + str(die2) + "]")
        
        # Roll was successful, they will go the next turn
        if die1 == die2:
            print("\nYou successfully rolled doubles. You will now go next turn.")
            player.inJail = False
            turns_in_jail = 3
            print()
        
        # Roll was not successful, they have 3 total turns to try again or pay fine
        else:
            print("\nYou did not roll doubles. You must wait another turn to try again or pay the fine.")
            turns_in_jail -= 1
            print("Turns left: " + str(turns_in_jail))
            
            # Player is out of turns and must pay the fine
            if turns_in_jail == 0:
                print("\nYou are out of turns and you must pay the fine. You will now go next turn.")
                total_cash = player.get_money_amount()
                total_cash -= board[location][3]
                player.set_money_amount(total_cash)
                
                if player.get_money_amount() < 0:
                    maybe_bankrupt(board, player)
                
                elif player.bankrupt == False:
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                    player.inJail = False
                    turns_in_jail = 3
                    
    return turns_in_jail, location


def main():
    """Main function of the game, loops until there is a winner (all other players go bankrupt)"""
    # Variables to help determine actions within the game
    playing_monopoly = True
    players = PlayerQuery()
    passed_go = False
    turns_in_jail = 3
    num_of_doubles = 0
    i = 0
    global board
                    
    print("Welcome to Monopoly!")
    print("\nEnter the total number of players for this game (2-6): ")
    
    # Catch invalid inputs
    while True:
        try:
            num_of_players = int(input())
            
            while num_of_players > 6 or num_of_players < 2:
                num_of_players = int(input("\nPlease enter a valid number: "))
                
            break
        
        except ValueError:
            print("\nPlease enter a valid number: ", end="")
            
    
    player_query = players.circular_queue(num_of_players)
    
    print("\n--------------------------------------------")
    print("           Time to start the game!            ")
    print("--------------------------------------------\n")
    
    # Continue playing the game until only one person remains
    while playing_monopoly:
        if num_of_players == 1:
            print("The game has officially ended!\n") 
            print(player_query[0].get_name() + " has won the game! Congratulations!")
            playing_monopoly = False
            continue
            
        print(player_query[i].get_name() + "'s turn!")
        
        # The player is in jail
        if player_query[i].inJail == True:
            turns_in_jail, location = player_in_jail(player_query[i], turns_in_jail, location)
            
            # Player went bankrupt while in jail
            if player_query[i].bankrupt == True:
                print("\n" + player_query[i].get_name() + " has gone bankrupt and is out of the game!")
                bankrupt(board, player_query[i])
                player_query.pop(i)
                i -= 1
                num_of_players -= 1
            
            # Go to next player
            num_of_doubles = 0
            i += 1
            
            if i >= num_of_players:
                i = 0
                
            print("\n--------------------------------------------\n")
            continue                 
        
        # The player is not in jail
        else:
            input("Press [Enter] to roll your dice.")
            
            location = player_query[i].get_location()
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)                
            dice = die1 + die2
            location += dice
            print("\nYou rolled [" + str(die1) + "][" + str(die2) + "]")
            
            # Player completed one loop around the board
            if location >= len(board):
                location -= 40
                passed_go = True
                                                
            print("You landed on: " + str(board[location][0]))
            player_query[i].set_location(location)
            
            # Player collects $200 if they passed go or landed on it
            if passed_go:
                print("\nYou passed or landed on Go, collect $200!")
                total_cash = player_query[i].get_money_amount()
                total_cash += board[0][3]
                player_query[i].set_money_amount(total_cash)
                print("This is your new total amount: $" + str(player_query[i].get_money_amount()))
                passed_go = False
            
            # Property is owned by someone
            if board[location][2] == False:
                # Find out who owns the property
                for j in range(num_of_players):
                    if j == i:
                        continue
                    
                    # Property is mortgaged, pay them nothing
                    if board[location] in player_query[j].get_properties() and board[location][4] == True:
                        print("\nThis property belongs to " + player_query[j].get_name() + ", but it is mortgaged.")
                        print("You owe them: $0")
                        break
                    
                    # Player is in jail, pay them nothing
                    if board[location] in player_query[j].get_properties() and player_query[j].inJail == True:
                        print("\nThis property belongs to " + player_query[j].get_name() + ", but they are in jail.")
                        print("You owe them: $0")
                        break
                    
                    # Pay the player their rent for the property
                    if board[location] in player_query[j].get_properties() and board[location][4] == False:
                        print("\nThis property belongs to " + player_query[j].get_name())
                        print("You owe them: $" + str(board[location][3]))
                        total_cash1 = player_query[i].get_money_amount()
                        total_cash2 = player_query[j].get_money_amount()
                        total_cash1 -= board[location][3]
                        total_cash2 += board[location][3]
                        player_query[i].set_money_amount(total_cash1)
                        player_query[j].set_money_amount(total_cash2)
                        
                        # Check if they might go bankrupt from paying the other player rent
                        if player_query[i].get_money_amount() < 0:
                            maybe_bankrupt(board, player_query[i])
                        
                        # Both player's are still in game
                        elif player_query[i].bankrupt == False:
                            print("\nThis is " + player_query[i].get_name() + "'s new total amount: $" + str(player_query[i].get_money_amount()))
                            print("This is " + player_query[j].get_name() + "'s new total amount: $" + str(player_query[j].get_money_amount()))
                            break
            
            # Community Chest
            elif board[location][1] == "CC":
                cash = community_chest()
                total_cash = player_query[i].get_money_amount()
                total_cash += cash
                player_query[i].set_money_amount(total_cash)
                
                # Check if they might go bankrupt from community chest
                if player_query[i].get_money_amount() < 0:
                    maybe_bankrupt(board, player_query[i])
            
                # Player is still in game
                elif player_query[i].bankrupt == False:
                    print("\nThis is your new total amount: $" + str(player_query[i].get_money_amount()))
            
            # Chance
            elif board[location][1] == "CH":
                cash = chance()
                total_cash = player_query[i].get_money_amount()
                total_cash += cash
                player_query[i].set_money_amount(total_cash)
                
                # Check if they might go bankrupt from chance
                if player_query[i].get_money_amount() < 0:
                    maybe_bankrupt(board, player_query[i])

                # Player is still in game
                elif player_query[i].bankrupt == False:
                    print("\nThis is your new total amount: $" + str(player_query[i].get_money_amount()))
                
            # Income tax
            elif board[location][1] == "IT":
                print("\nThis is income tax! Deducting $200 from your account.")
                total_cash = player_query[i].get_money_amount()
                total_cash -= board[location][3]
                player_query[i].set_money_amount(total_cash)

                # Check if they might go bankrupt from income tax
                if player_query[i].get_money_amount() < 0:
                    maybe_bankrupt(board, player_query[i])
            
                # Player is still in game
                elif player_query[i].bankrupt == False:
                    print("This is your new total amount: $" + str(player_query[i].get_money_amount()))
            
            # Free Parking
            elif board[location][1] == "FP":
                print("\nThis is free parking, enjoy a movie!")
                
            # Go To Jail
            elif board[location][1] == "GTJ":
                print("\nStop, you are under arrest! Go to jail!")
                
                # Send the player to jail by setting location
                location = 10
                player_query[i].set_location(10)
                player_query[i].inJail = True
                
                # Skip the rest of their turn
                num_of_doubles = 0
                i += 1
                
                if i >= num_of_players:
                    i = 0
                    
                print("\n--------------------------------------------\n")
                continue

            # Luxury Tax
            elif board[location][1] == "LT":
                print("\nThis is luxury tax! Deducting $100 from your account.")
                total_cash = player_query[i].get_money_amount()
                total_cash -= board[location][3]
                player_query[i].set_money_amount(total_cash)
                
                # Check if they might go bankrupt from luxury tax
                if player_query[i].get_money_amount() < 0:
                    maybe_bankrupt(board, player_query[i])
            
                # Player is still in game
                elif player_query[i].bankrupt == False:
                    print("This is your new total amount: $" + str(player_query[i].get_money_amount()))
            
            # The player has gone bankrupt from any of the previous outcomes
            if player_query[i].bankrupt == True:
                    print("\n" + player_query[i].get_name() + " has gone bankrupt and is out of the game!")
                    
                    # Remove the player from the game by reseting their properties and removing
                    # them from the board
                    bankrupt(board, player_query[i])
                    player_query.pop(i)
                    num_of_players -= 1
                    
                    # Go the next player
                    num_of_doubles = 0
                    if i >= num_of_players:
                        i = 0
                        
                    print("\n--------------------------------------------\n")
            
            # Player is not bankrupt and is still playing
            else:
                # Loop until player wishes to end their turn
                while True:
                    print(
                        "\nWhat would you like to do?\n"
                        "1. Buy property\n"
                        "2. Mortgage property\n"
                        "3. Unmortgage property\n"
                        "4. Buy houses\n"
                        "5. Sell houses\n"
                        "6. Check properties\n"
                        "7. Check cash amount\n"
                        "8. Trade (Not implemented)\n"
                        "9. End turn"
                    )
                    
                    # Catch invalid inputs
                    while True:
                        try:
                            ans = int(input())
                            
                            while ans > 9 or ans < 1:
                                ans = int(input("\nPlease enter a valid number: "))
                            
                            break
                        
                        except ValueError:
                            print("\nPlease enter a valid number: ", end="")
                    
                    # Player want to buy the property
                    if ans == 1:
                        total_cash = player_query[i].get_money_amount()
                        
                        # Already owned
                        if board[location] in player_query[i].get_properties():
                            print("\nYou already own this property!")
                        
                        # Owned by another player
                        elif board[location] not in player_query[i].get_properties() and board[location][2] == False:
                            print("\nSorry but this property is owned by someone else.")

                        # Unattainable
                        elif board[location][2] == None:
                            print("\nYou can't buy this property!")
                        
                        # Not enough cash
                        elif total_cash < board[location][1]:
                            print("\nYou don't have enough to buy this property.")
                        
                        # Player can buy the property
                        else:
                            print("\nCongrats! You just bought " + board[location][0] + " for: $" + str(board[location][1]))
                            total_cash -= board[location][1]
                            player_query[i].set_money_amount(total_cash)
                            print("This is your new total amount: $" + str(player_query[i].get_money_amount()))
                            
                            # Add property to the player's list of properties
                            player_query[i].set_properties(board[location])
                            board[location][2] = False
                    
                    # Mortgage a property
                    elif ans == 2:
                        mortgage_property(player_query[i])
                    
                    # Unmortgage a property     
                    elif ans == 3:
                        unmortgage_property(player_query[i])
                    
                    # Buy houses for a set
                    elif ans == 4:
                        buy_houses(board, player_query[i])
                    
                    # Sell houses from a set
                    elif ans == 5:
                        sell_houses(board, player_query[i])
                    
                    # Show the player their properties
                    elif ans == 6:
                        properties = player_query[i].get_properties()
                        show_properties = []
                        print("\nYou currently own these properties:")
                        
                        for k in range(len(properties)):
                            show_properties.append(properties[k][0])
                        
                        print(show_properties)
                    
                    # Show the player their total cash amount  
                    elif ans == 7:
                        print("\nYou currently have: $" + str(player_query[i].get_money_amount()))
                    
                    # Trade with another player (Not implemented)
                    elif ans == 8:
                        pass
                    
                    else:
                        break
                
                # Check rent prices for all properties
                check_rent(board, player_query[i])

                # Player got doubles
                if die1 == die2:
                    # Player has not exceeded the amount of doubles they can roll
                    if num_of_doubles < 2:
                        print("\nYou got doubles, go again!\n")
                        num_of_doubles += 1
                        continue
                    
                    # Player has exceeded the amount of doubles they can roll, send them to jail
                    else:
                        print("\nYou rolled doubles 3 times in a row. Sorry, but you must go to jail for speeding!")
                        location = 10
                        player_query[i].set_location(10)
                        player_query[i].inJail = True

                # Go to the next player
                num_of_doubles = 0
                i += 1
                
                if i >= num_of_players:
                    i = 0
                    
                print("\n--------------------------------------------\n")
        
        
if __name__ == '__main__':
    main()
