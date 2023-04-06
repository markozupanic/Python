#24. NapiÅ¡i program koji unosi rezultat nogometne utakmice za Å panjolsku i Hrvatsku te ispisuje tekst 
#âÅ panjolska je pobjednikâ u sluÄaju da je Å panjolska pobijedila, tekst âHrvatska je pobjednikâ u sluÄaju da 
#je Hrvatska pobijedila ili tekst âNerijeÅ¡enoâ u sluÄaju da su obje ekipe osvojile jednak broj bodova


golovi_spanjolske=int(input("Golovi Španjolske: "))
golovi_hrvatske=int(input("Golovi Hrvatska: "))

if(golovi_spanjolske>golovi_hrvatske):
    print("Španjoslka je pobjedila")
elif(golovi_hrvatske>golovi_spanjolske):
    print("Hrvatska pobjedila")
else:
    print("Nerješeno")



