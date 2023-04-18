#4. napisi program koji ce iz datoteke prethodnog zadatka ispisati prvih N linija 
# iz datoteke. N je broj koji odreÄuje korisnik
FILE_PATCH="nova_datoteka.txt"
def broj_redaka_za_ispisat():
    f=open(FILE_PATCH)
    broj_linija=int(input("Unesite broj linija: "))
    for i in range(broj_linija):
        print(f.readline(),end="")
        
    f.close()
        
    


broj_redaka_za_ispisat()
























