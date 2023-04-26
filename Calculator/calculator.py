class Calculator():
    def __init__(self) -> None:
        pass
    
    def start(self) -> None:
        self.equation = input("Unesi jednadzbu").replace(" ","")
        self.rawEquation = self.equation
 
    def parseString(self):
        self.numberList = []
        self.operatorList = []
        numberString = ""
        
        if(not self.equation[0].isnumeric()):
            self.operatorList.append("-")
            self.equation = self.equation[1:]
            
        else:
            self.operatorList.append("+")
        
        for i in self.equation:
            if i.isnumeric():
                numberString+=i
            else:
                self.numberList.append(int(numberString))
                self.operatorList.append(i)
                numberString = "" 
        self.numberList.append(int(numberString))  
        
    def calculate(self):
        result = 0

        for idx,operator in enumerate(self.operatorList):
            if(operator == "+"):
                result += self.numberList[idx]
                
            if(operator == "-"):
                result -= self.numberList[idx]
                
        return result
          
    def output(self):
        print(f"Jednadzba je {self.rawEquation}")
        print(f"Brojevi su : {self.numberList}")
        print(f"Operatori su : {self.operatorList}")
        
        #print(f"{'True' if True else 'False'}")
        #res = ("nisu","jesu")
        #res[self.calculate()==eval(self.rawEquation)]
        
        print(f"{'Rezultati su isti' if self.calculate() == eval(self.rawEquation) else 'Rezultati nisu isti'}")
         
    
    
    