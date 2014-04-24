#Could use these to improve the program
#raise Exception('Column is full')
 


import numpy as np
import pandas as pd

# relate numbers (1, -1, 0) to symbols ('x', 'o', ' ')
symbols = {1:'R', -1:'Y', 0:'_'}

COLUMNS = 7
ROWS = 6
row_labels = ['1', '2', '3', '4','5','6']
column_labels = ['1', '2', '3', '4','5','6','7']

# print game state matrix using symbols
def print_game_state(S):
    B = np.copy(S).astype(object)
    for n in [-1, 0, 1]:
        B[B==n] = symbols[n]

    df = pd.DataFrame(B, columns=column_labels, index=row_labels)
    print df

    
       

#the routine to check the winner at each move, possibilities to improve this using numpy
def isWinner(board, tile):
    
    # check horizontal spaces
    for y in range(ROWS):
        #This returns the row number
        x= board[y]
        #This returns the sum of 4 elements
        test_sum = [sum(x[i:4+i]) for i in range(COLUMNS-3)]
        #Convert it into a nparray and check if any element is equal to the required sum
        if np.any(np.array(test_sum) == 4*tile):
            print "\n-------Matched Horizontally-------\n"
            return True
    '''        
    for x in range(ROWS): 
        for y in range(COLUMNS -3 ):
            if board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3]== 4*tile:
                print "\n-------Matched Horizontally-------\n"
                return True
     '''  
    
    # check vertical spaces  
    for x in range(COLUMNS):
        #This returns the column
        y= board[:,x]
        #This returns the sum of 4 elements
        test_sum = [sum(y[i:4+i]) for i in range(ROWS-3)]
        #Convert it into a nparray and check if any element is equal to the required sum
        if np.any(np.array(test_sum) == 4*tile):
            print "\n-------Matched Vertically-------\n"
            return True
    
    '''
    for x in range(ROWS - 3):
        for y in range(COLUMNS):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                print "\n-------Matched Vertically-------\n"  
                return True
    '''
     
                       
    # check / diagonal spaces
    for x in range(ROWS - 3):
        for y in range(3, COLUMNS):            
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                print "\n-------Matched Diagonally /-------\n"  
                return True
    
                
    # check \ diagonal spaces    
    for x in range(ROWS - 3):
        for y in range(COLUMNS - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                print "\n-------Matched Diagonally \-------\n"
                return True
            
    return False
    
    
    
    
def move_still_possible(S):
   
    #Check if there is any empty space in the first row
    if np.any(S[0] ==0):
        return True
         
    return False
    
		    
def move_at_random(S, p):
     
    random_column = np.random.permutation(np.arange(COLUMNS))[0]
    
    row_count = ROWS-1
    while row_count >= 0:
        if S[row_count][random_column] == 0:
            break
        row_count -= 1

    if(row_count == -1):
        print '%d-column full, trying something else !!\n'%random_column
        return S
    
    
    S[row_count][random_column] = p 
       
    return S   
       
    
if __name__ == '__main__':
    # initialize 6x7 Connect4 board
    gameState = np.zeros((6,7), dtype=int)

    # initialize player number, move counter
    player = 1
    mvcntr = 1

    # initialize flag that indicates win
    noWinnerYet = True
    
    print_game_state(gameState)
     
    while move_still_possible(gameState) and noWinnerYet :
        # get player symbol
        name = symbols[player]
        print '%s moves\n' % name

        # let player move at random
        gameState = move_at_random(gameState, player)

        # print current game state
        print_game_state(gameState)
        
        # evaluate game state
        
        if isWinner(gameState, player):
            print 'player %s wins after %d moves\n' % (name, mvcntr)
            noWinnerYet = False
        
        # switch player and increase move counter
        player *= -1
        mvcntr +=  1


    if noWinnerYet:
        print 'game ended in a draw\n' 


