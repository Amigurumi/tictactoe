# welcome and game rules
def welcome ():
    print ('Welcome to TicTacToe by VB')
    print ('Game Rules:')
    print ('- Player 1 take the first turn with X')
    print ('- Player 2 take the second turn with O')
    print ('- Player 1 and 2 then take turn till the game ends')
    print ('- The game ends when there are 3 touching X or O in a row/column/diagnonal or the game board is full')

# get players' names
def get_players():
    player1 = input ('Enter Player 1 Name: ')
    player2 = input ('Enter Player 2 Name: ')
    return player1, player2

# get players' preffered symbols
def get_symbols(player1, player2):
    symbol1 = input (player1 + ', please choose your symbol (X or O):')
    symbol2 = input (player2 + ', please choose your symbol (X or O):')
    return symbol1, symbol2

# say hello and present initial view
def intro(p1, p2):
    print ('Hello', p1["name"], '.')
    print ('Hello', p2["name"], '.')
    print ('Here is your game board!')

# define grid  
def build_grid():
    grid = { 'a1':' ', 'a2':' ', 'a3':' ', 'b1':' ', 'b2':' ', 'b3':' ', 'c1':' ', 'c2':' ', 'c3':' '}
    return grid

# build view using 'format string'
def view_update(grid): 
    grid_view = f"""

            1   2   3 
        a | {grid['a1']} | {grid['a2']} | {grid['a3']} |
        b | {grid['b1']} | {grid['b2']} | {grid['b3']} |
        c | {grid['c1']} | {grid['c2']} | {grid['c3']} |   

        """
    print (grid_view)
    return grid_view

# set winning condition
def winning_condition(grid):        
    if grid ['a1'] != ' ' and grid['a1'] == grid['a2'] == grid['a3']:
        return True 
    elif grid ['b1'] != ' ' and grid['b1'] == grid['b2'] == grid['b3']:
        return True
    elif grid ['c1'] != ' ' and grid['c1'] == grid['c2'] == grid['c3']:
        return True
    elif grid ['a1'] != ' ' and grid['a1'] == grid['b1'] == grid['c1']:
        return True
    elif grid ['a2'] != ' ' and grid['a2'] == grid['b2'] == grid['c2']:
        return True
    elif grid ['a3'] != ' ' and grid['a3'] == grid['b3'] == grid['c3']:
        return True
    elif grid ['a1'] != ' ' and grid['a1'] == grid['b2'] == grid['c3']:
        return True
    else:
        return False

# check if the board is full: 
def full_board(grid):
    for x in grid:
        if grid[x] == ' ':
            return False     
    return True 
        
# prompt each player for their move - restrict their move to either X or O and empty space
def take_turn(grid, current_player):
    while True:
        move = input (current_player["name"] + "\'s turn. Which box would you like to place your move? ")
        if move in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']: 
            if grid[move] == ' ':
                grid.update({move: current_player["symbol"]})
                return grid
            else:
                print ('That space is occupied. Please choose another box!')
        else:
            print ('Move is out of range, please try again. Valid input is a1, a2, a3, b1, b2, b3, c1, c2 or c3.')
     
# closing remarks
def close_game(grid, current_player):
    if winning_condition(grid) == True:
        print (current_player["name"], ', YOU WON!!!')
        print ('Game over! I hope you both had fun!') 
    elif full_board(grid) == True:
        print ('The board is full. There is no winnder. Game over!')
        

# running the game
def gamestate():
    print (welcome())
    player1_name, player2_name = get_players()
    player1_symbol, player2_symbol = get_symbols(player1_name, player2_name)
    player1 = {"name": player1_name, "symbol": player1_symbol}
    player2 = {"name": player2_name, "symbol": player2_symbol}
    
    intro(player1, player2)
    grid = build_grid()
    grid_view = view_update (grid)
    # define current player and first turn 
    current_player = player1
    take_turn(grid, current_player)
    view_update(grid)
    while not winning_condition(grid) and not full_board(grid):
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
        take_turn(grid, current_player)
        view_update(grid)
             
    view_update(grid)
    close_game(grid, current_player)

# game loop here
if __name__ == "__main__":
    gamestate()