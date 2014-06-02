# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:57:26 2014

@author: ankur
"""


import numpy as np
 
#Change this to true if you want total finished games and X's wins and total nodes with proper termination
#change this to false if you want total number of possible combination of Xs and Os and moves  
print_game_trees = True







# relate numbers (1, -1, 0) to symbols ('x', 'o', '_')
symbols = {1:'x', -1:'o', 0:'_'}

HUMAN = 1
COMP = -1
TIE = 0
LEVEL =0
HUMAN_WON = False
COMP_WON = False
NO_ONE_WON = False
COUNT = 0
X_WINS = 0
O_WINS = 0 
TOTAL_FINISHED_GAME = 0 

#These are the number of nodes which don't consider the properly finished states, it continues even after that
TOTAL_NUMBER_OF_NODES = 0
 
#These are the number of nodes which consider the termiated states as well
TOTAL_NODES = 1

def set_winner(player):
    #Whenever we need to assign a global variable, redeclare it
    global HUMAN_WON,COMP_WON,NO_ONE_WON
    HUMAN_WON = False
    COMP_WON = False
    NO_ONE_WON = False
    
    if player == COMP:
        COMP_WON = True
    elif player == HUMAN:
        HUMAN_WON = True
    else: 
        NO_ONE_WON = True
        
        
        
def flip_player(player):
    return -1*player

def move_still_possible(S):
    return not (S[S==0].size == 0)


def move_at_random(S, p):
    xs, ys = np.where(S==0)

    i = np.random.permutation(np.arange(xs.size))[0]
    S[xs[i],ys[i]] = p

    return S


def available_moves(S):
    
    xs, ys = np.where(S==0)
    return xs,ys
    

def apply_move(S,x,y,player):
        
    S[x,y] = player
    return S


def move_was_winning_move(S, p):
    if np.max((np.sum(S, axis=0)) * p) == 3:
        return True

    if np.max((np.sum(S, axis=1)) * p) == 3:
        return True

    if (np.sum(np.diag(S)) * p) == 3:
        return True

    if (np.sum(np.diag(np.rot90(S))) * p) == 3:
        return True

    return False




# print game state matrix using symbols
def print_game_state(S):
    
    B = np.copy(S).astype(object)
    for n in [-1, 0, 1]:
        B[B==n] = symbols[n]
    print B


def isGameOver(S,p):
    """is the game over?"""
        
    if move_was_winning_move(S,p):
        if p == COMP:
            set_winner(COMP)
        else:
            set_winner(HUMAN)
        return True
     
    if move_still_possible(S) == False:
        set_winner(TIE)
        return True

    return False


#Concept of depth to be explained
def get_score(S,p):
    score = 0
    bGameOver = isGameOver(S,p)
    if bGameOver:
        if COMP_WON:
            score= 1 # Won
        elif HUMAN_WON:
            score = -1 # Opponent won
          
    return score # Draw


def choose_move(S,p,count_games,level):

    print_total_games(S,p,count_games,level) 



def print_total_games(board,player,count_games,level):
   
    global LEVEL,COUNT,X_WINS,O_WINS,TOTAL_FINISHED_GAME,TOTAL_NUMBER_OF_NODES,TOTAL_NODES
        
    xs,ys = available_moves(board)
    if not count_games:
        if xs.size == 0:
            COUNT+=1

    if count_games:
        if level == 9:
            return TOTAL_NODES
        
    for i in range(xs.size):
        board = apply_move(board,xs[i],ys[i],player)
            
            
        if count_games:
            TOTAL_NODES +=1
            if isGameOver(board,player) :
                
                TOTAL_FINISHED_GAME +=1
                    #total number of games, even if the game terminates
                if HUMAN_WON:
                    X_WINS +=1
                if COMP_WON:
                    O_WINS +=1
                    
                #reset the move and return from here
                board = apply_move(board,xs[i],ys[i],0) 
                continue
        else:
            TOTAL_NUMBER_OF_NODES += 1
          
          
        
        print_total_games(board,flip_player(player),count_games,level+1) 
        #clear the move      
        board = apply_move(board,xs[i],ys[i],0) 

    return


       
def play():
       # initialize 3x3 tic tac toe board
    gameState = np.zeros((3,3), dtype=int)
    
    # initialize player number, move counter
    level = 0
    player = HUMAN              
    choose_move(gameState, player,print_game_trees,level)
    

if __name__ == '__main__':

    play()
   
   

    if print_game_trees:
        print "\nX_WINS:", X_WINS
        print "\nTOTAL_FINISHED_GAMES",TOTAL_FINISHED_GAME
        print "\nTotal nodes considering terminated nodes ",TOTAL_NODES
    else:
        print "\nTotal Number of possible combinations of Xs and Os", COUNT
        print "\nTotal number of moves",TOTAL_NUMBER_OF_NODES