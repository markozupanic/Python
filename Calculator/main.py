from calculator import Calculator

def main():
    counter = 0
    while counter<20:
        calc = Calculator()
        calc.start()
        calc.parseString()
        calc.output()
        
        counter+=1
    
    
   




if __name__ == "__main__":
    main()