from engine import Engine
from board import Board
from player import Player


def main():
    engine = Engine()
    board = Board()
    player = Player()
    engine.newGame(board,player)
    

if __name__ == "__main__":
    main()