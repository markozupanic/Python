#2. napravite klasu GeometrijskiLik. klasa treba imati mogucnost proracuna oplosja i obujma kugle, 
# valjka i kvadra te ispis navedenih oplosja te koristenih formula za proracun. ispisite na ekran sve navedeno.
import math
class GeometrijskiLik:
    
    def __init__(self,r,h,a,b,c):
        self.r=r
        self.h=h
        self.a=a
        self.b=b
        self.c=c
        
    
    
    
    def oplosja_kugle(r):
        #OO=4⋅R2⋅π
        oplosjekugle=4*r**2*math.pi
        print(f"formula za oplošje kugle: 4⋅R2⋅π  rješenje: {oplosjekugle}")
    
    def obujam_kugle(r):
        #V=(4/3R**3)π
        obujamkugle=(4/3*r**3)*math.pi
        print(f"formula za obujam kugle: (4/3*r**3)*math.pi  rješenje: {obujamkugle}")
        
    def oplosje_valjka(r,h):
        #O=2rπ⋅(r+h)
        oplosjevaljka=2*r*math.pi*(r*h)
        print(f"formula za obujam valjka: 2*r*math.pi*(r*h)  rješenje: {oplosjevaljka}")
        
    def obujam_valjka(r,h):
        #V=r2πh
        obujamvaljka=r*2*math.pi*h
        print(f"formula za obujam valjka: r*2*math.pi*h  rješenje: {obujamvaljka}")
    def oplosje_kvadra(a,b,c):
        #2*(a*b+a*c+b*c)
        oplosjekvadra=2*(a*b+a*c+b*c)
        print(f"formula za obujam valjka: 2*(a*b+a*c+b*c)  rješenje: {oplosjekvadra}")
    def obujam_kvadra(a,b,c):
        #a*b*c
        obujamkvadra=a*b*c
        print(f"formula za obujam valjka: a*b*c  rješenje: {obujamkvadra}")
        












