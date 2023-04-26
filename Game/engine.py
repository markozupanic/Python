from board import Board
from player import Player

class Engine():
    def __init__(self) -> None:
        pass
    
    def update(self):
        while True:
            self.render()
            inp = input("Unesi smjer: ")
            if(inp == "quit"):
                print("izlaz")
                break
            
            moveX, moveY = self.convertInputToCoordinates(inp) # (movex = 0,movey = 1)
            x , y = self.player.getCoordinates()
            newX = x + moveX
            newY = y + moveY
            
            self.player.updateCoordinates(moveX,moveY) #update kordinata Player klase
            self.board.updatePlayerPosition(x,y,newX,newY) #update lokacije igrača na Board klasi
            
            
    
    def newGame(self, board : Board, player : Player):
        self.board = board
        self.player = player
        self.updatePlayer()
        self.update()
    
    def render(self):
        board = self.board.getBoard()
        formatedBoard = ""

        for y in range(len(board)):
            row = ""
            for x in range(len(board)):
                if board[y][x] == 1:
                    row += "[x] "
                    continue
                row += "[ ] "
                
            formatedBoard+=row + "\n"
            
        print(formatedBoard)
    
    def updatePlayer(self,xIncrement : int = 0 , yIncrement : int = 0 ):
        x,y = self.player.getCoordinates()
        self.board.putPlayer(x + xIncrement,y+yIncrement)
    
    def convertInputToCoordinates(self, inp : str) -> tuple[int,int]:
        coordinates = tuple()
        
        if(inp == "w"):
            coordinates = (0,-1)
        elif(inp == "s"):
            coordinates = (0,1)
        elif(inp == "d"):
            coordinates = (1,0)
        elif(inp == "a"):
            coordinates = (-1,0)
            
        return coordinates # tuple[int,int]
    
        
        