from board import board

def main():
    print("Welcome!\n")
    my_board = board()
    my_board.print_board()
    while (not my_board.game_won):
        print("\nwhite's turn")
        piece = input("what piece would you like to move? w1/w2\n")
        # TODO: check if piece is legal
        spot = input("where would you want to move " + piece + "?\n")
        # TODO: check if spot is legal
        my_board.white_turn(piece, spot)
        print("black's turn\n")
        my_board.print_board()
        my_board.black_turn()
        my_board.game_won = True

    
if __name__ == '__main__':
    main()