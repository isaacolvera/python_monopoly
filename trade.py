# Project 2 - "Monopoly Game" (trade.py)
#
# Author: Isaac Olvera

def trade(player_query, player):
    """Function that trades properties and/or money from one player to another"""
    select_player = 0
    new_query = []
    
    # Variables to determine what the player wants to trade
    pTrade_money = False
    opTrade_money = False
    pTrade_properties = False
    opTrade_properties = False
    
    # Get all the players that are in the game
    for person in player_query:
        if person == player:
            continue
        
        new_query.append(person)
        
    print(
        "\n--> Can only currently trade one property at a time <-- \n"
        "\nPlease select the player you'd like to trade with: "
    )
    
    # Player selects the person they want to trade with
    while select_player < len(new_query):
        print(str(select_player+1) + ". " + new_query[select_player].get_name())
        select_player += 1
    
    select_player += 1
    print(str(select_player) + ". None")
    
    # Catch invalid inputs
    while True:
        try:
            ans = int(input())
            
            while ans > select_player or ans < 1:
                ans = int(input("\nPlease enter a valid number: "))
            
            break
        
        except ValueError:
            print("\nPlease enter a valid number: ", end="")
    
    # The player does not want to trade
    if ans == select_player:
        print("\nGoing back to menu...")
    
    else:
        ans -= 1
        other_player = new_query[ans]
        
        print(
            "\nPlease select what you'd like to offer: \n"
            "1. Money\n"
            "2. Properties\n"
            "3. None"
        )
        
        # Catch invalid inputs
        while True:
            try:
                ans = int(input())
                
                while ans > 3 or ans < 1:
                    ans = int(input("\nPlease enter a valid number: "))
                
                break
            
            except ValueError:
                print("\nPlease enter a valid number: ", end="")
        
        # Player wants to trade their money
        if ans == 1:
            pTrade_money = True
            print("\nPlease enter the amount of money you want to give:")
            
            # Catch invalid inputs
            while True:
                try:
                    player_cash = int(input())
                    
                    while player_cash > player.get_money_amount() or player_cash < 0:
                        player_cash = int(input("\nPlease enter a valid number: "))
                    
                    break
                
                except ValueError:
                    print("\nPlease enter a valid number: ", end="")
        
        # Player wants to trade one of their properties     
        elif ans == 2:
            pTrade_properties = True                
            properties = player.get_properties()
            new_properties = []
            
            # Only allow properties with no houses (mortgaged is ok)
            for property in properties:
                if property[7] == 0 or property[7] == None:
                    new_properties.append(property)
            
            if new_properties == []:
                print("\nYou have no available properties to trade with!")
                return
            
            else:                    
                print("\nSelect the property you'd like to give: ")
                
                select_property = 0
                
                while select_property < len(new_properties):
                    print(str(select_property+1) + ". " + new_properties[select_property][0])
                    select_property += 1
                
                # Catch invalid inputs
                while True:
                    try:
                        choice = int(input())
                        
                        while choice > select_property or choice < 1:
                            choice = int(input("\nPlease enter a valid number: "))
                        
                        break
                    
                    except ValueError:
                        print("\nPlease enter a valid number: ", end="")
                        
                choice -= 1
                p_selected_property = new_properties[choice]
                                            
        else:
            print("\nCancelling trade...")
            return
        
        #######################################################################################################
        
        print(
            "\nPlease select what you'd like from " + other_player.get_name() + ": \n"
            "1. Money\n"
            "2. Properties\n"
            "3. None"
        )
        
        # Catch invalid inputs
        while True:
            try:
                ans = int(input())
                
                while ans > 3 or ans < 1:
                    ans = int(input("\nPlease enter a valid number: "))
                
                break
            
            except ValueError:
                print("\nPlease enter a valid number: ", end="")
        
        # Player wants money from the other player
        if ans == 1:
            opTrade_money = True
            print("\nPlease enter the amount of money you want:")
            
            # Catch invalid inputs
            while True:
                try:
                    op_cash = int(input())
                    
                    while op_cash > other_player.get_money_amount() or op_cash < 0:
                        op_cash = int(input("\nPlease enter a valid number: "))
                    
                    break
                
                except ValueError:
                    print("\nPlease enter a valid number: ", end="")
        
        # Player wants a property from the other player         
        elif ans == 2:
            opTrade_properties = True                
            properties = other_player.get_properties()
            new_properties = []
            
            # Only allow properties with no houses (mortgaged is ok)
            for property in properties:
                if property[7] == 0 or property[7] == None:
                    new_properties.append(property)
            
            if new_properties == []:
                print("\n" + other_player.get_name() + " has no available properties to trade with!")
                return
            
            else:                    
                print("\nSelect the property you want: ")
                
                select_property = 0
                
                while select_property < len(new_properties):
                    print(str(select_property+1) + ". " + new_properties[select_property][0])
                    select_property += 1
                
                # Catch invalid inputs
                while True:
                    try:
                        choice = int(input())
                        
                        while choice > select_property or choice < 1:
                            choice = int(input("\nPlease enter a valid number: "))
                        
                        break
                    
                    except ValueError:
                        print("\nPlease enter a valid number: ", end="")
                        
                choice -= 1
                op_selected_property = new_properties[choice]
                                            
        else:
            print("\nCancelling trade...")
            return
        
        #######################################################################################################
        
        print(
            "\n" + other_player.get_name() + " do you accept this deal?\n"
            "1. Yes\n"
            "2. No"
        )
        
        # Catch invalid inputs
        while True:
            try:
                ans = int(input())
                
                while ans > 2 or ans < 1:
                    ans = int(input("\nPlease enter a valid number: "))
                
                break
            
            except ValueError:
                print("\nPlease enter a valid number: ", end="")
        
        # Other player accepts the trade
        if ans == 1:
            # Player chose to trade their money
            if pTrade_money == True:
                pTotal_cash = player.get_money_amount()
                opTotal_cash = other_player.get_money_amount()
                pTotal_cash -= player_cash
                opTotal_cash += player_cash
                player.set_money_amount(pTotal_cash)
                other_player.set_money_amount(opTotal_cash)
            
            # Player chose to trade one of their properties
            if pTrade_properties == True:
                player_properties = player.get_properties()
                op_properties = other_player.get_properties()
                
                op_properties.append(p_selected_property)
                player_properties.remove(p_selected_property)
            
            # The other player is giving money in return
            if opTrade_money == True:
                pTotal_cash = player.get_money_amount()
                opTotal_cash = other_player.get_money_amount()
                pTotal_cash += op_cash
                opTotal_cash -= op_cash
                player.set_money_amount(pTotal_cash)
                other_player.set_money_amount(opTotal_cash)
            
            # The other player is giving one of their properties in return
            if opTrade_properties == True:
                player_properties = player.get_properties()
                op_properties = other_player.get_properties()
                
                player_properties.append(op_selected_property)
                op_properties.remove(op_selected_property)
            
            print("\nTrade completed!")
                    
        # Other player declines the trade
        else:
            print("\nCancelling trade...")
