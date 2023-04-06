#22. NapiÅ¡i program koji uÄitava prosjek ocjena na kraju Å¡kolske godine te ispisuje komentar na prosjek

hrvatski=int(input("Ocjena: "))
engleski=int(input("Ocjena: "))
vjeronauk=int(input("Ocjena: "))
tjelesni=int(input("Ocjena: "))
likovni=int(input("Ocjena: "))

prosjek_ocjena=(hrvatski+engleski+vjeronauk+tjelesni+likovni)/5
print(prosjek_ocjena)

if(prosjek_ocjena>=1 and prosjek_ocjena<=3.5):
    print("Los uspjeh")
else:
    print("Dobar uspjeh")