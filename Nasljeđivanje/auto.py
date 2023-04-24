from vozilo import Vozilo
class Auto(Vozilo):
    def dobivaVrstu(self):
        print("Ovo je auto")
        
Auto.dobivaVrstu(self=Auto)