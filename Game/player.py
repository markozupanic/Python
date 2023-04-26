import random

class Player():
    def __init__(self) -> None:
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
        print(self.x,self.y)
        
    def getCoordinates(self) -> tuple[int,int]:
        return (self.x,self.y)
    
    def updateCoordinates(self,xIncrement : int = 0,yIncrement : int = 0):
        self.x += xIncrement
        self.y += yIncrement
        
 
    # def __str__(self):
    #     return f"{self.x} {self.y}"