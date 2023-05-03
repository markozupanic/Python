#17. napravite program koji zahtijeva ucitavanje imena, prezimena i godina ako korisnik unese 1 te ponavljati unos dok god se ne unese 0. 
# program sprema podatke u rjecnik. kad korisnik unese broj 2, program treba traziti od unos prezimena te ispisati nalazi li se navedeno prezime
# u rjecniku. ako da, program treba ispisati podatke unesenog korisnika u obliku: 
# "kosnisnik <ime> <prezime> se nalazi u bazi i ima <godine> godina. ukoliko se korisnik ne nalazi u bazi,
# program treba ispisati odgovarajucu poruku te pitati korisnika zeli li ponovno pretrazivati bazu ili izaci. 
# ako korisnik odabere izlazak, program zavrsava sa izvodjenjem. ukoliko korisnik odabere trecu opciju,
# program treba ispisati sve spremljene korisnike u formatiranom stringu.
print("0:ugasite program")
print("1:unesite ime")
print("2:unesite prezime")
print("3:unesite godine")
opcija_sta_zeli_unjet=int(input("Koju opciju želite unjet: "))


ime_dict={}
prezime_dict={}
godine_dict={}

while(True):
  if(opcija_sta_zeli_unjet==0):
      break
  elif(opcija_sta_zeli_unjet==1):
      unos_ime=input("Unesite ime: ")
      ime="ime"
      ime_dict.setdefault("ime")
      ime_dict.update({ime,unos_ime})
      print(ime_dict)
  elif(opcija_sta_zeli_unjet==2):
      unos_prezime=input("Unesite prezime: ")
      prezime="prezime"
      prezime_dict.setdefault(prezime)
      prezime_dict.update({prezime,unos_prezime})
      print(prezime_dict)
  elif(opcija_sta_zeli_unjet==3):
      unos_godine=int(input("Unesite godine: "))
  else:
      print("Krivi broj!!!!")
      
      
      
      
    
    
    
    
    














