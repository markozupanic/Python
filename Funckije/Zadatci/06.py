#6. napisi funkciju koja, na osnovu unesenog polumjera, racuna povrsinu kruga, 
# njegovu kruznicu, obujam i oplosje kugle (koristi math biblioteku za racun svih operacija)

import math

def kruznica():
    unos=int(input("Unesite polumjer kružnice: "))
    povrsina_kruga=(unos**2)*math.pi
    print(povrsina_kruga)
    obujam_kruga=2*unos*math.pi
    print(obujam_kruga)
    oplosje_kugle=4*(math.pi*(unos**2))
    print(oplosje_kugle)




kruznica()












