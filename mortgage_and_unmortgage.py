# Project 2 - "Monopoly Game" (mortgage_and_unmortgage.py)
#
# Authors: Isaac Olvera and Dharmesh Tewari

def mortgage_property(player):
    """Function that mortgages a selected property from the player"""
    total_cash = player.get_money_amount()
    select_property = 0
    
    # Player has one or more possbile properties to mortgage
    properties = player.get_properties()
    new_properties = []
    
    # Get all of the properties that are not mortgaged already
    for property in properties:
        if property[4] == False:
            new_properties.append(property)
    
    # All of the player's properties are mortgaged or there are no properties
    if new_properties == []:
        print("\nYou have no available properties to mortgage.")
    
    # Player has one or more properties they can mortgage
    else:
        print("\nPlease select the property you want to mortage: ")
        
        while select_property < len(new_properties):
            print(str(select_property+1) + ". " + new_properties[select_property][0])
            select_property += 1
        
        select_property += 1
        print(str(select_property) + ". None")
        ans = int(input())
        
        while ans > select_property or ans < 1:
            ans = int(input("\nPlease enter a valid number: "))
        
        # Player does not want to mortgage any of their properties
        if ans == select_property:
            print("\nGoing back to menu...")
        
        # Mortage the property that the player selects, add the mortgage cash to the players account,
        # then set the isMortgaged value to True
        else:            
            ans -= 1
            property = new_properties[ans]

            if property[7] == 0 or property[7] == None:
                print("\nMortgaging " + property[0] + " for $" + str(property[5]))
                property[4] = True
                total_cash += property[5]
                player.set_money_amount(total_cash)
                print("This is your new total amount: $" + str(player.get_money_amount()))
            
            elif property[7] >= 1:
                print("\nYou can't mortgage properties with houses on them!")


def unmortgage_property(player):
    """Function that unmortgages a selected property from the player"""
    total_cash = player.get_money_amount()
    select_property = 0
    
    # Player has one or more possbile properties to unmortgage
    properties = player.get_properties()
    new_properties = []
    
    # Get all of the properties that are not unmortgaged already
    for property in properties:
        if property[4] == True:
            new_properties.append(property)
    
    # All of the player's properties are unmortgaged
    if new_properties == []:
        print("\nYou have no available properties to unmortgage.")
    
    # Player has one or more properties they can unmortgage
    else:
        print("\nPlease select the property you want to unmortage: ")
        
        while select_property < len(new_properties):
            print(str(select_property+1) + ". " + new_properties[select_property][0])
            select_property += 1
        
        select_property += 1
        print(str(select_property) + ". None")
        ans = int(input())
        
        while ans > select_property or ans < 1:
            ans = int(input("\nPlease enter a valid number: "))
        
        # Player does not want to unmortgage any of their properties
        if ans == select_property:
            print("\nGoing back to menu...")
        
        # Unmortage the property that the player selects, subtract the unmortgage cash from the players account,
        # then set the isMortgaged value to False
        else:
            ans -= 1
            property = new_properties[ans]
                       
            if total_cash >= property[6]:
                print("\nUnmortgaging " + property[0] + " for $" + str(property[6]))
                property[4] = False
                total_cash -= property[6]
                player.set_money_amount(total_cash)
                print("This is your new total amount: $" + str(player.get_money_amount()))
            
            else:
                print("\nYou do not have enough to unmortage this property")
