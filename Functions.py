from IPython.display import clear_output
import random
import time
moves = [' ']*10
p1marker = ''
p2marker = ''
marker = ''
position = ''
def display_board(board):
    clear_output()
    print(board[7] + " | " + board[8] + " | " + board[9])
    print('--|---|--')
    print(board[4] + " | " + board[5] + " | " + board[6])
    print('--|---|--')
    print(board[1] + " | " + board[2] + " | " + board[3])

def player_input():
    global p1marker, p2marker,marker
    while marker != 'X' and marker != 'O' :
        marker = input('what marker do u want player 1 (X or O):').upper()
    if marker == 'X':
        p1marker = 'X'
        p2marker = 'O'
        print('Player 1 uses {} and player 2 uses {}'.format(p1marker,p2marker))
    else:
        p1marker = 'O'
        p2marker = 'X'
        print('Player 1 uses {} and player 2 uses {}'.format(p1marker, p2marker))
#player_input()
def place_marker(board, marker, position, turn):
        print(turn + ' Turn')
        position = input('Where do you want to place the marker?: ')
        if board[int(position)] == ' ' :
            board[int(position)] = marker
        else :
            print("Wrong Move")
#place_marker(moves, p1marker,0, turn)
def win_check(board, marker):
    if board[1] == board[2] ==board[3] == marker or \
        board[4] == board[5] == board[6] == marker or \
            board[7] == board[8] == board[9] == marker or \
            board[1] == board[4] == board[7] == marker or \
            board[2] == board[5] == board[8] == marker or \
            board[3] == board[6] == board[9] == marker or \
            board[1] == board[5] == board[9] == marker or \
            board[7] == board[5] == board[3] == marker :

        return True
#win_check(moves, p1marker)

def choose_first():
    print('Choosing which player goes first')
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    if random.randint(0,1) == 0:
        print('Player 1 Goes First')
        return 'Player 1'
    else:
        print('Player 2 Goes first')
        return  'Player 2'
#choose_first()

def full_board_check(board):
    if board[1] != ' ' and \
        board[2] != ' ' and \
        board[3] != ' ' and \
        board[4] != ' ' and \
        board[5] != ' ' and \
        board[6] != ' ' and \
        board[7] != ' ' and \
        board[8] != ' ' and \
        board[9] != ' ' :
            print('Its a tie')
            return  True
#full_board_check(moves)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#replay()

def player_choice():
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:


        return position
#player_choice()