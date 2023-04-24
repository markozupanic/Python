#4. klasu Geometrijski_lik iz prethodne vjezbe preuredite tako da se iz nje izvode klase za kuglu i valjak.
# definirajte prikladne metode i atribute za pojedinu klasu. 
# neka u nadklasi (super klasi) bude definiran samo onaj atribut koji se ponavlja u podklasama

import math

class Geometrijski_lik:
    def __init__(self):
        self.ime = ""
    
    def opseg(self):
        pass
    
    def povrsina(self):
        pass

class Kugla(Geometrijski_lik):
    def __init__(self, poluprecnik):
        super().__init__()
        self.ime = "Kugla"
        self.r = poluprecnik
    
    def opseg(self):
        opseg = 2 * math.pi * self.r
        print(f"Opseg {self.ime} je {opseg}")
    
    def povrsina(self):
        povrsina = 4 * math.pi * self.r**2
        print("Povrsina {} je {:.2f}".format(self.ime, povrsina))
    
    def volumen(self):
        volumen = 4/3 * math.pi * self.r**3
        print("Volumen {} je {:.2f}".format(self.ime, volumen))

class Valjak(Geometrijski_lik):
    def __init__(self, poluprecnik, visina):
        super().__init__()
        self.ime = "Valjak"
        self.r = poluprecnik
        self.h = visina
    
    def opseg(self):
        opseg = 2 * math.pi * self.r
        print("Opseg {} je {:.2f}".format(self.ime, opseg))
    
    def povrsina(self):
        povrsina = 2 * math.pi * self.r * (self.r + self.h)
        print("Povrsina {} je {:.2f}".format(self.ime, povrsina))
    
    def volumen(self):
        volumen = math.pi * self.r**2 * self.h
        print("Volumen {} je {:.2f}".format(self.ime, volumen))


kugla = Kugla(5)
valjak = Valjak(3, 10)

kugla.opseg()   
kugla.povrsina()  
kugla.volumen()     

valjak.opseg()  
valjak.povrsina()   
valjak.volumen()    



