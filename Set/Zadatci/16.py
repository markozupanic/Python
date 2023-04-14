#19. vas omiljeni carobni aparat za kavu je podivljao. aparat treba ispitivati korisnika za kavu sve dok on ne unese "Q" ili 0. 
# aparat prihvaca samo kovanice od 2kn ili 5kn. kada korisnik ubaci kovanicu od 5kn, aparat nausmicno izbacuje dvije kave. 
# kada korisnik ubaci kovanicu od 2kn, aparat nasumicno izbaci jednu kavu. ako aparat sakupi 20kn, on se magicno napuni za 3 kave.
# neka set sljedeceg oblika simbolizira pocetnu kolicinu kave u aparatu: set_kava = {1, 2, 3, 4, 5, 6}. 
# set se treba umanjivati sa svakom isporucenom kavom.
import random
vrste_kava=["kava s mljekom","capucino","bijela kava","kava sa šlagom"]
sakupljeno=0
broj_kava_u_aparatu={1,2,3,4,5,6}

while(True):
    print("Prekid: 0 ili Q")
    kava=input("želite li kavu: ")
    if(kava=="0" or kava=="Q"):
        break
    kovanice=int(input("Ubacite kovanicu: "))
    if(kovanice==2):
        print(random.choice(vrste_kava))
    elif(kovanice==5):
        print(random.choice(vrste_kava))
        print(random.choice(vrste_kava))
        sakupljeno+=1
        
    if(sakupljeno==20):
        broj_kava_u_aparatu_list=list(broj_kava_u_aparatu)
        
    
    
    





















#20. nadogradite prethodni zadatak na nacin da ubacite u aparat i opciju za dodavanje mlijeka u kavu.
#kada korisnik ubaci kovanicu, aparat ga treba pitati zeli li kavu sa mlijekom ili bez. ukoliko korisnik odabere kavu sa mlijekom,
#ona se nasumicno uklanja iz sljedeceg seta: set_mlijeko = {1, 2, 3}. ukoliko korisnik zatrazi kavu sa mlijekom, a u aparatu ga vise nema,
#treba ispisati odgovarajucu poruku i po vasoj zelji nastaviti izvodjenje (npr. pitati korisnika za novu kavu ili mu isporuciti kavu bez mlijeka).
# u svim slucajevima treba se ispisati kakva je kava isporucena, koliko novca je ubaceno te koliki je iznos novca u aparatu nakon isporuke kave.



