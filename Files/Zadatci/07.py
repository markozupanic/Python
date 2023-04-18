#7. napravi program koji ce iz liste imena 'names' stvoriti datoteku te u nju u svakom retku pohraniti ime
names = ["ivan", "mario", "julija", "fran", "marko", "jan", "daniel", "ivan", "mario", "mario", "marija", "ana", "ante"]

FILE_PATH="pohranjivanje.txt"

def pohranjivanje_u_datoteku():
    
    f=open(FILE_PATH,"a")
    
    for i in range(len(names)):
        f.write(names[i])
        f.write("\n")
        
        
    


pohranjivanje_u_datoteku()

















