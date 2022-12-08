# Project 2 - "Monopoly Game" (rent.py)
#
# Authors: Isaac Olvera and Dharmesh Tewari

def check_rent(board, player):
    """Function that increase the rent of a space on the board"""
    properties = player.get_properties()
    num_of_railroads = 0
    railroads = []
    
    # Orange and Fullerton
    if board[1] in properties and board[3] in properties:
        if board[1][7] == 0:
            board[1][3] = 4
            board[3][3] = 8
        
        elif board[1][7] == 1:
            board[1][3] = 10
            board[3][3] = 20
        
        elif board[1][7] == 2:
            board[1][3] = 30
            board[3][3] = 60
        
        elif board[1][7] == 3:
            board[1][3] = 90
            board[3][3] = 180
        
        elif board[1][7] == 4:
            board[1][3] = 160
            board[3][3] = 320
        
        elif board[1][7] == 5:
            board[1][3] = 250
            board[3][3] = 450
    
    else:
        board[1][3] = 2
        board[3][3] = 4
    
    # Pomona, Rialto, and Corona
    if board[6] in properties and board[8] in properties and board[9] in properties:
        if board[6][7] == 0:
            board[6][3] = 12
            board[8][3] = 12
            board[9][3] = 16
        
        elif board[6][7] == 1:
            board[6][3] = 30
            board[8][3] = 30
            board[9][3] = 40
        
        elif board[6][7] == 2:
            board[6][3] = 90
            board[8][3] = 90
            board[9][3] = 100
        
        elif board[6][7] == 3:
            board[6][3] = 270
            board[8][3] = 270
            board[9][3] = 300
        
        elif board[6][7] == 4:
            board[6][3] = 400
            board[8][3] = 400
            board[9][3] = 450
        
        elif board[6][7] == 5:
            board[6][3] = 550
            board[8][3] = 550
            board[9][3] = 600
    
    else:
        board[6][3] = 6
        board[8][3] = 6
        board[9][3] = 8
        
    # Palmdale, Inglewood, and Lancaster
    if board[11] in properties and board[13] in properties and board[14] in properties:
        if board[11][7] == 0:
            board[11][3] = 20
            board[13][3] = 20
            board[14][3] = 24
        
        if board[11][7] == 1:
            board[11][3] = 50
            board[13][3] = 50
            board[14][3] = 60
        
        if board[11][7] == 2:
            board[11][3] = 150
            board[13][3] = 150
            board[14][3] = 180
        
        if board[11][7] == 3:
            board[11][3] = 450
            board[13][3] = 450
            board[14][3] = 500
        
        if board[11][7] == 4:
            board[11][3] = 625
            board[13][3] = 625
            board[14][3] = 700
        
        if board[11][7] == 5:
            board[11][3] = 750
            board[13][3] = 750
            board[14][3] = 900
            
    else:
        board[11][3] = 10
        board[13][3] = 10
        board[14][3] = 12
        
    # Rancho Cucamonga, West Covina, and Ontario
    if board[16] in properties and board[18] in properties and board[19] in properties:
        if board[16][7] == 0:
            board[16][3] = 28
            board[18][3] = 28
            board[19][3] = 32
            
        if board[16][7] == 1:
            board[16][3] = 70
            board[18][3] = 70
            board[19][3] = 80
            
        if board[16][7] == 2:
            board[16][3] = 200
            board[18][3] = 200
            board[19][3] = 220
            
        if board[16][7] == 3:
            board[16][3] = 550
            board[18][3] = 550
            board[19][3] = 600
            
        if board[16][7] == 4:
            board[16][3] = 750
            board[18][3] = 750
            board[19][3] = 800
            
        if board[16][7] == 5:
            board[16][3] = 950
            board[18][3] = 950
            board[19][3] = 1000
            
    else:
        board[16][3] = 14
        board[18][3] = 14
        board[19][3] = 16
        
    # Huntington Beach, Jurapa Valley, and Fontana
    if board[21] in properties and board[23] in properties and board[24] in properties:
        if board[21][7] == 0:
            board[21][3] = 36
            board[23][3] = 36
            board[24][3] = 40
            
        if board[21][7] == 1:
            board[21][3] = 90
            board[23][3] = 90
            board[24][3] = 100
            
        if board[21][7] == 2:
            board[21][3] = 250
            board[23][3] = 250
            board[24][3] = 300
            
        if board[21][7] == 3:
            board[21][3] = 700
            board[23][3] = 700
            board[24][3] = 750
            
        if board[21][7] == 4:
            board[21][3] = 875
            board[23][3] = 875
            board[24][3] = 925
            
        if board[21][7] == 5:
            board[21][3] = 1050
            board[23][3] = 1050
            board[24][3] = 1100
    
    else:
        board[21][3] = 18
        board[23][3] = 18
        board[24][3] = 20
    
    # San Bernardino, Costa Mesa, and Anaheim
    if board[26] in properties and board[27] in properties and board[29] in properties:
        if board[26][7] == 0:
            board[26][3] = 44
            board[27][3] = 44
            board[29][3] = 48
            
        if board[26][7] == 1:
            board[26][3] = 110
            board[27][3] = 110
            board[29][3] = 120
            
        if board[26][7] == 2:
            board[26][3] = 330
            board[27][3] = 330
            board[29][3] = 360
            
        if board[26][7] == 3:
            board[26][3] = 800
            board[27][3] = 800
            board[29][3] = 850
            
        if board[26][7] == 4:
            board[26][3] = 975
            board[27][3] = 975
            board[29][3] = 1025
            
        if board[26][7] == 5:
            board[26][3] = 1150
            board[27][3] = 1150
            board[29][3] = 1200
    
    else:
        board[26][3] = 22
        board[28][3] = 22
        board[29][3] = 24
    
    # Fresno, Long Beach, and San Francisco
    if board[31] in properties and board[32] in properties and board[34] in properties:
        if board[31][7] == 0:
            board[31][3] = 52
            board[32][3] = 52
            board[34][3] = 56
        
        if board[31][7] == 1:
            board[31][3] = 130
            board[32][3] = 130
            board[34][3] = 150
        
        if board[31][7] == 2:
            board[31][3] = 390
            board[32][3] = 390
            board[34][3] = 450
        
        if board[31][7] == 3:
            board[31][3] = 900
            board[32][3] = 900
            board[34][3] = 1000
            
        if board[31][7] == 4:
            board[31][3] = 1100
            board[32][3] = 1100
            board[34][3] = 1200
            
        if board[31][7] == 5:
            board[31][3] = 1275
            board[32][3] = 1275
            board[34][3] = 1400
    
    else:
        board[31][3] = 26
        board[33][3] = 26
        board[34][3] = 28
    
    # San Diego and Los Angeles
    if board[37] in properties and board[39] in properties:
        if board[37][7] == 0:
            board[37][3] = 70
            board[39][3] = 100
        
        if board[37][7] == 1:
            board[37][3] = 175
            board[39][3] = 200
            
        if board[37][7] == 2:
            board[37][3] = 500
            board[39][3] = 600
            
        if board[37][7] == 3:
            board[37][3] = 1100
            board[39][3] = 1400
            
        if board[37][7] == 4:
            board[37][3] = 1300
            board[39][3] = 1700
            
        if board[37][7] == 5:
            board[37][3] = 1500
            board[39][3] = 2000
    
    else:
        board[37][3] = 35
        board[39][3] = 50
    
    # Find the total amount of railraods that the player owns
    for property in properties:
        if property == board[5] or property == board[15] or property == board[25] or property == board[35]:
            railroads.append(property)
            num_of_railroads += 1
    
    # Player owns 0 railroads
    if num_of_railroads == 0:
        board[5][3] = 25
        board[15][3] = 25
        board[25][3] = 25
        board[35][3] = 25
    
    # Player owns 1 railroad
    if num_of_railroads == 1:
        for railroad in railroads:
            railroad[3] = 25
        
    # Player owns 2 railroads
    if num_of_railroads == 2:
        for railroad in railroads:
            railroad[3] = 50
    
    # Player owns 3 railroads
    elif num_of_railroads == 3:
        for railroad in railroads:
            railroad[3] = 100
    
    # Player owns 4 railroads
    elif num_of_railroads == 4:
        for railroad in railroads:
            railroad[3] = 200
