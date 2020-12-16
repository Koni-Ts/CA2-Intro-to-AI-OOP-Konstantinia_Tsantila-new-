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


# A function for placeing the human input as a mark into the board
def human_position_input(mark):
    '''
    This function will collect an input from the human user to place their mark on the board.
    '''
    while True:
        position_input = input(f'Human "{mark}" Enter a position between 1-9 to place your marker.')
        # we check if the input is digit and that is between 0 and 10 as the board has positions from 1 to 9
        if position_input.isdigit() and int(position_input) <10 and int(position_input) >0:
            # we assign position input to be an int
            position_input = int(position_input)
            # Then we check if the board is empty in that position
            if board[position_input] == " ":
                # and if so place the mark there
                return position_input
            else:
                #in case the position is already taken we ask user to provide another position
                print(f'Human "{mark}" Place is already taken, provide another position.')
        # For the first condition if not siatisfied we ask the user for valid input
        else:
            print(f'Human "{mark}" Invalid number, please enter a number between 1 and 9.')


# A function that will ask the user after every game is finished if they want a rematch
def new_game_ask():
    while True:
        rematch = input("Would you like to play again? Type Y/N.")
        # We provide both lower case and upper case as valid inputs
        if rematch in ["y","Y"]:
        # we create a new variable and give it a value of True
            next_game = True
            break
        # We provide both lower case and upper case as valid inputs
        elif rematch in ["n","N"]:
            print ("Thanks for playing, have a nice day!")
            # we create a new variable and give it a value of False
            next_game = False
            break
        else:
            # in case anything else is given as an input a valid imput prompt pops
            print ("Please type a valid input, Type Y/N")
    # while the next_game is True
    if next_game:
        # print new game to acknowledge to the user that is a new game
        print ("New game")
        # start the main game function main_human_vs_computer()
        main_human_vs_computer()
    else:
        return False

