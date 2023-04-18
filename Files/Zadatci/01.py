#1. napisi program koji ce napraviti novu datoteku. koristi mod "x"
FILE_PATH="nova_datoteka.txt"

def kreiranje_datoteke():
    f = open(FILE_PATH, "x")
    f.close()
 
    
    
#kreiranje_datoteke()    

#2. napisi program koji ce zapisati string "ja sam genijala, a ti socijala" u datoteku. koristi mod "w".

def upisivanje_u_datoteku():
    f=open(FILE_PATH,"w")
    f.write("ja sam genijala, a ti socijala")
    f.close()
    
upisivanje_u_datoteku()

























