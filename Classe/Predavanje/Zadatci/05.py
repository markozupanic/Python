#5. napravite klasu Zaposlenik. neka klasa sadrzi atribute za: ime, godine, mjesecnu placu. u klasi definirajte sljedece:
class Zaposlenik:
    
    def __init__(self,ime,godine,mjesecna_placa,):
        self.ime=ime
        self.godine=godine
        self.mjesecna_placa=mjesecna_placa
        






#a) metodu koja ispisuje ime, godine i placu u istom retku, koristeci formatiranje stringa
    def ispisivanje_podataka(self): 
      print(f"ime zaposlenika: {self.ime} | godine zaposlenika: {self.godine} | mjesečna plača: {self.mjesecna_placa}")


#b) metodu plati_rezije, koja iznosi sljedece: za struju 20% place, za vodu 12% place i za plin 30% place.
# metoda ispisuje ukupan iznos rezija te vraca iznos preostale place, nakon placanja rezija
    def plati_rezije(self):
        global preostalo
        struja=self.mjesecna_placa*(20/100)
        voda=self.mjesecna_placa*(12/100)
        plin=self.mjesecna_placa*(30/100)
        preostalo=self.mjesecna_placa-struja-voda-plin
        rezije_ukupno=struja+voda+plin
        print(f"raču za struju: {struja} | račun za vodu: {voda} | račun za plin: {plin}")
        print(f"preostalo od plače: {preostalo} | režije ukupno: {rezije_ukupno}")
        return preostalo
    
#c) metodu jesam_li_kreditno_sposoban, koja ce vracati True ili False, na nacin da preostalu mjesecnu placu pomnozite sa 12,
# zatim umanjite za 20.000kn i ispisete rezultat. metoda vraca False ako je iznos place manji od 0, odnosno True ako je iznos veci od 0
    def jesam_li_kreditno_sposoban(self):
        global kreditno_sposoban
        if((preostalo*12)-20000>0):
            kreditno_sposoban=False
            print(kreditno_sposoban)
        else:
            kreditno_sposoban=True
            print(kreditno_sposoban)
        
        
    def ukupna_kolicina_kredita(jesam_li_kreditno_sposoban):
        if(kreditno_sposoban==True):
            unos=int(input("Na koliko godina želite kredit: "))
            iznos_kredita=(unos*12)*preostalo
            iznos_kamate_mjesecno=iznos_kredita*(8/100)
            iznos_kamate_gosinje=iznos_kamate_mjesecno*12
            
            print(f"iznos kredita: {iznos_kredita} | iznos mjesečne kamate: {iznos_kamate_mjesecno} | iznos godišnje kamate: {iznos_kamate_gosinje}")





#d) metodu koja odredjuje ukupnu kolicinu kredita, ukoliko je zaposlenik kreditno sposoban. 
# neka metoda prima cijeli broj (godine otplate). taj broj pomnozite sa 12 te sa njegovom preostalom placom, 
# kako biste odredili ukupan moguci kredit. na taj iznos, zaracunajte kamatu od 8% te ispisite koliki ce mu biti iznosi kredita i 
# kamate na mjesecnoj i godisnjoj razini.


marko=Zaposlenik("marko",23,600)
andrea=Zaposlenik("andrea",22,500)
Zaposlenik.ispisivanje_podataka(marko)
Zaposlenik.ispisivanje_podataka(andrea)
Zaposlenik.plati_rezije(marko)
Zaposlenik.plati_rezije(andrea)
Zaposlenik.jesam_li_kreditno_sposoban(marko)
Zaposlenik.jesam_li_kreditno_sposoban(andrea)
Zaposlenik.ukupna_kolicina_kredita(marko)
Zaposlenik.ukupna_kolicina_kredita(andrea)













