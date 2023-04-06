#12. â¢Napisati program koji de omoguÄiti korisniku unos stranica trokuta.
#    â¢Program redom ispisuje stranice trokuta redoslijedom kojim ih je korisnik unio.
#    â¢Program provjerava da li takav trokut postoji. Ako postoji onda
#     se provjerava je li trokut jednakostraniÄan, raznostraniÄan ili jednakokraÄan.
#    â¢Nakon provjere, program ispisuje obavijest o postojanju takvog trokuta i vrsti trokuta
#    (jednakostraniÄan, raznostraniÄan ili jednakokraÄan.).
#    â¢U suprotnom ispisuje da trokut ne postoji.

stranica_a=input("Unesi stranicu a: ")
stranica_b=input("Unesi stranicu b: ")
stranica_c=input("Unesi stranicu c: ")

print(stranica_a+ " " +stranica_b+ " " +stranica_c)

jednakostranican=stranica_a==stranica_b==stranica_c
jednakokracan=stranica_a != stranica_b==stranica_c
raznostranican=stranica_a != stranica_b!=stranica_c

if(jednakostranican):
    print("Trokut je jednakostranican")
elif(jednakokracan):
    print("Trokut je jednakokračan")
elif(raznostranican):
    print("Trokut je raznostraničan")
else:
    print("Trokut ne postoji")










