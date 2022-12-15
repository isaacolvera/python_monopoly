# Project 2 - "Monopoly Game" (players.py)
#
# Author: Isaac Olvera 

class Player:
    """Player class that initizlizes basic information for the player"""
    
    def __init__(self):
        """Function that sets the player's name, money, places they own, etc."""
        self.name = ""
        self.money_amount = 1500
        self.properties = []
        self.bankrupt = False
        self.inJail = False
        self.location = 0
    
    def set_name(self, name):
        """Function that sets the name of the player"""
        self.name = name

    def get_name(self):
        """Function that gets the name of the player"""
        return self.name
    
    def set_money_amount(self, money_amount):
        """Function that sets the amount of money for the player"""
        self.money_amount = money_amount

    def get_money_amount(self):
        """Function that gets the amount of money for the player"""
        return self.money_amount
    
    def set_properties(self, property):
        """Function that sets the amount of places that the player owns"""
        self.properties.append(property)

    def get_properties(self):
        """Function that gets the amount of places that the player owns"""
        return self.properties
    
    def set_location(self, dice):
        """Function that sets the location of the player on the board"""
        self.location = dice

    def get_location(self):
        """Function that gets the location of the player on the board"""
        return self.location


class PlayerQuery:
    """Player queue class that initializes a query to hold player classes"""
    
    def circular_queue(self, num_of_players):
        """Function that creates the player_query to be used in the game"""
        player_count = []
        i = 1
        print()
        
        while i <= num_of_players:
            person = Player()
            name = input("Player " + str(i) + ": ")
            
            person.set_name(name)
            player_count.append(person)
            i += 1
        
        return player_count
