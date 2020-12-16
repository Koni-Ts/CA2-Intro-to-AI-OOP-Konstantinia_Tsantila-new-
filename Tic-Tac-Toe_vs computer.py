# A board to dislay during the game after each player move
def display_board():

    '''
    This function will draw the game display for each turn.
    '''
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# A function where the user chooses between X or O and automatically assign x to be the first one to play
def user_symbol_choice():
    '''
    This function will allow player to chose their symbol and assign X to play first.
    '''
    while True:
        symbol = input("Do you want to be X or O?" )
        # we include both x and capital X as valid options
        if symbol in ["x","X"]:
            print("You chose 'X'.\nYou play first" )
            # and returns the symbols x,o for our mark placement
            return 'x','o'
        # Same for o and capital O as valid options 
        if symbol in ["o","O"]:
            print("You chose 'O'.\nComputer plays first")
            # and returns the symbols o,x for our mark placement
            return 'o','x'
        # if input is anything else rather than the given options we ask user for valid input
        else:
            print('Enter correct input! X or O')

