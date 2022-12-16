# Project 2 - "Monopoly Game" (houses.py)
#
# Author: Isaac Olvera

def buy_houses(board, player):
    """Function that builds houses for a selected property from the player"""
    total_cash = player.get_money_amount()
    houses_price = 0
    select_property = 0

    # Player has one or more possbile properties to build houses on
    properties = player.get_properties()
    new_properties = []
    
    # Get all of the properties that are not mortgaged and are not utilities/railroads
    for property in properties:
        if property[7] == None:
            continue
        
        if property[7] == 5:
            continue
        
        if property[4] == False and property[7] < 5:
            new_properties.append(property)
    
    # Can't build houses on any of the available properties
    if new_properties == []:
        print("\nYou have no available properties to build houses on.")
    
    # Player has one or more properties they can build houses on
    else:
        print("\nPlease select the property (and its set) you want to build a house on: ")
        
        while select_property < len(new_properties):
            print(str(select_property+1) + ". " + new_properties[select_property][0])
            select_property += 1
        
        select_property += 1
        print(str(select_property) + ". None")
        
        # Catch invalid inputs
        while True:
            try:
                ans = int(input())
                
                while ans > select_property or ans < 1:
                    ans = int(input("\nPlease enter a valid number: "))
                
                break
            
            except ValueError:
                print("\nPlease enter a valid number: ", end="")
        
        # Player does not want to mortgage any of their properties
        if ans == select_property:
            print("\nGoing back to menu...")
        
        # Mortage the property that the player selects, add the mortgage cash to the players account,
        # then set the isMortgaged value to True
        else:
            ans -= 1
            property = new_properties[ans]
            
            if property == board[1] or property == board[3]:
                if board[1] in new_properties and board[3] in new_properties:
                    houses_price = 100
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print("\nBuilding houses on " + board[1][0] + " and " + board[3][0] + " for $" + str(houses_price))
                        board[1][7] += 1
                        board[3][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
            ####################################################################################################################
        
            elif property == board[6] or property == board[8] or property == board[9]:
                if board[6] in new_properties and board[8] in new_properties and board[9] in new_properties:
                    houses_price = 150
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[6][0] + ", " + 
                            board[8][0] + ", and " + 
                            board[9][0] + " for $" + str(houses_price)
                        )
                        
                        board[6][7] += 1
                        board[8][7] += 1
                        board[9][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
            ####################################################################################################################
        
            elif property == board[11] or property == board[13] or property == board[14]:
                if board[11] in new_properties and board[13] in new_properties and board[14] in new_properties:
                    houses_price = 300
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[11][0] + ", " + 
                            board[13][0] + ", and " + 
                            board[14][0] + " for $" + str(houses_price)
                        )
                        
                        board[11][7] += 1
                        board[13][7] += 1
                        board[14][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
            #################################################################################################################### 
        
            elif property == board[16] or property == board[18] or property == board[19]:
                if board[16] in new_properties and board[18] in new_properties and board[19] in new_properties:
                    houses_price = 300
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[16][0] + ", " + 
                            board[18][0] + ", and " + 
                            board[19][0] + " for $" + str(houses_price)
                        )
                        
                        board[16][7] += 1
                        board[18][7] += 1
                        board[19][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
            ####################################################################################################################
            
            elif property == board[21] or property == board[23] or property == board[24]:
                if board[21] in new_properties and board[23] in new_properties and board[24] in new_properties:
                    houses_price = 450
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[21][0] + ", " + 
                            board[23][0] + ", and " + 
                            board[24][0] + " for $" + str(houses_price)
                        )
                        
                        board[21][7] += 1
                        board[23][7] += 1
                        board[24][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
            ####################################################################################################################

            elif property == board[26] or property == board[27] or property == board[29]:
                if board[26] in new_properties and board[27] in new_properties and board[29] in new_properties:
                    houses_price = 450
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[26][0] + ", " + 
                            board[27][0] + ", and " + 
                            board[29][0] + " for $" + str(houses_price)
                        )
                        
                        board[26][7] += 1
                        board[27][7] += 1
                        board[29][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
            ####################################################################################################################
            
            elif property == board[31] or property == board[32] or property == board[34]:
                if board[31] in new_properties and board[32] in new_properties and board[34] in new_properties:
                    houses_price = 600
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[31][0] + ", " + 
                            board[32][0] + ", and " + 
                            board[34][0] + " for $" + str(houses_price)
                        )
                        
                        board[31][7] += 1
                        board[32][7] += 1
                        board[34][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")
        
        ####################################################################################################################
        
            elif property == board[37] or property == board[39]:
                if board[37] in new_properties and board[39] in new_properties:
                    houses_price = 400
                    
                    if total_cash < houses_price:
                        print("\nYou do not have enough to buy houses for this set.")
                    
                    else:
                        print(
                            "\nBuilding houses on " + 
                            board[37][0] + " and " + 
                            board[39][0] + " for $" + str(houses_price)
                        )
                        
                        board[37][7] += 1
                        board[39][7] += 1
                        total_cash -= houses_price
                        player.set_money_amount(total_cash)
                        print("This is your new total amount: $" + str(player.get_money_amount()))
                    
                else:
                    print("\nCan't build any houses (incomplete set, one or more properties are mortgaged, etc).")


def sell_houses(board, player):
    """Function that sells houses for a selected property from the player"""
    total_cash = player.get_money_amount()
    houses_price = 0
    select_property = 0
    
    # Player has one or more possbile properties to sell houses from
    properties = player.get_properties()
    new_properties = []
    
    # Get all of the properties that are not mortgaged and are not utilities/railroads
    for property in properties:
        if property[7] == None:
            continue
        
        if property[7] == 0:
            continue
        
        if property[4] == False and property[7] > 0:
            new_properties.append(property)
    
    # Can't sell houses on any of the available properties
    if new_properties == []:
        print("\nYou have no available properties to sell houses from.")
    
    # Player has one or more properties they can sell houses from
    else:
        print("\nPlease select the property (and its group) you want to sell a house from: ")
        
        while select_property < len(new_properties):
            print(str(select_property+1) + ". " + new_properties[select_property][0])
            select_property += 1
        
        select_property += 1
        print(str(select_property) + ". None")
        ans = int(input())
        
        while ans > select_property or ans < 1:
            ans = int(input("\nPlease enter a valid number: "))
        
        # Player does not want to sell any houses from their properties
        if ans == select_property:
            print("\nGoing back to menu...")
        
        # Mortage the property that the player selects, add the mortgage cash to the players account,
        # then set the isMortgaged value to True
        else:
            ans -= 1
            property = new_properties[ans]
            
            if property == board[1] or property == board[3]:
                if board[1] in new_properties and board[3] in new_properties:
                    houses_price = 50
                    
                    print("\nSelling houses from " + board[1][0] + " and " + board[3][0] + " for $" + str(houses_price))
                    board[1][7] -= 1
                    board[3][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
            
            #################################################################################################################
            
            elif property == board[6] or property == board[8] or property == board[9]:
                if board[6] in new_properties and board[8] in new_properties and board[9] in new_properties:
                    houses_price = 75
                    
                    print(
                        "\nSelling houses from " + 
                        board[6][0] + ", " + 
                        board[8][0] + ", and " + 
                        board[9][0] + " for $" + str(houses_price)
                    )
                    
                    board[6][7] -= 1
                    board[8][7] -= 1
                    board[9][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
            
            #################################################################################################################
            
            elif property == board[11] or property == board[13] or property == board[14]:
                if board[11] in new_properties and board[13] in new_properties and board[14] in new_properties:
                    houses_price = 150
                    
                    print(
                        "\nSelling houses from " + 
                        board[11][0] + ", " + 
                        board[13][0] + ", and " + 
                        board[14][0] + " for $" + str(houses_price)
                    )
                    
                    board[11][7] -= 1
                    board[13][7] -= 1
                    board[14][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
            
            ################################################################################################################# 
            
            elif property == board[16] or property == board[18] or property == board[19]:
                if board[16] in new_properties and board[18] in new_properties and board[19] in new_properties:
                    houses_price = 150
                    
                    print(
                        "\nSelling houses from " + 
                        board[16][0] + ", " + 
                        board[18][0] + ", and " + 
                        board[19][0] + " for $" + str(houses_price)
                    )
                    
                    board[16][7] -= 1
                    board[18][7] -= 1
                    board[19][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
                
            #################################################################################################################
            
            elif property == board[21] or property == board[23] or property == board[24]:
                if board[21] in new_properties and board[23] in new_properties and board[24] in new_properties:
                    houses_price = 225
                
                    print(
                        "\nSelling houses from " + 
                        board[21][0] + ", " + 
                        board[23][0] + ", and " + 
                        board[24][0] + " for $" + str(houses_price)
                    )
                    
                    board[21][7] -= 1
                    board[23][7] -= 1
                    board[24][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
                
            #################################################################################################################

            elif property == board[26] or property == board[27] or property == board[29]:
                if board[26] in new_properties and board[27] in new_properties and board[29] in new_properties:
                    houses_price = 225
                
                    print(
                        "\nSelling houses from " +
                        board[26][0] + ", " + 
                        board[27][0] + ", and " +
                        board[29][0] + " for $" + str(houses_price)
                    )
                    
                    board[26][7] -= 1
                    board[27][7] -= 1
                    board[29][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
                
            #################################################################################################################
            
            elif property == board[31] or property == board[32] or property == board[34]:
                if board[31] in new_properties and board[32] in new_properties and board[34] in new_properties:
                    houses_price = 300
                
                    print(
                        "\nSelling houses from " + 
                        board[31][0] + ", " + 
                        board[32][0] + ", and " + 
                        board[34][0] + " for $" + str(houses_price)
                    )
                    
                    board[31][7] -= 1
                    board[32][7] -= 1
                    board[34][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
                
            #################################################################################################################
            
            elif property == board[37] or property == board[39]:
                if board[37] in new_properties and board[39] in new_properties:
                    houses_price = 200
                
                    print("\nSelling houses from " + board[37][0] + " and " + board[39][0] + " for $" + str(houses_price))
                    board[37][7] -= 1
                    board[39][7] -= 1
                    total_cash += houses_price
                    player.set_money_amount(total_cash)
                    print("This is your new total amount: $" + str(player.get_money_amount()))
                
                else:
                    print("\nCan't sell any houses (incomplete set, one or more properties are mortgaged, etc).")
