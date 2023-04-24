#8. napravite klasu za procesiranje poruke. program treba raditi na sljedeci nacin:
 #a) korisnik unosi nekakav String kao input, oblika:

#<message>
#   <title>Naslov Poruke<title>
#  <body>Ovdje se nalazi moja poruka<body>
#<message>

#c) napravite funkciju unutar klase koja ce ispisati naslov i tijelo poruke u konzolu.

#primjer: za unos '<message><title>Naslov Poruke<title><body>Ovdje se nalazi moja poruka<body><message>', program vraca:
#Naslov: Naslov Poruke
#Poruka: Ovdje se nalazi moja poruka
    
    
class ProcesiranjePoruke():
    def unos_poruke():
        poruka=input("Unesite poruku: ")
        return poruka
        
    def ispisivanje_naslova_i_tijela(unos_poruke):
        naslov_poruke="Naslov Poruke"
        print("<message>")
        print(f"   <title>{naslov_poruke}<title>")
        print(f"   <body>{unos_poruke}<body>")
        print("<message>")
        
#ProcesiranjePoruke.unos_poruke()
ProcesiranjePoruke.ispisivanje_naslova_i_tijela(unos_poruke=ProcesiranjePoruke.unos_poruke())  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    