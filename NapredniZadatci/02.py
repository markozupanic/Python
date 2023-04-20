#3. Napravite program koji ce omoguciti popisivanje knjiga u knjizari.
# Obavezna su polja 'naslov', 'cijena' i 'godina_izdanja'. Dodajte polja kakva zelite.

knjige_lista=[]
cijena_lista=[]
godina_izdanja_lista=[]


while True:
    naslov_knjige=input("Unesite naslov: ")
    cijena_knjige=int(input("Unesite cijenu: "))
    godina_izdanja=int(input("Unesite godinu izdavanja: "))
    
    if(naslov_knjige=="-1"):
        break
    else:
        knjige_lista.append(naslov_knjige)
        
    if(cijena_knjige==-1):
        break
    else:
        cijena_lista.append(cijena_knjige)
    if(godina_izdanja==-1):
        break
    else:
        godina_izdanja_lista.append(godina_izdanja)
    

print(knjige_lista)
print(cijena_lista)
print(godina_izdanja_lista)













