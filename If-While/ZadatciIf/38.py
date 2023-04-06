#38. NapiÅ¡i program koji unosi Äetveroznamenkasti broj te ispisuje njegovu najmanju znamenku, ostatak 
#dijeljenja tog broja s 2 te poruku je li upisani broj paran ili neparan.

broj=int(input("Unesi četveroznamenkasti broj: "))
#broj_min=min(broj)
#print(broj_min)
ostatak_broja=broj%2
print(ostatak_broja)
if(broj%2==0):
    print("Paran")
else:
    print("Neparan")


broj_string=str(broj)
broj_min=min(broj_string)
print(broj_min)




