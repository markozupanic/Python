#3. napisi program koji ce iz datoteke iz prethodnog zadatka dohvatiti upisani tekst i ispisati ga,
# zatim rastavi navedeni string prema zarezu (",")
# te zapisi oba dijela u novim recima na kraj u datoteku iz prethodnog zadatka. koristi mod "a"
FILE_PATH="nova_datoteka.txt"

def dohvacanje_teksta_i_rastavljanje():
    f=open(FILE_PATH)
    a=f.readline()
    print(a)
    f.close
    
    
    f=open(FILE_PATH,"a")
    a=a.split(",")
    f.write(a[0])
    print("\n")
    f.write(a[1])
    print(a)




dohvacanje_teksta_i_rastavljanje()











