from chess.game import Game
from chess.player import Player

def main():
    player1 = Player('W', first_row=0)
    player2 = Player('B', first_row=7)
    game = Game(player1, player2)
    print(game.board)
    game.move(game.board.board[1][4], 3, 4) #TODO: need a cleaner way to describe moves
    print(game.board)

if __name__ == '__main__':
    main()

