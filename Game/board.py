class Board():
    def __init__(self) -> None:
        self.boardSize = 10
        self.board = []
        #row = [[0]*10]*10
        
        for y in range(self.boardSize):
            row = []
            for x in range(self.boardSize):
                row.append(0)
            self.board.append(row)
            
    def getBoard(self) -> "Board":
        return self.board
    
    def putPlayer(self,x : int, y : int):
        self.board[y][x] = 1
        
    def updatePlayerPosition(self,oldX : int,oldY : int,newX : int,newY : int):
        self.board[oldY][oldX] = 0
        self.board[newY][newX] = 1
        