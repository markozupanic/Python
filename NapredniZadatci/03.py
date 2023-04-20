#7. Napravite funkciju koja prima kvadratnu jednadzbu u formatu 'ax^2 + bx +c = 0'
#(pri unosu zamijeniti a b i c konkretnim brojevima), te uzvraca s dvjema nul-tockama za specificne slucajeve a b i c.
#Pretpostavite da je unos uvijek ispravan.

#T=( -b/2a , (4ac-b2)/2a ) 

unos_a=int(input("Unesite a:"))
unos_b=int(input("Unesite b:"))
unos_c=int(input("Unesite c:"))

T1=(-unos_b/(2*unos_a)) 
T2=((4*unos_a*unos_c)/(2*unos_a))


jednadjba=unos_a+unos_b+unos_c
if(jednadjba==0):
    print(f"T({T1},{T2})")
else:
    print("Unos nije ispravan")

#print(f"T({T1},{T2})")


















