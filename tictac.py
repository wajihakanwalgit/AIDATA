import random
from colorama import Fore, Style,init 
init(autoreset=True)

def display_board(board):
    print(Fore.CYAN + "Current Board:")
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell
        elif cell == 'O':
            return Fore.BLUE + cell
        else:
            return Fore.WHITE + cell
    print(' '+colored(board[0])+' | '+colored(board[1])+' | '+colored(board[2]))
    print(Fore.CYAN + "-----------"+Style.RESET_ALL)
    print(' '+colored(board[3])+' | '+colored(board[4])+' | '+colored(board[5]))
    print(Fore.CYAN + "-----------"+Style.RESET_ALL)
    print(' '+colored(board[6])+' | '+colored(board[7])+' | '+colored(board[8]))
    print(Style.RESET_ALL)
    print()
def player_choice():
    symbol=' '
    while symbol not in ['X', 'O']:
        symbol = input(Fore.YELLOW + "Choose your symbol (X or O): ").upper()
        if symbol not in ['X', 'O']:
            print(Fore.RED + "Invalid choice. Please choose X or O.")
    return symbol
def player_move(board, symbol):
    move = -1
    while move < 0 or move > 8 or board[move] != ' ':
        try:
            move = int(input(Fore.YELLOW + f"Player {symbol}, enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != ' ':
                print(Fore.RED + "Invalid move. Try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number between 0 and 8.")
    board[move] = symbol
def ai_move(board, ai_symbol,player_symbol):
    for i in rane(9):
        if board[i] == isdigit():
            board_copy=board.copy() 
            board_copy[i] = ai_symbol
            if check_winner(board, ai_symbol):
                board[i] = ai_symbol
                return
            for j in range(9):
                if board[j] == isdigit():
                    board_copy = board.copy()
                    board_copy[j] = player_symbol
                    if check_winner(board_copy, player_symbol):
                        board[i] = ai_symbol
                        return
            possible_moves = [i for i in range(9) if board[i] == isdigit()]  
            move=random.choice(possible_moves)
            board[move] = ai_symbol
def check_winner(board, symbol):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False
def check_full(board):
    return all(not spot.isdigit() for spot in board)    
def tictac():
    print(Fore.CYAN + "Welcome to Tic Tac Toe!")
    player_name= input(Fore.YELLOW + "Enter your name: ")
    while True :
        board=['1','2','3','4','5','6','7','8','9']
        player_symbol, ai_symbol = player_choice()
        turn="player"
        game_on = True

        while game_on:
            display_board(board)
            if turn == "player":
                player_move(board, player_symbol)
                if check_winner(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"{player_name} wins!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a draw!")
                    game_on = False
                turn = "ai"
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_winner(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a draw!")
                    game_on = False
                turn = "player"
        play_again = input(Fore.YELLOW + "Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(Fore.CYAN + "Thanks for playing! Goodbye!")
            break
if __name__ == "__main__":
    tictac()
    