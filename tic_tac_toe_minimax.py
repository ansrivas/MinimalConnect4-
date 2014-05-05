
import numpy as np
 

# relate numbers (1, -1, 0) to symbols ('x', 'o', '_')
symbols = {1:'x', -1:'o', 0:'_'}

HUMAN = 1
COMP = -1
TIE = 0

HUMAN_WON = False
COMP_WON = False
NO_ONE_WON = False

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


def choose_move(S,p):

    move,score = minimax_move(S,p) 
    S = apply_move(S,move[0],move[1],p)
    
    return S


def minimax_move(board,player):
   
    bestscore = None
    bestmove = None

    if player == COMP:
        bestscore = -2
    else:
        bestscore = 2
    
    xs,ys = available_moves(board) 
    for i in range(0,xs.size):
        board = apply_move(board,xs[i],ys[i],player)
        #apply a move, if this is the winning move, return from here 
        if isGameOver(board,player) :
            score = get_score(board,player)
        else:       
            move_position,score = minimax_move(board,flip_player(player)) 
        #clear the move      
        board = apply_move(board,xs[i],ys[i],0) 
      
        if player == COMP:
            if score > bestscore:
                bestscore = score
                bestmove = [xs[i],ys[i]]
        elif player == HUMAN:
            if score < bestscore:
                bestscore = score
                bestmove = [xs[i],ys[i]]

    return bestmove, bestscore


       
def play():
       # initialize 3x3 tic tac toe board
    gameState = np.zeros((3,3), dtype=int)
    #gameState = np.array([[-1,0, 1], [1,-1, -1],[0,1,1]])
    
    # initialize player number, move counter
    
    player = HUMAN              
    mvcntr = 1

    # initialize flag that indicates win
    noWinnerYet = True
    while move_still_possible(gameState) and noWinnerYet:
        # get player symbol
        name = symbols[player]
        print '%s moves' % name

        if player == HUMAN:
        # let player move at random
            gameState = move_at_random(gameState, player)
        else:
            print "AI turn"
        # let the computer choose its move using minimax algo    
            gameState = choose_move(gameState, player)
        # print current game state
        print_game_state(gameState)
            
        # evaluate game state
        if move_was_winning_move(gameState, player):
    
            print 'player %s wins after %d moves' % (name, mvcntr)
            noWinnerYet = False
            return player
            # switch player and increase move counter
        player *= -1
        mvcntr +=  1



    if noWinnerYet:
        print 'game ended in a draw' 
        return -10 # Some random integer to show that there was a game-draw 

if __name__ == '__main__':
    humanWinCounter = 0
    compWinCounter = 0 
    drawCounter = 0 
    #play()
   
    i = 0
    while i < 100:
        player = play()
        if player == HUMAN:
            humanWinCounter += 1
        elif player == COMP:
            compWinCounter += 1
        else:
            drawCounter += 1
        i += 1 
      
    print "Comp won\n",compWinCounter
    print "human won\n",humanWinCounter 
    print "Draw game\n", drawCounter 
