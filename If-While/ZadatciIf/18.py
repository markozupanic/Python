#18. Napisati program koji Äe omoguÄiti unos tri stranice trokuta.
#â¢Ako su sve tri stranice jednake ispisati: jednakostranican,
#â¢ako su dvije stranice jednake duljine, ispisati: jednakokracan,
#a u suprotnom raznostranican.

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









